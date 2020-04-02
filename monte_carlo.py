# DICA: a função uniform(a, b) do módulo random,
# gera um número aleatório no intervalo [a, b].

import geometria
import math
import time
import os

from flask import Flask, jsonify, request
from math import sqrt
from random import uniform

app = Flask(__name__)

@app.route('/')

def funcao():
      n = 1000000

      circulo1 = geometria.Circulo(1, (0, 0))
      circulo1.imprime_dados()
      quadradoArea = circulo1.quadrado_area()
      qnt = 0
      total = n

      tempo = (n/10000)*0.05812
      #print("Seu teste vai demorar", tempo, "de segundos, quer continuar? 1 SIM: ", end = '')
      inicio = time.perf_counter()
      for x in range(n):
            total -=1
            if circulo1.dentro((uniform(-1 * circulo1.raio, circulo1.raio),
                              uniform(-1 * circulo1.raio, circulo1.raio))) is True:
                  qnt += 1


            retorno = "Estimado: " + str(tempo) + " segundos \n"
            retorno += "Dentro:" + str(qnt) + "Fora:" + str(n - qnt) + "\n"
            retorno += "Probalidade de cair dentro do circulo:" + str(round((qnt/n * quadradoArea) /quadradoArea, 5)) + "\n"
            retorno += "Estimativa do PI:" + str((qnt/n) * quadradoArea)
            retrono += "Tempo que levou para calcular:" + str(round(time.perf_counter() - inicio, 5))
            return retorno
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+---#
