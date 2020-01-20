import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_time_series(df, y_columns, title='', x_axis_title='', y_axis_title = ''):
    """Plot different time series with the same y-axis.
    
    Parameters
    ----------
    df : pandas DataFrame
        The dataframe with the data to plot (incl. the x-values as an index)
    y_columns : list
        The columns of the dataframe to use. Maximal length = 2
    title : str, optional, default: ''
        Title to put above the plot
    x_axis_title : str, optional, default: ''
        Title of the x-axis
    y_axis_titles : list, optional, default: ['', '']
        List of y_axis_titles to use. Maximal length = 2
    """
    x = df.index
    
    fig = make_subplots(specs=[[{"secondary_y": False}]])

    for i in y_columns:
        # Add traces
        fig.add_trace(
            go.Scatter(x=x, y=df[i].values, name=i),
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
    fig.update_yaxes(title_text=y_axis_title)

    return fig