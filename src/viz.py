import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from .metrics import (summery_of_csv,smoker_per_gender,summery_of_csv_per_gender)


def viz_summery(df :pd.DataFrame):
    return NotImplemented

def viz_smoker_per_gender(df :pd.DataFrame) -> plt.subplots:
    """
    Visualize smokers per gender with two bars using smoker_per_gender funktion in metrics.py.

    **Requirements:** 
        DataFrame with Columns:
        "sex": with two different types.
        "smoker": yes or no if they are a smoker.
    
    **Return:**
        fig, ax based on matplotlib with two bars to visualize smokers per gender.

    """


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
    """
    Visualize disease per gender with a histogram.

    **Requirements:** 
        DataFrame with Columns:
        "sex": with two different types.
        "disease": bool 1 or 0. 1 for yes and 0 for no.
    
    **Return:**
        fig, ax based on matplotlib as a histogram to visualize disease per gender.
    """

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

def viz_bp_vs_age(df: pd.DataFrame) -> plt.subplots:
    """
    Visualize systolic_bp vs age and it´s trend with a scatter plot.

        **Requirements:** 
            DataFrame with Columns:
            "age": int with age.
            "systolic_bp": Float with the systolic_bp. 
        
        **Return:**
            fig, ax based on matplotlib as a scatter plot with Age and systolic_bp with an line show casing its trend.
    """


    X = df[["age"]].values
    Y = df["systolic_bp"].values

    model = LinearRegression()
    model.fit(X, Y)
    
    intercept = float(model.intercept_)
    slope = float(model.coef_[0])

    fig, ax = plt.subplots(figsize=(6, 5))

    ax.scatter(X[:,0], Y, alpha=0.6)
    x_line = np.linspace(X.min(), X.max(), 100)
    y_line = intercept + slope * x_line
    ax.plot(x_line, y_line, color="black")
    ax.set_xlabel("Age")
    ax.set_ylabel("Systolic_Bp")
    ax.set_title("Systolic_Bp increase over age")

    plt.tight_layout()
    plt.show()

    return fig, ax

