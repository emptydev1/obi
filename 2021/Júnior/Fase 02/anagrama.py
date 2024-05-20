# Verificar se duas frases são ou não anagramas
# Importante: N -> não são anagramas; S -> são anagramas

n = int(input())
a = sorted(c for c in input() if c.isalpha())
b = sorted(c for c in input() if c.isalpha())

print("N" if len(a) != len(b) and 1 <= n <= 200 or a != b else "S")