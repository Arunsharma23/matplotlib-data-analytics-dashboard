import matplotlib.pyplot as plt
product = [ 'A','B','C','D','E']
Sales = [ 100 , 400 , 300 , 800 , 500]

print(plt.bar(product , Sales , color = 'Blue', label= 'sales 2025'))
print(plt.xlabel('Products'),plt.ylabel('Sales'),plt.title('Sales of products in 2025'))
print(plt.legend())
print(plt.show())