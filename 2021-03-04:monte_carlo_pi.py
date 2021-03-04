import math
import random


def monte_carlo_pi():
    n = 10000000
    in_circ = 0
    for _ in range(n):
        x = 2*random.random() - 1
        y = 2*random.random() - 1
        r2 = x**2 + y**2
        if r2 <= 1:
            in_circ += 1
    return 4 * in_circ / n


diff = monte_carlo_pi()-math.pi
print(diff)
assert abs(diff) <= 1e-3
