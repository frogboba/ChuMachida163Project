'''
File contains plot_exercise and create_exercise functions
'''
from navbar import create_navbar
from dash import html, dcc
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


nav = create_navbar()

header = html.H3('Weekly Excercise Frequency and Sleep Efficiency')


def plot_exercise(csv_file) -> None:
    '''
    Takes a CSV file and converts it into a data frame with
    dropped null values
    Plots each level of Exercise frequency with Sleep efficiency
    and the number of people at each Sleep efficiency level
    in a histogram plot
    '''
    df = pd.read_csv(csv_file)
    df = df.dropna()
    df["Count"] = 1
    # 0 times excercised in a week
    df0 = df[df["Exercise frequency"] == 0.0]
    df0 = df0.groupby("Sleep efficiency")["Count"].sum()
    df0 = df0.reset_index()
    global fig0
    fig0 = px.histogram(df0, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 0 times a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig0.update_layout(yaxis_range=[0, 50])
    df1 = df[df["Exercise frequency"] == 1.0]
    df1 = df1.groupby("Sleep efficiency")["Count"].sum()
    df1 = df1.reset_index()
    global fig1
    fig1 = px.histogram(df1, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 1 time a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig1.update_layout(yaxis_range=[0, 50])
    fig1.update_traces(marker_color='red')
    df2 = df[df["Exercise frequency"] == 2.0]
    df2 = df2.groupby("Sleep efficiency")["Count"].sum()
    df2 = df2.reset_index()
    global fig2
    fig2 = px.histogram(df2, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 2 times a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig2.update_layout(yaxis_range=[0, 50])
    fig2.update_traces(marker_color='green')
    df3 = df[df["Exercise frequency"] == 3.0]
    df3 = df3.groupby("Sleep efficiency")["Count"].sum()
    df3 = df3.reset_index()
    global fig3
    fig3 = px.histogram(df3, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 3 times a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig3.update_layout(yaxis_range=[0, 50])
    fig3.update_traces(marker_color='purple')
    df4 = df[df["Exercise frequency"] == 4.0]
    df4 = df4.groupby("Sleep efficiency")["Count"].sum()
    df4 = df4.reset_index()
    global fig4
    fig4 = px.histogram(df4, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 4 times a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig4.update_layout(yaxis_range=[0, 50])
    fig4.update_traces(marker_color='pink')
    df5 = df[df["Exercise frequency"] == 5.0]
    df5 = df5.groupby("Sleep efficiency")["Count"].sum()
    df5 = df5.reset_index()
    global fig5
    fig5 = px.histogram(df5, x="Sleep efficiency", y="Count",
                        title="Excercise Frequency: 5 times a week",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig5.update_layout(yaxis_range=[0, 50])
    fig5.update_traces(marker_color='orange')


plot_exercise("Sleep_Efficiency.csv")


def create_exercise() -> dcc:
    '''
    Creates layout for Exercise page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
        dcc.Graph(
                  id='graph-1',
                  figure=fig1
                 ),
        dcc.Graph(
                  id='graph-2',
                  figure=fig2
                 ),
        dcc.Graph(
                  id='graph-3',
                  figure=fig3
                 ),
        dcc.Graph(
                  id='graph-4',
                  figure=fig4
                 ),
        dcc.Graph(
                  id='graph-5',
                  figure=fig5
                 ),
    ])
    return layout
