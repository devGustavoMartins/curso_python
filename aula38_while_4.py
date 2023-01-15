"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: # While de linhas começa
    coluna = 1
    while coluna <= qtd_colunas: # While de colunas começa dentro do while de linhas, portanto a cada rodada de linha terão 5 de colunas.
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('While terminou')