'''
File contains plot_smoking and create_smoking functions
'''
from navbar import create_navbar
from dash import html, dcc
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


nav = create_navbar()

header = html.H3('Smoking Status and Sleep Efficiency')


def plot_smoking(csv_file) -> None:
    '''
    Takes a CSV file and converts it into a data frame with
    dropped null values
    Plots Smoking status with Sleep efficiency
    and the number of people at each Sleep efficiency level
    in a histogram plot
    '''
    df = pd.read_csv(csv_file)
    df = df.dropna()
    df["Count"] = 1
    # smoked
    dfyes = df[df["Smoking status"] == "Yes"]
    dfyes = dfyes.groupby("Sleep efficiency")["Count"].sum()
    dfyes = dfyes.reset_index()
    global figyes
    figyes = px.histogram(dfyes, x="Sleep efficiency", y="Count",
                          title="Smoker",
                          labels={
                                 "Sleep efficiency": "Sleep Efficiency",
                                 "Count": "of People",
                          })
    figyes.update_layout(yaxis_range=[0, 100])
    figyes.update_traces(marker_color='red')
    # did not smoke
    df = df[df["Smoking status"] == "No"]
    dfno = df.groupby("Sleep efficiency")["Count"].sum()
    dfno = dfno.reset_index()
    global figno
    figno = px.histogram(dfno, x="Sleep efficiency", y="Count",
                         title="Non-Smoker",
                         labels={
                                 "Sleep efficiency": "Sleep Efficiency",
                                 "Count": "of People",
                          })
    figno.update_layout(yaxis_range=[0, 100])


plot_smoking("Sleep_Efficiency.csv")


def create_smoking() -> dcc:
    '''
    Creates layout for Smoking page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
        dcc.Graph(
                  id='graph-1',
                  figure=figyes
                 ),
        dcc.Graph(
                  id='graph-2',
                  figure=figno
                 ),
    ])
    return layout
