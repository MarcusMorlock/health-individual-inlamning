import pandas as pd
from .io_utiles import load_csv_file


class HealthAnalyzer:
    def __init__(self, csv_path: str, clean: bool = True ):

        self.df = load_csv_file(csv_path, clean=clean)