from sklearn.metrics import mean_absolute_error, make_scorer
import numpy as np
import pandas as pd


def relative_mean_absolute_error(y_true, y_pred):
    diff = np.abs(y_true-y_pred)
    return np.mean(diff/y_true)

def calculate_score(y_true, y_pred, metric=mean_absolute_error):
    df_results = pd.DataFrame([y_pred.values.flatten(), y_true.values.flatten()]).T
    df_results.columns = ['y_pred', 'y_true']
    df_results.dropna(axis='rows', inplace=True)
    score = metric(df_results['y_true'], df_results['y_pred'])
    return score