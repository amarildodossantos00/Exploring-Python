import math
x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)

distance = math.sqrt(pow(x2 - x1, 2) + (pow(y2 - y1, 2)))
print(f"{distance:.4f}")
