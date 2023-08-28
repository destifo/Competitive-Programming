import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt = courses["class"].value_counts().to_frame()
    return cnt[cnt["count"] >= 5].reset_index()["class"].to_frame()