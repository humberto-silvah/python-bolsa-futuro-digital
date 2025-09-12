def dicionario_tupla(chave,valor1):
    dicionario={}
    for i in range(len(chave)):
        dicionario[chave[i]] = valor1[i] 
    return dicionario


print()
print("21ª Transforme duas listas (uma de chaves, outra de valores)" \
" em um dicionário.")
chaves = ['nome', 'idade', 'cidade']
valores = ['João', 25, 'São Paulo']
print(dicionario_tupla(chaves,valores,),"\n")