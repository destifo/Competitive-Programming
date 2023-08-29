import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")
    exams = examinations.groupby(["student_id", "subject_name"],  as_index=False).size()
    df = df.merge(exams, on=["student_id", "subject_name"], how="left").rename(columns={"size": "attended_exams"}).sort_values(["student_id", "subject_name"])
    df["attended_exams"] = df["attended_exams"].fillna(0)
    
    return df[["student_id","student_name","subject_name","attended_exams"]]