#!/usr/bin/env python3
# pair_plot.py

import pandas as pd
import matplotlib.pyplot as plt
import itertools

DATASET_FILE = "datasets/dataset_train.csv"

# Couleurs par maison
HOUSE_COLORS = {
    'Gryffindor': 'red',
    'Slytherin': 'green',
    'Hufflepuff': 'yellow',
    'Ravenclaw': 'blue'
}

def parse_dataset(filename):
    df = pd.read_csv(filename)
    if df.shape[0] == 0 or df.shape[1] == 0:
        raise ValueError("Empty or invalid CSV")
    if 'Hogwarts House' not in df.columns:
        raise ValueError("CSV must contain 'Hogwarts House' column")
    return df

def scatter_matrix(df):
    # Colonnes numériques (les cours)
    numeric_cols = df.select_dtypes(include=['int', 'float']).columns
    numeric_cols = [c for c in numeric_cols if c != 'Index']
    n = len(numeric_cols)

    fig, axes = plt.subplots(n, n, figsize=(3*n, 3*n))
    plt.subplots_adjust(wspace=0.1, hspace=0.1)

    for i, col1 in enumerate(numeric_cols):
        for j, col2 in enumerate(numeric_cols):
            ax = axes[i, j]
            if i == j:
                # Histogramme sur la diagonale
                for house in df['Hogwarts House'].unique():
                    data = df[df['Hogwarts House'] == house][col1].dropna()
                    ax.hist(data, bins=10, alpha=0.5, color=HOUSE_COLORS[house])
                if j == 0:
                    ax.set_ylabel(col1)
                ax.set_xticks([])
                ax.set_yticks([])
            else:
                # Scatter plot pour les autres cases
                for house in df['Hogwarts House'].unique():
                    subset = df[df['Hogwarts House'] == house][[col2, col1]].dropna()
                    ax.scatter(subset[col2], subset[col1], alpha=0.5, color=HOUSE_COLORS[house], s=10)
                if i == n-1:
                    ax.set_xlabel(col2)
                if j == 0:
                    ax.set_ylabel(col1)
                ax.set_xticks([])
    ax.set_yticks([])
    # Légende
    handles = [plt.Line2D([0],[0], marker='o', color='w', markerfacecolor=c, markersize=8)
               for c in HOUSE_COLORS.values()]
    labels = HOUSE_COLORS.keys()
    fig.legend(handles, labels, loc='upper right')
    plt.suptitle("Scatter plot matrix of Hogwarts courses", y=0.92)
    plt.show()

def main():
    try:
        df = parse_dataset(DATASET_FILE)
        scatter_matrix(df)
        print("\nObservation:")
        print("- Les features dont les points sont bien séparés par maison sont intéressantes pour la régression logistique.")
        print("- Les features très corrélées peuvent être réduites à une seule.")
    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
