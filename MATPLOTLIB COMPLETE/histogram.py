import matplotlib.pyplot as plt
scores = [45,85, 75, 90, 60, 80, 70, 90, 100, ]
print(plt.hist(scores , bins=5, color = 'orange', edgecolor = 'black'))
print(plt.xlabel('scores'), plt.ylabel('Number of Students'), plt.title('Histogram of scores'))
print(plt.show())