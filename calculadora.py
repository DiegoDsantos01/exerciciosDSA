def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x/ y

print("Selecione a operação")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplição")
print("4 - Divisão")

print("-="*30) #Utilizado apenas para criar uma linha para separar melhor os prints

operação = (input("Digite a operação desejada: "))

num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if operação == "1":
    print(somar(num1, num2)) #Chama a função soma (criada no inicio do código) e passa as variaveis como parametro

elif operação =="2":
    print(subtrair(num1, num2)) 

elif operação == "3":
    print(multiplicar(num1, num2))

elif operação == "4":
    print(dividir(num1, num2))

else:
    print("Digite uma operação valida")