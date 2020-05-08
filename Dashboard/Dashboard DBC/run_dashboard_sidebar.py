"""
dcc.Location is used to track the current location. There are two callbacks,
one uses the current location to render the appropriate page content, the other
uses the current location to toggle the "active" properties of the navigation
links.
# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/page-3
"""
from utils import *
from app import app
from awards_layout_callbacks import Awards_layout
from courses_layout_callbacks import Course_Enrollment_Succcess_layout
from grades_layout_callbacks import  grades_layout

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("Dashboard", className="display-4"),
        html.Hr(),
        html.P("Check WCC statistics with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Awards", href="/page-1", id="page-1-link"),
                dbc.NavLink("Course Enroll and Success Rate", href="/page-2", id="page-2-link"),
                dbc.NavLink("Grades Distribution", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return Awards_layout
    elif pathname == "/page-2":
        return Course_Enrollment_Succcess_layout
    elif pathname == "/page-3":
        return grades_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=False)