from utils import *
from awards_data_processing import available_division_options
from courses_data_processing import Courses_data, available_semester_options

# https://stackoverflow.com/questions/55754626/layout-and-dropdown-menu-in-dash-python

# Course Enrollment and Success page layout settings
Course_Enrollment_Succcess_layout = html.Div([
    html.H2('Course Enrollment and Success Rate', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Div
        (children=''' Visualization for Course Enrollment and Success Rate statistics at Division, Department and Discipline level.'''),
    html.Div(children=''' Here "E" represents "Enrollment" and "SR" represents "Success Rate" '''),
    html.Br(),
    # College level table and figures - fixed across all operations
    html.Div([
        html.Div([
            # generate college level award table
            generate_table(aggregate_shown_table_enroll_succ(Courses_data), 100)], style={'width': '49%' ,'display': 'inline-block'}),
        # Now add a button to choose specific semester
        html.Div([
            html.Div([
                html.Div(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
                dcc.Dropdown(
                    id='Semester-dropdown-overall',
                    options=[{'label': i, 'value': i} for i in available_semester_options],
                    value='Fall',
                    clearable = False,
                    style={'height': '30px', 'width': '150px'}),
            ], style={'display': 'flex'}),
            html.Br(),
            # Add multiple axes figures
            html.Div(id='enroll-succ-content-overall'),
        ], style={'width': '50%' ,'float': 'right', 'marginTop': "-100px", 'display': 'inline-block'}),
    ]),
    # Division
    html.Br(),
    html.Div(children=''' Please choose a specific division for more detailed statistics below: '''),
    html.Br(),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
        id='Courses-dropdown-Division',
        options=[{'label': i, 'value': i} for i in available_division_options],
        value='ATP',
        clearable = False,
        style={'height': '30px', 'width': '300px'}
    ),
    # corresponding division content followed
    html.Br(),
    html.Div(id='Courses-content-Division'),
    html.Div([
        html.Div([
            html.Div(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
            dcc.Dropdown(
                id='Courses-dropdown-Division-semester',
                clearable = False,
                style={'height': '30px', 'width': '150px'}),
        ], style={'display': 'flex'}),
        html.Br(),
        # Add multiple axes figures
        html.Div(id='enroll-succ-content-division'),
    ], style={'width': '50%' ,'float': 'right', 'marginTop': "-430px", 'display': 'inline-block'}),

    # Department
    html.Br(),
    html.Div(children=''' Please choose a specific department for more detailed statistics below: '''),
    html.Br(),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
        id='Courses-dropdown-Department',
        clearable = False,
        style={'height': '30px', 'width': '300px'}
    ),
    # corresponding department content followed
    html.Br(),
    html.Div(id='Courses-content-Department'),
    html.Div([
        html.Div([
            html.Div(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
            dcc.Dropdown(
                id='Courses-dropdown-Department-semester',
                clearable = False,
                style={'height': '30px', 'width': '150px'}),
        ], style={'display': 'flex'}),
        html.Br(),
        # Add multiple axes figures
        html.Div(id='enroll-succ-content-department'),
    ], style={'width': '50%' ,'float': 'right', 'marginTop': "-430px", 'display': 'inline-block'}),

    # Discipline
    html.Br(),
    html.Div(children=''' Please choose a specific discipline for more detailed statistics below: '''),
    html.Br(),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
            id='Courses-dropdown-Discipline',
            clearable = False,
            style={'height': '30px', 'width': '300px'}
    ),
    # corresponding discipline content followed
    html.Br(),
    html.Div(id='Courses-content-Discipline'),
    html.Div([
        html.Div([
            html.Div(children="Please choose a specific semester for visualization: ", style={'margin-right': '1em'}),
            dcc.Dropdown(
                id='Courses-dropdown-Discipline-semester',
                clearable = False,
                style={'height': '30px', 'width': '150px'}),
        ], style={'display': 'flex'}),
        html.Br(),
        # Add multiple axes figures
        html.Div(id='enroll-succ-content-discipline'),
    ], style={'width': '50%' ,'float': 'right', 'marginTop': "-430px", 'display': 'inline-block'}),

    # Add specific courses information
    html.Br(),
    html.Div(children=''' Please choose a specific course number for more detailed statistics below: '''),
    html.Br(),
    # set up dropdown bar and choose courses number
    dcc.Dropdown(
            id='Courses-dropdown-CoursesNumber',
            clearable = False,
            style={'height': '30px', 'width': '300px'}
    ),
    # corresponding courses number content followed
    html.Br(),
    html.Div(id='Courses-content-CoursesNumber'),
    html.Div([
        html.Div(children="Please choose a specific term for visualization: ", style={'margin-right': '1em'}),
        html.Br(),
        dcc.Dropdown(
            id='Courses-dropdown-CoursesNumber-Term',
            clearable = False,
            style={'height': '30px', 'width': '150px'}
        ),
        html.Br(),
        # Add grades table
        html.Div(id='enroll-succ-content-CoursesNumber'),
        ], style={'width': '50%' ,'float': 'right', 'marginTop': "-400px", 'display': 'inline-block'}),

    html.Br(),
    dcc.Link('Go to Awards', href='/Awards', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Go to Add More', href='/Add-More', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Go back to home', href='/', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'})
])

