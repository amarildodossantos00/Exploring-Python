a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

triangle = ((a * c) / 2)
circle = (3.14159 * pow(c, 2))
trapezium = (((a + b) * c) / 2)
square = (pow(b, 2))
rectangle = a * b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")
