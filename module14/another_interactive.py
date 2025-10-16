import pandas as pd
import plotly.express as px

df = pd.read_cvs("avgIQpercountry.cvs")

df["Popultion = 2023"] = df["Popultion = 2023"].str.replace(',', '').astype(float)

fig = px.cheropleth(df, loactions='Country', locationmode='country names', color="Avrage IQ", hover_name="Country")

                                hover_data[]
