
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd


## Load CVS File
df = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/TopProducerDB.csv')
#print(df);

## printing table
## print(df.to_string())

## deleting a column in a dataframe in python
del df['Email Address Description']
df.shape
df.info()


