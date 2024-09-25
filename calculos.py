def freqColumns(columna):
    valores = {valor:columna.tolist().count(valor) for valor in set(columna.tolist())}
    return valores

def mostrarValoresNan(dataframe):
    dataframe.isna().sum()

def contarDuplicados(dataframe):
    dataframe.duplicated().sum()

def describirDataframe(dataframe):
    dataframe.describe(exclude=['object', 'bool'])
    dataframe.describe(include='object')
    dataframe.describe(include='bool')

def rangeInterQrtl(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    valor_min = Q1 - 1.5 * (Q3 - Q1)
    valor_max = Q3 + 1.5 * (Q3 - Q1)
    par_min_max = [valor_min, valor_max]
    return par_min_max

def dropOutliers(par, column, dataframe):
    filas_fuera_de_rango = dataframe.loc[(column < par[0]) | (column > par[1])]
    return filas_fuera_de_rango