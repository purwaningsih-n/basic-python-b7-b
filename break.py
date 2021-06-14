#output: 0 1 2 3
a = range(7)
for i in a:
    if i==4:
        break
    print(i)  

print()

#output: 3 4 5 6
i=2
while i<=10:
    i+=1
    if i == 7:
        break
    print(i) 

print()

#output: 1 2 3 4
i=1
while i<10:
    if i == 5:
        break
    print(i)
    i+=1 