class Fabrica:
    def __init__(self):
        self.num_linhas = 0            
        self.num_produtos = 0          
        self.tempos = []               
        self.preparos = []             
        self.custo_tempo = 0           
        self.linha_producao = []       

    def leitura_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                self.num_linhas = int(f.readline().strip())  
                self.num_produtos = int(f.readline().strip())  
                self.tempos = list(map(int, f.readline().strip().split()))  
                self.preparos = []
                for _ in range(self.num_produtos):
                    linha = f.readline().strip()
                    self.preparos.append(list(map(int, linha.split())))  
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False

    def imprimir_solucao(self):
        print(f"Custo total: {self.custo_tempo}")
        for i, linha in enumerate(self.linha_producao):
            print(f"Linha {i + 1}: {linha}")
