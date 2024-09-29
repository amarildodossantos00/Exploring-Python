a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

aux = (a + b + abs(a-b)) / 2
maiorab = int((aux + c + abs(aux - c)) / 2)
print(f"{maiorab} eh o maior")
