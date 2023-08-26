import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.sort_values(by="salary", ascending=False)["salary"].rename("SecondHighestSalary").drop_duplicates().to_frame()
    if df.shape[0] < 2:
        return pd.DataFrame.from_dict({"SecondHighestSalary": [None]})
    
    return df.iloc[1:2]