import pandas as pd

from .utils import apply_pca, normalize, def_number_of_clusters, apply_kmeans


def kmeans(df: pd.DataFrame):
    # PCA
    df_km = df[['APGAR5', 'PESO',
                'IDANOMAL', 'SEMAGESTAC']].copy()

    group = ['ESTCIVMAE', 'CODOCUPMAE', 'ESCMAE2010']
    df_km.loc[:, 'mother'] = apply_pca(df[group])

    # Normalização
    df_km = normalize(df_km)

    # Elbow Method
    n_cluster = def_number_of_clusters(df_km)

    # Kmeans
    df.loc[:, 'cluster'] = apply_kmeans(n_cluster, df_km)

    # to_parquet
    df.to_parquet('data/processed/DNprocessed.parquet.gzip',
                  compression='gzip')
    return df, n_cluster
