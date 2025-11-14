import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from .metrics import (summery_of_csv,smoker_per_gender,summery_of_csv_per_gender)


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

    return fig, ax

def viz_weight_per_gender(df: pd.DataFrame) -> plt.subplots:

    fig, ax = plt.subplots(figsize=(6, 5))

    df.boxplot(column="weight", by="sex", ax=ax)

    ax.set_title("Boxplot över vikt per kön")
    ax.set_ylabel("Vikt (kg)")
    
    plt.suptitle("")

    plt.tight_layout()
    plt.show()

    return fig, ax

def viz_weight_vs_height(df: pd.DataFrame) -> plt.subplots:
    fig, ax = plt.subplots(figsize=(6, 5))

    colors = {"F": "red", "M": "blue"}

    for sex in df["sex"].unique():
        subset = df[df["sex"] == sex]
        ax.scatter(subset["height"],subset["weight"], color=colors.get(sex, "gray"), label=sex, alpha=0.5)
    
    ax.set_xlabel("Längd (cm)")
    ax.set_ylabel("Vikt (kg)")
    ax.set_title("Scatterplot: Vikt vs Längd per kön")
    ax.legend(title="Kön")
    plt.tight_layout()
    plt.show()

    return fig, ax


