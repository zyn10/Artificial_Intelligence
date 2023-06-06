import numpy as np
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('cluster_validation_data.txt', sep=",", header=None)
df.head()

# normalize data
X = df.values
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)


def kmeans(X, k=3, max_iterations=100):
    '''
    X: multidimensional data
    k: number of clusters
    max_iterations: number of repetitions before clusters are established

    Steps:
    1. Convert data to numpy aray
    2. Pick indices of k random point without replacement
    3. Find class (P) of each data point using euclidean distance
    4. Stop when max_iteration are reached of P matrix doesn't change

    Return:
    np.array: containg class of each data point
    '''
    """
    IMPLEMENT THE CODE FOR K Means Implementaion From Scratch
    """
    return P


P = kmeans(X)
assert len(df) == len(P)
###denormalize data
X = sc.inverse_transform(X)
plt.figure(figsize=(15,10))
plt.scatter(X[:,0],X[:,1],c=P)
plt.show()