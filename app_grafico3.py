import matplotlib.pyplot as plt;
x= [1,2,3,4,5,6,7,8,9,10,11,12]
y=[5.2, 6.5, 5.4, 5.5, 6.9, 3.9, 8.8, 9.8, 8.0, 7.7, 7.3, 9.5]
plt.plot(x, y, c='blue', ls='-.', lw='1', marker='o')
plt.ylabel('Vendas', fontsize=16)
plt.xlabel('Meses', fontsize=16)
plt.show()