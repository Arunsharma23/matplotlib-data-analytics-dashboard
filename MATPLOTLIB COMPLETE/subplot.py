import matplotlib.pyplot as plt
hours = [1,2,3,4,5,6,7,8,]
exam = [30,40,50,60,70,80,90,100]
print(plt.subplot(2,1,1))
print(plt.plot( hours , exam ))
print(plt.title('line chart'))

print(plt.subplot(2,1,2))
print(plt.bar(hours , exam))
print(plt.title('bar chart'))

# print(plt.tight_layout())
print(plt.show())

