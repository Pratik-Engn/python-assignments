def division(num1,num2):
    """this is function for division
    here num1 is frist input which is the numerator
     and num2 is second input which is the denominator"""
    if num2==0:
       return "Such number does not exist"
    else:
        result=num1/num2
        return result

print(division(2,0))
help(division)