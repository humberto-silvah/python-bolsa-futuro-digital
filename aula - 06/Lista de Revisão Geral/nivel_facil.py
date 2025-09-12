<<<<<<< HEAD
def varre_lista(lista):
    for elemento in range(len(lista)):
        print (elemento)
=======
def varre_lista(lista):
    for elemento in lista:
        print (elemento)
>>>>>>> 2666cc34fccc3beda93fffd21ede0a11abcc2e3a

<<<<<<< HEAD
def verifica_p_n(numero):
    if (numero == 0):
        print("nulo")
    elif (numero > 0):
        print(numero,"é positivo")
    else:
        print("é negativo")

def imprime_num():
    for i in range(1,11):
        print(i)
    
#def cria_dicionario(chave, valor):

=======
def verifica_p_n(numero):
    if (numero == 0):
        print(numero,"nulo")
    elif (numero > 0):
        print(numero,"é positivo")
    else:
        print(numero,"é negativo")

def imprime_num(inicio, fim):
    for i in range(inicio,fim+1):
        print(i)
    
def cria_dicionario(lista_chaves, lista_valores):
    dicionario = {}
    for i in range(len(lista_chaves)):
        dicionario[lista_chaves[i]] = lista_valores[i]
    return dicionario

def soma(numerador, denominador):
    resultado = (numerador+denominador)
    return resultado

def contator_letras (palavra):
    quantidade = 0
    for i in palavra:
        quantidade +=1
    print(quantidade)

def add_elemento(lista,elemento):
    lista.append(elemento)
    return lista

def par_impar(numero):
    if numero == 0:
        print(0, "é nulo")
    elif (numero % 2 == 0):
        print(numero,"é par")
    else:
        print(numero, "é impar")

def meu_while(tamanho):
    contador = 1
    while (contador != tamanho+1):
        print(contador)
        contador+=1
    
def produtos(produtos,precoes):
    cria_dicionario(produtos,precoes)
    print(produtos)
    
print("Crie uma lista com os números de 1 a 5 e imprima cada elemento.")
numeros=[1,2,3,4,5]
varre_lista(numeros)

print("Peça um número ao usuário e verifique se é positivo, negativo ou zero.")
num1= -7 
num2= 10 
num3= 0
verifica_p_n(num1), verifica_p_n(num2), verifica_p_n(num3)

print("Use um loop `for` para imprimir os números de 1 a 10.")
imprime_num(1,10)

print("Crie um dicionário com nomes e idades de 3 pessoas e imprima cada par")
chave_nomes= ["ana","pedro","julia"]
valor_idades =[18,22,39]
print(cria_dicionario(chave_nomes,valor_idades))

print("Crie uma função que recebe dois números e retorna a soma.")
print(soma(20,5))

print("Peça uma palavra ao usuário e imprima o número de caracteres.")
contator_letras("pneumoultramicroscopicossilicovulcanoconiose")

print("Crie uma lista com 3 frutas e adicione uma nova fruta.")
feira=["abacate","banana","caju"]
add_elemento(feira,"uva")
print(feira)

print("Verifique se um número é par ou ímpar.")
par_impar(2), par_impar(999), par_impar(0)

print("Use um loop `while` para imprimir números de 1 a 5.")
meu_while(5)

print("Crie um dicionário de produtos e preços, depois imprima apenas os produtos.")
itens=["caneta","livro", "borracha"]
precoes=[2.5,199,2.5]
print(cria_dicionario(itens,precoes))
produtos(itens,precoes)
>>>>>>> 2666cc34fccc3beda93fffd21ede0a11abcc2e3a