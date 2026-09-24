import matplotlib.pyplot as plt
# hours = [1,2,3,4,5,6,7,8,]
# exam = [30,40,50,60,70,80,90,100]

# print(plt.scatter(hours , exam , color = 'green' , marker = 'o' , label = 'exam 2025'))
print(plt.scatter([1,2,3,4] , [30,40,50,60] , color = 'green' ,  label = 'Class A'))
print(plt.scatter([1,2,3,4] , [40,50,60,70] , color = 'blue' ,  label = 'Class B'))
print(plt.xlabel('Hour') , plt.ylabel('Exam score') , plt.title('Exam score'))
print(plt.legend())
print(plt.grid(color = 'Red' , linestyle = ':' , linewidth = 1))
print(plt.show())