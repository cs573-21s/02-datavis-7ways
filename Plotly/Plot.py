import plotly.express as px 
import numpy as np  
import pandas as pd
import csv

#https://stackoverflow.com/questions/42372617/how-to-plot-csv-data-using-matplotlib-and-pandas-in-python

df = pd.read_csv('cars-sample.csv', sep=',')

x = df['Weight']
y = df['MPG']

colorDict = {
    "bmw": "#F3B0AC",
    "ford": "#B7B74A",
    "honda": "#80D5B0",
    "mercedes": "#88CDF1",
    "toyota": "#7DCBF3"
}

color_map = ['#F3B0AC', '#B7B74A', '#80D5B0', '#88CDF1', '#7DCBF3']
    
plot = px.scatter(df, x, y, color="Manufacturer", size='Weight', opacity=0.5, color_discrete_map=colorDict) 
plot.show()