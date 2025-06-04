from dev.apriori.utils import *


def apriori (df: pd.DataFrame, n_cluster: int):
    df = feature_processing(df)
    df = map_categories(df)

    for number in range(n_cluster):
        temp = df.loc[df['cluster'] == number].copy()
        temp.drop('cluster', axis=1, inplace=True)

        rules = apply_apriori(temp)
        save_rules(rules, number)
