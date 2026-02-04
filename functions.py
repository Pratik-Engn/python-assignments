#user defined function
name=input("Enter your name: ")
def greeting_function(name):
    print(f"hello, {name} how are you?")
    print("how is your day going")

#calling it
greeting_function(name)
#practicing some return value function

def even_odd(num):
    if num % 2 == 0:
        return ("even")
    else:
        return ("odd")
num = int(input("Enter a number: "))
result = even_odd(num)
print(f"The given number is {result}")

#variable arguments
def student_marks(sid, name, *marks):
    avg = sum(marks)/len(marks)
    print(f"The average of {name} is {avg}")
student_marks(15,"Pratik",56,46)
student_marks(15,"Swarnak",95,65)
student_marks(15,"Suvajit",98,98)
student_marks(15,"Saheli",90,65)
#keyword arguments
def keywords(**kwargs):
    print(kwargs, type(kwargs))
keywords(a=20, b=35)