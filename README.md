# Tesco Customer Churn

AutoML Customer Churn Prediction using AutoGluon Framework

## Introduction

This will be using `AutoGluon` framework.

## Business Objective

## Environment Setup

Create an environment
- - -
conda create --name tescochurn python=3.9
- - -

Activate the  environment
- - -
conda activate tescochurn
- - -

Install packages in the environment
- - -
## Note this is for Mac. For Windows users, see official autogluon documentation
pip install torch==1.13.1 torchvision==0.14.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon streamlit jupyter
- - -

### Test your installation as follows:

```bash

(tescochurn) macbook@Gbemilekes-MBP tesco_customer_churn % python
Python 3.9.16 (main, Jan 11 2023, 10:02:19) 
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from autogluon.tabular import TabularDataset, TabularPredictor
```

If that works, you have good installation for `autogluon`.

And then for `Streamlit`

```bash

(tescochurn) macbook@Gbemilekes-MBP tesco_customer_churn % streamlit hello
  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.227:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!

This will automatically pop up on your default browser on this address: http://localhost:8501/





## Project Structure

Insurance Premium
|--README.md
|--images
|--data
|--main.py
|--main.ipynb
|--experimentation.ipynb
|--app.py

## Data Ingestion

## Exploratory Data Analysis (EDA)

## Features Engineering or Processing

## Model Building

## Model Evaluation

## Model Deployment

Deployment will be done on `Streamlit`
