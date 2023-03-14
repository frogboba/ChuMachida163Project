'''
File contains create_page_home function
'''
from dash import html
from navbar import create_navbar

nav = create_navbar()

header = html.H3('Welcome to the home page!')


def create_page_home():
    '''
    Creates layout for Home page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
    ])
    return layout
