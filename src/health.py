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
from .viz import(viz_smoker_per_gender,viz_disease_per_gender,viz_weight_vs_height)


class HealthAnalyser:
    def __init__(self, csv_path: str, clean: bool = False ):

        self.df = load_csv_file(csv_path, clean=clean)


    def summery_of_csv_per_gender(self):

        return summery_of_csv_per_gender(self.df)
    

    def summery_of_csv(self):
        
        return summery_of_csv(self.df)
    
    def smoker_per_gender(self):

        return smoker_per_gender(self.df)
    #########
    
    def bootstrap_ci(self, subject_to_test_in_df: str,n_boot:int = 1000):

        return bootstrap_ci(self.df,subject_to_test_in_df,n_boot)
    
    def sim_des(self,seed:int, number_sims:int):
        
        return sim_des(self.df,seed, number_sims)
    
    def smoker_systolic_bp_correlation_test(self):
        
        return smoker_systolic_bp_correlation_test(self.df)

    #########

    def regression_bp(self):
        
        return regression_bp(self.df)

    #########
    
    def viz_smoker_per_gender(self):

        return viz_smoker_per_gender(self.df)
    
    def viz_disease_per_gender(self):
        
        return viz_disease_per_gender(self.df)
    
    def viz_weight_vs_height(self):

        return viz_weight_vs_height(self.df)
    
