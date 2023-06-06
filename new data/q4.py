import seaborn as sb
import sklearn as sk
import numpy as np
import pandas as pd 
import random
import matplotlib.pyplot as plt
from math import *
from decimal import Decimal
from sklearn.compose import ColumnTransformer as transformer
from sklearn.preprocessing import OneHotEncoder as encoder
from sklearn.decomposition import PCA as compnentAnalysis






def minkowskiDistance(centeroid,point):
    centerValue=[]
    pointValue=[]
    for i in centeroid:
        centerValue.append(i)
    for i in point:
        pointValue.append(i)
    totalValue=0
    for i in range(0,len(centerValue)):
        totalValue=totalValue+((centerValue[i]-pointValue[i])**2)
    return sqrt(totalValue)

def isEqual(center,previousCenter):
    previous=[]
    cen=[]
    for i in previousCenter:
        previous.append(i)
    for i in center:
        cen.append(i)
    for i in range(0,len(previous)):
        if previous[i]!=cen[i]:
            return False
    
    return True

def getErrorValue(centeroids,data,totalClusters,totalError):
    allPoints=data.shape[0]
    for i in range(0,allPoints):
        totalError=totalError+minkowskiDistance(centeroids.loc[data['centeroid'][i]],data.loc[i])
    return sqrt(totalError)

def kmean(totalClusters,data):
    similar=0
    centeroids=data.sample(totalClusters)
    centeroids.reset_index(drop=True,inplace=True)
    allPoints=data.shape[0]
    data["centeroid"]=""
    data["Distance"]=""
    
    while similar!=totalClusters:
        for i in range(0,allPoints):
            distances=[]
            for j in range(0,totalClusters):
                distances.append( minkowskiDistance(centeroids.loc[j],data.loc[i]) )
            data.at[i, 'centeroid'] = distances.index(min(distances))
            data.at[i, 'Distance'] = min(distances)
        #print(data)
        Mean=data[data["centeroid"]==0].mean()
        similar=0
        for i in range(0,totalClusters):
            Mean=data[data["centeroid"]==i].mean()
            Mean.drop('centeroid', inplace=True)
            Mean.drop('Distance', inplace=True)
            if isEqual(Mean,centeroids.loc[i]):
                similar+=1
            else:
                centeroids.iloc[i]=Mean
        print("SEARCHING ",similar)
       
    errors.append(getErrorValue(centeroids,data.copy(),totalClusters,0))
    print("\n******************** CLUSTORS FOUND ************************")
    return data






def printScatterPlot(totalClusters,data,trn):
    reduced_data = compnentAnalysis(n_components=2).fit_transform(trn)
    results = pd.DataFrame(reduced_data,columns=['Record1','Record2'])
    results["centeroid"]=data["centeroid"].copy()
    for i in range(0,totalClusters):
        clusters=results[results['centeroid']==i]
        X=clusters['Record1']
        Y=clusters['Record2']
        plt.scatter(X,Y, c=np.arctan2(X, Y), cmap='rainbow', s=50, alpha=0.8)
        
    plt.show()
def printElbowPlot(clusters):
    sb.lineplot(x=clusters, y=errors)
    plt.show()

errors=[]  
CLUSTORS=6
def main():
    dataset = pd.read_csv("dataset.csv")  
    dataset.drop(dataset.columns[[0, 1, 2, 3, -2]], 1, inplace=True) 

    # (string -> standard)
    train = np.array(transformer(transformers=[("encoder", encoder(), [-7, -4])], remainder="passthrough") .fit_transform(dataset))
    df = pd.DataFrame (train, columns = ['c1', 'c2','c3', 'c4','c5', 'c6','c7', 'c8','c9', 'c10','c11', 'c12','c13', 'c14','c15', 'c16','c17', 'c18','c19', 'c20','c21', 'c22','c23', 'c24','c25'])

    df.drop(dataset.index[500:232726], inplace=True)
    df.reset_index(drop=True,inplace=True)

    data=kmean(CLUSTORS,df.copy())
    printScatterPlot(CLUSTORS,data,df.copy())
main()
