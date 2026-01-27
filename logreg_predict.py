import sys
import json
import math

from src.utils.parser import parse_dataset

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def normalize(x, m, s):
    return (x - m) / s if s != 0 else 0

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 logreg_predict.py dataset_test.csv weights.json")
        sys.exit(1)

    df = parse_dataset(sys.argv[1])

    with open(sys.argv[2], "r") as f:
        data = json.load(f)

    FEATURES = data["features"]
    norms = data["norms"]
    models = data["models"]

    predictions = []

    for idx, row in df.iterrows():
        x = [1.0]
        for feature in FEATURES:
            m, s = norms[feature]
            val = row[feature]
            x.append(normalize(val, m, s) if val == val else 0)

        scores = {}
        for house, weights in models.items():
            z = sum(weights[i] * x[i] for i in range(len(x)))
            scores[house] = sigmoid(z)

        predicted_house = max(scores, key=scores.get)
        predictions.append((idx, predicted_house))

    with open("houses.csv", "w") as f:
        f.write("Index,Hogwarts House\n")
        for idx, house in predictions:
            f.write(f"{idx},{house}\n")

    print("Prediction complete → houses.csv generated")

if __name__ == "__main__":
    main()
