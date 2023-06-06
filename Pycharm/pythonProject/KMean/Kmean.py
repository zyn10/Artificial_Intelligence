import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import random


def ManhatanDistance(centroid_List, record_value):
    sum = 0
    for i in range(len(record_value)):
        sum += abs(centroid_List[i] - record_value[i])
    return sum


def Cluster_distortion(centroids, data_set):
    cluster_error = 0
    # sum = 0
    for center, records in centroids.items():
       # sum = 0
        for record in records:
            cluster_error += ManhatanDistance(center, data_set[record])
        # cluster_error += sum
    return cluster_error


def Cluster(centroids, data_set):
    for i in range(50):  # len(data_set)
        # centroids_to_cluster_dis = {j: ManhatanDistance(data_set[j], data_set[i]) for j in centroids.keys()}
        centroids_to_cluster_dis = {j: ManhatanDistance(j, data_set[i]) for j in centroids.keys()}
        index = min(centroids_to_cluster_dis, key=centroids_to_cluster_dis.get)
        centroids[index].append(i)


def Means(centroids, data_set):
    sum = 0
    dic = {}
    for centerKey, centerValue in centroids.items():
        c = []
        if len(centerValue) != 0:
            for i in range(25):
                sum = 0
                for value in centerValue:
                    sum += data_set[value][i]
                c.append(sum/len(centerValue))
            dic[tuple(c)] = []
        else:
            dic[centerKey] = []
    return dic


def KMeans(no_of_cluster, data_set):
    global wcss
    for i in range(2, 50):
        centroids = {tuple(data_set[random.randrange(0, 50)]): [] for j in range(0, i)}
        Cluster(centroids, data_set)
        for j in range(6):
            centroids = Means(centroids, data_set)
            Cluster(centroids, data_set)
        wcss.append(Cluster_distortion(centroids, data_set))


wcss = []

dataset = pd.read_csv("dataset.csv")

print(dataset.head())

dataset.drop(dataset.columns[[0, 1, 2, 3, -2]], axis=1, inplace=True)
# print(dataset.columns[[0, 1, 2, 3, -2]])
print(dataset.head())

X = dataset

ct = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [-7, -4])], remainder="passthrough")
training_data = np.array(ct.fit_transform(X))

KMeans(len(training_data), training_data)

print(len(wcss))

plt.plot(range(2, 50), wcss)

plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')

plt.show()
