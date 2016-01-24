import math

def polysum(n, s):
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    peri = n * s

    return round(area + peri**2, 4)
