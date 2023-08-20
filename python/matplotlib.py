from numpy import *
from matplotlib.pyplot import *

#rasm nemoodar
x=arange(0,2*pi,0.01)                   #asli..delta x
y=sin(x)

plot(x,y)                               #asli..plot kardan=rasm kardan
grid(ls='--',lw=0.5)                    #khat chin
xlabel('x',fontsize=12)
ylabel('y',fontsize=12)
title('y=sin(x)')
xlim(0,2*pi)
ylim(-1,1)
show()                                  #asli..namyesh