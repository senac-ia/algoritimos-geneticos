from tiro import Tiro
from algoritmo_genetico import AlgoritmoGeneticoSimples

individuo = Tiro()
genetico = AlgoritmoGeneticoSimples(individuo)

print("Primeiro indivíduo:")
print(individuo.imprime())
print("\n")

individuo_adaptado = genetico.rodar()

print("\nPrimeiro mais adaptado:")
print(f"Quantidade de gerações: {genetico.qtd_geracoes()}")
print(f"Erro: {genetico.erro_final()}")
print(individuo_adaptado.imprime())