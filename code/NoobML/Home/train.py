import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR

class Train:
    def __init__(self):
        self.model_rf =RandomForestClassifier(n_estimators=20,criterion='gini') #for supervised classification
        self.model_svr = SVR(kernel = 'rbf')    #for supervised regression

    def random_forest(self,trainset, testset, target):
        idx = np.argwhere(trainset.columns.isin([target])).ravel()
        xtrain = trainset.drop(trainset.columns[idx], axis=1)

        ytrain = []
        extracted_col = trainset[target]
        ytrain = ytrain['verdict':extracted_col[1]]
        print(ytrain)
        return 0
        #self.model_rf.fit()



