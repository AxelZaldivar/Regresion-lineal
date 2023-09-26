import csv
import matplotlib.pyplot as plt

# Leer datos del archivo CSV y almacenarlos en listas
experiencia = []
salario = []

# Leer datos del archivo CSV y almacenarlos en listas usando list comprehensions
with open('Salary_dataset.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        experiencia.append(float(row[1]))
        salario.append(float(row[2]))

# Calcular los coeficientes de la regresión lineal
n = len(experiencia)
sum_x = sum(experiencia)
sum_y = sum(salario)
sum_x_squared = sum(x_i ** 2 for x_i in experiencia)
sum_xy = sum(experiencia[i] * salario[i] for i in range(n))

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = (sum_y - a * sum_x) / n

# Realizar predicciones
predicciones = [a * x + b for x in experiencia]

# Graficar los datos y la línea de regresión
plt.scatter(experiencia, salario, label='Datos reales', alpha=0.5)
plt.plot(experiencia, predicciones, color='red', linewidth=2, label='Línea de regresión')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
plt.legend()
plt.show()
