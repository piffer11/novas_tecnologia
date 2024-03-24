import math

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

x1, y1 = map(float, input("Digite as coordenadas do primeiro ponto (x1 y1): ").split())
x2, y2 = map(float, input("Digite as coordenadas do segundo ponto (x2 y2): ").split())

distancia = calcular_distancia(x1, y1, x2, y2)

print("A distância entre os pontos é: {:.4f}".format(distancia))
