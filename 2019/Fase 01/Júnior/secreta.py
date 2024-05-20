# Na calçada em frente ao Palácio Imperial, não se sabe a razão, existe uma sequência de N números desenhados no chão. A sequência tem a seguinte forma: ela começa e termina com o número 1; apenas os números 1 e 2 aparecem nela; e o número 2 aparece pelo menos uma vez.
# Neste problema, dada a sequência original de números desenhados no chão da calçada, o programa deve computar e imprimir a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada.

# 1. Dados de entrada
# 1.1 A primeira linha da entrada contém um inteiro N representando o tamanho da sequência. As N linhas seguintes contêm, cada uma, um inteiro Vi, para 1 ≤ i ≤ N, definindo a sequência de números desenhados no chão da calçada imperial.

# 2. Dados de saída
# 2.1 O programa deve imprimir uma linha contendo um número inteiro representando a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada.

size = int(input())
sequence = [int(input()) for _ in range(size)]

