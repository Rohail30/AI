x=3
y=2.5
z="Wali"
print("Value of x is ",x)
print("Value of x is ",y)
print("Value of x is ",z)

print("the type of x is ",type(x))
print("the type of x is ",type(y))
print("the type of x is ",type(z))

print("please enter your name")
name=input()
print("Your name is ", name)

print("Please enter youtr age ")
age = input()
a=int(age)
print(type(age))
print(type(a))

val1 = int(input("Enter Value: "))
val2 = int(input("Enter another Value: "))
print("the sum of entered values is ",(val1+val2))
print("the product of entered values is ",(val1*val2))
print("the difference of entered values is ",(val1*val2))

#Slicing
name=input("Enter Name: ")
n=name[0:3]
m=name[0:]
o=name[:4]
p=name[:]
print(m)
print(n)
print(o)
print(p)

"""
Array: list of homogenous data
list: can have multiple data types square bracket[]
tuple: can have multiple data types round bracket()
"""
#List
listt =[2,4,"Wali",3.5,6.5,"Muhammad"]
for i in listt:
    print(i)
print(" ")
print(len(listt))
print(" ")
sublist=listt[2:5]
for i in sublist:
    print(i)
print(" ")   
sublist=listt[:5]
for i in sublist:
    print(i)
print(" ")    
sublist=listt[2:]
for i in sublist:
    print(i)    
print(" ")
sublist=listt[:]
for i in sublist:
    print(i)    


#tuple
tup =(2,4,"Wali",3.5,6.5,"Muhammad")
for i in tup:
    print(i)
print(" ")
print(len(tup))
print(" ")
sublist=tup[2:5]
for i in sublist:
    print(i)
print(" ")   
sublist=tup[:5]
for i in sublist:
    print(i)
print(" ")    
sublist=tup[2:]
for i in sublist:
    print(i)    
print(" ")
sublist=tup[:]
for i in sublist:
    print(i)    
    
