import plotly.express as px
import csv

with open("coffe.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffe in ml", y="sleep in hours")
    fig.show()