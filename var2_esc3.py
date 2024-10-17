# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

# Simulación de datos de la producción diaria a lo largo del tiempo (antes y después de la
capacitación)
dias = np.arange(1, 31) # 30 días de seguimiento
produccion_antes = np.random.normal(1000, 50, size=30) # Producción antes de la
capacitación
produccion_despues = np.random.normal(1250, 50, size=30) # Producción después de la
capacitación
# Crear el Diagrama de Tendencias
plt.figure(figsize=(8, 6))
plt.plot(dias, produccion_antes, label='Antes', color='blue', marker='o')
plt.plot(dias, produccion_despues, label='Después', color='green', marker='o')
plt.title('Diagrama de Tendencias: Producción Diaria')
plt.xlabel('Días')
plt.ylabel('Producción Diaria (Unidades)')
plt.legend()
plt.grid(True)
plt.show()