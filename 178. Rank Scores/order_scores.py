import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    scores.sort_values("score", ascending=False, inplace=True)
    scores.drop(columns=["id"], inplace=True)
    return scores