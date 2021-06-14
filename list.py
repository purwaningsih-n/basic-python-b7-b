mylist = []
mylist.append("a")
mylist.append(12)
mylist.append(20)
print(mylist)
print(len(mylist))
del mylist[2]
print(mylist)

# [a, 12, 20]
# [0  1    2]

mylist[1]=30 #mengedit isi list
print(mylist)

a = int(input("Masukkan data ke dalam mylist : "))
mylist.append(a)
print(mylist)
print(len(mylist))