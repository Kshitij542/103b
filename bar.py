import pandas as pd
import plotly.express as px

df = pd.read_csv("intel.csv")
fig = px.bar(df, x='date', y='cases',color='country', title='Corona cases')
fig.show()
