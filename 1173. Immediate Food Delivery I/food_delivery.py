import pandas as pd

def orderType(order_date, pref_date) -> str:
    if order_date == pref_date:
        return "immediate"
    
    return "scheduled"


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    
    delivery["delivery_type"] = delivery.apply(lambda df: orderType(df["order_date"], df["customer_pref_delivery_date"]), axis=1)
    count = delivery["delivery_type"].value_counts()
    ans = pd.DataFrame({"immediate_percentage": [(count.get("immediate", 0)*100/count.sum()).round(2)]})
    
    return ans