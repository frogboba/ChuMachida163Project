'''
File contains display_page function which puts the Dash app together
and displays each graph and corresponding text
'''
from dash import html, dcc
from dash.dependencies import Input, Output
from home import create_page_home
from app import app
from alcohol import create_alcohol
from caffeine import create_caffeine
from exercise import create_exercise
from age import create_age
from smoking import create_smoking

server = app.server
app.config.suppress_callback_exceptions = True

global DATA_FILE
DATA_FILE = "Sleep_Efficiency.csv"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    '''
    Calls and returns each file with a graph
    '''
    if pathname == '/caffeine':
        return create_caffeine()
    if pathname == '/alcohol':
        return create_alcohol()
    if pathname == '/smoking':
        return create_smoking()
    if pathname == '/exercise':
        return create_exercise()
    if pathname == '/age':
        return create_age()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
