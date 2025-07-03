import pandas as pd

from dev.preprocess.utils import *


def preprocess ():
    columns = ['RACACOR', 'ESCMAE2010', 'CODOCUPMAE',
               'ESTCIVMAE', 'CONSULTAS', 'MESPRENAT',
               'SEMAGESTAC', 'PESO', 'APGAR5', 'PARTO',
               'IDANOMAL']

    df = pd.read_parquet('../data/raw/DN2023.parquet.gzip',
                         columns=columns)

    df.dropna(inplace=True)

    df = df[df['RACACOR'] != 3]
    df = df[df['RACACOR'] != 5]

    df = classify(df)

    df = remove_outliers(df, 'PESO')
    df = remove_outliers(df, 'SEMAGESTAC')

    return df