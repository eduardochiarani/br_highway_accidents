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

st.title('Mapas de Localização dos Acidentes')
st.markdown('> Partindo da análise de acidentes com vítimas causados por Ingestão de álcool, o mapa de localização indica a quantidade concentrada do fenômeno nas regiões geográficas, com detalhes de cada acidente ao clicar sobre o mesmo.')

defaults = ['PR'] 
opcoes = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
estados_selecionados = st.multiselect("Selecione os Estados para Visualização ***(Observação: Quanto mais estados, maior necessidade de processamento)***", opcoes, default=defaults)

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
df2 = df.loc[(df['acidentes_com_ing_alcool'] == 1) & (df['uf'].isin(estados_selecionados))]

df2.loc[:, 'latitude'] = pd.to_numeric(df2['latitude'].str.replace(',', '.'))
df2.loc[:, 'longitude'] = pd.to_numeric(df2['longitude'].str.replace(',', '.'))

map = Map(tiles="openstreetmap", control_scale=True)
marker_cluster = MarkerCluster(
    options={
        "maxClusterRadius": 30,  # Aglomerado mais próximo, ajuste do raio de agrupamento
        "spiderfyDistanceMultiplier": 1,  # distância para agrupar
        "disableClusteringAtZoom": 10  # Desabilita o cluster em um nível de zoom maior
    }
).add_to(map)

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

st.title('Mapas de Calor da Localização dos Acidentes')
st.markdown('> A representação visual indica a densidade dos acidentes em diferentes áreas geográficas. As cores mais frias indicam menos acidentes, enquanto para cores mais quentes, mais acidentes.')

# Mapa de calor
map_calor = Map(tiles="Cartodb dark_matter", control_scale=True)
map_calor.fit_bounds([[lat_min, lon_min], [lat_max, lon_max]])
HeatMap(
    df2[['latitude', 'longitude']].values,
    radius=15,           # raio para reduzir a densidade
    blur=15,             # nível de desfoque (quanto maior, mais suave será o gradiente de calor)
    min_opacity=0.2      # opacidade mínima para tornar os pontos menos visíveis
).add_to(map_calor)
st_folium(map_calor, width=800, height=600)