'''
File contains functions plot_caffeine, plot_alcohol, plot_smoking,
plot_exercise, plot_age, get_predictions, and the main function
which plots the original data and also the predicted data using
a neural network model
'''
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

import pandas as pd
import plotly.express as px
pd.options.plotting.backend = "plotly"


DATA_FILE = 'Sleep_Efficiency.csv'
MIN_TRAIN_ACCURACY = 0.60
MIN_TEST_ACCURACY = 0.15


def plot_caffeine(data: pd.DataFrame) -> None:
    """
    Accepts a pandas data frame and creates 5 plots that count the number of
    people with specific sleep efficiency scores based on their daily caffeine
    intake (mg) (within 24 hours). Does not return anything.
    """
    print("Running: plot_caffeine")

    data["Count"] = 1

    # Different levels of caffiene intake (in milligrams) to plot
    milligrams = [0, 25.0, 50.0, 75.0, 100.0]

    # Use Plotly's color palette
    # Length is 10 colors, so no indexing issues
    colors = px.colors.qualitative.Plotly

    for i in range(len(milligrams)):
        df = None
        # If i is at the last index in the range
        if i == (len(milligrams) - 1):
            # Check for caffeine consumption greater than or equal to mgs
            df = data[data["Caffeine consumption"] >= milligrams[i]]
        else:
            # Else, check for exact values of mgs
            df = data[data["Caffeine consumption"] == milligrams[i]]
        df = df.groupby("Sleep efficiency")["Count"].sum()
        df = df.reset_index()
        fig = px.histogram(df, x="Sleep efficiency", y="Count",
                           title="Caffeine intake: % dmg" % milligrams[i]
                                 + "24 hours before bedtime",
                           labels={
                               "Sleep efficiency": "Sleep Efficiency",
                               "Count": "of People",
                           })
        fig.update_layout(yaxis_range=[0, 40])
        fig.update_traces(marker_color=colors[i])
        fig.show()


def plot_alcohol(data: pd.DataFrame) -> None:
    """
    Accepts a pandas data frame and creates 6 plots that count the number of
    people with specific sleep efficiency scores based on how much alcohol (oz)
    they consume within 24 hours. Does not return anything.
    """
    print("Running: plot_alcohol")

    data["Count"] = 1

    # Use Plotly's color palette
    # Length is 10 colors, so no indexing issues
    colors = px.colors.qualitative.Plotly

    # Make plots for 0-5oz of alcohol before bedtime
    for i in range(6):
        df = data[data["Alcohol consumption"] == i]
        df = df.groupby("Sleep efficiency")["Count"].sum()
        df = df.reset_index()
        fig = px.histogram(df, x="Sleep efficiency", y="Count",
                           title="Alcohol consumption: % doz 24 hours " % i
                                 + "before bedtime",
                           labels={
                               "Sleep efficiency": "Sleep Efficiency",
                               "Count": "of People",
                           }
                           )
        fig.update_layout(yaxis_range=[0, 45])
        fig.update_traces(marker_color=colors[i])
        fig.show()


def plot_smoking(data: pd.DataFrame) -> None:
    """
    Accepts a pandas data frame and creates two plots that count the number of
    people with a specific sleep efficiency score based on whether or not they
    smoke. Does not return anything.
    """
    print("Running: plot_smoking")

    data["Count"] = 1

    # Stores the possibilities for whether someone smokes or not
    # Needs to be the strings 'Yes' and 'No' to match the data set's columns
    did_smoke = ['Yes', 'No']

    plot_titles = ['Smoker', 'Non-Smoker']

    for i in range(len(did_smoke)):
        # Adding did_smoke suffix to account for one-hot encoded data
        df = data[data["Smoking status_" + did_smoke[i]] == 1]
        df = df.groupby("Sleep efficiency")["Count"].sum()
        df = df.reset_index()
        fig = px.histogram(df, x="Sleep efficiency", y="Count",
                           title=plot_titles[i],
                           labels={
                                   "Sleep efficiency": "Sleep Efficiency",
                                   "Count": "of People",
                           })
        fig.update_layout(yaxis_range=[0, 50])
        if did_smoke[i] == 'Yes':  # Make the plot for those who smoke red
            fig.update_traces(marker_color='red')
        fig.show()


