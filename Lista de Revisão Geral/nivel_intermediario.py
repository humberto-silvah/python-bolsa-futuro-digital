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

print("Crie uma lista de números e calcule a soma de todos os elementos.")
numeros=[1,5,2,6,7]
print(calcula_lista(numeros))

print(" Crie um dicionário onde cada chave é um nome e o valor é uma tupla com (idade, cidade).")
nomes=["maria", "joao", "pedro"]
idades=[20,22,30]
cidades=["Campina Grande","Patos","Joao Pessoa"]
print(dicionario_tupla(nomes,idades,cidades))

print("Classifique um número como 'pequeno' (<10), 'médio' (10-50) ou 'grande' (>50).")
classifica_tamanho(-1)
classifica_tamanho(11)
classifica_tamanho(51)

print("mprima uma tabuada de 1 a 5 (ex: 1x1=1, 1x2=2, etc.).")
tabuada(3,4)

print("Crie uma função que recebe uma lista e retorna o maior número.")
numeros=[2,5,8,9.9,10,70]
print(verifica_maior_da_lista(numeros))

