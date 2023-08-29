import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(sales_person, on="sales_id", how="right")[["order_id", "name", "sales_id", "com_id"]]
    df = df.merge(company, on="com_id", how="left")
    filtered = set(df[df["name_y"] == "RED"]["name_x"].drop_duplicates())
    df = df[~df["name_x"].isin(filtered)]["name_x"].rename("name").drop_duplicates().to_frame()
    
    return df