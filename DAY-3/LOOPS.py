s = "HELLO WORLD"
for i in s:
    print(i)

i = 0
while i <len(s):
    print(s[i])
    i+=1

for i in range(0,10):
    if i%2==1:
        print(i)
    
for i in range(0,10):
    if i%2!=1:
        print(i)


i = 0
while i<10:
    if i%2!=1:
        print(i)
    i+=1

 
while i < len(s):
    if i == "o":
        i+=1
        break
    print(i)
    i+=1

for i in range(1,10):
    if i == 5:
        break
        print(i)
