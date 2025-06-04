import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


def apply_pca (df: pd.DataFrame):
    pca = PCA(n_components=1)
    return pca.fit_transform(df)


def normalize (df: pd.DataFrame):
    scaler = MinMaxScaler()
    return scaler.fit_transform(df)


def _calculate_wcss(data):
    from sklearn.cluster import KMeans
    wcss = []
    for n in range(2, 11):
        kmeans = KMeans(n_clusters=n, random_state=46)
        kmeans.fit(X=data)
        wcss.append(kmeans.inertia_)

    return wcss


def _optimal_number_of_clusters(wcss):
    from math import sqrt
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss)-1]

    distances = []
    for i in range(len(wcss)):
        x0 = i+2
        y0 = wcss[i]

        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
    return distances.index(max(distances)) + 2


def def_number_of_clusters (df: pd.DataFrame):
    return _optimal_number_of_clusters(_calculate_wcss(df))


def apply_kmeans (n: int, df: pd.DataFrame):
    kmeans = KMeans(n_clusters=n, random_state=46)
    kmeans.fit_transform(df)

    return kmeans.labels_