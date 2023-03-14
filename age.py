'''
File contains plot_age and create_age functions
'''
from navbar import create_navbar
from dash import html, dcc
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


nav = create_navbar()

header = html.H3('Age and Sleep Efficiency')


def plot_age(csv_file) -> None:
    '''
    Takes a CSV file and converts it into a data frame with
    dropped null values
    Plots the Age column with the Sleep efficiency column
    in a scatter plot
    '''
    df = pd.read_csv(csv_file)
    df = df.dropna()
    global fig
    fig = px.scatter(df, x="Age", y="Sleep efficiency")


plot_age("Sleep_Efficiency.csv")


def create_age():
    '''
    Creates layout for Age page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
        dcc.Graph(
                  id='graph-1',
                  figure=fig
                 ),
        html.Div(id='tabs-example-content-1')
    ])
    return layout
