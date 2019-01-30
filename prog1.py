
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:08:31 2018

@author: student
"""

print ('enter length')
l=int(input())
print ('enter breadth')
b=int(input())
if l==b:
    print('it is a square')
else:
    print('it is not a square')
    
    
print('enter an integer')
n1=int (input())
n2=input('enter another integer')
if n1>(int(n2)):
    print("the greater no is",n1)
elif (int(n2))>n1:
    print("the greater no is ",n2)
else:
    print("no.s are equal")
    

print ('enter quantity')
q=int(input())
cost=q*100
if cost>1000:
    cost1=cost-(cost*0.10)
else:
    cost1=cost
print("total cost for user",cost1)
    

print ('enter service year')
yr=int(input())
print ('enter salary')
sal=float(input())
if yr>5:
    sal1=sal+(sal*0.05)
else :
    sal1=sal;
print ('Year of service and salary are',yr,sal1)

print ('enter marks')
marks=int(input())     
if marks<25:
    print('F')
elif (marks>=25) and (marks<45):
    print('E')
elif (marks>=45) and (marks<50):
    print('D')
elif (marks>=50) and (marks<60):
    print('C')
elif (marks>=60) and (marks<80):
    print('B')
else:
    print('A')
    
a,b,c= eval(input('enter ages'))
if int(a)> int(b):
    if int (a)>int(c):
        print('Oldest age is',a)
elif int(b)> int(c):
    if int(b)> int(a):
        print('Oldest age is',b)
elif int(c)> int(b):
    if int(c)>int(a):
        print('oldest age is',c)
    
print('enter no.:')
a=int (input())
if a<0:
    a=a*-1;
print('absolute value',a)

print('enter no. of classes held')
n=(int)(input())
print('enter no. of classes attended')
m=(int)(input())
per=(m/n)*100;
if per>=75:
    print('Qualified',per)
else:
    print('not qualified',per)
    a=input('enter medical certificate Y/N')
    if a=='Y':
        print('Qualified due to medical cause')

        
x=2
y=5
z=0
print(x==2)
print(x!=5)
print(x!=5 and y>=5)
print(z!=0 or x==2)


print('age')
age=int (input())
print('Sex M/F')
sex=input()
print('Marital status Y/N')
mar=input()
if sex=='F':
    print('urban')
elif sex=='M' and (age>20 and age<40):
    print('Anywhere')
elif sex=='M' and (age>40 and age<60):
    print('urban')
else:
    print('Error')
    
print('enter year')
year=int (input())
if year%4==0:
    print('leap year')
elif year%100==0:
    print('not leap year')
elif year%400==0:
    print('leap year')
else:
    print('not leap')


a=100
b=20
c=30
print('a is greater')if (a>b and a>c) else print('b is greater') if(b>a and b>c)else print('c is greater') 

#happy and sad number           
print('enter no')
n=int(input())
m=n

def fac(m):
    ad=0;
    while m>0:
        c=m%10
        k=(c*c)
        ad=k+ad
        m=m//10
    if(ad==1): 
        print('happy no.')
    elif (ad==2) or (ad==3) or (ad==4) or( ad==5) or(ad==6)  or (ad==7) or (ad==8) or (ad==9):
        print('sad no')
    else:
        fac(ad)
fac(n)         

#1.square of all no.s from 0-10
m=0
while m<10:
    sq=m*m
    m=m+1
    print(sq)

#2.sum of even no.s
m=0
s=0
while m<10:
    if m%2==0 :
        s=s+m
    m=m+1
print(s)

#3.take 3 no.s and check how many nos b/w a and b are divisible by c
a,b,c=eval(input('enter 3 no.s'))
count=0
while a<b:
    if a%c==0:
        count=count+1
        print(a)
    a=a+1
print('no. of no.s divisible are:',count)

#4.print factorial f a given no.
n=5
m=1
fact=1
while m<6:
    fact=fact*m
    m=m+1
print(fact)

#5.Armstrong no.
import math
n=(int) (input('enter a no.'))
copy=n
sum=0
count=0
while copy>0 :
    count=count+1
    copy=copy//10
copy1=n
print(count)
while copy1>0 :
    rem=copy1%10
    sum=sum+(math.pow(rem,count))
    copy1=copy1//10
if(sum==n):
    print('armstrong no.')
else:
    print('not armstrong')

#6.krishnamurthy no. factorial of digits
   
n=int (input('enter a no'))
copy=n
sum=0
while copy>0:
    rem=copy%10
    m=1
    fac=1
    while m<=rem:
        fac=fac*m
        m=m+1
    sum=sum + fac
    copy=copy//10
    rem=1
if(sum==n):
    print('krishnamurthy no.')
else:
    print('not krishnamurthy')

#7.sum of digits of user given no.
n=int (input('enter a no'))
sum=0;
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print('sum:',sum)

#reverse no.
n=int (input('enter no.' ))
rev=0;
while n>0:
    rem=n%10
    rev=rem+rev*10
    n=n//10
print(rev)

#palindrom no.
n=int (input('enter no.' ))
rev=0
copy=n
while n>0:
    rem=n%10
    rev=rem+rev*10
    n=n//10
if(copy==rev):
    print('palindromic no')
else:
    print('not palindromic')

#11.special no
n=int (input('enter a no'))
copy=n
su=0
mul=1
while n>0:
    rem=n%10
    su=su+rem
    mul=mul*rem
    n=n//10
ad=su+mul
if ad==copy:
    print('special no.')
else:
    print('not special')

#12.amicable no.
a=int (input('enter no.'))
b=int (input('enter no.'))
s1=0
s2=0
m=1
while a>m:
    if( a%m==0):
        s1=s1+m
    m=m+1
m=1
while m<b:
    if(b%m==0):
        s2=s2+m
    m=m+1
if s1==b and s2==a:
    print('amicable no.')
else:
    print('not amicable')

#stop when u get a negative no.
a=1
while a!=0:
    a=int (input('enter a no.'))
    if(a<0):
        print('stop')
        break;
    else:
        s=s+a
print(s)

#gcd using recursion
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

m=int (input('enter a no.'))
n=int (input('enter another no.'))
g=gcd(m,n)
print('gcd is',g)

#sum of n no. using recursion
def s(n,s1):
    b= int (input('enter a no.'))
    s1=s1+n
    if b==0:
        print('add',s1)
    else:
        s(b,s1)

n=int (input('enter no.'))
x=0
s(n,x)

#difference of n no. using recursion
def s(n,s1):
    b= int (input('enter a no.'))
    s1=n-(s1)
    if b==0:
        print('sum',s1)
    else:
        s(b,s1)

n=int (input('enter no.'))
x=0
s(n,x)

#array list input
my_list=[]
my_list.append(int (input('enter element')))
while True:
    print('enter y for entering element and n for exit')
    ch=(input('enter choice'))
    if(ch=='y'):
        my_list.append(int (input('enter element')))
    else:
        print(my_list)
        break

#check whether element present in list
a=[1,2,3,4,5,6]
b=int (input('enter element'))
c=0
for item in a:
    if item==b:
        print('element present')
        c=c+1;
        break;
if c!=1:
    print('element not found')

#23.8.18
#1.check if string length is 2 or more and the first and last character are same then count
a=['abc','xyz','aba','1221']
b=0
c=0
for item in a:
    if len(item)>=2:
        b=b+1
        if item[0]==item[-1]:
            c=c+1
    
print (c)

##2.check if a list is empty or not
a=[]
if len(a)==0:
    print('empty list')
else:
    print('non empty')

a=[]
if not a:
    print('empty')
    
#3.take 2 list and if they have any common member
a=['ab',2,'ds']
b=['abc','ds',4]
for item in a:
   for item1 in b:
       if item==item1:
           print('true')

#4.remove 0th,4th and 5th element
a=['red','green','white','black','pink','yellow']
b=a[1:4]
print(b)

#5.remove even no.s from list
a=[1,2,3,4,5,6,7,8,9,10]
for item in a:
    if(item%2==0):
        a.remove(item)
print(a)

#6.shuffle and print specified list
import random
a=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(a)
print(a)

#7.delete first 5 and last 5 of a list containing squares
import math
i=1
a=[]
while i<=30:
    x=math.pow(i,2)
    b.append(x)
    i=i+1
a=b[0:5]
a=a+b[25:30]
print(a)

#8.permutation of a list 
import itertools
print(list(itertools.permutations([1,2,3])))
    
#9.access index of alist
a=[1,2,3,4,5]
for item in a:
     print(a.index(item))

#10.covert a list of characters into string
a=['v','i','c','t','o','r','y']
x=""
for item in a:
    x=x+item
print(x)

#11.select item randomly from a list
import random
a=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(a))

#12.second highest no in a list
a=[1,2,4,5,3,7,8]
max=a[0]
secmax=a[0]
for item in a:
    if item>max:
        max=item
for item in a:
    if item>secmax and item<max:
        secmax=item
print(secmax)

#13.frequency of a no. in a list
a=[1,2,3,2,4,1,2,4,2]
b=[]
c=0
for item in a:
     if item not in b:
         b.append(item)
for item in b:
    for item1 in a:
        if item==item1:
            c=c+1
    print(item,"=",c)
    c=0

#x to the power y
def power(x,y):
    if y>1:
        x=x+x
    else:
        return x
    y=y-1
    return power(x,y)

def main():
    x=2
    y=3
    z=power(x,y)
    print('ans:',z)

main()    

#largest no in array using recursion

def large(x,y,m):
    m1=x[y]
    j=len(x)
    print(j)
    if y!=(j-1):
        if m1>m:
            m=m1
        y=y+1
        return (x,y,m)
    else:
        return m


def main():
    x=[1,3,6,2,3,8,7]
    m=x[0]
    h=large(x,1,m)
    print(h)
    
main() 





