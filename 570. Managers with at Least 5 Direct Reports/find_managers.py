import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_count = employee["managerId"].value_counts().reset_index()
    filtered = manager_count[manager_count["count"] >= 5]
    return filtered.merge(employee, left_on="managerId", right_on="id", how="left")[["name"]].dropna()