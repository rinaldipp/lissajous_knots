import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from lissajous import lissajous_knot, plot_curves


app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
app.title = "Lissajous Knots"
server = app.server

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Lissajous Knots"),
                        html.H5("Rinaldi Petrolli"),
                        html.A("rinaldipp@gmail.com", href="mailto:rinaldipp@gmail.com"),
                    ],
                    width=True,
                ),
            ],
            align="end",
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H5("Parameters"),
                                html.P("A"),
                                dcc.Input(
                                        id="a",
                                        placeholder=3,
                                        type='number',
                                        value=3
                                    ),
                                html.P(""),
                                html.P("B"),
                                dcc.Input(
                                    id="b",
                                    placeholder=4,
                                    type='number',
                                    value=4,
                                ),
                                html.P(""),
                                html.P("C"),
                                dcc.Input(
                                    id="c",
                                    placeholder=2,
                                    type='number',
                                    value=2,
                                ),
                                html.P(""),
                                html.P("ϕ1 [0 to 2π]"),
                                dcc.Input(
                                    id="phi0",
                                    min=0, max=2 * np.pi, step=np.pi / 4,
                                    type='range',
                                    value=np.pi / 2,
                                ),
                                html.P(""),
                                html.P("ϕ2 [0 to 2π]"),
                                dcc.Input(
                                    id="phi1",
                                    min=0, max=2 * np.pi, step=np.pi / 4,
                                    type='range',
                                    value=np.pi / 2,
                                ),
                                html.P(""),
                                html.P("Number of points"),
                                dcc.Input(
                                    id="n_points",
                                    min=10, max=600, step=10,
                                    type='range',
                                    value=100,
                                ),


                            ],
                        ),
                        html.Hr(),
                        html.H5("Reference"),
                        html.P("LISSAJOUS KNOTS - M. G. V. BOGLE, J. E. HEARST, V. F. R. JONES and L. STOILOV (1994)"),
                        html.P("A, B, C = 1, 2, 3..."),
                        html.P("x = cos (At + ϕ1)"),
                        html.P("y = cos (Bt + ϕ2)"),
                        html.P("z = cos (Ct)"),
                        html.P("with 0 < t < 2π"),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                            dcc.Graph(id="display", style={"height": "80vh"}),
                    ],
                    width=True,
                ),
            ]
        ),
        html.Hr(),
        html.P(
            [
                html.A(
                    "Source code",
                    href="https://github.com/rinaldipp/lissajous_knots",
                ),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    [Output(component_id='display', component_property='figure')],
    [Input(component_id='a', component_property='value'),
     Input(component_id='b', component_property='value'),
     Input(component_id='c', component_property='value'),
     Input(component_id='phi0', component_property='value'),
     Input(component_id='phi1', component_property='value'),
     Input(component_id='n_points', component_property='value'),]
)
def update_graph(a, b, c, phi1, phi2, n_points):
    phi1 = float(phi1)
    phi2 = float(phi2)
    n_points = int(n_points)
    x, y, z, x_offset, y_offset, z_offset = lissajous_knot(a, b, c, phi1, phi2, n_points)
    fig = plot_curves(x, y, z, x_offset, y_offset, z_offset)

    return [fig]


if __name__ == "__main__":
    app.run_server(debug=True)