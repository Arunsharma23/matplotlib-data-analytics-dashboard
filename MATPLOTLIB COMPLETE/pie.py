import matplotlib.pyplot as plt
Regions = ['North', 'South', 'East', 'West']
rvenue = [20000, 15000, 30000, 25000]
print(plt.pie(rvenue , labels = Regions , autopct = '%1.1f%%' , colors = [ 'Gold', 'Yellow', 'Orange', 'Red'] , shadow = True))
print(plt.title('Revenue by Region'))
print(plt.show())
