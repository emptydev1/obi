# Escher foi um artista gráfico holandês que fazia incríveis ilustrações onde preenchia a tela com objetos auto-similares, cujos contornos encaixam neles próprios, criando simetrias geométricas
# Para ser considerado um perfil de Escher, a quantidade de elementos da sequencia deve ser um número par e a soma de suas extremidades e meios devem ser iguais
# Ex.: A1+AN igual a A2+AN-1 igual a A3+AN-2, e assim por diante

# 1. Dados de entrada
# 1.1 a primeira linha é um número inteiro com o tamanho da sequencia
# 1.2 a segunda linha é uma sequencia de números inteiros

# 2. Dados de saída
# 2.1 O programa deve retornar 'S' se o input for um perfil se Escher válido e 'N' caso contrario

size, sequence = int(input()), list(map(int, input().split(' ')))
tmp = [sequence[i] + sequence[size - 1 - i] for i in range(size)]

print('S' if size % 2 == 0 and all(e == tmp[0] for e in tmp) else 'N')

# 60% de precisão