import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on="departmentId", right_on="id", suffixes=("", "_r"))
    df.drop(columns=["departmentId", "id_r", "id"], inplace=True)
    df.rename(columns={"name": "Employee", "name_r": "Department"}, inplace=True)
    max_salaries = df.groupby("Department")["salary"].transform("max")
    df = df[df["salary"] == max_salaries]
    
    return df