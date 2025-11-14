import matplotlib.pyplot as plt
import pandas as pd
from .metrics import (summery_of_csv,)


def viz_summery(df :pd.DataFrame):
    return NotImplemented

def viz_smoker_per_gender(df :pd.DataFrame) -> plt.subplots:
    fig, ax = plt.subplots(figsize=(8, 6))

    