import pandas as pd

def ingest_data():
    url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    df = pd.read_csv(url)

    # Salvar bruto
    df.to_csv("data/bronze/co2_raw.csv", index=False)

    print("Bronze layer criado")

if __name__=="__main__":
    ingest_data()