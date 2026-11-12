import math


def ringi_pindala(raadius):
    return math.pi * raadius ** 2


for raadius in (2, 5, 10):
    print(f"Raadius {raadius}: {ringi_pindala(raadius):.2f}")
