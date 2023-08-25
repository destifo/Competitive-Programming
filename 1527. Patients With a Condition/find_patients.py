import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[patients["conditions"].str.contains(r" DIAB1") | patients["conditions"].str.startswith("DIAB1")]
    return df