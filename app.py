import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the processed data
df = pd.read_csv("processed_data.csv")

# Convert Date column to datetime and sort by date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f8f5f0",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.H1(
            "Soul Foods Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#8b1e3f",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Explore Pink Morsels sales over time by region.",
            style={
                "textAlign": "center",
                "color": "#444",
                "fontSize": "18px",
                "marginBottom": "25px"
            }
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.08)",
                "maxWidth": "1000px",
                "margin": "0 auto"
            },
            children=[
                html.Label(
                    "Filter by Region:",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "16px",
                        "color": "#333"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px", "marginBottom": "20px"},
                    inputStyle={"marginRight": "6px", "marginLeft": "12px"}
                ),

                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
        fig = px.line(
            filtered_df,
            x="Date",
            y="Sales",
            color="Region",
            title="Pink Morsels Sales Over Time - All Regions"
        )
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]
        fig = px.line(
            filtered_df,
            x="Date",
            y="Sales",
            title=f"Pink Morsels Sales Over Time - {selected_region.capitalize()} Region"
        )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#333"),
        title_font=dict(size=20),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)