# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv ("iris.data.csv", names= ['SepalLength','sepalWidth','PetalLenght','PetalWidth','Species'] , header=None)
data

IQR = data['SepalLength'].quantile(0.75) - data['SepalLength'].quantile(0.25)

upper = data['SepalLength'].quantile(0.75) +1.5*IQR

lower = data['SepalLength'].quantile(0.25) -1.5*IQR

atipicos = data['SepalLength'][(data['SepalLength']>upper)|(data['SepalLength']<lower)]

atipicos
IQR_SW = data['sepalWidth'].quantile(0.75) - data['sepalWidth'].quantile(0.25)

upper_SW = data['sepalWidth'].quantile(0.75) +1.5*IQR_SW

lower_SW = data['sepalWidth'].quantile(0.25) -1.5*IQR_SW 

atipicos_SW = data['sepalWidth'][(data['sepalWidth']>upper_SW)|(data['sepalWidth']>lower_SW)]

atipicos_SW

IQR_PL = data['PetalLenght'].quantile(0.75) - data['PetalLenght'].quantile(0.25)

upper_PL = data['PetalLenght'].quantile(0.75) +1.5*IQR_PL

lower_PL = data['PetalLenght'].quantile(0.25) -1.5*IQR_PL 

atipicos_PL = data['PetalLenght'][(data['PetalLenght']>upper_PL)|(data['PetalLenght']>lower_PL)]

atipicos_PL

IQR_PW = data['PetalWidth'].quantile(0.75) - data['PetalWidth'].quantile(0.25)

upper_PW = data['PetalWidth'].quantile(0.75) +1.5*IQR_PW

lower_PW = data['PetalWidth'].quantile(0.25) -1.5*IQR_PW 

atipicos_PW = data['PetalWidth'][(data['PetalWidth']>upper_PW)|(data['PetalWidth']>lower_PW)]

atipicos_PW

data.info()

data['SepalLength'].plot(kind='hist')
plt.show()

data['SepalLength'].plot(kind='box')
plt.show()

data.plot(kind='box')
plt.show()

