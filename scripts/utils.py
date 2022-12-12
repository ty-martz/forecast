import matplotlib.pyplot as plt

def plot_preds(data, preds, date_col_name='datetime', val_col_name='energy'):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(data[date_col_name], data[val_col_name], label='True')
    ax.plot(data[date_col_name], preds, label='Prediction')
    ax.set_title('Actual vs. Predicted Values')
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Value')
    plt.legend()
    plt.show()