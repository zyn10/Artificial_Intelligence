import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df = pd.DataFrame({'from': ['Spider Man', 'Civil War', 'Iron Man', 'Thor','Avengers','Ragnarok','Captain America','Ant Man','Hulk'],
'to': ['Avengers', 'Spider Man', 'Spider Man', 'Avengers','Thor','Thor','Avengers','Avengers','Avengers']})
# Build your graph
G = nx.from_pandas_edgelist(df, 'from', 'to')
# Plot it
nx.draw(G, with_labels=True)
plt.show()
