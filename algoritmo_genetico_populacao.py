GERACOES_MAX = 100000
ERRO_MIN = 0.1

class Populacao:
  def __init__(self, tamanho = 10):
    self.tamanho = tamanho
    self.populacao = []
    self.fitness = 0

  def fitness(self, individuo):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")

  def crossover(self):
    raise NotImplementedError("Implementar")

  def selecionar(self):
    nova_lista = sorted(self.populacao, key=self.fitness, reverse=True)
    self.populacao = nova_lista[0:10]

  def gerar_populacao(self):
    self.populacao = []

    for i in range(self.tamanho):
      self.populacao.append(Individuo())

  def top_fitness(self):
    return self.fitness(self.populacao[0])
  
  def top_individuo(self):
    return self.populacao[0]

class Individuo:
  pass

class AlgoritmoGeneticoPopulacao:
  def __init__(self, populacao, geracoes_max=GERACOES_MAX,
                          erro_min=ERRO_MIN):
    self.populacao = populacao
    self.geracoes_max = geracoes_max
    self.erro_min = erro_min
    self.erro = float('inf')
    self.geracoes = 1

  def erro_final(self):
    return self.erro

  def qtd_geracoes(self):
    return self.geracoes
    
  def rodar(self):
    ultimo_fitness = self.populacao.top_fitness() 

    while True:
      if self.geracoes <= self.geracoes_max and self.erro > self.erro_min:
        novo_individuo = self.individuo.mutacao()
        fitness = novo_individuo.fitness()
        if fitness < ultimo_fitness:
          self.erro = abs(fitness - ultimo_fitness)
          ultimo_fitness = fitness
          self.individuo = novo_individuo
        self.geracoes += 1
        if self.geracoes % 5000 == 0: print(f"Geração: {self.geracoes}, Erro: {self.erro}")
      else:
        break
    return self.individuo