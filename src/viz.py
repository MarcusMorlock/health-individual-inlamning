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

    bars_total  = ax.bar(x, Total, width=width, label="Total", color="steelblue")
    bars_smoker = ax.bar(x, Smokers, width=width, label="Smokers", color="orange")

    ax.set_title("Smoker per Gender")
    ax.set_xticks(x)
    ax.set_xticklabels(Sexes)
    ax.grid(True, axis="y", alpha=0.3, color="black")
    ax.legend()

    for bar in bars_total:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height +5,
                str(int(height)), ha="center", va="bottom", color="steelblue")
        
        
    for bar in bars_smoker:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height +5,
                str(int(height)), ha="center", va="bottom", color="orange")  

    plt.tight_layout()

    return fig, ax

def viz_disease_per_gender(df: pd.DataFrame) -> plt.subplots:

    # fig, ax = plt.subplots(figsize=(6, 5))

    # ax.hist(df["disease"], bins=2, color="orange", edgecolor="black", alpha=0.5 )

    # sexes = df["sex"].unique()
    # colors = ["orange", "blue"]

    # for sex, color in zip(sexes, colors):
    #     subset = df[df["sex"] == sex]["disease"]
    #     ax.hist(subset, bins=[-0.5, 0.5, 1.5], alpha=0.5, color=color, edgecolor="black", label=f"Kön: {sex}")

    # ax.set_xticks([0, 1])
    # ax.set_xticklabels(["Frisk", "Sjuk"])
    # ax.set_xlabel("Status")
    # ax.set_ylabel("Antal personer")
    # ax.set_title("Histogram över sjukdomsförekomst")

    # counts = [(df["disease"] == i).sum() for i in [0, 1]]
    # for count, patch in zip(counts, ax.patches):
    #     ax.text(patch.get_x() + patch.get_width() / 2, count + 0.5, str(int(count)), ha="center", va="bottom")

    d = df.copy()
    d["disease"] = d["disease"].astype(int)
    d["sex"] = d["sex"].astype(str)

    sexes = sorted(d["sex"].unique())
    n = len(sexes)

    fig, axes = plt.subplots(1, n, figsize=(6 +2*n, 5), sharey=True)

    if n == 1:
        axes = [axes]

    bins = [-0.5, 0.5, 1.5]

    for ax, sex in zip(axes, sexes):
        subset = d.loc[d["sex"] == sex, "disease"]
        ax.hist(subset, bins=bins, color="orange", edgecolor="black", alpha=0.7, rwidth=0.95)

        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Frisk", "Sjuk"])
        ax.set_xlabel("Status")
        ax.set_title(f"Kön: {sex}")

        counts = subset.value_counts().reindex([0, 1], fill_value=0).values
        for x, count in zip([0, 1], counts):
            ax.text(x, count + 0.5, str(int(count)), ha="center", va="bottom")
    
    axes[0].set_ylabel("antal_personer")
    fig.suptitle("Histogram över sjukdomsförekomst per kön", y=0.98)

    plt.tight_layout()
    plt.show()

    return fig, axes

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


