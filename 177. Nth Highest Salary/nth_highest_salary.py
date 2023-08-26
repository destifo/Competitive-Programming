import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    return employee.sort_values("salary", ascending=False)["salary"].drop_duplicates().rename("getNthHighestSalary").to_frame().iloc[N-1:N]