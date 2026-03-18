import pandas as pd

def transform_data():
    df = pd.read_csv("data/bronze/co2_raw.csv")

    df = df[['country', 'year', 'co2', 'co2_per_capita']]

    # tratar nulos
    df = df.dropna()

    # tipos corretos
    df['year'] = df['year'].astype(int)

    # salvar camada silver
    df.to_csv("data/silver/co2_clean.csv", index=False)

    print("Silver layer criada")

if __name__ == "__main__":
    transform_data()