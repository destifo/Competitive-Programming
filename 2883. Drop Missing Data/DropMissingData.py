import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # return students[students["name"].notna()]
    
    students.dropna(subset=["name"], inplace=True)
    
    return students
