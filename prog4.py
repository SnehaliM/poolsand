n,m=eval(input('no of rows,no of columns'))
a=[0]*n
for i in range(n):
    a[i]=[0]*m
for i in range(n):
    for j in range(m):
        a[i][j]=int(input('enter the number'))
print(a)

#.transpose of a matrix
n,m=eval(input('no of rows,no of columns'))
a=[0]*n
b=[0]*m
for i in range(n):
    a[i]=[0]*m
    
if i in range(m):
    b[i] = [0]*n
for i in range(n):
    for j in range(m):
        a[i][j]=int(input('enter the number'))
print(a)

for i in range(m):
    for j in range(n):
        x=a[j][i]
        b[i][j]=x
        print(b[i][j])
print(b)

#check diagonals are 1 or not
n=int(input('no of rows,no of columns'))
m=int(input())
c=0
a=[0]*n
for i in range(n):
    a[i]=[0]*m
for i in range(n):
    for j in range(m):
        a[i][j]=int(input('enter the number'))
for i in range(n):
    if a[i][i]==1:
        c=c+1;
if c==n:
    print('diagonals are 1');
        
print(a)

#.file creation
file_input=open('D:\\a.txt','w')
str1=input('enter')
file_input.write(str1);
file_input.close()

#file read
file_input=open('D:\\a.txt','w')
str1=' '
while str1!='0':
    str1=input('enter')
    file_input.write(str1)
file_input.close()
file_input=open('D:\\a.txt','r')
str2=file_input.readlines()
for line in str2:
    line=line.strip('\n')
    print(line)    
file_input.close()

#.copy 1 file to another
file_des = open('D:\\a.txt','w')
str1='ab'
while str1!='0':
    str1=input('enter')
    file_des.write(str1)
file_des.close()
file_input=open('D:\\b.txt','w')
file_input.close()
file_sou = open('D:\\a.txt','r')
str2=file_sou.readlines()
file_des=open('D:\\b.txt','w')
for line in str2:
    file_des.write(line)
    
file_sou.close()
file_des.close()

#str1=file_des.readLines()

for li in str1:
    li=li.strip('\n')
    print(li)

file_sou.close()
file_des.close()

#identical
file_a=open('D:\\a.txt','r')
file_b=open('D:\\b.txt','r')
str1=file_a.readlines()
str2=file_b.readlines()
if str1==str2:
    print('identical')

#frequency or degree of node
file_a=open('D:\\x.txt','w')

str1=' '
while str1!='0':
    str1=input('enter')
    file_a.write(str1)

file_a.close()
file_a=open('D://x.txt','r')
str2=file_a.readlines()
file_b=open('D:\\y.txt','w')
x=[]
a=[]
c=0
for line in str2:
    x=line
for it in x:
    if it not in a:
        a.append(it)
for item in a:
    for line in x:
        if item==line:
            c=c+1
            s=str(c)
    file_b.write(item+s)
    file_b.write('\n')
    c=0
            
file_b.close()
file_a.close()

#average
file_a=open('D:\\m.txt','w')
y=[]
str1=' '
while str1!='0':
    str1=input('enter')
    file_a.write(str1)
    

file_a.close()
file_a=open('D://n.txt','r')
str2=file_a.readlines()
y=str2.split(' ')
file_b=open('D:\\y.txt','w')

#4/10/18
#create a file and write multiple user lines
file_input=open('D:\\new.txt','w')
i=0
str=""
while i!=3:
    str=input('enter lines:')
    file_input.write(str)
    i=i+1
file_input.close()

#read a previous created file
file_input=open('D:\\new.txt','r')
str2=file_input.readlines()
for line in str2:
    line=line.strip('\n')
    print(line)    
file_input.close()

#merge two files in another file
file_so1=open('D:\\new.txt','r')
file_so2=open('D:\\b.txt','r')
file_des=open('D:\\x.txt','w')
str=file_so1.readlines()
for line in str:
    file_des.write(line)
str1=file_so2.readlines()    
for line1 in str1:
    file_des.write(line1)
file_des.close()
file_so2.close()
file_so1.close()
    
#count no. of characters, lines and words in a file
file_s=open('D:\\new.txt','r')
l=0
w=0
c=0
str=file_s.readlines()
x=[]
for line in str:
    x=line
i=0
print('characters:',len(x))

