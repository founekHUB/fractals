"""Výpočet a vykreslení podivného atraktoru nazvaného Quadruptwo."""

# MIT License
#
# Copyright (c) 2020 Pavel Tišnovský
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Quadruptwo attractor

# import všech potřebných knihoven - Numpy, Matplotlibu a standardní
# matematické knihovny
import matplotlib.pyplot as plt
import numpy as np
from math import sin, atan
from numpy import log as ln
from numpy import abs, sign, arctan


def sqr(x):
    """Square of x."""
    return x*x


def quadruptwo(x, y, a, b, c):
    """Funkce pro výpočet dalšího bodu podivného atraktoru Quadruptwo."""
    x_dot = y - sign(x)*sin(ln(abs(b*x-c)))*atan(sqr(ln(abs(c*x-b))))
    y_dot = a - x
    return x_dot, y_dot


# celkový počet vypočtených bodů na atraktoru
n = 400000

# počet bodů ze začátku výpočtu, které se nevykreslí
settle_down_points = 1

# prozatím prázdné pole připravené pro výpočet
x = np.zeros((n,))
y = np.zeros((n,))

# počáteční hodnoty pro výpočet
x[0], y[0] = (0.0, 0.0)

# parametry ovlivňující výpočet podivného atraktoru
A = 3.1
B = 1.8
C = -0.9

# vlastní výpočet atraktoru
for i in range(n-1):
    x_dot, y_dot = quadruptwo(x[i], y[i], A, B, C)
    x[i+1] = x_dot
    y[i+1] = y_dot

# vykreslení grafu
plt.plot(x[settle_down_points:], y[settle_down_points:], 'o', markersize=0.05)

# změna velikosti komponent v grafu
plt.tight_layout()

# uložení grafu pro jeho další zpracování
plt.savefig("quadruptwo.png")

# zobrazení grafu
plt.show()