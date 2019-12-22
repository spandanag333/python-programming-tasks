lists = []
for i in range(0,3):
    lists.append(int(input("enter the %d element:" %(i+1))))
lists.sort()
print(lists)
print("MEDIAN is %d" %(lists[1]))
