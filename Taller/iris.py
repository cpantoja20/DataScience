# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib as plt

data = pd.read_csv ("iris.data.csv", names= ['SepalLength','sepalWidth','PetalLenght','PetalWidth','Species'] , header=None)
data

IQR = data['SepalLength'].quantile(0.75) - data['SepalLength'].quantile(0.25)

upper = data['SepalLength'].quantile(0.75) +1.5*IQR

lower = data['SepalLength'].quantile(0.25) -1.5*IQR

atipicos = data['SepalLength'][(data['SepalLength']>upper)|(data['SepalLength']<lower)]

atipicos
IQR_SW = data['sepalWidth'].quantile(0.75) - data['sepalWidth'].quantile(0.25)

upper_SW = data['sepalWidth'].quantile(0.75) +1.5*IQR

lower_SW = data['sepalWidth'].quantile(0.25) -1.5*IQR

atipicos_SW = data['sepalWidth'][(data['sepalWidth']>upper)|(data['sepalWidth']>lower)]

atipicos_SW
