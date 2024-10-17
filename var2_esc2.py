# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

# Datos de simulación para antes de la automatización
personal_antes = [5] * 30
produccion_antes = np.random.normal(1000, 50, size=30) # Producción diaria antes de la
automatización
# Datos de simulación para después de la automatización
personal_despues = [5] * 30
produccion_despues = np.random.normal(1400, 50, size=30) # Producción diaria después de
la automatización
# Crear el Diagrama de Dispersión
plt.figure(figsize=(8, 6))
plt.scatter(personal_antes, produccion_antes, color='red', label='Antes')
plt.scatter(personal_despues, produccion_despues, color='green', label='Después')
plt.title('Diagrama de Dispersión: Personal vs Producción')
plt.xlabel('Cantidad de Personal')
plt.ylabel('Producción Diaria (Unidades)')
plt.legend()
plt.grid(True)
plt.show()