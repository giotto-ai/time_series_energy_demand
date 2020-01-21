<img src="https://www.giotto.ai/static/vector/logo.svg" alt="logo" width="850"/>

# Energy Demand Prediction in Switzerland with giotto-time

## What is it?
This repository contains the code for the blog post 'Energy Demand Prediction in Switzerland with giotto-time' [LINK HERE] where we use the Python time series library giotto-time [https://github.com/giotto-ai/giotto-time] to predict the mean daily energy demand (in megawatts) in Switzerland 21 days ahead using generalized autoregression models and linear regression with custom loss functions, both of which are provided by giotto-time. 

The 
'energy_demand_time_series.ipynb' showcases the most important functionalities of giotto-time and how to use them to:
* remove trends and deal with seasonalities
* make a causality test and thereby find the ideal shift between one time series and another to make predictions.
* easily create a range of different features
* use a generalized autoregression model to make predictions using the 'fit/predict' methods.

## Getting started
You want to start right away? The easiest way to get started is to create a conda environment as follows:
```
conda create python=3.7 --name time -y
conda activate time
pip install -r requirements.txt
```
Then the notebook 'energy_demand_time_series.ipynb' will walk you through the analysis and the prediction steps.

## Results
In this section we present the results. The figure below shows the reference values as well as the predictions for one of the models shown in the notebook. 

![alt text](data/figures/comparison.png)


An important point for this directory is to show different models giotto-time has to offer. In the table below we list the results for different models and different metrics.

|                               | rel. mean abs. error   | rel. mean squared error   | max. error   | SMAPE   | coeff. of determination   |
|:------------------------------|:-----------------------|:--------------------------|:-------------|:--------|:--------------------------|
| baseline                      | 0.14                   | 146.09                    | 2206.57      | 0.14    | -0.0                      |
| GAR Random Forest             | 0.08                   | 52.67                     | 1588.69      | 0.08    | 0.64                      |
| GAR Gradient Boosting         | 0.08                   | 47.53                     | 1579.78      | 0.07    | 0.68                      |
| GAR Lin. Reg.                 | 0.07                   | 41.65                     | 1499.79      | 0.07    | 0.73                      |
| Lin. Reg. with max error loss | 0.16                   | 174.82                    | 2319.84      | 0.18    | -0.23                     |
| Lin. Reg. with smape loss     | 0.08                   | 46.53                     | 1420.57      | 0.08    | 0.7                       |

---

