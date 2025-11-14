import pandas as pd
from .io_utiles import load_csv_file
from .metrics import(summery_of_csv, summery_of_csv_per_gender,smoker_per_gender)
from .viz import(viz_smoker_per_gender,viz_weight_per_gender)


class HealthAnalyser:
    def __init__(self, csv_path: str, clean: bool = False ):

        self.df = load_csv_file(csv_path, clean=clean)


    def summery_of_csv_per_gender(self):

        return summery_of_csv_per_gender(self.df)
    

    def summery_of_csv(self):
        
        return summery_of_csv(self.df)
    
    def smoker_per_gender(self):

        return smoker_per_gender(self.df)
    
    def viz_smoker_per_gender(self):

        return viz_smoker_per_gender(self.df)
    
    def viz_weight_per_gender(self):
        
        return viz_weight_per_gender(self.df)
    
