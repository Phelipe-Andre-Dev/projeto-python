import matplotlib.pyplot as plt;
carros = ['Onix', 'Strada', 'Gol', 'Tracker']
vendas = [9.5, 9.2, 9.1, 8.2]
plt.figure(figsize=(7,7))
plt.pie(x=vendas, labels=carros, autopct='%1.1f%%', startangle=90, 
shadow=True) 
plt.show()