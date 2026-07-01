from functools import reduce

a = [10,11,12,13,14,15]
double = map(lambda x:x*2,a)
print(list(double))

even = filter(lambda x:x%2==0,a)
print(list(even))

summ = reduce(lambda a,b:a+b,a)
print(summ)