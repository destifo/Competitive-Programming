import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df = customers
    
    df = df.drop_duplicates(subset=["email"], keep="first")
    
    return df
