# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:37:06 2018

@author: lab5
"""

#String Programs
#1.calculate length of string
a= input('enter a string')
c=0
for item in a:
    c=c+1
print(c)

#2.make a string from the first 2 and last 2 elements of a string
a=input('enter a string')
l=len(a)
if l<=2:
    print('empty string')
else:
    s=a[0:2]
    s=s+a[l-2:l]
    print(s)

#3.change all the occurance of the first character except first char itself
a=input('enter a string')
s=''
c=0
for item in a:
    if c!=0:
        if item==a[0]:
            s=s+'$'
            print(s)
        else:
            s=s+item
    else:
        c=c+1
        s=s+item
print(s)

#4.enter 2 strings and print them after swapping the first to characters of each
a=input('enter a string')
b=input('enter another string')
s=b[0]+b[1]+a[2:len(a)]
s1=a[0]+a[1]+b[2:len(b)]
print(s,' ',s1)

#5.replacing not..poor with good
a=input('enter a string')
b=a.split()
for item in b:
    if item=='not':
        p=b.index(item)
    if item=='poor':
        q=b.index(item)
del b[p:q]
b[p]='good'
for item in b:
    print(item)
    
    
str=input('enter:')
fst=str.find('not')
snd=str.find('poor')
print(fst,snd)
if (fst>snd and snd>0 and fst>0):
    str=str.replace(str[fst:(snd+4)],'good')
elif (fst<snd and snd>0 and fst>0):
    str=str.replace(str[fst:(snd+4)],'good')
print (str)    
#a=input('enter a string')
#b=a.split(' ')  
#a.replace('not','good','poor')    
#print(a)  
    
#6.function that takes a list of words and prints the largest one
a=['apple','orange','cucumber']
l=len(a[0])
s=a[0]
for item in a:
    if l<len(item):
        l=len(item)
        s=item
print(s)


#7.remove the characters which have odd index
a=input('enter word')
l=len(a)
s=''
c=0
while c<l:
    if(c%2==0):
       s=s+a[c]
    c=c+1
print(s)
        
#8.sorted alphanumericall
a=['new','word','is','entered'] 
a.sort()
print(a)    
    
#9.swap comma and dot in a string
a=input('enter a string')
for item in a:
    if item==',':
        s=s+'.'
    elif item=='.':
        s=s+','
    else:
        s=s+item
    
print(s)

#10.sum of digits of a given string
a= (input('enter a string'))

sum=0
for item in a:
    if item.isdigit()==True:
        s=int(item)
        sum=sum+s
print(sum)

#index of all characters in a string
a=input('enter string')
for items in a:
    x=a.index(items)
    print(x)
    
    
#.Matrix
n=3
m=3
a=[0]*n
b=[0]*n
for i in range(n):
    a[i]=[0]*m
    b[i]=[0]*m
for i in range(n):
    for j in range(m):
        a[i][j]=int (input())
#transpose
for i in range(n):
    for j in range(m):
        b[i][j]=a[j][i]

print(b)

#separation of words using multiple delemitre
import re
a=input('enter a string')
b=re.split(',| |;',a) 
print(b)
c=list(filter(str.strip,b))  
print(c) 


#length of a string
s=input('enter a string')
c=0
for item in s:
    c=c+1
print(c)
#concat string
s=input('enter a string')
l=len(s)
if l<2:
    print('empty string')
else:
    a=s[0:2]
    a=a+s[l-2:]
    print(a)
    
#replace
s=input('enter a string')    
s1=s[0]
s2=s[1:]
s3=s2.replace(s1,'$')
s4=s1+s3
print(s4)

#swapping
s=input('enter a string')
s1=input('enter a string')
s2=s[:2]+' '+s1[2:]
s3=s1[:2]+' '+s[2:]
print(s2)
print(s3)

#replace
s='the lyrics is not that poor'
p=s.find('not')
q=s.find('poor')
t=len('poor')
if p==-1 or q==-1 or p>q:
    print(s)
else:
    r=s.replace('[p:q+t]','good')
    print(r)