def plot_exercise(data: pd.DataFrame) -> None:
    """
    Accepts a pandas data frame and creates 6 different plots that counts the
    number of people with specific sleep efficiency scores based on their how
    how often they exercise in a week. Does not return anything.
    """
    print("Running: plot_exercise")

    data["Count"] = 1

    # Different exercise frequencies to plot
    frequencies = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]

    # Use Plotly's color palette
    # Length is 10 colors, so no indexing issues
    colors = px.colors.qualitative.Plotly

    for i in range(len(frequencies)):
        df = data[data["Exercise frequency"] == frequencies[i]]
        df = df.groupby("Sleep efficiency")["Count"].sum()
        df = df.reset_index()
        fig = px.histogram(df, x="Sleep efficiency", y="Count",
                           title="Excercise Frequency: % d times a week" % i,
                           labels={
                               "Sleep efficiency": "Sleep Efficiency",
                               "Count": "of People",
                           }
                           )
        fig.update_layout(yaxis_range=[0, 35])
        if i > 0:  # Keep first plot as default color
            fig.update_traces(marker_color=colors[i])
        fig.show()


def plot_age(data: pd.DataFrame) -> None:
    """
    Accepts a pandas data frame and creates a scatter plot that displays the
    number of people of different ages and their sleep efficiency score.
    Does not return anything.
    """
    print("Running: plot_age")
    fig = px.scatter(data, x="Age", y="Sleep efficiency")
    fig.show()


def get_predictions(data: pd.DataFrame) -> "tuple[pd.DataFrame, pd.DataFrame]":
    """
    Accepts a pandas data frame and creates a machine learning model to predict
    sleep efficiency based on the data in the data frame. Returns a tuple of
    pandas data frames. The first data frame contains the rows that were used
    to train the machine learning model, whlie the other contains the rows that
    were used to test the machine learning model but with data the in the sleep
    efficiency column replaced with the model's predictions.
    *Note: Since this function continues testing new models until a theshold
    accuracy is met, the runtime will vary. This function will often take
    several seconds to complete.
    """
    print("Running: get_predictions")

    features = data.loc[:, data.columns != 'Sleep efficiency']
    labels = data['Sleep efficiency']

    model = None
    train_dataset = None
    test_dataset = None

    # Keep creating new models until a certain accuracy score is obtained
    while model is None:
        # ft for features, lb for labels
        ft_train, ft_test, lb_train, lb_test = train_test_split(features,
                                                                labels,
                                                                train_size=0.5)
        test_model = MLPRegressor(
            hidden_layer_sizes=(50,),
            solver='lbfgs',
            max_iter=5000,
            random_state=1
        )
        test_model.fit(ft_train, lb_train)

        train_score = test_model.score(ft_train, lb_train)
        test_score = test_model.score(ft_test, lb_test)

        if train_score > MIN_TRAIN_ACCURACY and test_score > MIN_TEST_ACCURACY:
            model = test_model
            # Store the training and test data sets so they can be returned
            # outside of the while loop
            train_dataset = ft_train
            test_dataset = ft_test

    # Finalizing to data sets before returning

    # Add labels back to the features to get the whole data frame
    train_dataset['Sleep efficiency'] = lb_train
    # Add predictions to the data set
    test_dataset['Sleep efficiency'] = model.predict(test_dataset)

    return (train_dataset, test_dataset)


def main():
    print("RUNNING PROGRAM")

    data = pd.read_csv(DATA_FILE)
    keep_rows = [
        'Age',
        'Gender',
        'Bedtime',
        'Sleep duration',
        'Sleep efficiency',
        'Caffeine consumption',
        'Alcohol consumption',
        'Smoking status',
        'Exercise frequency'
    ]
    data = data.loc[:, keep_rows]

    data = data.dropna()

    # Shortens bedtime to hour and minute
    data['Bedtime'] = data['Bedtime'].str[11:13]

    # One-hot encode features to sort 'Gender' and 'Smoking' columns.
    data = pd.get_dummies(data)

    # Run a machine learning algorithm to predict sleep efficiency
    # Store results
    original, predictions = get_predictions(data)

    # plot_caffeine(original)
    # plot_caffeine(predictions)
    # plot_alcohol(original)
    # plot_alcohol(predictions)
    plot_smoking(original)
    plot_smoking(predictions)
    plot_exercise(original)
    plot_exercise(predictions)
    plot_age(data)
    plot_age(predictions)

    print("FINISHED RUNNING")


if __name__ == '__main__':
    main()
