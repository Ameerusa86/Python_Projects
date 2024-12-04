from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine


def create_dashboard(server):
    dash_app = Dash(__name__, server=server, url_base_pathname="/dashboard/")

    engine = create_engine("sqlite:///database/books.db")
    df = pd.read_sql("books", engine)

    dash_app.layout = html.Div(
        [
            dcc.Dropdown(
                id="availability-filter",
                options=[
                    {"label": "In stock", "value": "In stock"},
                    {"label": "Out of stock", "value": "Out of stock"},
                ],
                value="In stock",
            ),
            dcc.Graph(id="price-chart"),
        ]
    )

    @dash_app.callback(
        Output("price-chart", "figure"), Input("availability-filter", "value")
    )
    def update_chart(filter_value):
        filtered_df = df[df["availability"].str.contains(filter_value)]
        fig = px.histogram(filtered_df, x="price", nbins=20)
        return fig

    return dash_app
