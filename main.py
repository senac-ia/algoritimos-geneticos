from tiro import Tiro
from pop_tiros import PopTiros
#from geneticos.algoritmo_genetico_individuo import AlgoritmoGeneticoIndividuo
from geneticos.algoritmo_genetico_populacao import AlgoritmoGeneticoPopulacao

# individuo = Tiro()
# genetico = AlgoritmoGeneticoIndividuo(individuo)

# print("Primeiro indivíduo:")
# print(individuo.imprime())
# print("\n")

# individuo_adaptado = genetico.rodar()

# print("\nPrimeiro mais adaptado:")
# print(f"Quantidade de gerações: {genetico.qtd_geracoes()}")
# print(f"Erro: {genetico.erro_final()}")
# print(individuo_adaptado.imprime())

populacao = PopTiros(Tiro, 10)
genetico = AlgoritmoGeneticoPopulacao(populacao)

individuo_adaptado = genetico.rodar()

print("\nPrimeiro mais adaptado:")
print(f"Quantidade de gerações: {genetico.qtd_geracoes()}")
print(f"Erro: {genetico.erro_final()}")
print(individuo_adaptado.imprime())
