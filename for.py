 tp = (2, 3, 4)    #() = Tupla
 for i in tp:
     print(i)

 ListaDoMercado = ["Leita", "Frutas", "Carne"] #[] = Lista
 for i in ListaDoMercado:
     print(i)

 for contador in range(0, 5):
     print(contador)

 lista = [1,2,3,4,54,6]
 for num in lista:
     if num % 2 == 0:   #pra pegar os numeros pares
         print(num)

continue pula o q foi especificado e continua

def primeiraFunc():
    print("Hello World")

primeiraFunc()

print("-="*30)

def primeiraFunc(nome):
    print("Hello %s" %(nome))

primeiraFunc("Aluno")

print("-="*30)

def funcLeitura():
    for i in range(0, 5):
        print(f"Numero {i}")

funcLeitura()

print("-="*30)

def addNUm(primeiro_num, segundo_num):
    print("Primeiro numero: " + str(primeiro_num))
    print("Segundo numero: " + str(segundo_num))
    print("Soma: ", primeiro_num + segundo_num)

addNUm(42, 4)

print("-="*30)

listaB = [32,53,85,10,15,17,19]
soma = 0
for i in listaB:
    double_i = i * 2
    soma += double_i

print(soma)

print("-="*30)

