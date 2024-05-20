# O programa deve determinar quantos dias a Dona Lesma levará para subir o muro inteiro, considerando que ela sobe uma mesma quantidade todos os dias e a cada noite quando dorme ela escorrega outra determinada distancia

# 1. Dados de entrada
# 1.1 A primeira linha contém um inteiro A, a altura do muro. A segunda linha contém um inteiro S, distância que Dona Lesma sobe a cada dia. A terceira linha contém um inteiro D, a distância que Dona Lesma escorrega para baixo a cada noite.

# 2. Dados de saída
# 2.1 Seu programa deve produzir uma única linha, contendo um único inteiro, o número de dias que Dona Lesma demorará para chegar ao topo do muro.

height, dtn, dsn = [int(input()) for _ in range(3)]
progress, days = 0, 0

while progress < height:
    progress += dtn
    days += 1
    if progress >= height:
        break
    progress -= dsn

print(days)