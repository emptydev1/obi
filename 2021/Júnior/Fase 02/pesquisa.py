# Uma jornalista pesquisou em relação aos preços de álcool e gasolina em vários estados do país sobre qual dos dois é mais vantajoso para abastecer
# Ela considerou o álcool mais vantajoso quando seu preço é no máximo 70% do preço da gasolina
# O programa deve fornecer qual(is) estado(s) é(são) mais vantajoso(s) o álcool ou gasolina

# 1. Dados de entrada:
# 1.1 A primeira linha é a quantidade de estados em que a pesquisa foi realizada;
# 1.2 O restante das linhas contém informações sobre os identificadores de cada estado e os preços de álcool e gasolina, respectivamente

# 2. Dados de saída
# 2.1 O programa deve imprimir em linhas distintas qual estado é mais vantajoso a compra do álcool
# 2.2 Caso em nenhum dos estados seja vantajoso a compra do álcool, deve imprimir apenas '*'

amount = int(input())
states = [input().split(' ') for _ in range(amount)]
pref_al = [state[0] for state in states if float(state[1]) <= 70 / 100 * float(state[2])]

print('*') if len(pref_al) <= 0 else [print(state) for state in pref_al]