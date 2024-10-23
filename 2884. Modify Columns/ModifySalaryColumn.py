import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df["salary"] = df["salary"] * 2
    
    return df
