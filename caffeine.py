'''
File contains plot_caffeine and create_caffeine functions
'''
from navbar import create_navbar
from dash import html, dcc
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


nav = create_navbar()

header = html.H3('Caffeine Consumption and Sleep Efficiency')


def plot_caffeine(csv_file) -> None:
    '''
    Takes a CSV file and converts it into a data frame with
    dropped null values
    Plots each level of Caffeine consumption with Sleep efficiency
    and the number of people at each Sleep efficiency level
    in a histogram plot
    '''
    df = pd.read_csv(csv_file)
    df = df.dropna()
    df["Count"] = 1
    df0 = df[df["Caffeine consumption"] == 0]
    df0 = df0.groupby("Sleep efficiency")["Count"].sum()
    df0 = df0.reset_index()
    global fig0
    fig0 = px.histogram(df0, x="Sleep efficiency", y="Count",
                        title="Caffeine consumption: 0ml 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig0.update_layout(yaxis_range=[0, 90])
    df25 = df[df["Caffeine consumption"] == 25]
    df25 = df25.groupby("Sleep efficiency")["Count"].sum()
    df25 = df25.reset_index()
    global fig25
    fig25 = px.histogram(df25, x="Sleep efficiency", y="Count",
                         title="Caffeine consumption: 25ml 24 hours \
                                before bedtime",
                         labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                                })
    fig25.update_layout(yaxis_range=[0, 90])
    fig25.update_traces(marker_color='red')
    df50 = df[df["Caffeine consumption"] == 50]
    df50 = df50.groupby("Sleep efficiency")["Count"].sum()
    df50 = df50.reset_index()
    global fig50
    fig50 = px.histogram(df50, x="Sleep efficiency", y="Count",
                         title="Caffeine consumption: 50ml 24 hours \
                                before bedtime",
                         labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                                })
    fig50.update_layout(yaxis_range=[0, 90])
    fig50.update_traces(marker_color='green')
    df75 = df[df["Caffeine consumption"] == 75]
    df75 = df75.groupby("Sleep efficiency")["Count"].sum()
    df75 = df75.reset_index()
    global fig75
    fig75 = px.histogram(df75, x="Sleep efficiency", y="Count",
                         title="Caffeine consumption: 75ml 24 hours \
                                before bedtime",
                         labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                                })
    fig75.update_layout(yaxis_range=[0, 90])
    fig75.update_traces(marker_color='purple')
    df100 = df[df["Caffeine consumption"] >= 100]
    df100 = df100.groupby("Sleep efficiency")["Count"].sum()
    df100 = df100.reset_index()
    global fig100
    fig100 = px.histogram(df100, x="Sleep efficiency", y="Count",
                          title="Caffeine consumption: at least 100ml 24 hours \
                                 before bedtime",
                          labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                                 }
                          )
    fig100.update_layout(yaxis_range=[0, 90])
    fig100.update_traces(marker_color='pink')


plot_caffeine("Sleep_Efficiency.csv")


def create_caffeine():
    '''
    Creates layout for Caffeine page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
        dcc.Graph(
                  id='graph-1c',
                  figure=fig0
                 ),
        dcc.Graph(
                  id='graph-2c',
                  figure=fig25
                 ),
        dcc.Graph(
                  id='graph-3c',
                  figure=fig50
                 ),
        dcc.Graph(
                  id='graph-4c',
                  figure=fig75
                 ),
        dcc.Graph(
                  id='graph-5c',
                  figure=fig100
                 ),
    ])
    return layout
