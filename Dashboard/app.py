import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# we're adding the elements through a callback, so we can ignore the exception
app.config.suppress_callback_exceptions = True