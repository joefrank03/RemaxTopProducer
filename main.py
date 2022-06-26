
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd


## Load CVS File
df = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/TopProducerDB.csv')
print(df);

## Loading iris dataset
print(df.to_string())



