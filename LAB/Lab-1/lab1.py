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


#Class Task
#Write a program that takes input from the user and print it's table using list.

"""
num = int(input("Enter a number: "))
l= []
for i in range(11):
    l[i] = num * i 
    print(num*i)
    
print(l)
    
"""

n = int(input("Enter a number: "))
if(n%3==0):
    print("fizz")
elif(n%5==0):
    print("Buzz")
else:
    print("Nothing")

#Class Task
#Write a program that takes input from the user and print it's table using list.Should only be even

"""
Dictionary
Key Value Pair: 
person ={"Name":"Wali, "Geder":Male, "Age":"26"}
person is dictionary
person.values() are values--> "Wali", "Male"
Person.keys --> "Name", "Gender"
"""

person ={"Name":"Wali", "Gender":"Male", "Age":"26"}
print(person.keys())
print(person.values())
print("Person's name is", person["Name"])

#Task2 : Write a program that defines a person dictionary with the following keys 
#Name
#Age
#Gender
#Program
#University
#All the values should be assigned by user input


n = input("Enter name: ")
a = int(input("Enter age: "))
g = input("Enter Gender: ")
p = input("Enter Pogram: ")
u = input("Enter University: ")

d = {}

d["Name"] = n
d["age"] = a
d["Gender"] = g
d["Pogram"] = p
d["University"] = u

print(d)
