# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(f'A união dos dois sets é {s3}')
print(f'Os termos em comum entre os dois sets são {s4}')
print(f'Os elementos presentes só no primeiro set são {s5}')
print(f'Os elementos que não tem nos dois sets são {s6}')