import pandas as pd
from src.scrapys.olx import olxScrapy

def saveCSV():
    print("Inciando Busca...")
    lists = olxScrapy()

    print("Iniciando Salvamento...")
    for i, lst in enumerate(lists, start=1):
        df = pd.DataFrame(lst)
        df.to_csv(f'./db/olx2{i}.csv', index=False, encoding='utf-8', sep=',')
    print("Arquivos salvos com sucesso")
