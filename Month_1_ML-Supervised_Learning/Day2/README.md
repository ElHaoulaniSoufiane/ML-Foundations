# Day 02 — ft_compute_cost

## What I built
A function that measures how wrong the model's predictions are using 
Mean Squared Error — square each error, sum them, divide by 2m.

## What I learned
- J = (1/2m) × Σ(ŷ - y)² is the cost function formula
- Square first then sum — not sum then square (parentheses matter)
- A perfect line gives cost = 0.0
- np.sum() collapses the array into one number

## Function
ft_compute_cost(X, y, w, b) → scalar J

## Challenge
Looped over 100 values of w from 0 to 4.
Found minimum cost at w ≈ 1.98 — close to the true value of 2.0.
Not exactly 2.0 because linspace doesn't hit it perfectly.

## Tests
All 3 tests pass.