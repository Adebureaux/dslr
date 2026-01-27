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
