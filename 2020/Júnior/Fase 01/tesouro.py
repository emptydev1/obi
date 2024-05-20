# O capitão encontrou juntamente de seus marinheiros uma arca com uma grande quantidade de moedas
# O capitão sugere que cada marinheiro (exceto ele mesmo) ficaria com a mesma quantidade de moedas
# O capitão deverá receber o dobro de moedas
coins, sailors = int(input()), int(input())

print((coins // (sailors + 2)) * 2) # Divide a quantidade de moedas pela quantidade total de marinheiros (incluindo o capitão) somada a 1 e depois multiplica o resultado por dois para obter o dobro dessa divisão, o resultado será a quantidade de moedas que pertenceram ao capitão