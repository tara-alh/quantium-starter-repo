import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load and combine data
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3])

# Basic cleaning (just in case)
df.columns = df.columns.str.lower()

# Convert date column if it exists
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = Dash(__name__)

# Example visualisations (auto-adapts to columns)
numeric_cols = df.select_dtypes(include="number").columns

fig = px.line(
    df,
    x="date" if "date" in df.columns else df.index,
    y=numeric_cols[0] if len(numeric_cols) > 0 else None,
    title="Sales Over Time"
)

app.layout = html.Div([
    html.H1("Quantium Sales Dashboard"),

    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)