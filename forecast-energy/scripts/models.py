from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

class SMModel:

    def __init__(self, sm_model_choice='AR'): # options are 'AR', 'ARIMA', 'SARIMA'
        self.choice = sm_model_choice
        self.model = None

    def fit_(self, data, ar_lag=1, arima_order=(1,1,1), sarima_order=(1,1,1), season_order=(0,0,0,0), sarima_disp=False):
        if self.choice == 'AR':
            self.model = AutoReg(data, lags=ar_lag).fit()
        elif self.choice == 'ARIMA':
            self.model = ARIMA(data, order=arima_order).fit()
        elif self.choice == 'SARIMA':
            self.model = SARIMAX(data, order=sarima_order, seasonal_order=season_order).fit(disp=sarima_disp)
        else:
            raise ValueError(f"Bad model choice. You chose: {self.sm_model_choice}. When initializing SMModel class, choose between the models ('AR', 'ARIMA', 'SARIMA')")
        
        return self.model
    
    def predict_(self, start, end):
        if self.model is None:
            raise AssertionError(f'Model is not fit, use the fit_() method before using predict')
        else:
            preds = self.model.predict(start, end)
            return preds
