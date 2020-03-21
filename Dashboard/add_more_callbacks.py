from utils import *
from awards_data_processing import Awards_data, award_college, available_division_options, blank_table
from app import app

@app.callback(dash.dependencies.Output('Course-Success-content', 'children'),
              [dash.dependencies.Input('Course-Success-radios', 'value')])
def Course_Success_radios(value):
    return 'You have selected "{}"'.format(value)