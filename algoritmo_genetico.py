GERACOES_MAX = 100000
ERRO_MIN = 0.1

class Individuo:
  def fitness(self):
    raise NotImplementedError("Implementar")

  def mutacao(self):
    raise NotImplementedError("Implementar")

  def crossover(self):
    raise NotImplementedError("Implementar")

class AlgoritmoGeneticoSimples:
  def __init__(self, individuo, geracoes_max=GERACOES_MAX,
                          erro_min=ERRO_MIN):
    self.individuo = individuo
    self.geracoes_max = geracoes_max
    self.erro_min = erro_min
    self.erro = float('inf')
    self.geracoes = 1

  def erro_final(self):
    return self.erro

  def qtd_geracoes(self):
    return self.geracoes
    
  def rodar(self):
    ultimo_fitness = self.individuo.fitness() 

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

