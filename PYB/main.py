#IMPORTS
import sys
import plotly
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import csv

def downloadCsv():
    url = 'https://data.iledefrance.fr/explore/dataset/stationnement-velo-en-ile-de-france/download?format=csv'
    r = requests.get(url, allow_redirects=True)
    open('test.csv', 'wb').write(r.content)


def modifyCsv():
    lst=[]
    index = 1
    reader = csv.reader(open('test.csv', 'r'),delimiter=";")
    for row in reader:
        for i in range(0,len(row)):
            if(row[i]=="geo_point_2d"):
                index = i;
        lst.append(row)
    lst[0].pop(index)
    lst[0].append("Lat")
    lst[0].append("Lon")
    for i in range(1,len(lst)):
        value = lst[i].pop(index)
        value = value.split(",")
        lst[i].append(value[0])
        lst[i].append(value[1])

    f = open('numbers3.csv', 'w')
    with f:
        writer = csv.writer(f,delimiter=';')
        writer.writerows(lst)
       

#Ajouter x figures au dashboard
def joinFigures(app,*figures):
    output = []
    for i in range(0,len(figures)):
        output.append(dcc.Graph(figure=figures[i]))
    app.layout = html.Div(children=output)


#PROGRAMME
if __name__ == "__main__":

    downloadCsv()
    modifyCsv()
    
    #Lecture des données
    df = pd.read_csv('numbers3.csv',sep=';')

    #Création de l'histogramme
    fig1 = px.histogram(df, x="capacite",title="Histogramme du nombre de stationnements pour vélos en fonction de leur capacité d\'accueil")

    #Création de la carte intéractive
    fig2 = px.scatter_mapbox(df, lat="Lat", lon="Lon", hover_name="osm_id", hover_data=["type", "capacite","acces","payant","surveille","couvert"],color="capacite", zoom=9, title="Carte des stationnements pour vélos en Île de France",size="capacite", color_continuous_scale=px.colors.diverging.RdYlGn,range_color=[0,50])
    #Type d'affichage de la carte
    fig2.update_layout(mapbox_style="light", mapbox_accesstoken="pk.eyJ1IjoiaGVyZWFsIiwiYSI6ImNrMW92ZnJ3dDBvaWQzbWw4MWMyemRmMTkifQ.ybaNjSTBRj1Cw45T379ZMA")

    #Disposition des éléments graphiques de la page
    app = dash.Dash()
    #Ajoute de l'histogramme et de la carte au dashboard
    joinFigures(app,fig1,fig2)
    #Lancement de la page
    app.run_server(debug=True, threaded=True,use_reloader=False)
    
    
