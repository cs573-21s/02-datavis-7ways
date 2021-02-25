'''
Reference: https://docs.bokeh.org/en/latest/docs/reference/plotting.html
'''
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap
from bokeh.models import LinearInterpolator
import pandas as pd

# output to static HTML file
output_file("index.html")

p = figure(plot_width=800, plot_height=700, title="A2 bokeh")

df = pd.read_csv("../cars-sample.csv")

index_cmap = factor_cmap('Manufacturer', palette=['#f8766d', '#a3a500', '#00bf7d', '#00b0f6', '#e76bf3'],
                         factors=sorted(df['Manufacturer'].unique()))
size_mapper = LinearInterpolator(
    x=[df['Weight'].min(),df['Weight'].max()],
    y=[5,30]
)

p.scatter(
    x='Weight',
    y='MPG',
    source=df,
    alpha=0.5,
    color=index_cmap,
    size={'field': 'Weight', 'transform': size_mapper},
    legend_group='Manufacturer'
)

p.xaxis.axis_label = "Weight"
p.yaxis.axis_label = "MPG"

# show the results
show(p)