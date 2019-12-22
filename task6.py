A = int(input("enter the length of the first side of the triangle :"))
B = int(input("enter the length of the second side of the triangle :"))
C = int(input("enter the length of the third side of the triangle :"))
if A==B and B==C and C==A:
    print("EQUILATERAL TRIANGLE")
elif A!=B and B!=C and C!=A:
    print("SCALENE TRIANGLE")
elif A==B or B==C or C==A:
    print("ISOSCELES TRIANGLE")
else:
    print("INVALID TRIANGLE")