import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(lambda x:x.capitalize())
    return users.sort_values("user_id")