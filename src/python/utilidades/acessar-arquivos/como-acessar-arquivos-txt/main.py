# com o seguinte comando eu vou criar um arquivo txt e já abri-lo para editar nele

var = open("arquivinho.txt", 'w') # nome do arquivo, modo de abertura (nesse caso escrita)
# apartir desse momento, eu manipulo o cursor do editor de texto que está na posição zero
var.write('''
escrevendo na linha 1\n
escrevendo na linha 2\n
escrevendo na linha 3\n
sempre usando \+n pra pular linhas
''')
var.close() # fechando o arquivo

# o certo é:
# usar a estrutura with para fazer o fechamento do arquivo imediatamente:

with open("arquivinho.txt", "r") as var:
    lista_de_linhas = var.readlines()
    var.seek(0, 0) # voltando o cursor para o index zero
    stringão = var.read()

print()
print(lista_de_linhas)

print()
print(stringão)
