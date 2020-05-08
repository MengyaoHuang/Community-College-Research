from utils import *
from app import app
from awards_data_processing import Awards_data, award_college, available_division_options, blank_table

overall_control = dbc.FormGroup([
    html.H6(children=''' The table below shows overall college-level statistics: '''),
    html.Br(),
    dbc.Table.from_dataframe(award_college, striped=True, bordered=True, hover=True, size='sm'),
])

division_control = dbc.FormGroup([
    # division panel
    html.H6(children=''' Please choose a division for detailed statistics below: '''),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
        id='Awards-dropdown-Division',
        options=[{'label': i, 'value': i} for i in available_division_options],
        value='ATP',
        clearable=False,
        style={'height': '30px', 'width': '200px'}
    ),
    # corresponding content followed
    html.Br(),
    html.Div(id='Awards-content-Division'),
])

department_control = dbc.FormGroup([
    # department panel
    html.H6(children=''' Please choose a department for detailed statistics below: '''),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
            id='Awards-dropdown-Department',
            clearable=False,
            style={'height': '30px', 'width': '200px'}
    ),
    # corresponding content followed
    html.Br(),
    html.Div(id='Awards-content-Department'),
])

program_control = dbc.FormGroup([
    # program panel
    html.H6(children=''' Please choose a program for detailed statistics below: '''),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
            id='Awards-dropdown-Program',
            clearable=False,
            style={'height': '30px', 'width': '200px'}
    ),
    # corresponding content followed
    html.Br(),
    html.Div(id='Awards-content-Program'),
])


Awards_layout = dbc.Container([
    html.H1("Awards"),
    html.Div(children=''' Visualization for Awards statistics at Division, Department and Program level.'''),
    html.Hr(),
    # overall college-level panel
    dbc.Row([
        dbc.Col(overall_control),
        dbc.Col(
            dcc.Graph(
                id='basic-interactions',
                figure={
                    'data': figure_data_modify(award_college),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>College Awards</b>',
                        "margin": {'t': 60},
                        "width": 600,
                        "height": 360,
                    }
                }
            )
        ),
    ], align="center"),
    html.Br(),
    # division panel
    dbc.Row([
        dbc.Col(division_control),
        dbc.Col(id="Awards-content-Division-figure"),
    ], align="center"),
    html.Br(),
    # department panel
    dbc.Row([
        dbc.Col(department_control),
        dbc.Col(id="Awards-content-Department-figure"),
    ], align="center"),
    html.Br(),
    # program panel
    dbc.Row([
            dbc.Col(program_control),
            dbc.Col(id="Awards-content-Program-figure"),
    ], align="center"),
    html.Br(),
],fluid=True)


