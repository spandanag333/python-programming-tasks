def longstr():
    lists=[]
    n=int(input("enter the no of fruits:"))
    for i in range(0,n):
        lists.append(input("enter %d fruit: " %(i+1)))
    print(max(lists,key=len))
longstr()