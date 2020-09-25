import sys
import plotly
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html


def main():
    pass

if __name__ == "__main__":
    
    df = pd.read_csv('parkings.csv',sep=';')

    fig1 = px.histogram(df, x="capacite",range_x=[0,100])
    #fig.show()

    fig2 = px.scatter_mapbox(df, lat="Lat", lon="Lon", hover_name="osm_id", hover_data=["type", "capacite","acces","payant","surveille","couvert"],color="capacite", zoom=9, title="Carte des stationnements pour vélos en Ile de France",size="capacite", color_continuous_scale=px.colors.diverging.RdYlGn,range_color=[0,50])
    fig2.update_layout(mapbox_style="light", mapbox_accesstoken="pk.eyJ1IjoiaGVyZWFsIiwiYSI6ImNrMW92ZnJ3dDBvaWQzbWw4MWMyemRmMTkifQ.ybaNjSTBRj1Cw45T379ZMA")
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.show()

    app = dash.Dash()
    app.layout = html.Div([
        html.H1(children='Histogramme du nombre de stationnements pour vélos par leur capacité d\'accueil'),
        dcc.Graph(figure=fig1),
        html.H1(children='Carte des stationnements pour vélos en Ile de France'),
        dcc.Graph(figure=fig2)
    ])

    app.run_server(debug=True, use_reloader=False)

    