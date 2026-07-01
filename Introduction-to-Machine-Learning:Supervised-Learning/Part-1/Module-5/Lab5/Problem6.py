####Demonstrate impurity and information gain on a small synthetic binary dataset.


# Grade Cell: Question 6
#
# Task: Compute Gini and information gain for candidate splits.
#
# Instructions:
# 1. Generate a small 2D dataset with two classes (balanced-ish).
# 2. For a few split thresholds on x1 (e.g., -0.5, 0.0, 0.5), compute Gini(parent), Gini(left), Gini(right), and information gain.
# 3. Store gains in list `info_gain_values` aligned with `splits_x1` and show that the "middle" split has higher gain than edge splits.

def _entropy(y):
    y = np.asarray(y)
    if len(y) == 0:
        return 0.0
    _, c = np.unique(y, return_counts=True)
    p = c / c.sum()
    return float(-np.sum(p * np.log2(p, where=p > 0, out=np.zeros_like(p))))

def _info_gain(yp, yl, yr):
    n = len(yp)
    if n == 0:
        return 0.0
    return float(_entropy(yp) - (len(yl)/n)*_entropy(yl) - (len(yr)/n)*_entropy(yr))

x = np.array([1, 2, 3, 4, 6, 7, 8, 9])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

thresholds = [3, 5, 7]
info_gain_values: List[float] = [
    _info_gain(y, y[x < t], y[x >= t]) for t in thresholds
]

print(
    "Information gains (x1 splits at -0.5, 0.0, 0.5):",
    [round(v, 3) for v in info_gain_values],
)
