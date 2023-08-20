
a, b, c = input().split(' ')
a, b, c = float(a), int(b), int(c)


print ('a is %.4f'% a)
print (f"{a} is a")
print (f'b is {b}')
print ("c is %s"%c)
print ("c is {}".format(c))
print ("b, c is {}, {}".format(b, c))
print ("b, b is {0}, {0}".format(b, c))
print ("b, c is {B}, {C}".format(B=b, C=c))
print ("my score is {score:1.3f}".format(score=a))
print ("my score is {score:10.3f}".format(score=a)) # 10 fazaye ekhtesas dade shode ast
print (f"a is {a}")


x = [1, 2, 10, 3, 4]
x.sort()
print (x)
x.reverse() # = x[::-1]
print (x)
