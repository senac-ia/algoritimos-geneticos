import random
import math

senha_correta = ";/?h6fAdfd4,.fgSKYRfg6 5jY5W%@77f }gjnbn -49#$@#%%$&*&*"

# domínio
CARACTERES = "abcdefghijklmnopqrsuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !?@#$%ˆ&*()-=+[];:,.<>/?~\{\}\\|_"

# hiperparâmetro
tamanho_populacao = 100
tx_mutacao = 0.50
tx_crossover = 0.15
tx_tragedia = 0.05
geracoes_max = 100_000
geracoes_tragedia = 100

# utilidade
# se está aumentando, está melhorando o resultado
def fitness(senha):
  score = 0
  for i in range(len(senha_correta)):
    if senha_correta[i] == senha[i]: score += 1
  return score

def gerar_individuo():
  senha = ""
  for i in range(len(senha_correta)):
    senha += random.choice(CARACTERES)
  return senha

# retorna populuacao mutada com uma taxa
def mutacao(populacao):
  populacao_escolhida = random.choices(populacao, k=math.ceil(tx_mutacao*len(populacao)))
  return [mutacao_flip(individuo) for individuo in populacao_escolhida]

# flip de valor de gene de um gene aleatório
def mutacao_flip(individuo):
  novo_individuo = list(individuo)
  index = random.randint(0, len(individuo) - 1)
  novo_individuo[index] = random.choice(CARACTERES) # mutando gene
  return "".join(novo_individuo)

def crossover(populacao, geracao):
  funcao_decaimento_crossover = 1 #math.exp(-geracao/200)
  qtd = funcao_decaimento_crossover*tx_crossover*len(populacao)
  populacao_crossover = []
  populacao_escolhida = random.choices(populacao, k=math.ceil(qtd))
  [1, 2, 3, 4]
  for i in range(len(populacao_escolhida) - 1):
    for j in range(i+1, len(populacao_escolhida)):
      ind1 = populacao_escolhida[i]
      ind2 = populacao_escolhida[j]

      index = random.randint(0, len(senha_correta) - 1)
      populacao_crossover.append(ind1[0:index] + ind2[index:])
      populacao_crossover.append(ind2[0:index] + ind1[index:])

  return populacao_crossover

# escolhe os indivíduos mais aptos
def selecao_com_tragedia(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  if (geracao % geracoes_tragedia == 0):
    tamanho_tragedia = math.ceil(tamanho_populacao*tx_tragedia)
    novos_individuos = [gerar_individuo() for _ in range(0, tamanho_populacao - tamanho_tragedia)]
    return nova_populacao[0:tamanho_tragedia] + novos_individuos
  else:
    return nova_populacao[0:tamanho_populacao]

def selecao(populacao, geracao):
  nova_populacao = sorted(populacao, key=fitness, reverse=True)
  return nova_populacao[0:tamanho_populacao]

populacao = [gerar_individuo() for _ in range(0, tamanho_populacao)]
# ordernar lista
populacao = sorted(populacao, key=fitness, reverse=True)
geracao = 0

while fitness(populacao[0]) != len(senha_correta) and geracao < geracoes_max:
  geracao += 1
  populacao_mutada = mutacao(populacao)
  populacao_crossover = crossover(populacao, geracao)
  populacao = selecao(populacao_mutada + populacao + populacao_crossover, geracao)
  if geracao % 100 == 0 or (geracao % 10 == 0 and geracao < 100):
    print("---------------- Intermediário: " + str(geracao)+ " ----------------")
    print("Senha: " + populacao[0])
    print("Tx Acerto: " + str(fitness(populacao[0])))

print("---------------- Final " + str(geracao) + " ----------------")
print("Senha: " + populacao[0])
print("Tx Acerto: " + str(fitness(populacao[0])))