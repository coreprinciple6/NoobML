import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score
#import cPickle

class Train:
    def __init__(self):
        self.model_rf = RandomForestClassifier(n_estimators=20,criterion='gini') #for supervised classification
        self.model_svr = SVR(kernel = 'rbf')    #for supervised regression

    def random_forest(self,trainset, testset, target):
        # idx = np.argwhere(trainset.columns.isin([target])).ravel()
        # copyset = trainset.copy()
        val = []
        for name in trainset:
            if name==target:
                xtrain = trainset.drop([target], axis=1)
                xtest = testset.drop([target], axis=1)
            else:
                val.append(name)
        ytrain = trainset.drop(val, axis=1)
        ytest = testset.drop(val, axis=1)

        self.model_rf.fit(xtrain,ytrain)

        # score = self.eval(self.model_rf,xtest,ytest)
        # print(score)

        return 0

    def eval(self, model, xtest, ytest):
            ypred = model.predict(xtest)
            score = accuracy_score(ytest,ypred)
            #smth to do with graph
            return score

    def inference(self, model, xtest):
            ypred = model.predict(xtest)
            return ypred

    # def store_model(self,model):
    #     path =
    #     with open('path/to/file/.pkl/.pth/', 'wb') as f:
    #         cPickle.dump(rf, f)
    #
    # def load_model(self,model):
    #     with open('path/to/file', 'rb') as f:
    #         rf = cPickle.load(f)
    #
    #     preds = rf.predict(new_X)

