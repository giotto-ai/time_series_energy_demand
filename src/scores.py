from sklearn.metrics import mean_absolute_error, make_scorer
import numpy as np
import pandas as pd


def relative_mean_absolute_error(y_true, y_pred):
    """Calculate the relative mean absolute error

    Parameters
    ----------
    y_true : array-like object
        The reference values
    y_pred : array-like object
        The predicted values
    """
    diff = np.abs(y_true-y_pred)
    return np.mean(diff/y_true)

def calculate_score(y_true, y_pred, metric=mean_absolute_error):
    """Function to calculate a score with a given metric for the output of the GAR model
    
    Parameters
    ----------
    y_true : pandas DataFrame
        The dataframe with the reference data (has NaNs in the lower right half)
    y_pred : pandas DataFrame
        The dataframe with the predicted values, i.e. the output of the GAR model
    metric : object, optional, default: mean_absolute_error (from scikit-learn)
        A function that calculates a score and takes as input y_true an y_pred (e.g.
        from scikit-learn)
    """
    df_results = pd.DataFrame([y_pred.values.flatten(), y_true.values.flatten()]).T
    df_results.columns = ['y_pred', 'y_true']
    df_results.dropna(axis='rows', inplace=True)
    score = metric(df_results['y_true'], df_results['y_pred'])
    return score