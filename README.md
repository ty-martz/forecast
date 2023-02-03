# Forecast Energy Production and Demand

Python scripts to intake data and build models to forecast furture data. Accompanying notebook to explore electricity data sources

Data files courtesy of [Kaggle](https://www.kaggle.com):
1. [Green Energy Forecasting](https://www.kaggle.com/datasets/shibumohapatra/forecasting-green-energy)
2. [UK Electricity Consumption](https://www.kaggle.com/datasets/albertovidalrod/electricity-consumption-uk-20092022?select=historic_demand_2009_2023_noNaN.csv)


### Utilizing the Files
- Download the repo: `git clone https://github.com/ty-martz/forecast.git`
- Run the `example.ipynb` file, which shows the usage of the scripts to output plots and summaries of forecasted predictions. This can be used as a basis for other datasets to use the same
- Models tested include:
    1. AR
    2. ARIMA
    3. SARIMAX