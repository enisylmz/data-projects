#Entering to Pandas introduction to pandas for data manipulation (pandasta veri işleme)
#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv CSV file 
import pandas as pd 

arr=pd.array([1,2,3])
print(arr)

df=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(df)

#First 5 rows 'head'

print('First 5 rows \n',df.head())

#Last 5 rows 'tail'
print('Last 5 rows \n',df.tail())

# info about data set that we have 'info'
print(df.info())

# describe about data etc.(count,mean,max,std values) 'describe'

print(df.describe())

#Exercises 
#select a csv files and filter some columns or rows(i will go with same csv file)
selectedColumn = df[['species']] # i selected the colum which is 'species'
print(selectedColumn)

# filter rows

filteredRows = df[(df['sepal_length'] >5.0) & (df['species'] =='setosa')]  # sepal lengthi 5 ten buyuk olan ve speciesi setosaya esit olan satırlı getir 
print(filteredRows)