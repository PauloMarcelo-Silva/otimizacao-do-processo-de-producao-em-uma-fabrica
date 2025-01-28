import random

def perturbacao(fabrica):
    linha = random.randint(0, fabrica.num_linhas - 1)
    pos1 = random.randint(0, len(fabrica.linha_producao[linha]) - 1)
    pos2 = random.randint(0, len(fabrica.linha_producao[linha]) - 1)

    if pos1 != pos2:
        fabrica.linha_producao[linha][pos1], fabrica.linha_producao[linha][pos2] = fabrica.linha_producao[linha][pos2], fabrica.linha_producao[linha][pos1]
