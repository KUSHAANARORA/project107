import pandas as pd
import plotly.express as py
with open ("data1.csv")as f:
  df = pd.read_csv(f)
  figure = py.scatter(df,x="level",y="attempt")
  figure.show()