# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15HwLsqqn6dQnRFrpJMzv0JQIsc4HsSlY
"""

# Gráfico de Control para el Tiempo de Entrega
plt.figure(figsize=(12, 6))
mean = df['TiempoEntrega'].mean()
std_dev = df['TiempoEntrega'].std()
plt.plot(df['TiempoEntrega'].rolling(window=30).mean(), label='Media Móvil de Tiempo de
Entrega')
plt.axhline(mean, color='green', linestyle='--', label='Media')
plt.axhline(mean + 3*std_dev, color='red', linestyle='--', label='Límite Superior de Control')
plt.axhline(mean - 3*std_dev, color='blue', linestyle='--', label='Límite Inferior de Control')
plt.xlabel('Número de Registro')
plt.ylabel('Tiempo de Entrega (días)')
plt.title('Gráfico de Control: Tiempo de Entrega')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()