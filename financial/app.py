import pandas as pd
import plotly.graph_objs as go
from dash import dcc, html, dash

# Load the data and create forecasts
df = pd.read_csv('data/customer_product.csv')
# ... code to create forecasts

# Create the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Subscription Forecasting'),
    html.Div([
        dcc.Graph(id='forecast-graph'),
    ], style={'width': '80%', 'display': 'inline-block'}),
    html.Div([
        dcc.Markdown(id='forecast-summary'),
    ], style={'width': '20%', 'display': 'inline-block'})
])

# Define the callbacks
@app.callback(
    [dash.dependencies.Output('forecast-graph', 'figure'),
     dash.dependencies.Output('forecast-summary', 'children')],
    [dash.dependencies.Input('product-dropdown', 'value')])
def update_forecast(product):
    # ... code to filter data by product and create forecasts
    
    # Create the plotly figure
    trace_actual = go.Scatter(
        x=df_actual.index, y=df_actual['subscribers'],
        mode='lines', name='Actual'
    )
    trace_forecast = go.Scatter(
        x=df_forecast.index, y=df_forecast['subscribers'],
        mode='lines', name='Forecast'
    )
    trace_upper_bound = go.Scatter(
        x=df_forecast.index, y=df_forecast['upper_bound'],
        mode='lines', fill=None, line=dict(color='gray'), showlegend=False
    )
    trace_lower_bound = go.Scatter(
        x=df_forecast.index, y=df_forecast['lower_bound'],
        mode='lines', fill='tonexty', line=dict(color='gray'), showlegend=False
    )
    layout = go.Layout(
        title=f'Subscription Forecast for {product}',
        xaxis={'title': 'Date'},
        yaxis={'title': 'Number of subscribers'},
        margin={'l': 40, 'b': 40, 't': 60, 'r': 10},
        legend={'x': 0, 'y': 1},
        hovermode='closest'
    )
    fig = go.Figure(data=[trace_actual, trace_forecast, trace_upper_bound, trace_lower_bound], layout=layout)
    
    # Create the forecast summary
    forecast_summary = f"Forecast summary for {product}:<br>"
    forecast_summary += f"Next quarter: {df_forecast.iloc[0]['forecast']:.0f} ({df_forecast.iloc[0]['lower_bound']:.0f} - {df_forecast.iloc[0]['upper_bound']:.0f})<br>"
    forecast_summary += f"Next year: {df_forecast.iloc[4]['forecast']:.0f} ({df_forecast.iloc[4]['lower_bound']:.0f} - {df_forecast.iloc[4]['upper_bound']:.0f})<br>"
    forecast_summary += f"Next 5 years: {df_forecast.iloc[20]['forecast']:.0f} ({df_forecast.iloc[20]['lower_bound']:.0f} - {df_forecast.iloc[20]['upper_bound']:.0f})"
    
    return fig, forecast_summary

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
