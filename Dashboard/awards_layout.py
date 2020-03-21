from utils import *
from awards_data_processing import Awards_data, award_college, available_division_options, blank_table

# Awards page layout settings
Awards_layout = html.Div([
    html.H2('Awards', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Div(children=''' Visualization for Awards statistics at Division, Department and Program level.'''),
    # College level table and figures - fixed across all operations
    html.Div([
        html.Div([
            # generate college level award table
            generate_table(award_college, 150)], style={'width': '49%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='basic-interactions',
                figure={
                    'data': figure_data_modify(award_college),
                    'layout': {
                        'clickmode': 'event+select',
                        'yaxis': {'title': '<b>Number of Awards<b>'},
                        'xaxis': {'title': '<b>Academic Year<b>'},
                        'title': '<b>College Awards</b>'
                    }
                }
            ),

        ], style={'width': '49%', 'float': 'right', 'marginTop': "-50px", 'display': 'inline-block'}),
    ]),
    html.Br(),
    html.Div(children=''' Please choose a specific division for more detailed statistics below: '''),
    html.Br(),
    # set up dropdown bar and connect to interactive graph below
    dcc.Dropdown(
        id='Awards-dropdown-Division',
        options=[{'label': i, 'value': i} for i in available_division_options],
        value='ATP',
        clearable=False,
        style={'height': '30px', 'width': '300px'}
    ),
    # corresponding content followed
    html.Br(),
    html.Div(id='Awards-content-Division'),
    # set up department dropdown bar under given division and show
    html.Br(),
    html.Div(children=''' Please choose a specific department under chosen division: '''),
    html.Br(),
    dcc.Dropdown(
        id='Awards-dropdown-Department',
        clearable=False,
        style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Awards-content-Department'),
    # set up program bar under given department
    html.Br(),
    html.Div(children=''' Please choose a specific program under chosen department: '''),
    html.Br(),
    dcc.Dropdown(
        id='Awards-dropdown-Program',
        clearable=False,
        style={'height': '30px', 'width': '300px'}
    ),
    html.Br(),
    html.Div(id='Awards-content-Program'),

    html.Br(),
    dcc.Link('Go to Course Enrollment and Success Rate', href='/Course-Enrollment-and-Success-Rate',
             style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Go to Add More', href='/Add-More',
             style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Go back to home', href='/',
             style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
])

