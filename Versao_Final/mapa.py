import pandas as pd 
import numpy as np
import folium
from folium.plugins import HeatMap
import math
import webbrowser

data = pd.read_excel('data.xlsx')

categorias = data["Categorias"].copy()
categorias = categorias.drop_duplicates()
categorias = categorias.values.tolist()

maps = []
for i in categorias:
    mapa = folium.Map(location=[-14.7476, -50.5702], zoom_start = 4.5)
    list = []
    
    for index, linha in data.iterrows():
        if (linha['Número'] > 0 and linha['Categorias'] == i):        
            list.append([linha['LAT'],linha['LONG'], linha['Número']])

    HeatMap(list, radius= 15).add_to(mapa)
    mapa.save(i+'.html')

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

webbrowser.open('http://127.0.0.1:8050/')  # Go to example.com
app = dash.Dash()
app.layout = html.Div([
    html.Div([
        html.H1('Opções',style={'textAlign': 'left', 'font-weight':'bold', 'margin-left': '0em', 'margin-right': '0em', 'display': 'inline-block', 'width': '100%'}),
        dcc.Dropdown(
        id="categorias",
        options= categorias,
        value=categorias[0],
        clearable=False, 
        optionHeight = 40,
        style = dict(
            font = '30%',
            display = 'inline-block',
            verticalAlign = "middle",
            horizontalAlign = 'middle',
            )
        ), 
    ]),
    
    html.Div([
    html.H1('Mapa',style={'textAlign': 'center', 'font-weight':'bold', 'margin-left': '0em', 'margin-right': '0em', 'display': 'inline-block', 'width': '100%'}),
    html.Iframe(id = 'mapa_selecionado', srcDoc= open('Eletrônico.html').read(), width= '100%', height='1000')]),
])

@app.callback(
    Output("mapa_selecionado", "srcDoc"),
    Input("categorias", "value")
    )
def display_series(categorias):
    return open(categorias+'.html').read()

app.run_server(debug=True, use_reloader=False) 

