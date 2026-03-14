import numpy as np

def ft_predict(X,w,b):
    y_hat = np.dot(X,w) + b
    return y_hat

def ft_compute_cost(X,y,w,b):
    m = len(y)
    cost_sum = np.sum((ft_predict(X,w,b) - y) ** 2)
    j = (1/(2*m)) * cost_sum
    return j

X = np.array([[1.], [2.], [3.], [4.], [5.]])
y = np.array([3., 5., 7., 9., 11.])

# Test 1 — perfect fit → cost must be 0
w_perfect = np.array([2.])
b_perfect = 1.0
print(ft_compute_cost(X, y, w_perfect, b_perfect) == 0.0)

# Test 2 — bad fit → cost must be > 0
w_bad = np.array([0.5])
b_bad = 0.0
print(ft_compute_cost(X, y, w_bad, b_bad) > 0)

# Test 3 — better line has lower cost than worse line
w_ok = np.array([1.8])
b_ok = 1.2
print(ft_compute_cost(X, y, w_ok, b_ok) < ft_compute_cost(X, y, w_bad, b_bad))

# Challenge
# Find The Lowest MSE
w_values = np.linspace(0.0, 4.0, 100)
cost = {}
for w in w_values:
    cost[w] = ft_compute_cost(X,y,[w],b_perfect)
target_j = min(cost.values())

# Find The Matching W
for w_val,j in cost.items():
    if j == target_j:
        print(f"The best Wight is {w_val} because He have {target_j} lowst MSE")

