import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from math import radians


class JateamentoDeGranalhas:

    def __init__(self):
        self.xb = 1.5
        self.yb = 5.0
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)

        self._adiciona_sliders()
        self._adiciona_reset_button()
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

        ax_slider_y = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor=axcolor)
        self.slider_y = Slider(ax_slider_y, 'yb', -10.0, 10.0, valinit=self.yb)
        self.slider_y.on_changed(self._slider_y_changed)

        ax_slider_theta = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor=axcolor)
        self.slider_theta = Slider(ax_slider_theta, 'Angulo Theta', 0, 360, valinit=0)
        self.slider_theta.on_changed(self.update)

    def _adiciona_reset_button(self):
        """Adiciona um butão para resetar os sliders"""
        ax_reset = plt.axes([0.83, 0.025, 0.1, 0.04])
        self.reset_button = Button(ax_reset, 'Resetar', hovercolor='0.975')
        self.reset_button.on_clicked(self._reset_sliders)

    def _slider_x_changed(self, val):
        """Handler para alterações no slider de xb"""
        self.xb = val
        self.update(0)

    def _slider_y_changed(self, val):
        """Handler para alterações no slider de yb"""
        self.yb = val
        self.update(0)

    def _reset_sliders(self, event):
        """Dá o reset nos controles do slides para os valores iniciais """
        self.slider_x.reset()
        self.slider_y.reset()
        self.slider_theta.reset()


if __name__ == "__main__":
    simulador = JateamentoDeGranalhas()
    plt.show()
