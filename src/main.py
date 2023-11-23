import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from math import radians


class JateamentoDeGranalhas:

    def __init__(self):
        self.xb = 1.5
        self.yb = 5.0
        self.fig, self.ax = plt.subplot()
        plt.subplots_adjust(bottom=0.35)

        self._adiciona_sliders()
        self._add_reset_button()
        self.update(0)

    def calcula_zona_jateada(self, x, y, theta):
        """Calcular a zona jateada em função do ângulo (theta)"""
        jateado = self.yb + np.sin(theta) * (x - self.xb)
        return jateado

    def update(self, val):
        """Atualiza o gráfico com base nos valores dos sliders"""
        self.ax.clear()

        x = np.linspace(0, np.pi, 1000)
        y = 10 * np.cos(x)
        theta = radians(self.slider_theta.val)
        jateado = self.calcula_zona_jateada(x, y, theta)

        self.ax.plot(x, y, label='Curva')
        self.ax.plot(x, jateado, label='Zona Jateada', linestyle='--')
        self.ax.plot(round(self.xb, 2), round(self.yb, 2), 'ro', label='Ponto b')

        self.ax.legend()
        plt.draw()

    def _adiciona_sliders(self):
        """Adiciona sliders para interação com o usuário"""
        axcolor = 'lightgoldenrodyellow'

        ax_slider_x = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor=axcolor)
        self.slider_x = Slider(ax_slider_x, 'xb', 0.1, 10.0, valinit=self.xb)
        self.slider_x.on_changed(self._slider_x_changed)

        ax_slider_y = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor=axcolor)
        self.slider_y = Slider(ax_slider_y, 'yb', 0.1, 10.0, valinit=self.yb)
        self.slider_y.on_changed(self._slider_y_changed)

        ax_slider_theta = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor=axcolor)
        self.slider_theta = Slider(ax_slider_theta, 'Angulo Theta', 0, 360, valinit=0)
        self.slider_theta.on_changed(self.update)


simulador = JateamentoDeGranalhas()
