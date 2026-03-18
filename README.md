# 🌍 CO2 Data Pipeline & Analytics Dashboard

## 📊 Visão Geral

Este projeto implementa um pipeline de dados completo utilizando a arquitetura **Medallion (Bronze → Silver → Gold)** para ingestão, transformação e análise de dados globais de emissões de CO₂.

Os dados são processados e disponibilizados em um dashboard interativo para exploração analítica.

---

## 🎯 Objetivos

- Construir um pipeline de dados escalável e organizado
- Aplicar boas práticas de engenharia de dados
- Transformar dados brutos em insights analíticos
- Disponibilizar visualização interativa para tomada de decisão

---

## 🧱 Arquitetura
Fonte (Our World in Data)
↓
🥉 Bronze (dados brutos)
↓
🥈 Silver (dados tratados)
↓
🥇 Gold (dados analíticos)
↓
📊 Dashboard (Streamlit)

## 📁 Estrutura do Projeto
co2_pipeline/
│
├── data/
│ ├── bronze/
│ ├── silver/
│ └── gold/
│
├── src/
│ ├── ingest.py
│ ├── transform.py
│ └── load.py
│
├── app.py
├── requirements.txt
└── README.md


---

## 🌐 Fonte de Dados

Dataset público disponibilizado pelo **Our World in Data**:

https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv

---

## ⚙️ Tecnologias Utilizadas

- Python  
- Pandas  
- Streamlit  
- Plotly  

---

## 🔄 Pipeline de Dados

### 🥉 Bronze Layer
- Ingestão de dados brutos via CSV online
- Armazenamento sem transformação

```bash
python src/ingest.py

🥈 Silver Layer

Limpeza de dados

Tratamento de valores nulos

Padronização de tipos

python src/transform.py

🥇 Gold Layer

Agregações analíticas

Preparação para consumo em dashboards

python src/load.py

📊 Dashboard

O dashboard foi desenvolvido com Streamlit e permite:

Seleção dinâmica de países

Visualização temporal de emissões

Comparação entre países

Análise exploratória interativa

▶️ Executar
streamlit run app.py

🔍 Insights Obtidos

Países industrializados lideram emissões absolutas

Emissões per capita oferecem uma visão mais precisa de impacto ambiental

Crescimento acelerado de emissões em economias emergentes

🔐 Boas Práticas Aplicadas

Separação de responsabilidades por camada

Pipeline idempotente

Estrutura modular de código

Uso de cache para performance no dashboard

🚀 Possíveis Melhorias

Integração com Apache Spark para processamento distribuído

Armazenamento em Data Lake (S3 / BigQuery)

Orquestração com Apache Airflow

Uso de formato Parquet para otimização de leitura

Deploy do dashboard em ambiente cloud

📌 Sobre o Projeto

Este projeto foi desenvolvido com foco em demonstrar habilidades práticas em:

Engenharia de Dados

Análise de Dados

Construção de pipelines

Desenvolvimento de dashboards interativos

📎 Contato

Se quiser trocar ideias sobre dados, engenharia ou analytics, fique à vontade para conectar!