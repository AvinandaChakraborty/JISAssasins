'''#Answer 18

import math
x=int(input("Enter x"))
y=int(input("Enter y"))
res=math.pow(x,y)
print(res)'''

#Answer 15

'''import math
x=int(input("Enter x"))
y=int(input("Enter y"))
z=int(input("Enter z"))
res=math.pow(x,y+z)
print(res)'''
#Answer 20

'''import string
#'
letter=str(input("Enter :"))
res = lambda msg: msg.replace("a","*")
print(res(letter))'''

#Answer 19
'''
import math
x=int(input("Enter x"))
y=int(input("Enter y"))
z=int(input("Enter z"))


l1 =x+y
l2=y+z
l3=z+x
if(l1>z):
    True
elif(l2>x):
    True
else:
    True
print("It is a triangle")
'''
#Answer 12

'''import string
letter=str(input("Enter a sentence:"))
words=letter.split(" ")
words.reverse()
print(' '.join(words))'''

#Answer 8

'''import math
x=(input("Enter a number: "))#1234
sum=0
for i in range(len(x)):
    sum+=int(x[i])
print(sum)'''

#Answer 25

'''import math
ch=input("Enter your own character: ")
if ((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
    print("The given character",ch,"is an Alphabet.")
elif (ch>='0' and ch<='9'):
    print("The given character",ch,"is a digit.")
else:
    print("The given character",ch,"is invalid")'''

#Answer 26
import math
'''salary=int(input("Enter your Salary:"))
if(salary>=5000):
   hra= salary * (0.15)
   da= salary * (1.5)
   grosssalary= hra+da+salary
   print("Gross salary",grosssalary)
else:
    hra= salary *(0.1)
    da= salary * (1.1)
    grosssalary=hra+da+salary
    print("Gross salary",grosssalary)'''

#Answer 1
'''class calc:
    def __init__(self):
        a=input("Enter a four digit number ")
        count1=count2=count3=0
        for x1 in a:
            x=int(x1)
            if(x==0):
                count1=count1+1
            elif(x%2==0):
                count2=count2+1
            else:
                count3=count3+1
                print("Number of zeros =",count1,"Number of odd numbers =",count3,"Number of even numbers =",count2)

object=calc()'''

#Answer 7
'''import math
n=int(input("Enter a number:"))
x=0
while(n>0):
     l=n%10
     x=x+l
     n=n//10

print("The total sum of digits is:",x)'''

#Answer 24
'''import math
num=int(input("Enter a number:"))
print("Multiplication table of",num)
for i in range(1,11):
    print(num,"x",i,"=",num*i)'''


#answer 9
'''import math
n = int(input("Enter a Number :"))

rev = 0
fd = 0
s = 0

ld = n % 10

while n > 0:
    r = n % 10

    rev = rev * 10 + r

    n = int(n / 10)

fd = rev % 10

s = fd + ld

print("Sum of first and last digit is :", s)'''

#Answer 10

'''print("Enter 'x' for exit.")
string=input("Enter any string to remove all vowels from it:")
if string=='x':
    exit()
else:
    newstr=string;
    print("\nRemoving vowels from the given string...");
    vowels=('a','e','i','o','u');
    for x in string.lower():
        if x in vowels:
            newstr=newstr.replace(x,"");
            print("New string after successfully removing all the vowels:");
            print(newstr);'''





