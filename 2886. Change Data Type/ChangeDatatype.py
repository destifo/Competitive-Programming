import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    df = students
    df["grade"] = df["grade"].astype(int)
    
    return df
