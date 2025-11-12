import pandas as pd

# age,sex,height,weight,systolic_bp,cholesterol

def summery_of_csv(df: pd.DataFrame) -> pd.DataFrame:
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
    summery_of_csv = df[columns].agg(["sum", "mean", "median", "std", "min", "max"])
    
    return summery_of_csv

def summery_of_csv_per_gender(df: pd.DataFrame) -> pd.DataFrame:
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
    
    summery_per_gender = df.groupby("sex")[columns].agg(["mean", "median", "std", "min", "max"])
    
    return summery_per_gender