#1
def gip(x, y):
    return (x ** 2 + y ** 2)**(0.5)

a1, b1 = map(float, input("Катеты 1-го треугольника a1, b1 = ").split())
a2, b2 = map(float, input("Катеты 2-го треугольника a2, b2 = ").split())
c1 = gip(a1, b1)
print("Гипотенуза 1-го треугольника =", c1)
c2 = gip(a2, b2)
print("Гипотенуза 2-го треугольника =", c2)
if c1 == c2:
    print("Гипотенузы равны")
if c1 > c2:
    print("Гипотенуза 1-го треугольника больше")
else:
    print("Гипотенуза 2-го треугольника больше")

#2
s = input().split()
for i in range(len(s)):
    s[i] = "".join(sorted(s[i]))
print(" ".join(s))
