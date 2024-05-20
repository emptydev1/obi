# Um novo professor contratado pela prefeitura que irá ensinar a crianças a jogar tenis reuniu todas as crianças interessadas em aprender
# Ao final do primeiro mes de aulas e treinamentos todos os participantes participaram de um torneio onde cada um disputou 6 jogos
# O professor vai utilizar o desempenho das crianças para separa-las em 3 grupos
# Se o participante venceu 5 ou 6 jogos, faz parte do grupo 1
# Se o participante venceu 3 ou 4 jogos, faz parte do grupo 2
# Se o participante venceu 1 ou 2 jogos, faz parte do grupo 3
# Se o participante não venceu nenhum jogo, não faz parte de nenhum grupo
# Caso o participante não faça parte de nenhum grupo, o programa deve retornar -1
# Importante: V -> venceu a partida; P -> perdeu a partida

matches = sum([1 if input().upper() == "V" else 0 for _ in range(6)])

print(1 if matches >= 5 else 2 if matches >= 3 and matches <= 4 else 3 if matches >= 1 and matches <= 2 else -1)