'''
File contains plot_alcohol and create_alcohol functions
'''
from navbar import create_navbar
from dash import html, dcc
import plotly.express as px
import pandas as pd
pd.options.plotting.backend = "plotly"


nav = create_navbar()

header = html.H3('Alcohol Consumption and Sleep Efficiency')


def plot_alcohol(csv_file):
    '''
    Takes a CSV file and converts it into a data frame with
    dropped null values
    Plots each level of Alcohol consumption with Sleep efficiency
    and the number of people at each Sleep efficiency level
    in a histogram plot
    '''
    df = pd.read_csv(csv_file)
    df = df.dropna()
    df["Count"] = 1
    df0 = df[df["Alcohol consumption"] == 0]
    df0 = df0.groupby("Sleep efficiency")["Count"].sum()
    df0 = df0.reset_index()
    global fig0
    fig0 = px.histogram(df0, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 0oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig0.update_layout(yaxis_range=[0, 90])
    df1 = df[df["Alcohol consumption"] == 1]
    df1 = df1.groupby("Sleep efficiency")["Count"].sum()
    df1 = df1.reset_index()
    global fig1
    fig1 = px.histogram(df1, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 1oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig1.update_layout(yaxis_range=[0, 90])
    fig1.update_traces(marker_color='red')
    df2 = df[df["Alcohol consumption"] == 2]
    df2 = df2.groupby("Sleep efficiency")["Count"].sum()
    df2 = df2.reset_index()
    global fig2
    fig2 = px.histogram(df2, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 2oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig2.update_layout(yaxis_range=[0, 90])
    fig2.update_traces(marker_color='green')
    df3 = df[df["Alcohol consumption"] == 3]
    df3 = df3.groupby("Sleep efficiency")["Count"].sum()
    df3 = df3.reset_index()
    global fig3
    fig3 = px.histogram(df3, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 3oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig3.update_layout(yaxis_range=[0, 90])
    fig3.update_traces(marker_color='purple')
    df4 = df[df["Alcohol consumption"] == 4]
    df4 = df4.groupby("Sleep efficiency")["Count"].sum()
    df4 = df4.reset_index()
    global fig4
    fig4 = px.histogram(df4, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 4oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig4.update_layout(yaxis_range=[0, 90])
    fig4.update_traces(marker_color='pink')
    df5 = df[df["Alcohol consumption"] == 5]
    df5 = df5.groupby("Sleep efficiency")["Count"].sum()
    df5 = df5.reset_index()
    global fig5
    fig5 = px.histogram(df5, x="Sleep efficiency", y="Count",
                        title="Alcohol consumption: 5oz 24 hours \
                               before bedtime",
                        labels={
                            "Sleep efficiency": "Sleep Efficiency",
                            "Count": "of People",
                        }
                        )
    fig5.update_layout(yaxis_range=[0, 90])
    fig5.update_traces(marker_color='orange')
    global figpredict
    figpredict = px.histogram(df5, x="Sleep efficiency", y="Count",
                              title="Alcohol consumption: 5oz 24 hours \
                                     before bedtime",
                              labels={
                                "Sleep efficiency": "Sleep Efficiency",
                                "Count": "of People",
                                     })
    fig5.update_layout(yaxis_range=[0, 90])
    fig5.update_traces(marker_color='orange')


plot_alcohol("Sleep_Efficiency.csv")


def create_alcohol():
    '''
    Creates layout for Alcohol page on Dash app
    Returns the layout
    '''
    layout = html.Div([
        nav,
        header,
        dcc.Graph(
                  id='graph-0',
                  figure=fig0
                 ),
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
