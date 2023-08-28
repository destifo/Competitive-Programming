import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby("sell_date")["product"].unique().reset_index()
    df["num_sold"] = df["product"].apply(lambda x:len(x))
    df["product"] = df["product"].apply(lambda x:sorted(x))
    df["product"] = df["product"].apply(lambda x:",".join(x))
    df = df.rename(columns={"product": "products"}).sort_values("sell_date")
    
    return df[["sell_date", "num_sold", "products"]]


def categorize_products2(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby("sell_date")["product"].agg([
        ("num_sold", 'nunique'),
        ("products", lambda x: ",".join(sorted(x.unique())))
    ]).reset_index().sort_values("sell_date")