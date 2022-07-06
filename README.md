### Load CVS file
* df = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/TopProducerDB.csv')

###Print Table
* print(df.to_string())

### Deleting a column in a dataframe in python permanently 
* df.drop(['Email Address Description'],axis=1, inplace=True)

### Renaming multiple columns
* df = dataframe
* df.rename(columns={'columnOne':'newColumn','columnTwo':'newColumn'}, inplace=True)



