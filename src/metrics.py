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

def bootstrap_ci(df: pd.DataFrame,subject_to_test_in_df: str,n_boot:int = 1000):

    bp = df[subject_to_test_in_df].values

    np.random.seed(519)

    means = []

    for _ in range(n_boot):
        sample = np.random.choice(bp, size=len(bp), replace=True)
        means.append(sample.mean())

    lower = np.percentile(means, 2.5)
    higher = np.percentile(means, 97.5)


    return lower, higher

def sim_des(df: pd.DataFrame, seed:int = 519, number_sims:int = 1000):

    real_prob = df["disease"].mean()

    np.random.seed(seed)

    simulated = np.random.choice([0, 1], size=number_sims, p=[1-real_prob, real_prob])
    sim_prob = simulated.mean()

    return real_prob, sim_prob