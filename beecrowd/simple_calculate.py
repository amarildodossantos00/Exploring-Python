cprod1, uprod1, price1 = input().split()

cprod1 = int(cprod1)
uprod1 = int(uprod1)
price1 = float(price1)

cprod2, uprod2, price2 = input().split()

cprod2 = int(cprod2)
uprod2 = int(uprod2)
price2 = float(price2)

vbuy = (uprod1 * price1) + (uprod2 * price2)
print(f"VALOR = PAGAR: R$ {vbuy:.2f}")
