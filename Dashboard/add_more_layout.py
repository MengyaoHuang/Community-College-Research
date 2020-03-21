from utils import *

# Course Success Rate page layout settings
Add_More_layout = html.Div([
    html.H2('Add More'),
    dcc.RadioItems(
        id='Course-Success-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='Course-Success-content'),
    html.Br(),
    dcc.Link('Go to Awards', href='/Awards', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Course Enrollment and Success Rate', href='/Course-Enrollment-and-Success-Rate', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Go back to home', href='/', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'})
])