# O jogo de dominó tradicional, conhecido como duplo-6, possui 28 peças. Cada peça está dividida em dois quadrados e dentro de cada quadrado há entre 0 e 6 círculos. O jogo é chamado de duplo-6 justamente porque esse é o maior número de círculos que aparece num quadrado de uma peça. A figura ao lado mostra uma forma de organizar as 28 peças do jogo duplo-6 em 7 linhas.
# Existe uma fórmula com a qual podemos calcular facilmente o número de peças de um jogo do tipo duplo-N, para um número N natural qualquer: ((N+1)*(N+2))/2. Neste problema, o programa deverá utilizar esta fórmula para calcular e imprimir quantas peças existem num jogo de dominó do tipo duplo-N. Sendo "N" o número fornecido
n = int(input())

print(int(((n + 1) * (n + 2)) / 2))