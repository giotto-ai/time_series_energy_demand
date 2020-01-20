# Energy Demand Prediction in Switzerland

## What is it?
This repository contains the code for the blog post 'TITLE HERE' [LINK HERE] where we use the Python time series library giotto-time [https://github.com/giotto-ai/giotto-time] to predict the mean daily energy demand (in MW) in Switzerland 21 days ahead using a generalized autoregression model. 

The notebook 'energy_demand_time_series.ipynb' showcases the most important functionalities of giotto-time and how to use them to:
* remove trends and deal with seasonalities
* make a causality test and thereby find the ideal shift between one time series and another to make predictions.
* easily create a range of different features
* use a generalized autoregression model to make predictions using the 'fit/predict' methods.

## Getting started
You want to dive right in? The easiest way to get started is to create a conda environment as follows:
```
conda create python=3.7 --name time -y
conda activate time
pip install -r requirements.txt
```
Then the notebook 'TITLE HERE' will walk you through the analysis and the prediction steps.

## Results

![alt text](data/figures/predictions.png)
Figure here [actual values vs. predictions], score, 
