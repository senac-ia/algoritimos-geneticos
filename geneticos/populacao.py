class Populacao:
  def __init__(self, Individuo, tamanho=10):
    self.populacao = [Individuo()]*tamanho
    self.fitness = 0

  def fitness_populacao(self, individuo):
    return individuo.fitness()

  def mutacao(self):
    nova_lista = []
    for individuo in self.populacao:
      nova_lista.append(individuo.mutacao())
    return nova_lista

  def crossover(self):
    raise NotImplementedError("Implementar")

  def selecionar(self, populacao1, populacao2):
    self.populacao = self.populacao + populacao1 + populacao2
    nova_lista = sorted(self.populacao, key=self.fitness_populacao, reverse=True)
    self.populacao = nova_lista[0:10]

  def top_fitness(self):
    return self.top_individuo().fitness()
  
  def top_individuo(self):
    return self.populacao[0]

class Individuo:
  pass