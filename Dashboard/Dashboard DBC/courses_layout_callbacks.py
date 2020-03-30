from utils import *
from awards_data_processing import available_division_options
from courses_data_processing import Courses_data, available_semester_options
from app import app

# College level table and figures - fixed across all operations
overall_control = dbc.FormGroup([
    html.H6(children=''' The table below shows overall college-level statistics: '''),
    html.Br(),
    dbc.Table.from_dataframe(aggregate_shown_table_enroll_succ(Courses_data), striped=True, bordered=True, hover=True, size='sm'),
])

division_control = dbc.FormGroup([
    html.H6(children=''' Please choose a specific division for more detailed statistics below: '''),
    dcc.Dropdown(
            id='Courses-dropdown-Division',
            options=[{'label': i, 'value': i} for i in available_division_options],
            value='ATP',
            clearable = False,
            style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Courses-content-Division'),
])

department_control = dbc.FormGroup([
    html.H6(children=''' Please choose a specific department for more detailed statistics below: '''),
    dcc.Dropdown(
        id='Courses-dropdown-Department',
        clearable=False,
        style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Courses-content-Department'),
])

discipline_control = dbc.FormGroup([
    html.H6(children=''' Please choose a specific discipline for more detailed statistics below: '''),
    dcc.Dropdown(
        id='Courses-dropdown-Discipline',
        clearable=False,
        style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Courses-content-Discipline'),
])

course_control = dbc.FormGroup([
    html.H6(children=''' Please choose a specific course number for more detailed statistics below: '''),
    dcc.Dropdown(
        id='Courses-dropdown-CoursesNumber',
        clearable = False,
        style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Courses-content-CoursesNumber'),
])

overall_figure_control = dbc.FormGroup([
    dbc.Row([
        html.H6(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
        dcc.Dropdown(
            id='Semester-dropdown-overall',
            options=[{'label': i, 'value': i} for i in available_semester_options],
            value='Fall',
            clearable=False,
            style={'height': '30px', 'width': '150px'}
        ),
        ]),
    html.Br(),
    html.Div(id='enroll-succ-content-overall'),
])

division_figure_control = dbc.FormGroup([
    dbc.Row([
        html.H6(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
        dcc.Dropdown(
            id='Courses-dropdown-Division-semester',
            clearable=False,
            style={'height': '30px', 'width': '150px'},
        ),
        ]),
    html.Br(),
    html.Div(id='enroll-succ-content-division'),
])

department_figure_control = dbc.FormGroup([
    dbc.Row([
        html.H6(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
        dcc.Dropdown(
            id='Courses-dropdown-Department-semester',
            clearable = False,
            style={'height': '30px', 'width': '150px'}
        ),
    ]),
    html.Br(),
    html.Div(id='enroll-succ-content-department'),
])

discipline_figure_control = dbc.FormGroup([
    dbc.Row([
        html.H6(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
        dcc.Dropdown(
            id='Courses-dropdown-Discipline-semester',
            clearable = False,
            style={'height': '30px', 'width': '150px'}
        ),
    ]),
    html.Br(),
    html.Div(id='enroll-succ-content-discipline'),
])

course_table_control = dbc.FormGroup([
    dbc.Row([
        html.H6(children="Please choose a specific term for visualization: ", style={'margin-right': '1em'}),
        dcc.Dropdown(
            id='Courses-dropdown-CoursesNumber-Term',
            clearable = False,
            style={'height': '30px', 'width': '150px'}
        ),
    ]),
    html.Br(),
    html.Div(id='enroll-succ-content-CoursesNumber'),
])

Course_Enrollment_Succcess_layout = dbc.Container([
    html.H1("Course Enrollment and Success Rate"),
    html.Div(children=''' Visualization for Course Enrollment and Success Rate statistics at Division, Department and Discipline level.'''),
    html.Div(children=''' Here "E" represents "Enrollment" and "SR" represents "Success Rate" '''),
    html.Hr(),
    # overall college-level panel
    dbc.Row([
        dbc.Col(overall_control),
        dbc.Col(overall_figure_control),
    ], align="center"),
    # division panel
    dbc.Row([
        dbc.Col(division_control),
        dbc.Col(division_figure_control),
    ], align="center"),
    # department panel
    dbc.Row([
        dbc.Col(department_control),
        dbc.Col(department_figure_control),
    ], align="center"),
    # discipline panel
    dbc.Row([
        dbc.Col(discipline_control),
        dbc.Col(discipline_figure_control),
    ], align="center"),
    # courses panel
    dbc.Row([
        dbc.Col(course_control),
        dbc.Col(course_table_control),
    ], align="center"),
],fluid=True)


# overall output figure
@app.callback(dash.dependencies.Output('enroll-succ-content-overall', 'children'),
              [dash.dependencies.Input('Semester-dropdown-overall', 'value')])
def Enroll_succ_overall(value):
    temp_frame = aggregate_shown_table_enroll_succ(Courses_data)
    # plot
    # change titlefont and tickfont if needed
    # yaxis2=dict(title='yaxis2 title', titlefont=dict(color='rgb(148, 103, 189)'),
    # tickfont=dict(color='rgb(148, 103, 189)'), overlaying='y', side='right')
    # left bar chart: Success Rate Right line chart: Enrollment
    suc_col = str(value) + '(SR)'
    enrol_col = str(value) + '(E)'
    success_trace = go.Bar(x=temp_frame['AcadYr'], y=temp_frame[suc_col], name= 'Success Rate')
    enroll_trace = go.Scatter(x=temp_frame['AcadYr'], y=temp_frame[enrol_col], name= 'Enrollment', yaxis='y2')
    return html.Div([
        dcc.Graph(
            id='enroll-succ-content-overall-graph',
            figure={
                'data': [success_trace, enroll_trace],
                'layout': go.Layout(
                    title=dict(text='<b>{} Semester Overall College</b>'.format(value), side='left'),
                    # title='<b>{} Semester: Course Enrollment and Success Rate</b>'.format(value),
                    xaxis=dict(title='<b>Academic Year<b>'),
                    yaxis=dict(title='<b>Success Rate(%)<b>', range=[0, 100], showgrid=False),
                    yaxis2=dict(title='<b>Enrollment<b>', overlaying='y', side='right',
                                range=[0, 1.2*max(temp_frame[enrol_col])], showgrid=False, tickformat=','),
                    # legend_orientation="h",
                    # legend=dict(orientation="h"),
                    legend={'x':-0.1, 'y':-0.1, "orientation":"h"},
                    margin={'t': 40},
                    width=650,
                    height=350,
                )
            }
        )
    ])

# Courses division table
@app.callback(dash.dependencies.Output('Courses-content-Division', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value')])
def Courses_dropdown_division(value):
    temp_frame = courses_subset(Courses_data, div_list=[value])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    return dbc.Table.from_dataframe(temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Courses division semester button
@app.callback(dash.dependencies.Output('Courses-dropdown-Division-semester', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value')])
def Courses_dropdown_division_semester(value):
    temp_frame = courses_subset(Courses_data, div_list=[value])
    available_semester_options = list(temp_frame['FWS'].unique())
    available_semester_options = sorted(available_semester_options)
    return [{'label': i, 'value': i} for i in available_semester_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-Division-semester', 'value'),
              [dash.dependencies.Input('Courses-dropdown-Division-semester', 'options')])
def set_courses_dropdown_division_semester_first(available_options):
    return available_options[0]['value']

# division output figure
@app.callback(dash.dependencies.Output('enroll-succ-content-division', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Division-semester', 'value')])
def Enroll_succ_division(value1, value2):
    temp_frame = courses_subset(Courses_data, div_list=[value1])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    # plot
    # change titlefont and tickfont if needed
    # yaxis2=dict(title='yaxis2 title', titlefont=dict(color='rgb(148, 103, 189)'),
    # tickfont=dict(color='rgb(148, 103, 189)'), overlaying='y', side='right')
    # left bar chart: Success Rate Right line chart: Enrollment
    suc_col = str(value2) + '(SR)'
    enrol_col = str(value2) + '(E)'
    success_trace = go.Bar(x=temp_frame['AcadYr'], y=temp_frame[suc_col], name= 'Success Rate')
    enroll_trace = go.Scatter(x=temp_frame['AcadYr'], y=temp_frame[enrol_col], name= 'Enrollment', yaxis='y2')
    return html.Div([
        dcc.Graph(
            id='enroll-succ-content-division-graph',
            figure={
                'data': [success_trace, enroll_trace],
                'layout': go.Layout(
                    title=dict(text='<b>{} Semester Division {}</b>'.format(value2, value1)),
                    # title='<b>{} Semester: Course Enrollment and Success Rate</b>'.format(value),
                    xaxis=dict(title='<b>Academic Year<b>'),
                    yaxis=dict(title='<b>Success Rate(%)<b>', range=[0, 100], showgrid=False),
                    yaxis2=dict(title='<b>Enrollment<b>', overlaying='y', side='right',
                                range=[0, 1.2*max(temp_frame[enrol_col])], showgrid=False, tickformat=','),
                    # legend_orientation="h",
                    # legend = dict(orientation="h"),
                    legend={'x': -0.1, 'y': -0.1, "orientation": "h"},
                    margin={'t': 40},
                    width=650,
                    height=350,
                )
            }
        )
    ])

# Department Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Courses-dropdown-Department', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value')])
def Courses_dropdown_department(value):
    temp_frame = courses_subset(Courses_data, div_list=[value])
    available_department_options = list(temp_frame['Dept'].unique())
    available_department_options = sorted(available_department_options)
    return [{'label': i, 'value': i} for i in available_department_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-Department', 'value'),
              [dash.dependencies.Input('Courses-dropdown-Department', 'options')])
def set_department_first(available_options):
    return available_options[0]['value']

# Courses department table
@app.callback(dash.dependencies.Output('Courses-content-Department', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value')])
def Courses_dropdown_department_content(value1, value2):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    return dbc.Table.from_dataframe(temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Courses department semester button
@app.callback(dash.dependencies.Output('Courses-dropdown-Department-semester', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value')])
def Courses_dropdown_department_semester(value1, value2):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2])
    available_semester_options = list(temp_frame['FWS'].unique())
    available_semester_options = sorted(available_semester_options)
    return [{'label': i, 'value': i} for i in available_semester_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-Department-semester', 'value'),
              [dash.dependencies.Input('Courses-dropdown-Department-semester', 'options')])
def set_courses_dropdown_division_semester_first(available_options):
    return available_options[0]['value']

# department output figure
@app.callback(dash.dependencies.Output('enroll-succ-content-department', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department-semester', 'value')])
def Enroll_succ_department(value1, value2, value3):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    # plot
    # change titlefont and tickfont if needed
    # yaxis2=dict(title='yaxis2 title', titlefont=dict(color='rgb(148, 103, 189)'),
    # tickfont=dict(color='rgb(148, 103, 189)'), overlaying='y', side='right')
    # left bar chart: Success Rate Right line chart: Enrollment
    suc_col = str(value3) + '(SR)'
    enrol_col = str(value3) + '(E)'
    success_trace = go.Bar(x=temp_frame['AcadYr'], y=temp_frame[suc_col], name= 'Success Rate')
    enroll_trace = go.Scatter(x=temp_frame['AcadYr'], y=temp_frame[enrol_col], name= 'Enrollment', yaxis='y2')
    return html.Div([
        dcc.Graph(
            id='enroll-succ-content-division-graph',
            figure={
                'data': [success_trace, enroll_trace],
                'layout': go.Layout(
                    title=dict(text='<b>{} Semester Division {} Department {}</b>'.format(value3, value1, value2)),
                    # title='<b>{} Semester: Course Enrollment and Success Rate</b>'.format(value),
                    xaxis=dict(title='<b>Academic Year<b>'),
                    yaxis=dict(title='<b>Success Rate(%)<b>', range=[0, 100], showgrid=False),
                    yaxis2=dict(title='<b>Enrollment<b>', overlaying='y', side='right',
                                range=[0, 1.2*max(temp_frame[enrol_col])], showgrid=False, tickformat=','),
                    # legend_orientation="h",
                    # legend = dict(orientation="h"),
                    legend={'x': -0.1, 'y': -0.1, "orientation": "h"},
                    margin={'t': 40},
                    width=650,
                    height=350,
                )
            }
        )
    ])

# Discipline Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Courses-dropdown-Discipline', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value')])
def Courses_dropdown_discipline(value1, value2):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2])
    available_discipline_options = list(temp_frame['Disc'].unique())
    available_discipline_options = sorted(available_discipline_options)
    return [{'label': i, 'value': i} for i in available_discipline_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-Discipline', 'value'),
              [dash.dependencies.Input('Courses-dropdown-Discipline', 'options')])
def set_discipline_first(available_options):
    return available_options[0]['value']

# Courses discipline table
@app.callback(dash.dependencies.Output('Courses-content-Discipline', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value')])
def Courses_dropdown_discipline_content(value1, value2, value3):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    return dbc.Table.from_dataframe(temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Courses discipline semester button
@app.callback(dash.dependencies.Output('Courses-dropdown-Discipline-semester', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value')])
def Courses_dropdown_discipline_semester(value1, value2, value3):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3])
    available_semester_options = list(temp_frame['FWS'].unique())
    available_semester_options = sorted(available_semester_options)
    return [{'label': i, 'value': i} for i in available_semester_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-Discipline-semester', 'value'),
              [dash.dependencies.Input('Courses-dropdown-Discipline-semester', 'options')])
def set_courses_dropdown_discipline_semester_first(available_options):
    return available_options[0]['value']

# discipline output figure
@app.callback(dash.dependencies.Output('enroll-succ-content-discipline', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline-semester', 'value')])
def Enroll_succ_discipline(value1, value2, value3, value4):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    # plot
    # change titlefont and tickfont if needed
    # yaxis2=dict(title='yaxis2 title', titlefont=dict(color='rgb(148, 103, 189)'),
    # tickfont=dict(color='rgb(148, 103, 189)'), overlaying='y', side='right')
    # left bar chart: Success Rate Right line chart: Enrollment
    suc_col = str(value4) + '(SR)'
    enrol_col = str(value4) + '(E)'
    success_trace = go.Bar(x=temp_frame['AcadYr'], y=temp_frame[suc_col], name= 'Success Rate')
    enroll_trace = go.Scatter(x=temp_frame['AcadYr'], y=temp_frame[enrol_col], name= 'Enrollment', yaxis='y2')
    return html.Div([
        dcc.Graph(
            id='enroll-succ-content-division-graph',
            figure={
                'data': [success_trace, enroll_trace],
                'layout': go.Layout(
                    title=dict(text='<b>{} Semester Division {} Department {} Discipline {}</b>'.format(value4, value1, value2, value3)),
                    # title='<b>{} Semester: Course Enrollment and Success Rate</b>'.format(value),
                    xaxis=dict(title='<b>Academic Year<b>'),
                    yaxis=dict(title='<b>Success Rate(%)<b>', range=[0, 100], showgrid=False),
                    yaxis2=dict(title='<b>Enrollment<b>', overlaying='y', side='right',
                                range=[0, 1.2*max(temp_frame[enrol_col])], showgrid=False, tickformat=','),
                    # legend_orientation="h",
                    legend={'x': -0.1, 'y': -0.1, "orientation": "h"},
                    margin={'t': 40},
                    width=650,
                    height=350,
                )
            }
        )
    ])

# Courses Number Output dropdown bar and fix default value
@app.callback(dash.dependencies.Output('Courses-dropdown-CoursesNumber', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value')])
def Courses_dropdown_CoursesNumber(value1, value2, value3):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3])
    available_CoursesNumber_options = list(temp_frame['Num'].unique())
    # sort CoursesNumber in order
    available_CoursesNumber_options = sorted(available_CoursesNumber_options)
    return [{'label': i, 'value': i} for i in available_CoursesNumber_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-CoursesNumber', 'value'),
              [dash.dependencies.Input('Courses-dropdown-CoursesNumber', 'options')])
def set_CoursesNumber_first(available_options):
    return available_options[0]['value']

# Courses Number table
@app.callback(dash.dependencies.Output('Courses-content-CoursesNumber', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value'),
               dash.dependencies.Input('Courses-dropdown-CoursesNumber', 'value')])
def Courses_dropdown_CoursesNumber_content(value1, value2, value3, value4):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3], num_list=[value4])
    temp_frame = aggregate_shown_table_enroll_succ(temp_frame)
    return dbc.Table.from_dataframe(temp_frame, striped=True, bordered=True, hover=True, size='sm')

# Courses CoursesNumber semester button
@app.callback(dash.dependencies.Output('Courses-dropdown-CoursesNumber-Term', 'options'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value'),
               dash.dependencies.Input('Courses-dropdown-CoursesNumber', 'value')])
def Courses_dropdown_CoursesNumber_Term(value1, value2, value3, value4):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3], num_list=[value4])
    available_term_options = list(temp_frame['Term'].unique())
    available_term_options = sorted(available_term_options)
    return [{'label': i, 'value': i} for i in available_term_options]
@app.callback(dash.dependencies.Output('Courses-dropdown-CoursesNumber-Term', 'value'),
              [dash.dependencies.Input('Courses-dropdown-CoursesNumber-Term', 'options')])
def set_courses_dropdown_CoursesNumber_Term_first(available_options):
    return available_options[0]['value']

# CoursesNumber output table
@app.callback(dash.dependencies.Output('enroll-succ-content-CoursesNumber', 'children'),
              [dash.dependencies.Input('Courses-dropdown-Division', 'value'),
               dash.dependencies.Input('Courses-dropdown-Department', 'value'),
               dash.dependencies.Input('Courses-dropdown-Discipline', 'value'),
               dash.dependencies.Input('Courses-dropdown-CoursesNumber', 'value'),
               dash.dependencies.Input('Courses-dropdown-CoursesNumber-Term', 'value')])
def Enroll_succ_CoursesNumber(value1, value2, value3, value4, value5):
    temp_frame = courses_subset(Courses_data, div_list=[value1], dept_list=[value2], disc_list=[value3], num_list=[value4], term_list=[value5])
    temp_frame = aggregate_shown_table_enroll_succ_grades(temp_frame)
    return dash_table.DataTable(
        data=temp_frame.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in temp_frame.columns],
        style_table={'maxHeight': '250px', 'overflowY': 'scroll', 'maxWidth': '580px', 'overflowX': 'scroll'},
        style_cell={'fontSize': 15, 'font-family': 'sans-serif', 'text-align': 'center'},
        style_header={'fontWeight': 'bold'},
    )