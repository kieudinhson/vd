import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import title
phan = ['1','2','3','4','5']
tile = [20,25,5,20,10]
explode = [0,0,0.1,0,0]
plt.pie(tile,explode=explode,labels=phan,shadow=True,startangle=45)
plt.axis('Equal')
plt.legend(title='List of Firms')
plt.show()