while i<len(x):
    if x[i]=='.':
        l=l+1
        w=w+1
    elif x[i]==' ':
        w=w+1
    i=i+1
print('lines:',l+1)
print('words:',w+1)
file_s.close()



file_s=open('D:\\new.txt','r')
l=0
w=0
c=0
str=file_s.readlines()
print('no. of lines',len(str))
for line in str:
    line=line.strip('\n')
    words=line.split(' ')
    w=w+len(words)
    l=l+len(line)
print('no. of words',w)
print('no. of characters',l)


#read even positioned lines in a file
file_s=open('D:\\new.txt','r')
str=file_s.readlines()
i=0
for line in str:
    i=i+1
    if i%2==0:
        print(line)
file_s.close()

#read odd positioned lines in a file
file_s=open('D:\\new.txt','r')
str=file_s.readlines()
i=0
for line in str:
    i=i+1
    if i%2!=0:
        print(line)
file_s.close()

#replace a user given word by another user replacing word in afile
file_s=open('D:\\new.txt','r')
file_d=open('D:\\y.txt','w')
rep=input('enter word to be replaced')
nw=input('enter new word')
a=0
b=''
str=file_s.readlines()
for line in str:
    l1=line.strip('\n')
    l2=l1.split(' ')
    if rep in l2:
        a=l2.index(rep)
        l2[a]=nw
    for i in l2:
        b=b+i
    file_d.write(b)
file_s.close()
file_d.close()
    
#read last n lines of file 
file_s=open('D:\\new.txt','r')
file_d=open('D:\\z.txt','w')
n=(int)(input('enter no. of lines')) 
str=file_s.readlines()
i=0
for line in str:
   l1=line.strip('\n')
   if i>n:
       file_d.write(line)
   i=i+1
    
file_d.close()
file_s.close()
        
#find longest word
file_s=open('D:\\new.txt','r')
str=file_s.readlines()
l=0
s=''
for line in str:
    l1=line.strip('\n')
    l2=l1.split(' ')
    for i in l2:
        if len(i)>=l:
            s=i
            print(s)
            l=len(i)
print(s)
file_s.close()

#combine each line from first file with corresponding line in 2nd file
file_f=open('D:\\new.txt','r')
file_s=open('D:\\x.txt','r')
file_d=open('D:\\m.txt','w')
i=0
str=file_f.readlines()
str1=file_s.readlines()
for line in str:
    if i==0:
        file_d.write(line)
        for line1 in str1:
            file_d.write(line1)
    i=i+1
file_d.close()
file_s.close()
file_f.close()

#remove newline characters from a file
file_f=open('D:\\new.txt','r')
file_d=open('D:\\m.txt','w')
str=file_f.readlines()
for line in str:
    line=line.strip('\n')
    file_d.write(line)
    
file_f.close()
file_d.close()
        
#mcq

file_q=open('D:\\q.txt','r')
file_a=open('D:\\ans.txt','r')
str=file_q.readlines()
str1=file_a.readlines()
sc=0
y=[]
c=0
for line in str:
    print(line)
    x=input("enter your answer")
    for line1 in str1:
        y=line
   
    if x==y[c]:
        sc=sc+2
    else:
        sc=sc-0.25
    c=c+1
       
print(sc)
file_q.close()
file_a.close()




dir(int)
print(int.__add__(2,3))

class demo:
    def _dm1_(self,a):
        self.a=a
        print(str(a)+'ho')
        
class dem(demo):
    def _dm2_(self,b):
        print(b)
 
class d:
    def main():
        ob=dem()
        ob._dm2_('ab')
        ob._dm1_('ac')

import collections
m=[1,2,5,2,1,5,7]
ctr=collections.Counter(m)
print('freq:',ctr)

def scndlarge(n):
    count=0
    n1=n2=float('-inf')
    for x in n:
        count=count+1
        if x>n2:
            if x>=n1:
                n1,n2=x,n1
            else:
                n2=x
    return n2 if count>=2 else None

def main():
    n=[1,3,4,5,6,7,2,13,8]
    y=scndlarge(n)
    print(y)
main()

import random 
color=['red','yellow','green','blue']
x=random.choice(color)
print(x)

import Calender
yy=int(input('enter year'))
mm=int(input('enter month'))
print(Calender.(yy,mm))

import datetime
nw=datetime.datetime.now()
print(nw.strftime('%d-%m-%y %H:%M:%S'))

