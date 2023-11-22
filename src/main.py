import numpy as np
import matplotlib.pyplot as plt
import math


class JateamentoDeGranalhas:

    def __init__(self):

        self.calcula_curva()

    def calcula_zona_jateada(self, x, y, theta):
        '''
        Calcular a zona jateada em função do ângulo (theta)
        '''
        jateado = np.sin(theta) * np.cos(x)

        return jateado

    def calcula_curva(self):
        '''
        Printa e calcula a curva y = 10 * np.cos(x), no intervalo de 0 ≤ x ≤ pi
        '''
        x = np.linspace(0, np.pi, 1000)
        y = 10 * np.cos(x)

        plt.title('Processo de jateamento de granalhas')
        plt.plot(x, y, label='cos(x)')
        plt.legend()
        plt.show()


simulador = JateamentoDeGranalhas()
