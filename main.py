import requests
import pandas as pd
from load import carregar_para_postgres

# Fazer a request da API
def make_request(url, params = None):
    response = requests.get(url, params = params)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        response = None
    else:
        response = response.json()
    return response
    
#Url e Loop para pegar todos os dados da API 
url_primeira_pagina = f'https://dadosabertos.camara.leg.br/api/v2/deputados'
deputados = []

while(url_primeira_pagina):
    dados = make_request(url_primeira_pagina)
    deputados.extend(dados['dados'])
    proxima_pagina = None
    for links in dados['links']:
        if links['rel'] == 'next':
            proxima_pagina = links['href']
            break
    url_primeira_pagina = proxima_pagina
        
        
# Criando DaraFrame dos Deputados
df_dados = pd.DataFrame(deputados)
df = df_dados[['id', 'nome', 'siglaPartido', 'siglaUf']].copy()
df.set_index('id', inplace = True)

# Renomeando o DataFrame
df.rename(columns = {'siglaPartido': 'partido', 'siglaUf': 'uf'}, inplace = True)

# Despesas de cada Deputado
lista_ids_deputados = df.index.tolist()
lista_todas_despesas = []
for id_deputado in lista_ids_deputados:
    url_pagina_despesa = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas'
    contador_pagina = 1
    while url_pagina_despesa:
        dados_da_pagina = make_request(url_pagina_despesa)
        print(f"    -> Buscando página {contador_pagina} de despesas...")
        contador_pagina += 1
        if dados_da_pagina and dados_da_pagina['dados']:
            despesas_desta_pagina = dados_da_pagina['dados']
            for despesa in despesas_desta_pagina:
                despesa['id_deputado'] = id_deputado
            lista_todas_despesas.extend(despesas_desta_pagina)
            url_pagina_despesa = None 
            for link in dados_da_pagina['links']:
                if link['rel'] == 'next':
                    url_pagina_despesa = link['href']
                    break 
        else:
            url_pagina_despesa = None


# Criando DataFrame das Despesas
df_despesas = pd.DataFrame(lista_todas_despesas)
df_despesas.set_index('id_deputado', inplace=True)

if __name__ == "__main__":
    df.to_csv('deputados.csv', index = True)
    df_despesas.to_csv('despesas.csv', index=True)
    
    # Carregando os Dataframes para PostgreSQL
    carregar_para_postgres(df, 'deputados')
    carregar_para_postgres(df_despesas, 'despesas')
    
    