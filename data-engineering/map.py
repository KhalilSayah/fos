import folium
import pandas as pd


def generate_map(filename):
    df= pd.read_csv(filename)
    #Algeria map
    mapp = folium.Map(location=[28.0290, 1.6667], zoom_start=5)
    tooltip = "Temperature"
    #createmarker
    for i in df.index:
        folium.Marker(
        [df['latitude'][i], df['longitude'][i]], popup="<i>"+str(df['temperature'][i])+"</i>", tooltip=tooltip
        ).add_to(mapp)
        
    return mapp

def main():
    filename = "transformed_data.csv"
    m = generate_map(filename)
    m.save("temperature.html")

main()

