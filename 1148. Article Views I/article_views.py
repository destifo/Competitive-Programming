import pandas as pd
import numpy as np

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views["viewer_id"] == views["author_id"]]
    df = df[["viewer_id"]].rename(columns={"viewer_id": "id"})
    unique_ids = np.array(df["id"].unique())
    unique_ids.sort()
    ans = pd.DataFrame(unique_ids, columns=["id"])
    
    return ans