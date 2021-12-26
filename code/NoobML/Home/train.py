import pandas as pd
import numpy as np

class Feature_engineer:
    def __init__(self):
        pass

    def Mapping(data):
        for column in data:
            print(column.dtype.name)

        return 6666

    def clean(self,data):
        ''' clean csv by filling all nulls with average and removing columns with majority null'''
        for column in data:
            z = data[column].isnull().sum()
            if (z>0):
                #does not write to csv file
                data[column] = np.where(data[column].isna() == True, data[column].mean(), data[column])
        return data
    def map(self,data):
        for column in data:
            if isinstance(data[column], str):
                print(data[column].dtype)
                print('WHY IS THIS HAPPENING')


       #  for column in train_data:
       #      df = column
       #  print(df)
       # # if(train_data.dtypes is np.object):
       #     # print(train_data)
       #
       #  return z



    # find correlation in train csv


    # create 2nd train and test dataframe holding features and target


    # call training script


    # run test data and store result


    #calculate accuracy and return statement

