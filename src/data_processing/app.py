# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("pink_m_sales.csv")

@app.callback (
    Output("pink_morsels_sales_graph", "figure"),
    Input("region_radio", "value")
)
def updateGraph(selected_region):
    if selected_region == "All":
        dff = df
    else:
        dff = df[df["region"] == selected_region]
    fig = px.line(dff, x="date", y="sales", color="region")
    fig.update_layout(
        plot_bgcolor='#f2ecff',
        paper_bgcolor='#b1abe2',
        font_color='#5C6784'
    )
    return fig

fig = updateGraph("All")

app.layout = html.Div(
    style={'backgroundColor': '#b1abe2', 'color':'#5C6784'},
    children=[
    html.H1(children='Pink Morsels Sales 2018-2022', style={'textAlign': 'center', 'font-family': "Helvetica Neue"}),

    html.Div(
        style={'textAlign': 'center', 'font-family': "Helvetica Neue"},
        children=['''
        Sales by region:
        ''',
        dcc.RadioItems(
            id="region_radio", 
            options=[{'label':'All', 'value':'All'}, 
                    {'label':'North', 'value':'north'}, 
                    {'label':'South', 'value':'south'}, 
                    {'label':'West', 'value':'west'}, 
                    {'label':'East', 'value':'east'}], 
            value='All',
            inline=True),
        ]
        ),

    dcc.Graph(
        id='pink_morsels_sales_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
