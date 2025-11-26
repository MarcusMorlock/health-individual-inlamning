import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

# age,sex,height,weight,systolic_bp,cholesterol
# id,age,sex,height,weight,systolic_bp,cholesterol,smoker,disease
# columns = ["age","sex","height","weight","systolic_bp","cholesterol","smoker","disease"]

def summery_of_csv(df: pd.DataFrame) -> pd.DataFrame:

    """
    descriptive statistics of requirements columns from **DataFrame**.

    Requirements:
        The DataFrame must contain the following columns:
            - "age"
            - "height"
            - "weight"
            - "systolic_bp"
            - "cholesterol"

    **Returns:**
       a new dataframe with: sum, mean, median, std, min, max. of columns from original.
    """
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]

    summery_of_csv = df[columns].agg(["sum", "mean", "median", "std", "min", "max"])
    
    return summery_of_csv

def summery_of_csv_per_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    descriptive statistics of requirements columns from **DataFrame** groupby "sex".

    Requirements:
        The DataFrame must contain the following columns:
            - "sex"
            - "age"
            - "height"
            - "weight"
            - "systolic_bp"
            - "cholesterol"

    **Returns:**
       a new dataframe with: mean, median, std, min, max. of columns from original groupby "sex".
    """
    
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
    
    summery_per_gender = df.groupby("sex")[columns].agg(["mean", "median", "std", "min", "max"])
    
    return summery_per_gender

def smoker_per_gender(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Total amount of individuals and number of smokers per gender in a **DataFrame**.

    **Requirements:**
        Columns "sex" and "smoker"

    **Returns:**
        New DataFrame grouped by 
        Total: total number of individuals per "sex" 
        Smokers: number of "smokers" per "sex"
    """
    
    df["smokers_flaged"] = df["smoker"].map({"Yes": 1, "No": 0})
    smoker_per_gender = df.groupby("sex").agg(Total=("sex", "count"), Smokers=("smokers_flaged", "sum"))
    
    return smoker_per_gender

## Testing data

def bootstrap_ci(df: pd.DataFrame,subject_to_test_in_df: str,n_boot:int = 1000):

    """
    Estimate a 95% confidence interval for the mean of a column within a **DataFrame** using bootstrap resampling.

        **Requirements:** 

            subject_to_test_in_df: the column within the dataframe to be tested.
            df: the dataframe.

        **Explanation:**
            n_boot: the range of the test, default set at 1000.

        **Return:**
            Float: lower and higher bounds of the 95% confidence interval for the mean of the selected column.
    """

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
    """
    Runs a simulation to try and determine the probability the result is made up by chance.

        **Requirements:** 
            DataFrame: Column "disease" within the DataFrame.
            "disease: 1 or 0 to represent bool true or false.

        **Explanation:**
            seed: the np random seed selected, default = 519.
            number_sims: the amount of simulations ran

        **Return:**
            real_prob(real probability), sim_prob(simulated probability).
    """

    real_prob = df["disease"].mean()

    np.random.seed(seed)

    simulated = np.random.choice([0, 1], size=number_sims, p=[1-real_prob, real_prob])
    sim_prob = simulated.mean()

    return real_prob, sim_prob

def smoker_systolic_bp_correlation_test(df: pd.DataFrame):
    """
    Perform a one-sided independent t-test comparing systolic_bp between smokers and non-smokers.

        **Requirements:** 
            DataFrame:
                - "smoker": String with "yes" and "no".
                - "systolic_bp": Float representing the blood pressure of individuals.
        **Return:**
            - t_stat: the t-statistics from the independent t-test.
            - p_value_one_sided: the one-sided p-value indicating significance of the difference.
    """

    smokers_bp = df.loc[df["smoker"] == "Yes", "systolic_bp"]
    nonsmokers_bp = df.loc[df["smoker"] == "No", "systolic_bp"]

    t_stat, p_value = stats.ttest_ind(smokers_bp, nonsmokers_bp, equal_var=False)

    if t_stat > 0:
        p_value_one_sided = p_value / 2
    else:
        p_value_one_sided = 1 - (p_value / 2)

    return t_stat, p_value_one_sided

# Linjer Algebra 

def regression_bp (df: pd.DataFrame):
    """
    A linear regression model to predict systolic_bp using age and weight.

        **Requirements:** 
            DataFrame with columns:
            - "age": age of individuals.
            - "weight": weight of individuals.
            - "systolic_bp": the systolic_bp of individuals.

        **Return:**
            dict:
            - "model": the fitted LinearRegression model.
            - "coef": array of regression coefficients.
            - "age": coefficients for age.
            - "weight": coefficients for weight.
            - "intercept": regression intercept.
            - "r2": R^2 score.
            - "n": number of observations in the DataFrame.
    """
    

    # X = förklarande variabler (features)
    # Y = målfunktion (target)
    # X = det du vill använda för att förklara eller förutsäga något
    # Y = det du vill förutsäga eller analysera


    X = df[["age", "weight"]].values
    Y = df["systolic_bp"].values

    model = LinearRegression()
    model.fit(X, Y)

    coef = model.coef_      # [β1, β2] → hur mycket age och weight påverkar blodtrycket
    intercept = model.intercept_ # β0 → grundvärde när age=0 och weight=0
    


    r2 = model.score(X, Y) # R² → hur bra modellen förklarar variationen i Y
    # R² = 0 → modellen förklarar ingenting. Den är lika bra som att bara gissa medelvärdet.
    # R² = 1 → modellen förklarar all variation perfekt (alla punkter ligger exakt på linjen).
    # R² = 0.405 → modellen förklarar ca 40 % av variationen i blodtrycksvärdena. Resten (60 %) beror på andra faktorer som inte finns med i modellen (t.ex. gener, stress, kost, sjukdomar).

    return {
        "model": model,
        "coef": coef,
        "age": coef[0],
        "weight": coef[1],
        "intercept": intercept,
        "r2": r2,
        "n": len(df)
    }

