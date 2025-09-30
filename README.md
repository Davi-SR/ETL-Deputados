# 🏛️ ETL Deputados

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/downloads/)  
[![Pandas](https://img.shields.io/badge/Pandas-2.x-blue?logo=pandas)](https://pandas.pydata.org/)  
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)](https://www.postgresql.org/)  
[![Requests](https://img.shields.io/badge/Requests-Library-FF9E0F?logo=python)](https://pypi.org/project/requests/)  
[![Status](https://img.shields.io/badge/Status-Ativo-success?logo=github)](https://github.com/Davi-SR/ETL-Deputados)  

---

## 📖 Visão Geral  
Este projeto é um **pipeline de ETL (Extract, Transform, Load)** que consome dados da [API da Câmara dos Deputados](https://dadosabertos.camara.leg.br/), extrai **informações dos deputados e suas despesas 💰**, organiza em **DataFrames pandas** e carrega os dados em um banco **PostgreSQL** 📊.

---

## ⚙️ Fluxo do Projeto
1. **📡 Extração**  
   - Deputados (`/deputados`)  
   - Despesas (`/deputados/{id}/despesas`)  

2. **🔄 Transformação**  
   - Seleção, renomeação de colunas e criação de índices  
   - Junção entre deputados e suas despesas  

3. **💾 Carga**  
   - Exportação para arquivos CSV (`deputados.csv`, `despesas.csv`)  
   - Armazenamento no PostgreSQL   

---

## 📂 Estrutura do Repositório
ETL-Deputados/
│── main.py # Orquestra ETL
│── load.py # Função de carga no PostgreSQL
│── .gitignore
│── .env (⚠ criar manualmente)


---

## 🚀 Começando

### 🔑 Pré-requisitos
- Python **3.9+** 🐍  
- Banco de dados **PostgreSQL** 💽  

### 📦 Instalação
```bash
git clone https://github.com/Davi-SR/ETL-Deputados.git
cd ETL-Deputados
pip install -r requirements.txt   # caso crie este arquivo

```
🛠️ Configuração do Banco (Docker 🐳 opcional)
```bash
docker run --name etl-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=etl_deputados \
  -p 5432:5432 -d postgres:15
```
No arquivo .env:
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/etl_deputados

▶️ Como Rodar
```bash
python main.py
```
➡️ Resultado:

    CSVs: deputados.csv, despesas.csv
    Tabelas PostgreSQL: deputados, despesas

👨‍💻 Autor
Projeto desenvolvido por Davi-SR ✨
