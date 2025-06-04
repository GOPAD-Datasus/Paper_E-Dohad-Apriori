import pandas as pd
from efficient_apriori import apriori


def _semagestac(x):
    if x < 28:
        return 'Risco: Prematuro extremo (<28)'
    elif x < 31:
        return 'Risco: Muito prematuro (<31)'
    elif x < 33:
        return 'Risco: Prematuro moderado (<33)'
    elif x < 36:
        return 'Risco: Prematuro tardio (<36)'
    elif x < 37:
        return 'Risco: Prematuro (<37)'
    elif x > 42:
        return 'Risco: Pós-termo (>42)'
    else:
        return 'Semana de gestação saudável (>37)'


def _peso (x):
    if x < 2500:
        return 0 # risco
    elif x > 4000:
        return 2
    else:
        return 1


def _apgar (x):
    if x < 7:
        return 0
    else:
        return 1

def feature_processing (df: pd.DataFrame):
    df['SEMAGESTAC'] = df['SEMAGESTAC'].apply(_semagestac)
    df['PESO'] = df['PESO'].apply(_peso)
    df['APGAR5'] = df['APGAR5'].apply(_apgar)
    return df


def map_categories (df: pd.DataFrame):
    map = {
        1: 'Solteira',
        2: 'Casada',
        3: 'Viuva',
        4: 'Divorciada',
        5: 'União'}

    df['ESTCIVMAE'] = df['ESTCIVMAE'].map(map)

    map = {
        1: 'Vaginal',
        2: 'Cesáreo'}

    df['PARTO'] = df['PARTO'].map(map)

    map = {
        1: 'Consulta: 0',
        2: 'Consultas: 1 a 3',
        3: 'Consultas: 4 a 6',
        4: 'Consultas: 7+'}

    df['CONSULTAS'] = df['CONSULTAS'].map(map)

    map = {
        0: 'Risco: Apgar baixo (<7)',
        1: 'Apgar saudável (>7)'}

    df['APGAR5'] = df['APGAR5'].map(map)

    map = {
        1: 'Branca',
        2: 'Negra'}

    df['RACACOR'] = df['RACACOR'].map(map)

    map = {
        0: 'Risco: Peso baixo (<2500)',
        1: 'Peso saudável (>2500)',
        2: 'Risco: Peso alto (>4000)'}

    df['PESO'] = df['PESO'].map(map)

    map = {
        0: 'Sem anomalias',
        1: 'Risco: Presença de anomalias'}

    df['IDANOMAL'] = df['IDANOMAL'].map(map)

    map = {
        0: 'Sem escolaridade',
        1: 'Fundamental I',
        2: 'Fundamental II',
        3: 'Médio',
        4: 'Superior incompleto',
        5: 'Superior completo'}

    df['ESCMAE2010'] = df['ESCMAE2010'].map(map)

    df['MESPRENAT'] = (df['MESPRENAT']
                       .apply(lambda x: f'Inicio PN: {x}° mês'))

    df['CODOCUPMAE'] = (df['CODOCUPMAE']
                        .apply(lambda x: f'Ocupação: {x}'))

    return df


def apply_apriori (df: pd.DataFrame):
    main_list = list(df.itertuples(index=False, name=None))
    item_sets, rules = apriori(main_list,
                              min_support=0.25,
                              min_confidence=0.75,
                              max_length=5)
    return rules


def save_rules (rules, number: int):

    list_rhs, list_lhs, list_supp = [], [], []
    list_conf, list_lift, list_conv = [], [], []

    for i in rules:
        list_rhs.append(i.rhs)
        list_lhs.append(i.lhs)
        list_supp.append(i.support)
        list_conf.append(i.confidence)
        list_lift.append(i.lift)
        list_conv.append(i.conviction)

    data = {
        'rhs': list_rhs,
        'lhs': list_lhs,
        'supp': list_supp,
        'conf': list_conf,
        'lift': list_lift,
        'conv': list_conv
    }

    temp = pd.DataFrame(data)
    temp.to_csv(f'../data/rules/rules_{number}.csv')