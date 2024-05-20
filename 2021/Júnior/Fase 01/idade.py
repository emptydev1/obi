# Nomes: Cibele, Camila, Celeste
# Cibele nasceu antes de Camila (Cibele < Camila)
# Celeste nasceu depois de Camila (Cibele > Camila)
# Objetivo: determinar a idade de Camila apartir de 3 numeros inteiros
# 1. Se Cibele nasceu antes de Camila e Celeste nasceu depois de Camila, então isso significa dizer que Camila está no centro (meio)
# 2. Dito isso, basta retornar a segunda maior idade fornecida

print(sorted([int(input()) for _ in range(3)], reverse=True)[1]) # organizando os valores numéricos do maior para o menor e imprimindo a segunda maior idade