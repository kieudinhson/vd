from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
divisions = ['Div-A','Div-B','Div-C','Div-D','Div-E']
divisions_average_marks = [70,82,73,65,68]
#variance = [50,8,7,6,4]
boys_average_marks = [68,67,72,61,46]

index = np.arange(5)
width = 0.3

plt.bar(index,divisions_average_marks, width ,color='red')#plt.barh bieeu do ngang     xerr ngang(yerr =variance)
plt.bar(index+width,boys_average_marks, width,color='blue')#yerr =variance 
plt.title("Bieu do 2 cot ")
plt.ylabel("Divisions")
plt.xlabel("Marks")
plt.xticks(index+width/2,divisions)
plt.legend(loc='best')
plt.show()