import pandas as pd
import numpy as np
from scipy import stats

# age,sex,height,weight,systolic_bp,cholesterol
# id,age,sex,height,weight,systolic_bp,cholesterol,smoker,disease
# columns = ["age","sex","height","weight","systolic_bp","cholesterol","smoker","disease"]

def summery_of_csv(df: pd.DataFrame) -> pd.DataFrame:
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]

    summery_of_csv = df[columns].agg(["sum", "mean", "median", "std", "min", "max"])
    
    return summery_of_csv

def summery_of_csv_per_gender(df: pd.DataFrame) -> pd.DataFrame:
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
    
    summery_per_gender = df.groupby("sex")[columns].agg(["mean", "median", "std", "min", "max"])
    
    return summery_per_gender

def smoker_per_gender(df: pd.DataFrame) -> pd.DataFrame:
    df["smokers_flaged"] = df["smoker"].map({"Yes": 1, "No": 0})
    smoker_per_gender = df.groupby("sex").agg(Total=("sex", "count"), Smokers=("smokers_flaged", "sum"))
    
    return smoker_per_gender