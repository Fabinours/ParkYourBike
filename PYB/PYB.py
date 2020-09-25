#IMPORTS
import sys
import plotly
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

#PROGRAMME
if __name__ == "__main__":
    
    #Lecture des données
    df = pd.read_csv('parkings.csv',sep=';')

    #Création de l'histogramme
    fig1 = px.histogram(df, x="capacite",title="Histogramme du nombre de stationnements pour vélos en fonction de leur capacité d\'accueil")

    #Création de la carte intéractive
    fig2 = px.scatter_mapbox(df, lat="Lat", lon="Lon", hover_name="osm_id", hover_data=["type", "capacite","acces","payant","surveille","couvert"],color="capacite", zoom=9, title="Carte des stationnements pour vélos en Île de France",size="capacite", color_continuous_scale=px.colors.diverging.RdYlGn,range_color=[0,50])
    #Type d'affichage de la carte
    fig2.update_layout(mapbox_style="light", mapbox_accesstoken="pk.eyJ1IjoiaGVyZWFsIiwiYSI6ImNrMW92ZnJ3dDBvaWQzbWw4MWMyemRmMTkifQ.ybaNjSTBRj1Cw45T379ZMA")

    #Disposition des éléments graphiques de la page 
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(figure=fig1),#histogramme
        dcc.Graph(figure=fig2)#carte
    ])
    #Lancement de la page
    app.run_server(debug=True, use_reloader=False)

    