from dev import apriori, kmeans, preprocess


if __name__ == '__main__':
    df = preprocess()
    df, n_cluster = kmeans(df)
    apriori(df, n_cluster)
