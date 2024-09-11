nome = input()
sfixo = float(input())
tvendas = float(input())

percentagem = 15/100
total_mes = sfixo + (tvendas * percentagem)
print(f"TOTAL = R$ {total_mes:.2f}")
