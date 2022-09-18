with open("frutas.txt", "r") as var:
    lista_de_frutas = var.readlines()

print(f'a lista tem {len(lista_de_frutas)} linhas')

print()
print(lista_de_frutas)

with open('frutas.txt', 'a') as var:
    var.write('\n') # pulando a linha que eu tinha esquecido
    var.write('10\n11\n12\n...')

# cada vez que eu rodo esse código ele irá adicionar mais três linhas ao arquivo