print("hello world")
#seperator
print("hello", "world", sep="***")
#restricted string
print(r"hello\nworld")
#path read using double backslash
print("c:\\newfolder\\test.txt")
#using r
# print("C:\Users\ASUS\OneDrive\Desktop\PyConf\django_socet")
#type casting
a=10
x=float(a)
print(x)
print(type(x))

list = [1,2,3,4,5,True]
list[-1]=False
print(list)


angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
if angle1 == angle2 == angle3:
    print("Equilateral Triangle")
elif angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
    print("Isosceles Triangle")
else:   
    print("Scalene Triangle")

# for loop z
for row in range(5):
    line = ""
    for col in range(5):
        if row == 0 or row+col==4 or row==4:
            line += "*"
        else:
            line += " "
    print(line)
# for loop a
for row in range(5):
    line = ""
    for col in range(5):
        if (row == 0) or (col==0)or( col==4)or(row==2):
            line += "*"
        else:
            line += " "
    print(line)

# for loop print G
# for row in range(5):
#     line = ""
#     for col in range(5):
#         if (row == 0  and col<4) or (col == 4 and row>1) or (col==2 and row>1) or (row==4 and col<3)or(row>0 and col==0):
#             line += "*"
#         else:
#             line += " "


a= int(input("Enter the number: "))
for i in range(1,11):
    print(a,"x",i,"=",a*i)
