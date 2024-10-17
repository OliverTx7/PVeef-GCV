# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
# Datos iniciales del escenario
demanda = 1500 # demanda diaria de unidades
capacidad_antes = 1000 # capacidad diaria antes de la optimización
capacidad_despues = 1300 # capacidad diaria después de la optimización
# Simulamos los días de operación (30 días)
dias = 30
produccion_antes = np.random.normal(capacidad_antes, 50, dias) # producción diaria antes
(con desviación)
produccion_despues = np.random.normal(capacidad_despues, 50, dias) # producción diaria
después
# Definimos la función para crear el diagrama de control
def diagrama_control(produccion, capacidad, titulo):
 media = np.mean(produccion)
 std = np.std(produccion)
 lsc = media + 3 * std # Limite Superior de Control
 lic = media - 3 * std # Limite Inferior de Control
plt.figure(figsize=(10, 6))
 plt.plot(produccion, marker='o', linestyle='-', color='blue', label='Producción diaria')
 plt.axhline(media, color='green', linestyle='--', label='Media')
 plt.axhline(lsc, color='red', linestyle='--', label='LSC (3σ)')
 plt.axhline(lic, color='red', linestyle='--', label='LIC (3σ)')
 plt.axhline(capacidad, color='orange', linestyle='-', label='Capacidad de producción')
 plt.title(titulo)
 plt.xlabel('Día')
 plt.ylabel('Unidades producidas')
 plt.legend()
 plt.show()
# Simulación del escenario "Antes"
print("Simulación del escenario antes de la mejora")
diagrama_control(produccion_antes, capacidad_antes, 'Diagrama de Control - Antes de la
Mejora')
# Simulación del escenario "Después"
print("Simulación del escenario después de la mejora")
diagrama_control(produccion_despues, capacidad_despues, 'Diagrama de Control - Después
de la Mejora')