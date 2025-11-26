import pandas as pd
from .io_utiles import load_csv_file
from .metrics import(
    summery_of_csv,
    summery_of_csv_per_gender,
    smoker_per_gender,
    bootstrap_ci,
    sim_des,
    smoker_systolic_bp_correlation_test,
    regression_bp
    )
from .viz import(viz_smoker_per_gender,
                 viz_disease_per_gender,
                 viz_weight_vs_height,
                 viz_bp_vs_age
                 )


class HealthAnalyser:
    def __init__(self, csv_path: str, clean: bool = False ):

        self.df = load_csv_file(csv_path, clean=clean)


    def summery_of_csv_per_gender(self):
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
        return summery_of_csv_per_gender(self.df)
    

    def summery_of_csv(self):
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
        return summery_of_csv(self.df)
    
    def smoker_per_gender(self):
        """
        Calculate Total amount of individuals and number of smokers per gender in a **DataFrame**.

        **Requirements:**
            Columns "sex" and "smoker"

        **Returns:**
            New DataFrame grouped by 
            Total: total number of individuals per "sex" 
            Smokers: number of "smokers" per "sex"
        """
        return smoker_per_gender(self.df)
    #########
    
    def bootstrap_ci(self, subject_to_test_in_df: str,n_boot:int = 1000):
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

        return bootstrap_ci(self.df,subject_to_test_in_df,n_boot)
    
    def sim_des(self,seed:int, number_sims:int):
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
        return sim_des(self.df,seed, number_sims)
    
    def smoker_systolic_bp_correlation_test(self):
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
        return smoker_systolic_bp_correlation_test(self.df)

    #########

    def regression_bp(self):
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
        
        return regression_bp(self.df)

    #########
    
    def viz_smoker_per_gender(self):

        """
        Visualize smokers per gender with two bars using smoker_per_gender funktion in metrics.py.

        **Requirements:** 
            DataFrame with Columns:
            "sex": with two different types.
            "smoker": yes or no if they are a smoker.
        
        **Return:**
            fig, ax based on matplotlib with two bars to visualize smokers per gender.
        """

        return viz_smoker_per_gender(self.df)
    
    def viz_disease_per_gender(self):
        """
        Visualize disease per gender with a histogram.

        **Requirements:** 
            DataFrame with Columns:
            "sex": with two different types.
            "disease": bool 1 or 0. 1 for yes and 0 for no.
        
        **Return:**
            fig, ax based on matplotlib as a histogram to visualize disease per gender.
        """
        
        return viz_disease_per_gender(self.df)

    
    def viz_weight_vs_height(self):
        """
        Visualize weight vs height with a scatter plot.

            **Requirements:** 
                DataFrame with Columns:
                "sex": with two different types.
                "weight": Float representing weight.
                "height": Float representing height.
        
            **Return:**
                fig, ax based on matplotlib as a scatter plot with weight and height split by gender(red = Female, blue = Male).
        """

        return viz_weight_vs_height(self.df)
    
    def viz_bp_vs_age(self):
        """
        Visualize systolic_bp vs age and it´s trend with a scatter plot.

            **Requirements:** 
                DataFrame with Columns:
                "age": int with age.
                "systolic_bp": Float with the systolic_bp. 
            
            **Return:**
                fig, ax based on matplotlib as a scatter plot with Age and systolic_bp with an line show casing its trend.
        """

        return viz_bp_vs_age(self.df)
    
