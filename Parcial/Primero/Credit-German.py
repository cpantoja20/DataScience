# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:39:26 2021

@author: sindy
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv ("credit-german.csv", sep=";")
data

data.info()
