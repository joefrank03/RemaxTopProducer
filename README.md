### Load CVS file
* df = pd.read_csv('/Users/ferna/PycharmProjects/RemaxTopProducer/TopProducerDB.csv')

### UTF Encoding
* df = pd.read_csv("file.cvs",encoding='utf8')

### Changing columns to upper case
* df.columns = df.columns.str.upper()

### check for missing data
* print(df.isnull().any())
* false = no missing data, true = missing data

### Checking the count for NaN in each column
* print(df.isnull().sum())

### Columns with NAN using Integer
* df.isnull().sum()

###Print Table
* print(df.to_string())

### Deleting a column in a dataframe in python permanently 
* df.drop(['Email Address Description'],axis=1, inplace=True)

### Renaming multiple columns
* df = dataframe
* df.rename(columns={'columnOne':'newColumn','columnTwo':'newColumn'}, inplace=True)


