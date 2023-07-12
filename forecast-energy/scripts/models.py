from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
from dtw import dtw

def euc_func(a, b):
    return np.linalg.norm(a - b)

def dtw_forecast(train_data, test_data):
    """
    Fits a DTW model on training data and uses it to make predictions on testing data.
    
    Parameters:
    -----------
    train_data : Training time series data.
    test_data : Testing time series data.
    window_size : Size of the Sakoe-Chiba warping window. Default is 5.
    dist_fun : Distance function to use. Default is euclidean distance.
    step_pattern : Step pattern to use. Default is the Rabiner-Juang step pattern.
        
    Returns:
        Predicted values for the testing data.
    """
    # Compute the distances between the training and testing data
    distances = np.zeros((len(test_data), len(train_data)))
    for i, test_point in enumerate(test_data):
        for j, train_point in enumerate(train_data):
            distance = dtw(test_point, train_point)
            print(f"TEST output = {distance}")
            distances[i, j] = distance
    
    # Find the nearest neighbor in the training data for each testing point
    nn_indices = np.argmin(distances, axis=1)
    y_pred = train_data[nn_indices]
    
    return y_pred


class SMModel:

    def __init__(self, sm_model_choice='AR'): # options are 'AR', 'ARIMA', 'SARIMA', 'DTW'
        self.choice = sm_model_choice
        self.model = None
        self.dtw_results = None

    def fit_(self, data, ar_lag=1, arima_order=(1,1,1), sarima_order=(1,1,1), season_order=(0,0,0,0), sarima_disp=False):
        if self.choice == 'AR':
            self.model = AutoReg(data, lags=ar_lag).fit()
        elif self.choice == 'ARIMA':
            self.model = ARIMA(data, order=arima_order).fit()
        elif self.choice == 'SARIMA':
            self.model = SARIMAX(data, order=sarima_order, seasonal_order=season_order).fit(disp=sarima_disp)
        elif self.choice == 'DTW':
            self.model = 'DTW'
        else:
            raise ValueError(f"Bad model choice. You chose: {self.sm_model_choice}. When initializing SMModel class, choose between the models ('AR', 'ARIMA', 'SARIMA')")
        
        return self.model
    
    def predict_(self, start, end, dtw_train=None, dtw_test=None):
        if self.model is None:
            raise AssertionError(f'Model is not fit, use the fit_() method before using predict')
        elif self.model == 'DTW':
            if dtw_train is None or dtw_test is None:
                raise AssertionError('train and test data are not specified for the DTW model, use the `dtw_train` and `dtw_test` params')
            else:
                preds = dtw_forecast(dtw_train, dtw_test)
        else:
            preds = self.model.predict(start, end)
            return preds
