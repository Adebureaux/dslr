import sys

from src.utils.parser import parse_dataset
from src.stats.descriptive import (
    count,
    mean,
    std,
    min_value,
    max_value,
    percentile
)

def describe_numerical_features(dataset):
    numeric_dataset = dataset.select_dtypes(include=["int", "float"])
    results = {}

    for col in numeric_dataset.columns:
        data = []
        for v in numeric_dataset[col]:
            if isinstance(v, (int, float)) and v == v:
                data.append(v)

        if len(data) == 0:
            continue

        results[col] = {
            "Count": count(data),
            "Mean": mean(data),
            "Std": std(data),
            "Min": min_value(data),
            "25%": percentile(data, 25),
            "50%": percentile(data, 50),
            "75%": percentile(data, 75),
            "Max": max_value(data),
        }

    stats = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    index_width = max(len(s) for s in stats)

    col_widths = {}
    col_names = {}
    for col in results:
        short_col = col[:12] if len(col) > 12 else col
        col_names[col] = short_col

        max_val_len = max(
            len(f"{results[col][stat]:.6f}")
            for stat in stats
        )
        col_widths[col] = max(len(short_col), max_val_len)

    print(" " * (index_width + 2), end="")
    for col in results:
        print(f"{col_names[col]:>{col_widths[col] + 2}}", end="")
    print()

    for stat in stats:
        print(f"{stat:<{index_width}}", end="  ")
        for col in results:
            value = results[col][stat]
            print(f"{value:>{col_widths[col] + 2}.6f}", end="")
        print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 describe.py <dataset.csv>")
        sys.exit(1)

    try:
        dataset = parse_dataset(sys.argv[1])
        describe_numerical_features(dataset)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
