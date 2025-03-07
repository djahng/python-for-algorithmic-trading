import math
import random
import numpy as np

# Gemoetric Brownian Motion:
# S_T = S_0 * exp((r - 0.5 * sigma ** 2) * T + sigma * z * sqrt(T))

def brownian(n, S_0=100, r=0.05, T=1.0, sigma=0.2):
    values = []
    for _ in range(n):
        S_T = S_0 * math.exp((r - 0.5 * sigma ** 2) * T + sigma * random.gauss(0, 1) * math.sqrt(T))
        values.append(S_T)

    return values

def np_brownian(n, S_0=100, r=0.05, T=1.0, sigma=0.2):
    return S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.random.standard_normal(n) * np.sqrt(T))


# Compare the execution time for a pure python implementation vs numpy.
if __name__ == "__main__":
    import time

    n = 1_000_000

    # Time a pure python implementation
    t_start = time.perf_counter()
    _ = brownian(n)
    t_end = time.perf_counter()

    print(f"Pure python: {(t_end-t_start):.4f} seconds")

    # Time a numpy implementation
    t_start = time.perf_counter()
    _ = np_brownian(n)
    t_end = time.perf_counter()

    print(f"Numpy: {(t_end-t_start):.4f} seconds")
