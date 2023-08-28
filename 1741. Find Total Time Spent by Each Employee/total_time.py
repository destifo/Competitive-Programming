import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees.apply(lambda x: x["out_time"]-x["in_time"], axis=1)
    df = employees.groupby(["emp_id", "event_day"])["total_time"].sum().to_frame().reset_index().rename(columns={"event_day": "day"})
    
    return df