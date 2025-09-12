def calcula_lista(lista_numeros):
    resultado=sum(lista_numeros)
    return resultado

def dicionario_tupla(chave,valor1,valor2):
    dicionario={}
    for i in range(len(chave)):
        dicionario[chave[i]] = valor1[i] , valor2[i]
    return dicionario

def classifica_tamanho(numero):
    if (numero < 10):
        print(f"{numero}, é pequeno")
    elif (numero >=10) and (numero <= 50):
        print(f"{numero}, é medio")
    elif (numero > 50):
        print(f"{numero}, é grande")

def tabuada(inicio, fim):
    for num in range(inicio, fim + 1):  
        print(f"\nTabuada do {num}:")
        for i in range(1, 11):  
            print(f"{num} x {i} = {num * i}")
    
def verifica_maior_da_lista(lista):
    return max(lista)

def contar_frequencia(palavra):
    frequencia = {}
    for letra in palavra:
       
        letra = letra.lower()
        if letra.isalpha():
            if letra in frequencia:
                frequencia[letra] += 1
            else:
                frequencia[letra] = 1
    return frequencia


def teste_polindromo(palavra):
    frase = palavra.replace(" ", "").lower()

    if frase == frase[::-1]:
        print(f"{palavra}, é Polindromo")
    else:
        print(f"{palavra}, não é Polimbromo")

def imprime_par(inicio,fim):
    par = []
    for i in range(inicio,fim + 1):
        if (i % 2 == 0):
            par.append(i)
    return par

def fatorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado *= i
    return resultado

print("11ª Crie uma lista de números e calcule a soma de todos os elementos.")
calcula=[1,5,2,6,7]
print(calcula_lista(calcula),"\n")

print("12ª Crie um dicionário onde cada chave é um nome e o valor é uma tupla com (idade, cidade).")
nomes=["maria", "joao", "pedro"]
idades=[20,22,30]
cidades=["Campina Grande","Patos","Joao Pessoa"]
print(dicionario_tupla(nomes,idades,cidades),"\n")

print("13ª Classifique um número como 'pequeno' (<10), 'médio' (10-50) ou 'grande' (>50).")
classifica_tamanho(-1)
classifica_tamanho(11)
classifica_tamanho(51)
print()

print("14ª mprima uma tabuada de 1 a 5 (ex: 1x1=1, 1x2=2, etc.).")
tabuada(3,4)
print()
print("15ª Crie uma função que recebe uma lista e retorna o maior número.")
maior=[2,5,8,9.9,10,70]
print(verifica_maior_da_lista(maior),"\n")

print("16ª Conte a frequência de cada letra em uma palavra (ex: 'hello' → {'h':1, 'e':1, 'l':2, 'o':1}).")
print(contar_frequencia("Hello World"),"\n")

print("17ª Crie uma lista de dicionários representando livros (título, autor, ano) e imprima todos.")
livros=["O Senhor dos Anéis",
        "A Guerra dos Tronos",
        "1984",
        "O Guia do Mochileiro das Galáxias"]
autores=["J.R.R. Tolkien",
         "George R.R. Martin",
         "George Orwell",
         "Douglas Adams"]
ano=[1954,1996,1949,1979]
print(dicionario_tupla(livros,autores,ano),"\n")

print("18ª Verifique se uma string é um palíndromo")
teste_polindromo("Hello Wrod")
teste_polindromo("ana")
print()

print("19ª Imprima apenas os números pares entre 1 e 20.")
print(imprime_par(1,20),"\n")

print("20ª Crie uma função recursiva para calcular o fatorial de um número.")
print(fatorial(5),"\n")




