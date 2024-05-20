# Um pangrama é uma palavra que contém todas as letras do alfabeto e, no portugues, também pode incluir palavras acentuadas (desconsiderado nesse problema em especifico)
# Serão desconsideradas as letras: k, w e y
# Ex.: grave e cabisbaixo, o filho justo zelava pela querida mae doente
# Importante: S -> é um pangrama | N -> não é um pangrama
letters = "abcdefghijlmnopqrstuvxz" # letras do alfabeto em caixa baixa, não incluindo as letras k, w e y
phrase = list(filter(lambda c: c in letters, list(input()))) # obtendo a cadeia de caracteres e filtrando apenas as letras

print('S' if all(c in phrase for c in list(letters)) else 'N')