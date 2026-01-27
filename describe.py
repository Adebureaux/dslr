import sys
import math
import pandas as pd

def parse_dataset(filename):
    try:
        dataset = pd.read_csv(filename)

        if dataset.shape[0] == 0 or dataset.shape[1] == 0:
            raise ValueError("Empty or invalid CSV")

        return dataset

    except FileNotFoundError:
        raise FileNotFoundError("Error: file not found")

    except pd.errors.EmptyDataError:
        raise ValueError("Error: empty CSV")

    except pd.errors.ParserError:
        raise ValueError("Error: impossible to parse CSV")

    except Exception as e:
        raise ValueError(f"Unknown error: {e}")


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

        # COUNT
        count = 0
        for _ in data:
            count += 1

        # MEAN
        total = 0
        for v in data:
            total += v
        mean = total / count

        # STD
        if count > 1:
            var_sum = 0
            for v in data:
                var_sum += (v - mean) ** 2
            std = math.sqrt(var_sum / (count - 1))
        else:
            std = 0.0

        # MIN / MAX
        min_val = data[0]
        max_val = data[0]
        for v in data:
            if v < min_val:
                min_val = v
            if v > max_val:
                max_val = v

        # SORT
        sorted_data = data[:]
        sorted_data.sort()

        # PERCENTILES
        def percentile(p):
            idx = p * (count - 1)
            lo = int(idx)
            hi = lo + 1 if lo + 1 < count else lo
            frac = idx - lo
            return sorted_data[lo] * (1 - frac) + sorted_data[hi] * frac

        results[col] = {
            "Count": count,
            "Mean": mean,
            "Std": std,
            "Min": min_val,
            "25%": percentile(0.25),
            "50%": percentile(0.50),
            "75%": percentile(0.75),
            "Max": max_val,
        }

    # DISPLAY
    stats = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

    index_width = max(len(s) for s in stats)

    col_widths = {}
    col_names = {}
    for col in results:
        short_col = col[:12] if len(col) > 12 else col
        col_names[col] = short_col

        max_val_len = max(
            len(f"{results[col][stat.capitalize()]:.6f}")
            for stat in stats
        )
        col_widths[col] = max(len(short_col), max_val_len)

    # HEADER
    print(" " * (index_width + 2), end="")
    for col in results:
        print(f"{col_names[col]:>{col_widths[col] + 2}}", end="")
    print()

    # ROWS
    for stat in stats:
        print(f"{stat:<{index_width}}", end="  ")
        for col in results:
            value = results[col][stat.capitalize()]
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
