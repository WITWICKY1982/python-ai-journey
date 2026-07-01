list_1 = [1,2,3,4,5]
list_1
list_1.append(10)
list_1
list_1.extend([10,11,12,13,14])
list_1.insert(2,10)
list_1.remove(10)
list_1.insert(1,2)
list_1.remove(2)

list_1.extend([8,6,7,9,11,10])
list_1.sort(reverse= True)
list_1
list_1.index(12)
list_1.count(11)
l1 = list_1.copy()
for i in l1:
    print(i)

for i in l1:
    print(i*2)

for i in l1:
    if i%2==0:
        print(i)
l3 = []
for i in l1:
    l3.append(i*2)
print(l3)

l2 = [1,2,3,4,5]
sum = 0
for i in l2:
    sum+=i
print(sum)


nl = [1,2,3,4,[5,6],7,8]
nl[4].append(99)
nl[4].insert(2,10)
nl

[i for i in l2]
[i*2  for i in l2 if i%2==0 ]

[i for i in l2 if i%2==0]

dicet = {
"dhruv":12,"pranav":11
}
dicet.pop("dhruv")
print(dicet)
dicet["dhruv"] = 500
print(dicet)
dicet.keys()
dicet.values()
dicet.items()
print(dicet.get("dhruv"))

for i in dicet:
    print(i)

for i in dicet.items():
    print(i)

for i in dicet.values():
    print(i)
for i in dicet.keys():
    print(i)

for key,value in dicet.items():
    print(key,"=",value)
dicet["dhruv"]