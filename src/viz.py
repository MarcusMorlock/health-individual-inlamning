import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .metrics import (summery_of_csv,smoker_per_gender)


def viz_summery(df :pd.DataFrame):
    return NotImplemented

def viz_smoker_per_gender(df :pd.DataFrame) -> plt.subplots:
    smokers = smoker_per_gender(df)

    Sexes = smokers.index
    Total = smokers["Total"]
    Smokers = smokers["Smokers"]

    x = np.arange(len(Sexes))
    width = 0.80

    fig, ax = plt.subplots(figsize=(6,5))

    ax.bar(x, Total, width=width, label="Total")
    ax.bar(x, Smokers, width=width, label="Smokers")
    ax.set_title("Smoker per Gender")
    ax.set_xticks(x)
    ax.set_xticklabels(Sexes)
    ax.grid(True, axis="y", alpha=0.3, color="black")
    ax.legend()

    plt.tight_layout()


