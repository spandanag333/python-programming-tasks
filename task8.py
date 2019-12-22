n = int(input("enter the number of elements: "))
list=[]
for i in range(0,n):
    list.append(int(input("enter %d element:" %(i+1))))
p=1
for j in range(0,n):
    p=p*list[j]
print(p)