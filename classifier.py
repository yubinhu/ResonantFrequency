from joblib import dump, load
import numpy as np
import pandas

from sklearn.ensemble import AdaBoostRegressor



data_path = "../Data/"
features_path = data_path + "default_features/"
annotation_path = data_path + "annotations/"

def sample(df):
    # assume column[0] is the time frame, so always sample it
    columns = df.columns
    l = []
    for i in range(len(columns)):
        if i%8 != 0:
            l.append(columns[i])
    df.drop(columns = l, inplace=True)

def getVectors(feature):
    X1 = np.array([])
    for i in range(30):
        temp = np.array(feature.values.tolist()[i][1:])
        X1 = np.concatenate((X1, temp), axis=0)


    X2 = np.array([])
    for i in range(30,60):
        temp = np.array(feature.values.tolist()[i][1:])
        X2 = np.concatenate((X2, temp), axis=0)
    
    X3 = np.array([])
    for i in range(60,90):
        temp = np.array(feature.values.tolist()[i][1:])
        X3 = np.concatenate((X3, temp), axis=0)

    Xf = np.vstack((X1,X2,X3))
    return Xf

def read(si):
    filename = str(si)+".csv"
    feature = pandas.read_csv(features_path+filename, header=0, sep=';')
    sample(feature)
    # feature.drop(index=feature.index[:30], axis=0, inplace=True)
    return getVectors(feature)





ada = load('ada.joblib')
ada2 = load('ada2.joblib')

def classify(song_id):
    # return True if happy, False if sad
    X = read(song_id)

    y = ada.predict(X)
    

    happy = 0
    
    for i in y:
        if i>0:
            happy+=1
    excited = 0
    y2 = ada2.predict(X)
    for i in y2:
        if i>0:
            excited+=1
    return happy>1, excited>1

result = classify(910)
print(result)