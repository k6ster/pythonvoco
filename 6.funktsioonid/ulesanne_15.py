def hinne(punktid):
    if punktid >= 90:
        return 5
    if punktid >= 75:
        return 4
    if punktid >= 60:
        return 3
    if punktid >= 50:
        return 2
    return 1

print(hinne(82))
