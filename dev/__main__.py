from dev.apriori.apriori import apriori
from dev.kmeans.kmeans import kmeans
from dev.preprocessing.preprocess import preprocess


if __name__ == '__main__':
    df = preprocess()
    df, n_cluster = kmeans(df)
    apriori(df, n_cluster)