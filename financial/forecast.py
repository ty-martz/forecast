import pandas as pd
from prophet import Prophet

# Load the data into a Pandas DataFrame
data = pd.read_csv('./financial/data/customer_product.csv')

# Rename columns to match Prophet's requirements
data = data.rename(columns={'signup_date_time': 'ds', 'product': 'product_type'})

# Convert dates to Pandas datetime objects
data['ds'] = pd.to_datetime(data['ds'])
data['cancel_date_time'] = pd.to_datetime(data['cancel_date_time'])

# Group the data by month and count the number of customers for each month
monthly_data = data.resample('M', on='ds').agg({'customer_id': 'nunique', 'product_type': 'first'})
monthly_data = monthly_data.rename(columns={'customer_id': 'y'})

# Create a Prophet model and fit it to the data
model = Prophet()
model.fit(monthly_data)

# Generate future dates to forecast
future_dates = model.make_future_dataframe(periods=20, freq='M')

# Make predictions for the future dates
forecast = model.predict(future_dates)

# Extract the forecasts and uncertainty intervals for the next quarter, year, and 5 years
quarterly_forecast = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2023-06-30')][['ds', 'yhat']]
quarterly_uncertainty = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2023-06-30')][['ds', 'yhat_lower', 'yhat_upper']]

yearly_forecast = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2024-04-30')][['ds', 'yhat']]
yearly_uncertainty = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2024-04-30')][['ds', 'yhat_lower', 'yhat_upper']]

five_year_forecast = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2028-04-30')][['ds', 'yhat']]
five_year_uncertainty = forecast[(forecast['ds'] >= '2023-04-30') & (forecast['ds'] <= '2028-04-30')][['ds', 'yhat_lower', 'yhat_upper']]

# Print the forecasts and uncertainty intervals
print("Quarterly forecast:")
print(quarterly_forecast)
print("Quarterly uncertainty:")
print(quarterly_uncertainty)

print("Yearly forecast:")
print(yearly_forecast)
print("Yearly uncertainty:")
print(yearly_uncertainty)

print("Five-year forecast:")
print(five_year_forecast)
print("Five-year uncertainty:")
print(five_year_uncertainty)
