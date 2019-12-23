import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

sankey_df = pd.read_csv('budget.csv')
pie_df = pd.read_csv('budget_pie.csv')

app.layout = html.Div(children=[
    html.H1(children='Money Flows'),

    dcc.Graph(
        id='sankey',
        style = {'height': '80vh'},
        figure = go.Figure(data=[go.Sankey(
                node = {
                    "pad": 15,
                    "thickness": 20,
                    "line": dict(color = "black", width = 0.5),
                    "label": sankey_df['label'].dropna(axis=0, how='any'),
                    "color": sankey_df['color'].dropna(axis=0, how='any')
                },
                link = {
                    "source": sankey_df['source'].dropna(axis=0, how='any'),
                    "target": sankey_df['target'].dropna(axis=0, how='any'),
                    "value": sankey_df['value'].dropna(axis=0, how='any')
                }
            )])
    ),

    dcc.Graph(
        id='pie',
        figure = go.Figure(data=[go.Pie(
            labels = pie_df['label'].dropna(axis=0, how='any'),
            values = pie_df['value'].dropna(axis=0, how='any')
        )
        ])
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
