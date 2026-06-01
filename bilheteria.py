#aluno1:padronizar nome do filme
def formatar(name):
    return name.upper()
#aluno2:verificador de idade
def verify_age(age):
     if age >= 18:
        return "autorizado✅"
     else:
        return "não autorizado"
#aluno3:mensagem de retorno
def create_mesage(status):
     if status == "autorizado✅":
        return "tenha uma otima sessão!!!"
     else: 
        return "sentimos muito em informar, mas você não tem a idade minima."
#aluno4:execução do algoritmo
film_enter = input("Digite o filme escolhido: ")
age_enter = int(input("Digite sua idade: "))
name_final = formatar(film_enter)
status_acess = verify_age(age_enter)
mesage = create_mesage(status_acess)
print(f"\nfilme:{name_final}")
print(f"status:{status_acess}")
print(f"mensagem:{mesage}")