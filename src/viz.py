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

def viz_disease_per_gender(df: pd.DataFrame) -> plt.subplots:

    fig, ax = plt.subplots(figsize=(6, 5))

    ax.hist(df["disease"], bins=2, color="orange", edgecolor="black", alpha=0.5 )

    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Frisk", "Sjuk"])
    ax.set_xlabel("Status")
    ax.set_ylabel("Antal personer")
    ax.set_title("Histogram över sjukdomsförekomst")

    counts = [(df["disease"] == i).sum() for i in [0, 1]]
    for count, patch in zip(counts, ax.patches):
        ax.text(patch.get_x() + patch.get_width() / 2, count + 0.5, str(int(count)), ha="center", va="bottom")


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


