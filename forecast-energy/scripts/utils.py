import matplotlib.pyplot as plt
import numpy as np

def plot_preds(data, preds, date_col_name='datetime', val_col_name='energy'):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(data[date_col_name], data[val_col_name], label='True')
    ax.plot(data[date_col_name], preds, label='Prediction')
    ax.set_title('Actual vs. Predicted Values')
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Value')
    plt.legend()
    plt.show()

def summ_and_score(model, ytrue, ypred):
    print(model.summary())
    print('')
    mape = np.mean(np.abs(ypred - ytrue) / np.abs(ytrue))
    rmse = np.mean((ypred-ytrue)**2)**0.5
    corr = np.corrcoef(ypred, ytrue)[0,1]
    print('<><><><><><><><>')
    print(f'MAPE = {mape}')
    print(f"RMSE = {rmse}")
    print(f"Correlation Coefficient = {corr}")
    print('<><><><><><><><>')

# TODO: Visualize forecast data on test set