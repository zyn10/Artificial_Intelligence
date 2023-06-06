from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn.cluster as sk
import numpy as np
import random


df = pd.read_csv('Mall_Customers.csv')
df = pd.DataFrame(df)
df1 = pd.DataFrame(df['Annual_Income_(k$)'], df['Spending_Score'])

Inertia_List = []
No_of_Cluster = []

for i in range(1, 15):
    Kmeans = sk.KMeans(n_clusters=i, init='k-means++')
    Kmeans.fit(df1)
    No_of_Cluster.append(i)
    Inertia_List.append(Kmeans.inertia_)

plt.plot(range(1, 15), Inertia_List)
plt.title('K Means Clustering')

plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

X = np.array(df.loc[:,['Annual_Income_(k$)','Spending_Score']]).reshape(-1, 2)

Kmeans = sk.KMeans(n_clusters=3, init='k-means++')
Kmeans.fit(df1)

y = Kmeans.fit_predict(X)


plt.scatter(X[0:, 0],X[0:, 1])
plt.scatter(Kmeans.cluster_centers_[:, 0], Kmeans.cluster_centers_[:, 1], s=100, c='red')


plt.show()

