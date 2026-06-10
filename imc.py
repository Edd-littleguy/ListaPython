#etapa 1 - calculo do imc
def cal_imc(peso,altura):
   imc = peso / (altura * altura)
   return imc
#etapa 2 - classificar o imc
def classificar_imc(valor_imc):
   if valor_imc >= 25:
      return "ACIMA DO PESO"
   else:
      return "PESO NORMAL"
#etapa 3 - mensagem de saída
def mensagem(status):
   if status == "ACIMA DO PESO":
      return "ATENÇÃO: procure um medico.."
   else:
      return "muito bem!, continue assim!!!"
#etapa 4 - integraçao de projeto
valor_peso = float(input("digite seu peso atual: ")) 
valor_altura = float(input("digite sua altura: "))  

resultado = cal_imc(valor_peso, valor_altura)
classificar = classificar_imc(resultado)

saida = mensagem(classificar)

print("=" * 50)
print(f"seu IMC e:")