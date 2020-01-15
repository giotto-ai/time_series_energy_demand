# Data handling
import pandas as pd

# Statistical tools
from statsmodels.tsa.stattools import adfuller


def dickey_fuller_test(ts, threshold=1):
    """
    Perform a Dickey Fuller test to test for stationarity.

    Parameters
    ----------
    ts : pandas series or numpy array
        A time series
    
    threshold : int, default 1
        Which critical value to use (in percent). Can be either 1, 5 or 10.

    Returns
    -------
    df : pandas DataFrame
        The results with rows: Test statistic, p-value, number of lags used, number of observations used,
        critical value 1%, critical value 5%, critical value 10%.

    """
    print('Results of Dickey-Fuller Test:')

    dickey_fuller = adfuller(ts, autolag='AIC')
    results = [i for i in dickey_fuller[0:4]]
    critical_labels = [i[0] for i in list(dickey_fuller[4].items())]
    critical_labels = ["critical value " + i for i in critical_labels]
    critical_values = [i[1] for i in list(dickey_fuller[4].items())]

    labels = ["Test statistic", "p-value", "Numb. lags used", "Numb. observations used"]
    labels += critical_labels
    results += critical_values

    df = pd.DataFrame(results, index=labels, columns=["results"])

    index_dict = {1: -3, 5: -2, 10: -1}

    if df.loc[labels[index_dict[threshold]]].values[0] < results[0]:
        print("Time series is not stationary.")
    else:
        print("Time series is stationary.")
        
    return df
