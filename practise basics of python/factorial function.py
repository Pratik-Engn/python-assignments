#factorial function
num1=int(input("Enter your number:"))

def factorial(num1):
    factorial=1
    while num1>1:
        factorial=factorial*num1
        num1=num1-1
    return factorial

print(factorial(num1))

#by recurrsion
num1=int(input("Enter your number (this) is through recurrssion:"))
def fact_recursive(num1):
    if num1==1:
        return 1
    else:
        factorial=num1*fact_recursive(num1-1)
        return factorial
print(fact_recursive(num1))

#global and local variable
n=1
def fn(num):
    n=5
    print(F"incoming variable {n}")

fn(24)

#function as a argument
def add(num1):
    return num1+1

def square(num1):
    return num1**2

num1=int(input("Enter your number:"))
res=square(add(num1))
print(F'the number is {res}')

#lamda function
fun=lambda a,b:a+b
res=fun(2,3)
print(res)
#just for fun
num1=int(input("Enter your number which is going to be the base:"))
num2=int(input("Enter your number which exponents you wanna find from the input :"))
func=lambda num1,num2:num1**num2
res=func(num1,num2)
print(f'the answer is {res}')

#filter function
seq=[1,2,3,4,5,6,7,8,9]
odd= lambda x: True if x%2==0 else False
filtered=filter(odd,seq)
print(list(filtered))
