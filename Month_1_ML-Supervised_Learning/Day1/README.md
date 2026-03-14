# Day 01 — ft_predict

## What I built
A function that computes predictions for all examples at once using dot product.

## What I learned
- prediction = w · x + b
- np.dot(X, w) replaces a for loop — this is vectorization
- Vectorization is faster and cleaner than looping over examples

## Function
```python
ft_predict(X, w, b) → (m,) array of predictions
```

## Tests
All 3 tests pass — single feature, multiple features, zero weights.