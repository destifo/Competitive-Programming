import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"rich_count": [store[store["amount"] > 500].drop_duplicates(subset=["customer_id"]).shape[0]]})


def count_rich_customers2(store: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"rich_count": [store[store["amount"] > 500]["customer_id"].nunique()]})