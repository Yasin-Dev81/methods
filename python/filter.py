# exampel 1
def is_more_than_15(score) :
    return (15 <= score) 

scores = [1, 5, 12, 16, 20]
print ("exampel 1:", list(filter(is_more_than_15, scores)))

print ("-"*10)
# exampel 2
def somthing(name:str) :
    return (name.isalpha())

names = ["ali", "yasin", "emran", "ahmad", "mahdi"]

print ("exampel 2:" , list(filter(somthing, names)))

print ("-"*10)
# exampel with lambda
scores = [1, 5, 12, 16, 20]
print ("exampel with lambda:", list(filter(lambda score: 15 <= score, scores)))
