def count(values):
    return len(values)

def mean(values):
    return sum(values) / len(values)

def min_value(iterable, key=None):
    min = sorted(iterable, key=key)
    return min[0]

def max_value(iterable, key=None):
    max = sorted(iterable, key=key, reverse=True)
    return max[0]

def std(values):
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5

def percentile(values, p):
    values = sorted(values)
    k = (len(values) - 1) * (p / 100)
    f = int(k)
    c = min_value([f + 1, len(values) - 1])
    return values[f] + (values[c] - values[f]) * (k - f)
