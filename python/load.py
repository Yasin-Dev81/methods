from numpy import *
from matplotlib.pyplot import *

#x=array([1,2,5,7])
#y=array([5,6,9,0])
#print(sum(x*y))
#print(inner(x,y))

data=loadtxt('signal.txt')          #imput kardan dadeh

x=data[:,0]
y=data[:,1]

plot(x,y)
show()