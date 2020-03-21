from utils import *
from awards_data_processing import available_division_options
from courses_data_processing import Courses_data, available_semester_options
from app import app

# overall output figure
@app.callback(dash.dependencies.Output('enroll-succ-content-overall', 'children'),
              [dash.dependencies.Input('Semester-dropdown-overall', 'value')])
def Enroll_succ_overall(value):
    # filter out specific semester subset
    # overall figure must have all possible semesters
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
                    title=dict(text='<b>{} Semester Overall College</b>'.format(value)),
                    # title='<b>{} Semester: Course Enrollment and Success Rate</b>'.format(value),
                    xaxis=dict(title='<b>Academic Year<b>'),
                    yaxis=dict(title='<b>Success Rate(%)<b>', range=[0, 100], showgrid=False),
                    yaxis2=dict(title='<b>Enrollment<b>', overlaying='y', side='right',
                                range=[0, 1.2*max(temp_frame[enrol_col])], showgrid=False, tickformat=','),
                    # legend_orientation="h",
                    legend=dict(orientation="h"),
                    margin=dict(t=35, b=0),
                    height=400
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
    return html.Div([
        html.Div([generate_table(temp_frame, 100)], style={'width': '49%','display': 'inline-block'})
    ])

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
                    legend = dict(orientation="h"),
                    margin=dict(t=35, b=0),
                    height=400
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
    return html.Div([
        html.Div([generate_table(temp_frame, 100)], style={'width': '49%','display': 'inline-block'})
    ])

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
                    legend = dict(orientation="h"),
                    margin=dict(t=35, b=0),
                    height=400
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
    return html.Div([
        html.Div([generate_table(temp_frame, 100)], style={'width': '49%','display': 'inline-block'})
    ])

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
                    legend = dict(orientation="h"),
                    margin=dict(t=35, b=0),
                    height=400
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
    return html.Div([
        html.Div([generate_table(temp_frame, 100)], style={'width': '49%','display': 'inline-block'})
    ])

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
        style_table={'maxHeight': '250px', 'overflowY': 'scroll', 'maxWidth': '700px', 'overflowX': 'scroll'},
        style_cell={'fontSize': 15, 'font-family': 'sans-serif', 'text-align': 'center'},
        style_header={'fontWeight': 'bold'},
    )
    """
    return html.Div([
            html.Div([generate_table(temp_frame, 100)], style={'width': '49%','display': 'inline-block'})
    ])
    """

