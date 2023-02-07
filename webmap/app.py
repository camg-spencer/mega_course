import folium
import pandas as pd

volcanoes = pd.read_csv("Volcanoes.txt")

map = folium.Map(location=(38.58, -99.09), zoom_start=5.5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for (i, row) in volcanoes.iterrows():
    fg.add_child(folium.Marker(location=(row["LAT"], row["LON"]), popup=row["NAME"], icon=folium.Icon(color="red")))

map.add_child(fg)

map.save("Map1.html")