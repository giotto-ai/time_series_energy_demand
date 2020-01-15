import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_time_series(df, y_columns, names, title='', x_axis_title='', y_axis_titles = ['', '']):
    """Plot up to two time series with different y-axes.
    
    Parameters
    ----------
    df : pandas DataFrame
        The dataframe with the data to plot (incl. the x-values as an index)
    y_columns : list
        The columns of the dataframe to use. Maximal length = 2
    names : list
        Names to give to the scatter objects
    title : str, optional, default: ''
        Title to put above the plot
    x_axis_title : str, optional, default: ''
        Title of the x-axis
    y_axis_titles : list, optional, default: ['', '']
        List of y_axis_titles to use. Maximal length = 2
    """
    x = df.index
    y_1 = df[y_columns[0]]
    
    if len(y_columns)==2:
        y_2 = df[y_columns[1]]
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=x, y=y_1, name=names[0]),
        secondary_y=False,
    )
    
    if len(y_columns)==2:
        fig.add_trace(
            go.Scatter(x=x, y=y_2, name=names[1]),
            secondary_y=True,
        )

    # Add figure title
    fig.update_layout(
        title={
        'text':title,
        'y':0.9,
        'x':0.5,
        }
    )

    # Set x-axis title
    fig.update_xaxes(title_text=x_axis_title)

    # Set y-axes titles
    fig.update_yaxes(title_text=y_axis_titles[0], secondary_y=False)
    
    if len(y_columns)==2:
        fig.update_yaxes(title_text=y_axis_titles[1], secondary_y=True)

    return fig