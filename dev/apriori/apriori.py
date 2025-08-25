import pandas as pd

from .utils import create_categories, map_categories, apply_apriori, save_rules


def apriori(df: pd.DataFrame, n_cluster: int) -> None:
    df = create_categories(df)
    df = map_categories(df)

    for number in range(n_cluster):
        temp = df.loc[df['cluster'] == number].copy()
        temp.drop('cluster', axis=1, inplace=True)

        rules = apply_apriori(temp)
        save_rules(rules, number)