# Making your app interactive by adding @callbacks
# Division Output table and graph
@app.callback(dash.dependencies.Output('Awards-content-Division', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value')])
def Awards_dropdown_division(value):
    temp_frame = awards_subset(Awards_data, div_list=[value])
    temp_frame = aggregate_shown_table(temp_frame)
    return dbc.Table.from_dataframe(temp_frame, striped=True, bordered=True, hover=True, size='sm')

@app.callback(dash.dependencies.Output('Awards-content-Division-figure', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value')])
def Awards_dropdown_division_figure(value):
    temp_frame = awards_subset(Awards_data, div_list=[value])
    temp_frame = aggregate_shown_table(temp_frame)
    return dbc.Col(
            dcc.Graph(
                id='basic-interactions',
                figure={
                    'data': figure_data_modify(temp_frame),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>Division {}: Awards</b>'.format(value),
                        "margin": {'t': 60},
                        "width": 600,
                        "height": 360,
                    }
                }
            )
    )

# Department Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Awards-dropdown-Department', 'options'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value')])
def Awards_dropdown_department(value):
    temp_frame = awards_subset(Awards_data, div_list=[value])
    available_department_options = list(temp_frame['Dept'].unique())
    return [{'label': i, 'value': i} for i in available_department_options]
@app.callback(dash.dependencies.Output('Awards-dropdown-Department', 'value'),
              [dash.dependencies.Input('Awards-dropdown-Department', 'options')])
def set_department_first(available_options):
    return available_options[0]['value']

# Department Output table and figures
@app.callback(dash.dependencies.Output('Awards-content-Department', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value')])
def Awards_content_department(value1, value2):
    temp_frame = awards_subset(Awards_data, div_list=[value1], dept_list=[value2])
    temp_frame = aggregate_shown_table(temp_frame)
    # combine LAM and LMTA
    if "LAM" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LAM": "LAM/LMTA"})
    if "LMTA" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LMTA": "LAM/LMTA"})
    # merge
    fill_temp_frame = pd.concat([blank_table, temp_frame]).drop_duplicates()
    fill_temp_frame = fill_temp_frame.fillna(0).groupby("AcadYr").sum().reset_index()
    # drop all zero columns
    fill_temp_frame = fill_temp_frame.loc[:, (fill_temp_frame != 0).any(axis=0)]
    return dbc.Table.from_dataframe(fill_temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Department Output table and figures
@app.callback(dash.dependencies.Output('Awards-content-Department-figure', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value')])
def Awards_content_department_figure(value1, value2):
    temp_frame = awards_subset(Awards_data, div_list=[value1], dept_list=[value2])
    temp_frame = aggregate_shown_table(temp_frame)
    # combine LAM and LMTA
    if "LAM" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LAM": "LAM/LMTA"})
    if "LMTA" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LMTA": "LAM/LMTA"})
    # merge
    fill_temp_frame = pd.concat([blank_table, temp_frame]).drop_duplicates()
    fill_temp_frame = fill_temp_frame.fillna(0).groupby("AcadYr").sum().reset_index()
    # drop all zero columns
    fill_temp_frame = fill_temp_frame.loc[:, (fill_temp_frame != 0).any(axis=0)]
    return dbc.Col(
        dcc.Graph(
            id='basic-interactions',
            figure={
                'data': figure_data_modify(fill_temp_frame),
                'layout': {
                    'clickmode': 'event+select',
                    'yaxis': {'title': '<b>Number of Awards<b>'},
                    'xaxis': {'title': '<b>Academic Year<b>'},
                    'title': '<b>Division {} Department {}: Awards</b>'.format(value1, value2),
                    "margin": {'t': 60},
                    "width": 600,
                    "height": 360,
                }
            }
        )
    )

# Program Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Awards-dropdown-Program', 'options'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value')])
def Awards_dropdown_program(value1, value2):
    temp_frame = awards_subset(Awards_data, div_list=[value1], dept_list=[value2])
    available_program_options = list(temp_frame['Prog'].unique())
    return [{'label': i, 'value': i} for i in available_program_options]
@app.callback(dash.dependencies.Output('Awards-dropdown-Program', 'value'),
              [dash.dependencies.Input('Awards-dropdown-Program', 'options')])
def set_program_first(available_options):
    return available_options[0]['value']

# Program Output table and figures
@app.callback(dash.dependencies.Output('Awards-content-Program', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value'),
               dash.dependencies.Input('Awards-dropdown-Program', 'value')])
def Awards_content_program(value1, value2, value3):
    temp_frame = awards_subset(Awards_data, div_list=[value1], dept_list=[value2], prog_list=[value3])
    temp_frame = aggregate_shown_table(temp_frame)
    # combine LAM and LMTA
    if "LAM" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LAM": "LAM/LMTA"})
    if "LMTA" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LMTA": "LAM/LMTA"})
    # merge
    fill_temp_frame = pd.concat([blank_table, temp_frame]).drop_duplicates()
    fill_temp_frame = fill_temp_frame.fillna(0).groupby("AcadYr").sum().reset_index()
    # drop all zero columns
    fill_temp_frame = fill_temp_frame.loc[:, (fill_temp_frame != 0).any(axis=0)]
    return dbc.Table.from_dataframe(fill_temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Program Output table and figures
@app.callback(dash.dependencies.Output('Awards-content-Program-figure', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value'),
               dash.dependencies.Input('Awards-dropdown-Program', 'value')])
def Awards_content_program_figure(value1, value2, value3):
    temp_frame = awards_subset(Awards_data, div_list=[value1], dept_list=[value2], prog_list=[value3])
    temp_frame = aggregate_shown_table(temp_frame)
    # combine LAM and LMTA
    if "LAM" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LAM": "LAM/LMTA"})
    if "LMTA" in list(temp_frame.columns):
        temp_frame = temp_frame.rename(columns={"LMTA": "LAM/LMTA"})
    # merge
    fill_temp_frame = pd.concat([blank_table, temp_frame]).drop_duplicates()
    fill_temp_frame = fill_temp_frame.fillna(0).groupby("AcadYr").sum().reset_index()
    # drop all zero columns
    fill_temp_frame = fill_temp_frame.loc[:, (fill_temp_frame != 0).any(axis=0)]
    return dbc.Col(
        dcc.Graph(
            id='basic-interactions',
            figure={
                'data': figure_data_modify(fill_temp_frame),
                'layout': {
                    'clickmode': 'event+select',
                    'yaxis': {'title': '<b>Number of Awards<b>'},
                    'xaxis': {'title': '<b>Academic Year<b>'},
                    'title': '<b>Division {} Department {} Program {}: Awards</b>'.format(value1, value2, value3),
                    "margin": {'t': 60},
                    "width": 600,
                    "height": 360,
                }
            }
        )
    )