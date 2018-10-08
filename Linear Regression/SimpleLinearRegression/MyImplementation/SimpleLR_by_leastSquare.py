## @Sitabja Pal, 20/9/2018, Simple Linear Regression by Least Square Method ##
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def minSquare(x,y,x_mean,y_mean,n):
    num,denom=0,0
    for i in range(n):
        num+=(x[i]-x_mean)*(y[i]-y_mean)
        denom+=(x[i]-x_mean)**2
    m=num/denom
    c=y_mean-(m*x_mean)
    return m,c


def RSquareValue(y1,y,n):
    num,denom=0,0
    for i in range(n):
        num+=(y1[i]-y_mean)**2
        denom+=(y[i]-y_mean)**2
    r=num/denom
    return r


df=pd.read_csv('Lregressiondata.txt')
df.head()
#print(df.describe())
x=df['no']
#print(x)
y=df['\tlabel']
#print(y)
x_mean,y_mean=x.mean(),y.mean()
m,c=minSquare(x,y,x_mean,y_mean,len(x))
y1=[]
for i in range(len(x)):
    y1.append(m*x[i]+c)
r=RSquareValue(y1,y,len(y1))
print("R square value or accuracy is: "+str(r)+"   or  "+str(r*100)+" %")
plt.scatter(x,y)
plt.plot(x,y1,'r--')
plt.show()