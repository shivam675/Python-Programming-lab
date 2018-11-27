x=int(input("enter eng  marks for A")) 
y=int(input("enter maths mrks for A")) 
z=int(input("enter sci mrks for A"))
k=int(input("enter eng marks for B"))
l=int(input("enter maths mrks for B"))
m=int(input("enter sci mrks for B"))
p=(x+y+z)/3
n=(k+l+m)/3
if p>n:
 print("A has scored highest avg mrks")
else:
 print("B has highest avg mrks")
