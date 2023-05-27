import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np 
categorias = ('Hatch Compacto', 'Sedan', 'Suv')
indice = np.arange(len(categorias))
vendas = [11.9, 8.9, 8.4] 
plt.bar(indice, vendas, color='blue')
plt.bar(indice, vendas)
plt.xticks(indice, categorias)
plt.ylabel('Vendas em milhares')
plt.title('As três categorias mais vendidas')
plt.show()

