# Uma empresa está desenvolvendo um novo relógio eletrônico para atletas de alto desempenho. Uma das funcionalidades do novo relógio é que ele vai medir a frequência cardíaca atual (batidas do coração por minuto) e a capacidade de oxigenação atual do atleta. O relógio também vai calcular e armazenar a frequência cardíaca em repouso do atleta.
# O rélogio deve emitir um aviso para: diminuir o ritimo do exercício quando a frequencia cardiaca atual for tres vezes maior que a frequencia cardiaca em repouso ou a capacidade de oxigenação for menor que 95 | aumentar o rítimo do exercício quando se a frequencia cardiaca atual é menor que duas vezes a frequencia cardiaca em repouso e a capacidade de oxigenação atual é maior que 97 | manter o rítimo de treino se nenhuma das condições anteriores ocorrer

# 1. Dados de entrada
# A entrada é composta por três linhas, cada uma contendo um único número inteiro.
# 1.1 A primeira linha contém o inteiro R, a frequência cardíaca em repouso do atleta.
# 1.2 A segunda linha contém o inteiro F, a frequência cardíaca atual do atleta.
# 1.3 A terceira linha contém o inteiro C, a capacidade de oxigenação atual do atleta.

# 2. Dados de saída
# O programa deve produzir uma única linha, contendo uma única palavra, em letras minúsculas, que deve ser 'aumentar', 'diminuir', ou 'manter', de acordo com os critérios estabelecidos acima.

fcr, fca, coa = [int(input()) for _ in range(3)]

print('diminuir' if fca >= (fcr * 3) or coa < 95 else 'aumentar' if fca < (fcr * 2) and coa > 97 else 'manter')