from utils import *
from awards_data_processing import Awards_data, award_college, available_division_options, blank_table
from courses_data_processing import Courses_data
from awards_callbacks import *
from app import app
from awards_layout import Awards_layout
from add_more_layout import Add_More_layout
from courses_layout import Course_Enrollment_Succcess_layout
import awards_callbacks
import add_more_callbacks
import courses_callbacks
# https://dash.plot.ly/urls

app.layout = html.Div([
     # add multiple pages
     dcc.Location(id='url', refresh=True),
     html.Div(id='page-content')
])
# Set up initial page for Awards, Course Enrollment, Course Success Rate links
index_page = html.Div([
    # add markdown text
    html.H2("Washtenaw Community College", style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.H3("Institutional Research Dashboard", style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Div([
        html.P('Check out Washtenaw Community College official website for more colllege information if needed!'),
        html.P('This Dashboard contains statistical information related to Awards, Course Enrollment and Course Success Rate.')]),
    dcc.Link('Awards', href='/Awards', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Course Enrollment and Success Rate', href='/Course-Enrollment-and-Success-Rate', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
    html.Br(),
    dcc.Link('Add More', href='/Add-More', style={'font-family': 'Times New Roman, Times, serif', 'font-weight': 'bold'}),
])

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Awards':
        return Awards_layout
    elif pathname == '/Course-Enrollment-and-Success-Rate':
        return Course_Enrollment_Succcess_layout
    elif pathname == '/Add-More':
        return Add_More_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=False)