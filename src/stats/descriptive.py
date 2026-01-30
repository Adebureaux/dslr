def count(values):
    return len(values)

def mean(values):
    return sum(values) / len(values)

def min_value(iterable, key=None):
    it = iter(iterable)
    try:
        best = next(it)
    except StopIteration:
        raise ValueError("min_value() arg is an empty sequence")

    best_key = key(best) if key else best

    for item in it:
        item_key = key(item) if key else item
        if item_key < best_key:
            best = item
            best_key = item_key

    return best

def max_value(iterable, key=None):
    it = iter(iterable)
    try:
        best = next(it)
    except StopIteration:
        raise ValueError("max_value() arg is an empty sequence")

    best_key = key(best) if key else best

    for item in it:
        item_key = key(item) if key else item
        if item_key > best_key:
            best = item
            best_key = item_key

    return best

def std(values):
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5

def percentile(values, p):
    values = sorted(values)
    k = (len(values) - 1) * (p / 100)
    f = int(k)
    c = min_value([f + 1, len(values) - 1])
    return values[f] + (values[c] - values[f]) * (k - f)
