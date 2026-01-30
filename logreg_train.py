import sys
import json
import math

from src.utils.parser import parse_dataset
from src.stats.descriptive import mean, std


FEATURES = [
    "Astronomy",
    "Herbology",
    "Defense Against the Dark Arts",
    "Divination",
    "Charms",
    "Flying",
]

HOUSES = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
LEARNING_RATE = 0.01
EPOCHS = 3000


def sigmoid(z):
    """
    Mathematical function that maps any real-valued number
    into a value between 0 and 1:

    g(x) = 1 / (1 + e ** -x)
    """
    return 1 / (1 + math.exp(-z))


def normalize_column(col):
    """
    The normalization makes sure the data appears on the same scale
        so it can be read properly
    """
    m = mean(col)
    s = std(col)
    return [(x - m) / s if s != 0 else 0 for x in col], m, s


def prepare_features(df):
    X = []
    norms = {}

    for feature in FEATURES:
        values = df[feature].dropna().tolist()
        norm_col, m, s = normalize_column(values)
        norms[feature] = (m, s)
        X.append(norm_col)

    X = list(zip(*X))
    X = [[1.0] + list(row) for row in X]
    return X, norms


def train_one_vs_all(X, y):
    """
    The weights are trained by houses and then adjusted in an array

    The model will then be able to singularize one house vs the others
        depending on the type of grades presented in a sucject.

    In this function, for n_interactions the model predicts a result,
        evaluates its own result and corrects its weights.

        X : dataset
        y : prediction labels
    """
    weights = [0.0] * len(X[0])

    for _ in range(EPOCHS):
        for i in range(len(X)):
            z = sum(weights[j] * X[i][j] for j in range(len(weights)))
            pred = sigmoid(z)
            error = pred - y[i]

            for j in range(len(weights)):
                weights[j] -= LEARNING_RATE * error * X[i][j]

    return weights


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 logreg_train.py dataset_train.csv")
        sys.exit(1)

    df = parse_dataset(sys.argv[1])
    df = df.dropna(subset=FEATURES + ["Hogwarts House"])

    X, norms = prepare_features(df)

    models = {}

    for house in HOUSES:
        y = [1 if h == house else 0 for h in df["Hogwarts House"]]
        weights = train_one_vs_all(X, y)
        models[house] = weights

    with open("weights.json", "w") as f:
        json.dump({
            "features": FEATURES,
            "norms": norms,
            "models": models
        }, f)

    print("Training complete → weights.json generated")


if __name__ == "__main__":
    main()
