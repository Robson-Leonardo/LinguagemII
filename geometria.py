import math


class Circulo:
    def __init__(self, raio, centro):
        # Instanciar as duas variáveis (raio e centro)
        self.raio = raio
        self.centro = centro

    def imprime_dados(self):
        # Método que imprime os dados do círculo, raio e centro
        print("Raio:", self.raio)
        print("Posição do centro:", self.centro)

    def area(self):
        # Método que devolve a área do circulo
        return round(math.pi * self.raio ** 2, 4)

    def perimetro(self):
        # Método que devolve o perímetro do circulo
        return round((2 * math.pi) * self.raio, 4)

    def dentro(self, ponto):
        # Método que recebe um ponto (tupla) e devolve:
        # True, se o ponto está dentro do círculo e
        # False, caso contrário
        dist = distancia(self.centro, ponto)
        #print(ponto)
        if dist <= self.raio:
            return True
        else:
            return False

    def quadrado_area(self):
        return (self.raio * 2) ** 2


def distancia(a, b):
    # Função que recebe dois pontos (tuplas), 'a' e 'b',
    # calcula e devolve a distância entre eles.
    aX = a[0]
    aY = a[1]
    bX = b[0]
    bY = b[1]
    return math.sqrt((bX - aX) ** 2 + (bY - aY) ** 2)

#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+---#
