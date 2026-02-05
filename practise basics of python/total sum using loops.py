#highest score
scores=[1,2,3,4,5,6,7,8,9]
highest=scores[0]
for score in scores:
    if score>highest:
        highest=score

print(f"The highest score is {highest}")
#lowest
scores=[1,2,3,4,5,6,7,8,9]
lowest=scores[0]
for score in scores:
    if score<lowest:
        lowest=score

print(f"The highest score is {lowest}")
#shortcut
scores=[1,2,3,4,5,6,7,8,9]
print(f"the highest number",max(scores))
#break statement check
for number in range(1,10):
    if number % 2==0:
       break
    print(number)
#continue statement it helps in finding numbers which are not divisble by 2
for number in range(1,10):
    if number % 2==0:
       continue
    print(number)

#checking infinete property of while loop
num=1
while num<5:
    print(num)
