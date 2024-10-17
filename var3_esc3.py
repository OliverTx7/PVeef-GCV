# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

import matplotlib.pyplot as plt
import numpy as np
# Simulamos los datos para la capacidad de producción antes y después de la optimización del
inventario
dias = np.arange(1, 31) # 30 días de seguimiento
produccion_antes_tendencia = np.random.normal(1000, 50, size=30) # Producción antes de la
optimización
produccion_despues_tendencia = np.random.normal(1350, 50, size=30) # Producción después
de la optimización
# Crear el gráfico de tendencia
plt.figure(figsize=(10, 5))
# Tendencia antes de la optimización
plt.plot(dias, produccion_antes_tendencia, label='Antes del JIT', color='red', marker='o')
# Tendencia después de la optimización
plt.plot(dias, produccion_despues_tendencia, label='Después del JIT', color='green',
marker='o')
# Configuración del gráfico
plt.title('Análisis de Tendencias: Capacidad de Producción Antes y Después del JIT')
plt.xlabel('Días')
plt.ylabel('Producción Diaria (Unidades)')
plt.legend()
plt.grid(True)
plt.show()