# Algne arvuta1 prindib 8, kuid x saab väärtuseks None, sest print ei tagasta summat.
def arvuta1(a, b):
    print(a + b)
    return a + b


def arvuta2(a, b):
    return a + b


x = arvuta1(5, 3)
y = arvuta2(5, 3)
print("x =", x)
print("y =", y)
print("Uus arvutus:", x + y)
