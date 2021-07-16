import pandas as pd
import numpy as np

def Mapping(data):
    for column in data:
        print(column.dtype.name)

    return 6666

def Feature_engineer(train_data,test_data,target):
    for column in train_data:
        z = train_data[column].isnull().sum()
        if (z>0):
            train_data[column] = np.where(train_data[column].isna() == True, train_data[column].mean(), train_data[column])

    for column in test_data:
        z = test_data[column].isnull().sum()
        if (z>0):
            test_data[column] = np.where(test_data[column].isna() == True, test_data[column].mean(), test_data[column])


    for column in train_data:
        df = column
    print(df)
   # if(train_data.dtypes is np.object):
       # print(train_data)

    return z



# find correlation in train csv


# create 2nd train and test dataframe holding features and target


# call training script


# run test data and store result


#calculate accuracy and return statement

