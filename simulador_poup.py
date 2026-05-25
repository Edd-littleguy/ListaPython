#simulador de investimentos--
aporte = float(input("quanto você vai depositar por mês?"))
juros = float(input("qual é a taxa de juros atual da poupança?"))
meses = int(input("por quantos meses você vai investir?"))
juros_decimal = juros/100
total = 0 
for mes in range (1, meses +1):
  total = total + aporte
  total = total + (total*juros_decimal)
  print(f"Mês {mes}: saldo total = R${total}")
print(f"ao final de {meses} meses, você terá o valor de R$:{total:.2f}")
