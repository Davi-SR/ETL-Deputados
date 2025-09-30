from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def carregar_para_postgres(dataframe, nome_tabela):
    load_dotenv()
    string_conexao = os.getenv("DATABASE_URL")
    
    # 2. Criando a Engine
    engine = create_engine(string_conexao)
    
    
    dataframe.to_sql(
        name=nome_tabela,
        con=engine,
        if_exists='replace',
        index=True
    )
    print(f"Dados carregados com sucesso na tabela '{nome_tabela}'")