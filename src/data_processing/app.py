# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_m_sales.csv")

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales 2018-2022'),

    html.Div(children='''
        How did the price increase affect sales?
    '''),

    dcc.Graph(
        id='pink_morsels_sales_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
