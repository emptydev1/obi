# Quatro amigos decidiram jogar tenis em duplas
# O nivel do jogador é respresentado por um número inteiro que, quanto maior, melhor o jogador
# Os jogadores querem uma partida justa, então o nível dos times, que é definido com a soma do nível dos jogadores do time, sejam o mais próximos possíveis
# O programa deve encontrar a menor diferença possível entre os níveis dos times
a, b, c, d = [int(input()) for _ in range(4)] # obter o nível de cada um dos quatro jogadores

print(min(abs((a + b) - (c + d)), abs((a + c) - (b + d)), abs((a + d) - (b + c)))) # imprime o menor resultado das possíveis diferenças absolutas 