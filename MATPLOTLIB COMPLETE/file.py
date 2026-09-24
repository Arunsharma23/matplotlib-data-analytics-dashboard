import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

# create plot

print(plt.plot(x,y , color = 'Green' , marker = 'o'))
print(plt.xlabel('x axs') , plt.ylabel('y axs') , plt.title('linechart'))

print(plt.savefig('linechart.png') , dpi = 300 , bbox_inches = 'tight')
print(plt.show())