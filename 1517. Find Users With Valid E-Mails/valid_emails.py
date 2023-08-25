import pandas as pd
import re

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users["mail"].str.match(r'[a-zA-Z][0-9a-zA-Z_.-]*@leetcode\.com')]

    return df