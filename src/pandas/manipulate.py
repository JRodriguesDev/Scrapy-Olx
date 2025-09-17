import pandas as pd

data = pd.read_csv('./db/olx1.csv', sep=',')
dtBack = data.copy()
loc = dtBack['location'] == 'Contagem'

print(dtBack['location'][loc])

