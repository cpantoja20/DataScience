import pandas as pd
import numpy as np


data = pd.read_csv("bank-full.csv")

data["marital"].plot(kind='hist')
plt.show()