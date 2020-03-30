import dash
import dash_auth
import dash_bootstrap_components as dbc

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'wcc': 'ir123'
}

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)
# we're adding the elements through a callback, so we can ignore the exception
app.config.suppress_callback_exceptions = True

