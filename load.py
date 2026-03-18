import pandas as pd

def create_gold():
    df = pd.read_csv("data/silver/co2_clean.csv")

    # agregação
    df_gold = df.groupby(['country', 'year']).agg({
        'co2': 'sum',
        'co2_per_capita': 'mean'
    }).reset_index()

    df_gold.to_csv("data/gold/co2_analytics.csv", index=False)

    print("Gold layer criada")

if __name__ == "__main__":
    create_gold()