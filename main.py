
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
import sys
import os


# Load CVS File
df = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/TopProducerDB.csv')
df.info()
df.shape
#printing table
print(df.to_string())



## deleting a column in a dataframe in python
# df.drop(['Email Address Description'],axis=1, inplace=True)
# print(df.to_string())

# x = input("x: ")
# # print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# Load Remax Sales CSV file
# how to find the file path using the command prompt
# dir "\realEstateSales.csv/"s
# realEstateSales = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/realEstateSales.csv')
# print(realEstateSales.to_string())
# realEstateSales.info()

