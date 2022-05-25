
x = [0,1,2,2,3,0,4,2]
num = 2
x = list(y for y in x if y != num)
# x = list(filter(lambda y: (y!=num), x))
print(x)