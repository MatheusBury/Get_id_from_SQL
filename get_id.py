import pandas as pd
import re

"""
Version: 1
@Author Matheus Bury create 19/03/24
"""

def extrair_id(string):
    match = re.search(r'"id":"([^"]+)"', string)
    if match:
        return match.group(1)
    else:
        return None

nome_arquivo = r'Caminho/do/arquivo.csv'

df = pd.read_csv(nome_arquivo)

# Extrair o ID das colunas Picture01 e Picture02
df['Picture01_ID'] = df['Picture01'].apply(extrair_id)
df['Picture02_ID'] = df['Picture02'].apply(extrair_id)
df['Picture03_ID'] = df['Picture03'].apply(extrair_id)

combined_ids = pd.concat([df['Picture01_ID'], df['Picture02_ID'],df['Picture03_ID']], ignore_index=True)
total_linhas = combined_ids.shape[0]
print("O total de linhas é:", total_linhas)

novo_nome_arquivo = 'output.csv'
combined_ids.to_csv(novo_nome_arquivo, index=False, header=['Combined_ID'])

