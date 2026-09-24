import matplotlib.pyplot as plt
x = ['monday' , 'tuesday', 'wednesday', 'thursday', 'friday']
y = [10 ,20 ,50,60,40]

print(plt.plot( x , y, color = 'green', marker = 'o', linestyle = '--', linewidth = 2))
print(plt.title(' Days of the week'))
print(plt.xlabel('Days'),plt.ylabel('Num of sale'))

print(plt.legend(loc = 'upper left' , fontsize=12))
print(plt.grid(color = 'Red' ,linestyle = ':', linewidth = 1))
print(plt.xlim(1 , 5) , plt.ylim(30, 70))
print(plt.xticks([1,2,3,4,5], ['monday' , 'tuesday', 'wednesday', 'thursday', 'friday']))
print(plt.yticks([30,40,50,60,70], ['30' , '40', '50', '60', '70']))
print(plt.show())

