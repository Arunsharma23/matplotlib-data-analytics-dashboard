import matplotlib.pyplot as plt
fig, ax= plt.subplots(1,2, figsize=(10,5))
x = [1,2,3,4,5]
y = [10,20,30,40,50]

print(ax[0].plot(x,y))
print(ax[0].set_title('Line chart'))

print(ax[1].bar(x,y))
print(ax[1].set_title('Bar chart'))

print(plt.suptitle('Line and Bar chart'))
print(plt.tight_layout())
print(plt.show())