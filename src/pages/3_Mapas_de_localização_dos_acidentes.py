import streamlit as st
import pandas as pd
import numpy as np
from folium import Map, CircleMarker
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from folium.plugins import HeatMap

st.set_page_config(
    page_title="Mapas e Visualizações",
    page_icon="🗺️",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title('Mapas de localização dos acidentes')
st.markdown('> Partindo da análise de acidentes com vítimas causados por Ingestão de álcool nas rodovias federais do Brasil, os mapas de localização e calor, indicam a concentração geográfica do fenômeno por clusterização.')
# Análise de dados de ingestão de alcool
df = pd.read_csv('./data/processed/df_concat.csv')
df['acidentes_com_ing_alcool'] = np.where(
    ((df['feridos_leves'] > 0) | (df['feridos_graves'] > 0) | (df['mortos'] > 0)) & 
    (df['causa_acidente'] == "Ingestão de álcool pelo condutor"), 1, 0)

df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S')
df['periodo_dia'] = pd.cut(df['horario'].dt.hour,
                           bins=[0, 6, 12, 18, 24],
                           labels=['Madrugada', 'Manhã', 'Tarde', 'Noite'],
                           include_lowest=True)
df['periodo_dia'] = df['periodo_dia'].astype('object')


# Mapa
# condicao SC e PR para reduzir dados exibidos no mapa
condicao = ['PR']
df2 = df.loc[(df['acidentes_com_ing_alcool'] == 1) & (df['uf'].isin(condicao))]

df2.loc[:, 'latitude'] = pd.to_numeric(df2['latitude'].str.replace(',', '.'))
df2.loc[:, 'longitude'] = pd.to_numeric(df2['longitude'].str.replace(',', '.'))

map = Map(tiles="openstreetmap", control_scale=True)
marker_cluster = MarkerCluster(
    options={
        "maxClusterRadius": 30,  # Aglomerado mais próximo, ajuste do raio de agrupamento
        "spiderfyDistanceMultiplier": 1,  # Ajusta a distância para agrupar
        "disableClusteringAtZoom": 10  # Desabilita o cluster em um nível de zoom maior
    }
).add_to(map)

# icon_create_function = """\
# function(cluster) {
#     return L.divIcon({
#         html: '<div style="background-color: rgba(255, 0, 0, 0.6); \
#                          color: white; width: 30px; height: 30px; \
#                          border-radius: 50%; text-align: center; \
#                          line-height: 30px; font-weight: bold;">' + cluster.getChildCount() + '</div>',
#         className: 'leaflet-div-icon',
#         iconSize: new L.Point(0, 0),
#         iconAnchor: [15, 15]
#     });
# }"""
# marker_cluster = MarkerCluster(icon_create_function=icon_create_function).add_to(map)

for index, row in df2.iterrows():
    CircleMarker(
        [row["latitude"], row["longitude"]],
        radius=2,
        color='green',
        fill=True,
        fill_color='green',
        popup=f"""
            <div style="min-width: 250px;">
                <b>BR: </b> {row['br']} <br>
                <b>Km: </b> {row['km']} <br>
                <b>Dia da semana: </b> {row['dia_semana']} <br>
                <b>Período do dia: </b> {row['periodo_dia']} <br>
                <b>Veículos env.: </b> {row['veiculos']} <br>
                <b>Ilesos: </b> {row['ilesos']} <br>
                <b>Feridos leves: </b> {row['feridos_leves']} <br>
                <b>Feridos graves: </b> {row['feridos_graves']} <br>
                <b>Mortos: </b> {row['mortos']}
            </div>
        """
    ).add_to(marker_cluster)

lat_min = df2['latitude'].min()
lat_max = df2['latitude'].max()
lon_min = df2['longitude'].min()
lon_max = df2['longitude'].max()
map.fit_bounds([[lat_min, lon_min], [lat_max, lon_max]])
st_folium(map, width=800, height=600)

st.empty()

# Mapa de calor
map_calor = Map(tiles="Cartodb dark_matter", control_scale=True)
map_calor.fit_bounds([[lat_min, lon_min], [lat_max, lon_max]])
HeatMap(
    df2[['latitude', 'longitude']].values,
    radius=15,           # Ajuste o raio para reduzir a densidade
    blur=15,             # Ajuste o nível de desfoque (quanto maior, mais suave será o gradiente de calor)
    min_opacity=0.2      # Ajuste a opacidade mínima para tornar os pontos menos visíveis
).add_to(map_calor)
st_folium(map_calor, width=800, height=600)