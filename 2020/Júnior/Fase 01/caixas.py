# O programa deve definir quantas viagens um drone precisa fazer para carregar 3 caixas, considerando que não seja restritamente necessário fazer 3 viagens, caso seja possível colocar uma caixa dentro de outra
# Uma caixa pode ser colocada dentro da outra caso seja menor (C1 < C2). Além disso, duas caixas podem ser colocadas dentro de outra, se a soma do tamanho de ambas for menor que a terceira ((C1 + C2) < C3)
c1, c2, c3 = sorted([int(input()) for _ in range(3)], reverse=True)

print(1 if (c3 < c2 < c1) or ((c2 + c3) < c1) else 2 if (c2 < c1 and c3 >= c2) or (c3 < c1 and c2 >= c3) else 3)