import time
import numpy as np
import pandas as pd
from vnd import vnd
from algoritmo_guloso import algoritmo_guloso

def calcular_resultados(fabrica, instancia, num_execucoes=10, sol_otima=None):
    # Variáveis para armazenar os resultados das execuções
    tempos_guloso = []
    solucoes_guloso = []
    tempos_vnd = []
    solucoes_vnd = []

    melhor_sol_guloso = float('inf')
    melhor_sol_vnd = float('inf')
    
    for _ in range(num_execucoes):
        # Algoritmo Guloso
        start_time = time.time()
        custo_guloso = algoritmo_guloso(fabrica)
        tempos_guloso.append(time.time() - start_time)
        solucoes_guloso.append(custo_guloso)
        melhor_sol_guloso = min(melhor_sol_guloso, custo_guloso)
        
        # VND
        start_time = time.time()
        vnd(fabrica)
        tempos_vnd.append(time.time() - start_time)
        solucoes_vnd.append(fabrica.custo_tempo)
        melhor_sol_vnd = min(melhor_sol_vnd, fabrica.custo_tempo)

    # Cálculo da média e GAP
    media_sol_guloso = np.mean(solucoes_guloso)
    media_tempos_guloso = np.mean(tempos_guloso)
    gap_guloso = ((media_sol_guloso - sol_otima) / sol_otima) * 100 if sol_otima else None

    media_sol_vnd = np.mean(solucoes_vnd)
    media_tempos_vnd = np.mean(tempos_vnd)
    gap_vnd = ((media_sol_vnd - sol_otima) / sol_otima) * 100 if sol_otima else None

    # Criando a tabela com os resultados
    resultado = {
        'Instancia': instancia,
        'Algoritmo': ['Guloso', 'VND'],
        'Média Solução': [media_sol_guloso, media_sol_vnd],
        'Melhor Solução': [melhor_sol_guloso, melhor_sol_vnd],
        'Média Tempo (s)': [media_tempos_guloso, media_tempos_vnd],
        'GAP (%)': [gap_guloso, gap_vnd]
    }
    
    return pd.DataFrame(resultado)
