## @Sitabja Pal, 21/9/2018, Simple Linear Regression by Gradient Descent Algorithm ##
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
df=pd.read_csv('Lregressiondata.txt')
df.head()
x_points=df['no']
y_points=df['\tlabel']
m = 0
b = 0
y = lambda x : m*x + b
learn = .003
def summation(y, x_points, y_points):
    total1 = 0
    total2 = 0
    
    for i in range(1, len(x_points)):
        total1 += y(x_points[i]) - y_points[i]
        total2 += (y(x_points[i]) - y_points[i]) * x_points[i]
        
    return total1 / len(x_points), total2 / len(x_points)
for i in range(1000):
    s1, s2 = summation(y, x_points, y_points)
    m = m - learn * s2
    b = b - learn * s1
#plot_line(y, x_points)
print(m,b,sep='\n')
plt.plot(x_points, y_points, 'bo')
y_data=[y(i) for i in x_points]
plt.plot(x_points, y_data, 'r--')
plt.show()