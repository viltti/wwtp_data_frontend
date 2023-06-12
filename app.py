import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import os

from layouts import home_layout, create_features_layout, create_variable_graph, overview_layout
from services import get_variable_names, get_variable_data, get_history_data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], suppress_callback_exceptions=True)
server = app.server

navbar = dbc.Navbar(
    [
        dbc.Container(
            [
                dbc.NavbarToggler(id='navbar-toggler'),
                dbc.Collapse(
                    dbc.Row(
                        [
                            dbc.Col(dbc.NavItem(dbc.NavLink('Overview', href='/overview'))),
                            dbc.Col(html.Img(src='assets/waterlogo.png', height='80px')),
                            dbc.Col(dbc.NavItem(dbc.NavLink('Features', href='/features'))),
                        ],
                        
                        className='flex-grow-1',
                        align='center'
                    ),
                    id='navbar-collapse',
                    navbar=True,
                ),
            ],
        ),
    ],
    color='black',
    dark=True,
    id='navbar'
)

app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/overview":
        data = get_history_data()
        df = pd.DataFrame(data)  
        description = df.describe()  
        return overview_layout(description)
    elif pathname == "/features":
        variables = get_variable_names()
        features_layout = create_features_layout(variables)
        return features_layout
    elif pathname.startswith("/features/"):
        variable = pathname.split("/")[-1]
        print('variable name:', variable)
        data = get_variable_data(variable)
        return create_variable_graph(variable, data)
    else:
        return home_layout()
        


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)

