import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram

data_filmes=pd.read_csv("maisAssistidos.csv")
data_filmes.head()
X=data_filmes.iloc[:,1:]
Y=data_filmes['Nome do filme']
X=X.replace(to_replace =['?'],value=-1)
X.head()

model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
model = model.fit(X)
labels = model.labels_


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)





plt.title('dentograma hierárquico')
# plot the top three levels of the dendrogram
plot_dendrogram(model, truncate_mode='level')
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()