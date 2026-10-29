import numpy as np 
import matplotlib.pyplot as plt

diasX = ["lun", "mar", "mie", "jue", "vie"]
califa_va_y = [6, 9, 8, 5, 10]

plt.bar(diasX, califa_va_y)
plt.title("califas en VA de valeria yaretzi NC 1341")
plt.xlabel("dias semana habil")
plt.ylabel("calificaciones en VA")
plt.grid(True)

# Guardar la gráfica como archivo de imagen antes de mostrarla
plt.savefig("image.png", bbox_inches='tight')

plt.show()