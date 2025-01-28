import time
from fabrica import Fabrica
from algoritmo_guloso import algoritmo_guloso
from vnd import vnd
from ils import ils
from calculo_e_resultados import calcular_resultados  # Importando a nova função

def main():
    start = time.time()
    fabrica = Fabrica()

    # Carregar o arquivo de entrada
    if not fabrica.leitura_arquivo(r"C:\Users\paulo\Faculdade\Programação Linear Inteira\otimizacao-do-processo-de-producao-em-uma-fabrica\Instancias\n10m2_A.txt"):
        exit(1)
    
    # Supondo que você tenha a solução ótima de cada instância
    sol_otima = 100  # Substitua pelo valor da solução ótima
    
    # Calcular resultados (10 execuções)
    resultados = calcular_resultados(fabrica, 'n10m2_A', sol_otima=sol_otima)
    
    # Exibir a tabela
    print(resultados)

    # Algoritmo Guloso
    custo_inicial = algoritmo_guloso(fabrica)
    print("Custo Inicial:", custo_inicial)
    
    # VND
    vnd(fabrica)
    print("Custo após VND:", fabrica.custo_tempo)

    # ILS
    ils(fabrica)
    print("Custo após ILS:", fabrica.custo_tempo)

if __name__ == "__main__":
    main()



