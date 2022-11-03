import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import pandas as pd

app = Dash(__name__)


## Data selection 
df = yf.download('AAPL', start='2019-01-01', end='2020-01-01')
print(df)


## Input search bar
ALLOWED_TYPES = (
    "ticker", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

app.layout = html.Div(
    [
        dcc.Input(
            id="input_{}".format(_),
            type=_,
            placeholder="input type {}".format(_),
        )
        for _ in ALLOWED_TYPES
    ]
    + [html.Div(id="out-all-types")]
)


@app.callback(
    Output("out-all-types", "children"),
    [Input("input_{}".format(_), "value") for _ in ALLOWED_TYPES],
)
def cb_render(*vals):
    return " | ".join((str(val) for val in vals if val))


if __name__ == "__main__":
    app.run_server(debug=True)









