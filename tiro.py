import math
import random
from geneticos.individuo import Individuo

class Tiro(Individuo):
  GRAVIDADE = 9.80665  # m/sˆ2
  THETA_MAX = math.pi / 2  # em radianos
  THETA_MIN = 0
  VELOCIDADE_MAX = 1000  # em m/s
  VELOCIDADE_MIN = 1  # em m/s
  VARIACAO_THETA = 0.0174533  # 1 grau
  VARIACAO_VELOCIDADE = 10  # 10 msg/s
  X_ALVO = 10000  # distância do alvo em metros

  def __init__(self,
                theta=random.uniform(THETA_MIN, THETA_MAX),
                velocidade=random.uniform(VELOCIDADE_MIN, VELOCIDADE_MAX)):
    self.theta = theta  # em radianos
    self.velocidade = velocidade  #

  def fitness(self):
    x_tiro = self._alcance()
    return abs(self.X_ALVO - x_tiro)

  # atualiza os dados do individuo atual
  # dica a variacao pode ser em quantidades
  # positivas ou negativas de Theta ou velocidade
  # usando VARIACAO_THETA e VARIACAO_VELOCIDADE
  # algo com random.uniform(min, max)
  def mutacao(self):
    theta = -1
    velocidade = -1
    while theta < self.THETA_MIN or theta > self.THETA_MAX:
      theta = self.theta + random.uniform(-10 * self.VARIACAO_THETA,
                                          10 * self.VARIACAO_THETA)
    while velocidade < self.VELOCIDADE_MIN or velocidade > self.VELOCIDADE_MAX:
      velocidade = self.velocidade + random.uniform(-2 * self.VARIACAO_VELOCIDADE,
                                                    2 * self.VARIACAO_VELOCIDADE)

    return Tiro(theta, velocidade)

  def _alcance(self):
    return (self.velocidade * self.velocidade *
            math.sin(2 * self.theta)) / self.GRAVIDADE

  def imprime(self):
    return "Theta: " + str(self.theta) + "\nVelocidade: " + str(
        self.velocidade) + "\nFitness: " + str(self.fitness())
