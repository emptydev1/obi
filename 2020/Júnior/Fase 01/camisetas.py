# Uma empresa confeccionou camisetas para os premiados da Olímpiada Municipal de Programação, que informaram os seus tamanhos preferidos da camiseta (pequeno ou médio).
# Graças a uma falha, houve um engano ao produzir as camisetas, pois a quantidade confeccionada de cada tamanho foi foi incorreta.
# O programa deve verificar se os premiados receberam a camisa conforme o tamanho selecionado

# 1. Entrada
# 1.1 A primeira linha contém o número de premiados
# 1.2 A segunda contém os tamanhos solicitados por cada premiado, sendo 1 as camisas pequenas e 2 as camisas médias
# 1.3 A terceira linha contém o número de camisetas pequenas produzidas
# 1.4 A quarta linha contém o número de camisetas médias produzidas

# 2. Saída
# 2.1 O programa deve produzir uma única linha, contendo um único caractere, que deve ser a letra maiúscula 'S' se todos os premiados serão atendidos com a camiseta do tamanho que escolheram, ou a letra maiúscula 'N' caso contrário

amount, sizes, sizep, sizem = int(input()), list(map(int, input().split(' '))), int(input()), int(input())

print('S' if len(list(filter(lambda n: n == 1, sizes))) == sizep and len(list(filter(lambda n: n == 2, sizes))) == sizem else 'N')