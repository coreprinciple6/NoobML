import pandas as pd
import numpy as np

class Feature_engineer:
    '''
    class to hold func for all kinds of processing related to supervised and unsupervised data
    '''
    def __init__(self):
        pass

    def clean(self,data):
        ''' clean csv by filling all nulls with average and removing columns with majority null'''
        for column in data:
            z = data[column].isnull().sum()
            if (z>0):
                #does not write to csv file
                data[column] = np.where(data[column].isna() == True, data[column].mean(), data[column])
        return data

    def map(self,data):
        drop_col =[]
        for column in data:
            try:
                #check if columns can be converted to float
                check = float(data[column][0])
            except:
                #map cols to int
                unique = data[column].unique()
                #if len of unique values more than 3/4 of total len then no mapping
                if len(unique) < (0.75*len(data[column])):
                    idx = 1
                    seen_first = {}
                    for word in data[column]:
                        if word not in seen_first:
                            seen_first[word] = idx
                            idx += 1
                    # move mapped values to dataframe
                    for i,item in enumerate(data[column]):
                        if item in seen_first:
                            data[column][i] = seen_first[item]
                else:
                    drop_col.append(column)

        for item in drop_col:
            idx = np.argwhere(data.columns.isin([item])).ravel()
            data = data.drop(data.columns[idx], axis=1)
        return data

    # find correlation in train csv
    def correlation(self,data,target):
        # for i,item in enumerate(data[target]):
        #     data[target][i] = float(item)

        for column in data:
            if column == target:
                continue
            else:
                result = data[target].corr(data[column])
            print(result)
        #     # if result>0:
            #     print('attention \n',result)
            # else:
            #     print('no')

