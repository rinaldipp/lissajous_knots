import numpy as np
import plotly.graph_objects as go


def lissajous_knot(a, b, c, phi1, phi2, n_points, offset=1.5):
    """
    Calculate X, Y and Z cartesian coordinates for Lissajous knots according.
    Reference: LISSAJOUS KNOTS - M. G. V. BOGLE, J. E. HEARST, V. F. R. JONES and L. STOILOV

    Parameters
    ----------
    a : int
        Parameter for the X coordinates.
    b : int
        Parameter for the Y coordinates.
    c : int
        Parameter for the Z coordinates.
    phi1 : float
        Phase value for the X coordinates.
    phi2 : float
        Phase value for the Y coordinates.
    n_points : int
        Number of curve sampling points.
    offset : float, optional
        Percentual distance between 3D object and 2D projections.

    Returns
    -------
    Arrays for XYZ coordinates of 3D curve and XYZ coordinates of 2D projections.
    """
    t = np.linspace(-np.pi, np.pi, n_points)
    x = np.cos(a * t + phi1)
    y = np.cos(b * t + phi2)
    z = np.cos(c * t)

    x_offset = np.min(x) * np.ones(x.shape) * offset
    y_offset = np.min(y) * np.ones(y.shape) * offset
    z_offset = np.min(z) * np.ones(z.shape) * offset

    return x, y, z, x_offset, y_offset, z_offset


def plot_curves(x, y, z, x_offset, y_offset, z_offset, figsize=(850, 850)):
    """
    Plot 3D Lissajous Knot and its 2D projections.

    Parameters
    ----------
    x : array
        X axis cartesian coordinates of the 3D curve.
    y : array
        Y axis cartesian coordinates of the 3D curve.
    z : array
        Z axis cartesian coordinates of the 3D curve.
    x_offset : array
        X axis cartesian coordinates of the 2D projection.
    y_offset : array
        Y axis cartesian coordinates of the 2D projection.
    z_offset : array
        Z axis cartesian coordinates of the 2D projection.
    figsize : tuple, optional
        Plotly Figure width and height in pixels.

    Returns
    -------
    Plotly Figure object.
    """
    fig = go.Figure()
    n_points = len(x)
    for n in range(n_points):
        showlegend = True if n == 0 else False
        name = "3D"
        fig.add_trace(go.Scatter3d(
            x=[x[n], x[n + 1]] if n < n_points - 1 else [x[n], x[0]],
            y=[y[n], y[n + 1]] if n < n_points - 1 else [y[n], y[0]],
            z=[z[n], z[n + 1]] if n < n_points - 1 else [z[n], z[0]],
            mode="lines",
            line=dict(
                color='darkgoldenrod',
                width=6,
            ),
            name=name,
            legendgroup=name,
            showlegend=showlegend,
        ))

        name = "X Offset"
        fig.add_trace(go.Scatter3d(
            x=[x_offset[n], x_offset[n + 1]] if n < n_points - 1 else [x_offset[n], x_offset[0]],
            y=[y[n], y[n + 1]] if n < n_points - 1 else [y[n], y[0]],
            z=[z[n], z[n + 1]] if n < n_points - 1 else [z[n], z[0]],
            mode="lines",
            line=dict(
                color='mediumspringgreen',
                width=3,
            ),
            name=name,
            legendgroup=name,
            showlegend=showlegend,
        ))

        name = "Y Offset"
        fig.add_trace(go.Scatter3d(
            x=[x[n], x[n + 1]] if n < n_points - 1 else [x[n], x[0]],
            y=[y_offset[n], y_offset[n + 1]] if n < n_points - 1 else [y_offset[n], y_offset[0]],
            z=[z[n], z[n + 1]] if n < n_points - 1 else [z[n], z[0]],
            mode="lines",
            line=dict(
                color='mediumspringgreen',
                width=3,
            ),
            name=name,
            legendgroup=name,
            showlegend=showlegend,
        ))

        name = "Z Offset"
        fig.add_trace(go.Scatter3d(
            x=[x[n], x[n + 1]] if n < n_points - 1 else [x[n], x[0]],
            y=[y[n], y[n + 1]] if n < n_points - 1 else [y[n], y[0]],
            z=[z_offset[n], z_offset[n + 1]] if n < n_points - 1 else [z_offset[n], z_offset[0]],
            mode="lines",
            line=dict(
                color='mediumspringgreen',
                width=3,
            ),
            name=name,
            legendgroup=name,
            showlegend=showlegend,
        ))

    fig.update_layout(
        title=dict(
            text="<b>" + f"Lissajous Knot" + "</b>",
            xanchor="left",
            xref="paper",
            x=0,
            yanchor="bottom",
            yref="paper",
            y=1,
            pad=dict(b=3, l=0, r=0, t=0)
        ),
        template="plotly_dark",
        width=figsize[0], height=figsize[1],
        scene_camera=dict(
            eye=dict(x=1.50, y=1.50, z=1.50),
                          up=dict(x=0, y=0, z=1),
                          center=dict(x=0, y=0, z=0),
                          projection_type="orthographic"),
        scene={'xaxis_title': "x",
               'yaxis_title': "y",
               'zaxis_title': "z",
               'xaxis': dict(showticklabels=False,
                             showgrid=False,
                             showline=True,
                             zeroline=False,
                             showbackground=False),
               'yaxis': dict(showticklabels=False,
                             showgrid=False,
                             showline=True,
                             zeroline=False,
                             showbackground=False),
               'zaxis': dict(showticklabels=False,
                             showgrid=False,
                             showline=True,
                             zeroline=False,
                             showbackground=False),
               },

    )
    fig.update_layout({
        "plot_bgcolor": "rgba(0, 0, 0, 0)",
        "paper_bgcolor": "rgba(0, 0, 0, 0)",
    })

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"scene.camera.eye": {"x": 1.5, "y": 1.5, "z": 1.5},
                               "scene.camera.up": {"x": 0, "y": 0, "z": 1},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Default",
                        method="relayout",
                    ),
                    dict(
                        args=[{"scene.camera.eye": {"x": 0, "y": 0, "z": 2.5},
                               "scene.camera.up": {"x": 0, "y": 1, "z": 0},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Top",
                        method="relayout",
                    ),
                    dict(
                        args=[{"scene.camera.eye": {"x": 2.5, "y": 0, "z": 0},
                               "scene.camera.up": {"x": 0, "y": 0, "z": 1},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Lateral Right",
                        method="relayout",
                    ),
                    dict(
                        args=[{"scene.camera.eye": {"x": -2.5, "y": 0, "z": 0},
                               "scene.camera.up": {"x": 0, "y": 0, "z": 1},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Lateral Left",
                        method="relayout",
                    ),
                    dict(
                        args=[{"scene.camera.eye": {"x": 0, "y": 2.5, "z": 0},
                               "scene.camera.up": {"x": 0, "y": 1, "z": 1},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Front",
                        method="relayout",
                    ),
                    dict(
                        args=[{"scene.camera.eye": {"x": 0, "y": -2.5, "z": 0},
                               "scene.camera.up": {"x": 0, "y": 1, "z": 1},
                               "scene.camera.center": {"x": 0, "y": 0, "z": 0}}],
                        label="Rear",
                        method="relayout",
                    ),
                ]),
                type="buttons",
                direction="right",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0,
                y=0,
                xanchor="left",
                yanchor="top",
                bgcolor="grey",
                font_color="black"
            ),
        ]
    )

    return fig

