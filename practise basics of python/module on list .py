#Fstring Method in Python
from ctypes.macholib.framework import framework_info

num1=90
num2=50
print(f"John scored {num1} in Physics and {num2} in Maths")
#Practice List operations
days_of_weeks=["mon","tue","wed","thur","fri","sat","sun"]
print(len(days_of_weeks))
print(days_of_weeks[6])
#append in listing
days_of_weeks=["mon","tue","wed","thur","fri","sat","sun"]
days_of_weeks.append("bullshit day")
print(days_of_weeks)
#remove function
days_of_weeks.remove("bullshit day")
print(days_of_weeks)
#insert function for list
days_of_weeks=["mon","tue","wed","thur","fri","sat","sun"]
days_of_weeks.insert(7,"none")
print(days_of_weeks)
#extend function in listing
fruits=["orange","apple","banana"]
fruits.extend(["grapes","watermelon"])
print(fruits)
#pop function
fruits=["orange","apple","banana"]
fruits.pop(0)
print(fruits)

#more operations on listing
#Reverse
num1=[1,2,3,4,5,6]
num1.reverse()
print(num1)
#sort
num1=[1,2,3,4,5,6]
num1.sort()
print(num1)
#reverse
num1=[1,2,3,4,5,6]
num1.sort(reverse=True)
print(num1)
#count making a programe for count in list
numbers=[1,2,3,4,5,6,7,8,9,10,10,11,12,13,13,14,15,16,17,18,19,20]
print(F'The numbers are: {numbers}')
item_to_count=int(input("Enter a number: "))
print(numbers.count(item_to_count))
#nested
num1=[1,2,3,4,5,6,[1,2,3,4,5,6]]
print(num1[6][0])