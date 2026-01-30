import matplotlib.pyplot as plt
import itertools

from src.config.constants import LABELED_DATASET_FILE, HOUSE_COLORS
from src.utils.parser import parse_dataset
from src.stats.descriptive import mean, std


def pearson_correlation(x, y):
    """
    Measure linear correlation between two data
    -> Meaning looking at what is the correlation between x and y axes.
    """
    mx = mean(x)
    my = mean(y)

    num = 0
    for i in range(len(x)):
        num += (x[i] - mx) * (y[i] - my)

    den = std(x) * std(y) * (len(x) - 1)
    if den == 0:
        return 0.0

    return num / den


def find_most_similar_features(dataset):
    """
    Find out which two subjects have to closest
        distribution of grades accross houses

    To do so, calculate correlation for every subject then sort the results
    """
    numeric_cols = dataset.select_dtypes(include=['int', 'float']).columns
    numeric_cols = [c for c in numeric_cols if c != 'Index']

    correlations = []

    for col1, col2 in itertools.combinations(numeric_cols, 2):
        x = []
        y = []

        for v1, v2 in zip(dataset[col1], dataset[col2]):
            if (
                isinstance(v1, (int, float)) and v1 == v1 and
                isinstance(v2, (int, float)) and v2 == v2
            ):
                x.append(v1)
                y.append(v2)

        if len(x) > 1:
            corr = pearson_correlation(x, y)
            correlations.append((col1, col2, corr))

    correlations.sort(key=lambda x: x[2], reverse=True)
    return correlations


def plot_scatter(dataset, feature_x, feature_y, corr_value):
    """
    Create a figure to show the closest graded two features of the dataset
        by displaying their grades
    """
    plt.figure(figsize=(9, 7))
    for house, color in HOUSE_COLORS.items():
        subset = dataset[dataset["Hogwarts House"]
                         == house][[feature_x, feature_y]].dropna()
        plt.scatter(
            subset[feature_x],
            subset[feature_y],
            alpha=0.6,
            s=20,
            color=color,
            label=house
        )

    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f"{feature_x} vs {feature_y} (corr={corr_value:.3f})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def main():
    try:
        dataset = parse_dataset(LABELED_DATASET_FILE)
        correlations = find_most_similar_features(dataset)

        feature_x, feature_y, corr_value = correlations[0]

        print(
            f"The two most similar features are: "
            f"{feature_x} and {feature_y} "
            f"(correlation = {corr_value:.3f})"
        )

        plot_scatter(dataset, feature_x, feature_y, corr_value)

    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
