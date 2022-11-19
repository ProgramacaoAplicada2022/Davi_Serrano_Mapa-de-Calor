from calendar import month
from codecs import ignore_errors
from datetime import datetime
from fileinput import close
from turtle import title
import dash_bootstrap_components as dbc
from binascii import unhexlify
from operator import length_hint
from tkinter.messagebox import IGNORE
from unicodedata import name
from unittest import result
from winreg import DisableReflectionKey
from alpha_vantage.timeseries import TimeSeries
from dataclasses import dataclass
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dash import Dash, html, dcc
from numpy import histogram, size
import plotly.graph_objects as go
import pandas as pd
from dash import dash_table
from datetime import datetime
import plotly.graph_objects as go
from IPython.display import display
import plotly.graph_objects as go

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

tickers = ['RJ', 'SP', 'POA', 'SJC', 'BSB', 'RCF', 'FRT', 'SLV', 'RB', 'MN']
names = {'RJ':'Rio de Janeiro', 'SP':'São Paulo', 'POA':'Porto Alegre', 'SJC':'São jose dos Campos', 'BSB':'Brasília', 'RCF':'Recife', 'FRT':'Fortaleza', 'SLV':'Salvador', 'RB':'Rio Branco', 'MN':'Manaus' }


##------------------------------------------------------------##

#App

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.Div([
        html.H1(id ='Criminalidade'),
        dcc.Dropdown(
        id="ticker",
        options= tickers,
        value="RJ",
        clearable=False,
        ), 
    ]),
    html.Div([
        dcc.Graph(id='table1'),
        ]),
    html.Div([
        dcc.Graph(id="graph1"),
        dcc.Graph(id="graph2"),
        dcc.Graph(id="graph3"),
    ],),
])

@app.callback(
Output("Criminalidade", "Locais"),
Input("ticker", "value")
    )

def display_series(ticker):
    return names[ticker]
    
app.run_server(debug=True)