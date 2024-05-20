# Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a soma das idades dos seus três filhos é igual à idade dela.
# Nesse problema será dado a idade de Dona Monica e a idade de seus dois filhos mais novos
# O programa deve retornar a idade do filho mais velho

# 1. Dados de entrada
# 1.1 A primeira linha da entrada contém um inteiro M representando a idade de dona Mônica. A segunda linha da entrada contém um inteiro A representando a idade de um dos filhos. A terceira linha da entrada contém um inteiro B representando a idade de outro filho.

a1, a2, a3 = sorted([int(input()) for _ in range(3)], reverse=True)

print(max(a2, a3, a1 - a2 - a3)) # retornar a idade do filho mais velho de Dona Monica