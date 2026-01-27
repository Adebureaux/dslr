import pandas as pd
import matplotlib.pyplot as plt
import itertools

DATASET_FILE = "datasets/dataset_train.csv"

def parse_dataset(filename):
    dataset = pd.read_csv(filename)
    if dataset.shape[0] == 0 or dataset.shape[1] == 0:
        raise ValueError("Empty or invalid CSV")
    return dataset

def find_most_similar_features(dataset):
    numeric_cols = dataset.select_dtypes(include=['int', 'float']).columns
    numeric_cols = [c for c in numeric_cols if c != 'Index']

    corr_matrix = dataset[numeric_cols].corr()

    correlations = []
    for col1, col2 in itertools.combinations(numeric_cols, 2):
        corr = corr_matrix.loc[col1, col2]
        correlations.append((col1, col2, corr))

    correlations.sort(key=lambda x: x[2], reverse=True)
    return correlations

def plot_scatter(dataset, feature_x, feature_y, corr_value):
    colors = {
        "Gryffindor": "red",
        "Slytherin": "green",
        "Hufflepuff": "gold",
        "Ravenclaw": "blue"
    }

    plt.figure(figsize=(9,7))
    for house, color in colors.items():
        subset = dataset[dataset["Hogwarts House"] == house][[feature_x, feature_y]].dropna()
        plt.scatter(subset[feature_x], subset[feature_y], alpha=0.6, s=20, color=color, label=house)

    plt.xlabel(feature_x)
    plt.ylabel(feature_y)
    plt.title(f"{feature_x} vs {feature_y} (corr={corr_value:.3f})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def main():
    try:
        dataset = parse_dataset(DATASET_FILE)
        correlations = find_most_similar_features(dataset)

        for i in range(10):
            feature_x, feature_y, corr_value = correlations[i]
            print(f"{i+1}. {feature_x} / {feature_y} (correlation = {corr_value:.3f})")
            plot_scatter(dataset, feature_x, feature_y, corr_value)

    except Exception as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
