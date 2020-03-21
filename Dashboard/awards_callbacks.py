from utils import *
from awards_data_processing import Awards_data, award_college, available_division_options, blank_table
from app import app

# Making your app interactive by adding @callbacks
# Division Output table and graph
@app.callback(dash.dependencies.Output('Awards-content-Division', 'children'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value')])
def Awards_dropdown_division(value):
    temp_frame = awards_subset(Awards_data, div_list=[value])
    temp_frame = aggregate_shown_table(temp_frame)
    return html.Div([
        html.Div([generate_table(temp_frame, 150)], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='Awards-division-graph',
                figure={
                    'data': figure_data_modify(temp_frame),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>Division {}: Awards</b>'.format(value)
                    }
                }
            ),

        ], style={'width': '49%', 'float': 'right', 'marginTop': "-50px", 'display': 'inline-block'}),
    ])


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
    return html.Div([
        html.Div([generate_table(fill_temp_frame, 150)], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='Awards-department-graph',
                figure={
                    'data': figure_data_modify(temp_frame),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>Division {} Department {}: Awards</b>'.format(value1, value2)
                    }
                }
            ),
        ], style={'width': '49%', 'float': 'right', 'marginTop': "-50px", 'display': 'inline-block'}),
    ])


# Program Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Awards-dropdown-Program', 'options'),
              [dash.dependencies.Input('Awards-dropdown-Division', 'value'),
               dash.dependencies.Input('Awards-dropdown-Department', 'value')])
def Awards_dropdown_department(value1, value2):
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
    return html.Div([
        html.Div([generate_table(fill_temp_frame, 150)], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='Awards-program-graph',
                figure={
                    'data': figure_data_modify(temp_frame),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>Division {} Department {} Program {}: Awards</b>'.format(value1, value2, value3)
                    }
                }
            ),
        ], style={'width': '49%', 'float': 'right', 'marginTop': "-50px", 'display': 'inline-block'}),
    ])
