# Uma empresa que desenvolve carros previsa integrar um sistema para melhorar o piloto automático dos carros, esse sistema dirá se o carro deverá manter a velocidade, acelrar ou desacelerar
# Considere que o carro B esteja entre os carros A e C
# O carro B precisa ser acelerado se a distância da sua traseira para a traseira do carro A for menor do que a distância da sua traseira para a traseira do carro C. Se for maior, ele precisa ser desacelerado. Se for igual, precisa manter a velocidade atual. Quer dizer, o carro B precisa ser acelerado se (B-A) < (C-B), desacelerado se (B-A) > (C-B) e manter a velocidade se (B-A) for igual a (C-B).

# 1. Dados de entrada
# 1.1 primeira linha da entrada contém um inteiro A.
# 1.2 A segunda linha da entrada contém um inteiro B.
# 1.3 A terceira linha da entrada contém um inteiro C.
# 1.4 Os três inteiros representam as posições atuais das traseiras dos carros A, B e C, respectivamente.

# 2. Dados de saída
# 2.1 O programa deve imprimir uma linha contendo um inteiro: 1 se o carro B precisa acelerar; -1 se precisa desacelerar; ou 0 se precisa manter a velocidade atual.

a, b, c = [int(input()) for _ in range(3)]

print(1 if (b - a) < (c - b) else -1 if (b - a) > (c - b) else 0)