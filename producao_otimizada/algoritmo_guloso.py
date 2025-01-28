def algoritmo_guloso(fabrica):
    fabrica.linha_producao = [[] for _ in range(fabrica.num_linhas)]
    maior_custo_linha = 0  

    for i in range(fabrica.num_produtos):
        linha_menor_tempo = -1
        menor_tempo_total = float('inf')

        for j in range(fabrica.num_linhas):
            tempo_total = 0
            for k in range(len(fabrica.linha_producao[j])):
                produto_ant = fabrica.linha_producao[j][k]
                tempo_total += fabrica.tempos[produto_ant - 1]

                if k > 0:
                    produto_atual = fabrica.linha_producao[j][k - 1]
                    tempo_total += fabrica.preparos[produto_ant - 1][produto_atual - 1]

            if tempo_total < menor_tempo_total:
                menor_tempo_total = tempo_total
                linha_menor_tempo = j

        fabrica.linha_producao[linha_menor_tempo].append(i + 1)
        fabrica.custo_tempo += fabrica.tempos[i]

        if len(fabrica.linha_producao[linha_menor_tempo]) > 1:
            produto_ant = fabrica.linha_producao[linha_menor_tempo][-2]
            fabrica.custo_tempo += fabrica.preparos[produto_ant - 1][i]

    for i in range(fabrica.num_linhas):
        custo_linha = 0
        for j in range(len(fabrica.linha_producao[i])):
            produto = fabrica.linha_producao[i][j]
            custo_linha += fabrica.tempos[produto - 1]

            if j > 0:
                produto_ant = fabrica.linha_producao[i][j - 1]
                custo_linha += fabrica.preparos[produto_ant - 1][produto - 1]

        if custo_linha > maior_custo_linha:
            maior_custo_linha = custo_linha

    fabrica.custo_tempo = maior_custo_linha
    return fabrica.custo_tempo