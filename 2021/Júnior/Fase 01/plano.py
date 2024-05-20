# O plano permite que João use uma quota de até X megabytes
# Se toda a quota não é utilizada, são adicionados os megabytes restantes para o próximo mes
# Ex.: 1° mes: 150/200 | 2° mes: 220/250 | 3° mes: 230 -> o limite inicial é 200, se ele usa 150 no primeiro mes, os 50 restantes sao passados para o proximo mes, o que totaliza 250; nesse segundo mes ele usa 220 de 250, que faz com que reste 30 de quota que sao passados para o terceiro mes, totalizando 230
# Determinar quanto João terá de quota disponivel no mes N + 1

quota, months = int(input()), int(input()) # obter os valores numéricos "quota" (quota inicial) e "months" (quantidade de meses)
quota_uses = [int(input()) for _ in range(months)] # obter os valores da quantidade de uso de quota em cada mes

print(quota + sum([quota - quota_uses[i] for i in range(len(quota_uses))])) # somar o valor do quota inicial com a soma do restante dos meses anteriores