import pandas as pd
import plotly.express as px

df = pd.read_csv("covidData.csv")
print(df)
print(df.columns)

chart = px.scatter(df,x="date",y="cases",title="covid cases per day graph",color="country")
chart.show()