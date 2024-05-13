import numpy as np
import random
import matplotlib.pyplot as plt


x1=np.arange(0, 50, 1)
y1=x1*2

pontos_x = [random.randint(0,100)]
pontos_y = [random.randint(0, 100)]

plt.plot(x1,y1,color="red")

plt.scatter(pontos_x, pontos_y, color="blue", label="Pontos extras")

plt.title("Perceptron")
plt.show()