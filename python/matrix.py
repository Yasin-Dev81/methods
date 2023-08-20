from numpy import *

x=array([[1,2,0],[4,5,11]])          #matrix
y=array([[0,5,6],[7,9,6]])

print(x)
print(x.dtype)          #type deraye
print(type(x))
print(x.shape)          #satr & sotoon
print(x.ndim)           #? abaad
print(x.size)           #tedad deraye
print(transpose(x))     #jabejayi satr & sotoon
print(transpose(x).dot(y))         #x*y

print('z=',x*y)
