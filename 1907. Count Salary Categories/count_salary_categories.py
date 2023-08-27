import pandas as pd


def bankAccountType(income: int) -> str:
    
    if income < 20000:
        return "Low Salary"
    elif income <= 50000:
        return "Average Salary"
    return "High Salary"


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    accounts["category"] = accounts["income"].apply(lambda income: bankAccountType(income))
    count = accounts["category"].value_counts()
    income_types = ["Low Salary", "Average Salary", "High Salary"]
    ans = pd.DataFrame(
        {
            "category": income_types, 
            "accounts_count": [count.get(income_types[0], 0), count.get(income_types[1], 0), count.get(income_types[2], 0)]
        }
    )
    
    return ans