
# exampel 1
def power_two(num) :
    return num**2

my_numbers = [1, 2, 3, 4, 5, 6] # list of numbers
Map = map(power_two, my_numbers) # map
print ("exampel 1:", list(Map)) # list of map

print ("-"*10)
# exampel 2
def somthing(num1, num2) :
    return num1*num2

x = [1, 2, 3]
y = [4, 5, 6]
print ("exampel 2:", list(map(somthing, x, y)))

print ("-"*10)
# exampel 3
def somthing2(name, score) :
    return {"name": name, "score": score}

names = ["ali", "yasin", "emran", "ahmad", "mahdi"]
scores = [1, 5, 12, 16, 20]

print ("exampel 3:", list(map(somthing2, names, scores)))

print ("-"*10)
#exampel with lambda
names = ["ali", "yasin", "emran", "ahmad", "mahdi"]
scores = [1, 5, 12, 16, 20]

print ("exampel with lambda:", list(map(lambda name, score: {"name": name, "score": score}, names, scores)))
