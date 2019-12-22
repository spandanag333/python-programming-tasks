n = int(input("enter the number of elements: "))
list=[]
for i in range(0,n):
    list.append(int(input("enter %d element:" %(i+1))))
even=odd=0
for j in range(0,n):
    if list[j]%2==0:
        even+=1
    elif list[j]!=0:
        odd+=1
print("number of even numbers in the list are %d" %(even))
print("number of odd numbers in the list are %d" %(odd))