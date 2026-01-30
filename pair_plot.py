import matplotlib.pyplot as plt

from src.config.constants import LABELED_DATASET_FILE, HOUSE_COLORS
from src.utils.parser import parse_dataset


def scatter_matrix(df):
    """
    Create a figure that shows every subjects plotted two by two
    """
    numeric_cols = df.select_dtypes(include=["int", "float"]).columns
    numeric_cols = [c for c in numeric_cols if c != "Index"]
    n = len(numeric_cols)

    fig, axes = plt.subplots(n, n, figsize=(3 * n, 3 * n))
    plt.subplots_adjust(wspace=0.1, hspace=0.1)

    for i, col1 in enumerate(numeric_cols):
        for j, col2 in enumerate(numeric_cols):
            ax = axes[i, j]

            short_col1 = col1[:12] if len(col1) > 12 else col1
            short_col2 = col2[:12] if len(col2) > 12 else col2

            if i == j:
                for house in df["Hogwarts House"].unique():
                    data = df[df["Hogwarts House"] == house][col1].dropna()
                    ax.hist(
                        data,
                        bins=10,
                        alpha=0.5,
                        color=HOUSE_COLORS[house]
                    )
                ax.set_xticks([])
                ax.set_yticks([])
                if j == 0:
                    ax.set_ylabel(short_col1)

            else:
                for house in df["Hogwarts House"].unique():
                    subset = df[df["Hogwarts House"]
                                == house][[col2, col1]].dropna()
                    ax.scatter(
                        subset[col2],
                        subset[col1],
                        alpha=0.5,
                        s=10,
                        color=HOUSE_COLORS[house]
                    )
                ax.set_xticks([])
                ax.set_yticks([])
                if i == n - 1:
                    ax.set_xlabel(short_col2)
                if j == 0:
                    ax.set_ylabel(short_col1)

    handles = [
        plt.Line2D([0], [0], marker="o", linestyle="", color=c, markersize=8)
        for c in HOUSE_COLORS.values()
    ]
    labels = HOUSE_COLORS.keys()

    fig.legend(handles, labels, loc="upper right")
    plt.suptitle("Scatter plot matrix of Hogwarts courses", y=0.92)
    plt.show()


def main():
    try:
        dataset = parse_dataset(LABELED_DATASET_FILE)
        scatter_matrix(dataset)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
