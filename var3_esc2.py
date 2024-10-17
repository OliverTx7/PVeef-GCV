# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

# Datos simulados: Calidad de materias primas (en %) y producción diaria
calidad_antes = np.random.normal(65, 10, size=30) # Calidad de materias primas antes de la
mejora
produccion_antes = np.random.normal(950, 50, size=30) # Producción antes de la mejora
calidad_despues = np.random.normal(90, 5, size=30) # Calidad de materias primas después
de la mejora
produccion_despues = np.random.normal(1300, 50, size=30) # Producción después de la
mejora
# Crear el Diagrama de Correlación
plt.figure(figsize=(10, 5))
# Correlación antes de la mejora
plt.subplot(1, 2, 1)
plt.scatter(calidad_antes, produccion_antes, color='blue')
plt.title('Diagrama de Correlación (Antes)')
plt.xlabel('Calidad de Materias Primas (%)')
plt.ylabel('Producción Diaria (Unidades)')
plt.grid(True)
# Correlación después de la mejora
plt.subplot(1, 2, 2)
plt.scatter(calidad_despues, produccion_despues, color='green')
plt.title('Diagrama de Correlación (Después)')
plt.xlabel('Calidad de Materias Primas (%)')
plt.ylabel('Producción Diaria (Unidades)')
plt.grid(True)
plt.tight_layout()
plt.show()