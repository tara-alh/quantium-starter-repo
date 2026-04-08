import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("processed_data.csv")

# Convert Date column to datetime and sort by date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create the line chart
fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsels Sales Over Time"
)

# Add axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsels Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)