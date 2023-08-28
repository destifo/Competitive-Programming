import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cnt = orders["customer_number"].value_counts().reset_index()
    max_order = cnt["count"].max()
    return cnt[cnt["count"] == max_order]["customer_number"].to_frame()


def largest_orders2(orders: pd.DataFrame) -> pd.DataFrame:
    return orders["customer_number"].mode().to_frame()