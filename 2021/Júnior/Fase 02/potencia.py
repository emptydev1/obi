# A profa. Vilma percebeu que ao publicar o enunciado de algumas questões de potenciação na Internet, a formatação das questões foi corrompida, fazendo com que os expoentes não fossem exibidos corretamente
# Ex.: 2^4 + 12^3 + 300^3 + 15^2 + 4^2 -> 24 + 123 + 3003 + 152 + 42
# O programa deve calcular o valor das expeessões originais

print(sum([int(term[:-1]) ** int(term[-1]) for term in [input() for _ in range(int(input()))]]))