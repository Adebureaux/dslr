import math


def count(values):
    return len(values)


def mean(values):
    return sum(values) / len(values)


def min_value(values):
    min = values[0]
    for d in values:
        if not math.isnan(d):
            if min is None or d < min:
                min = d
    return min


def max_value(values):
    max = values[0]
    for d in values:
        if not math.isnan(d):
            if max is None or d > max:
                max = d
    return max


def std(values):
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5


def percentile(values, p):
    values = sorted(values)
    k = (len(values) - 1) * (p / 100)
    f = int(k)
    c = min(f + 1, len(values) - 1)
    return values[f] + (values[c] - values[f]) * (k - f)
