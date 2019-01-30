# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:37:27 2018

@author: student
"""
#30/8/18
#1.program to iterations over set
a=set();
a={1,2,3,4,5};
for letter in set(a):
    print(letter);

#2.add members in a set
a={1,2,3,4,5}
a.add(23);
a.update([7,6])
print(a)

#3.remove items from set
a={1,2,3,4,5};
a.discard(3);
a.remove(2);
print(a);

4.#remove item from set if it is present in set
a={1,2,3,4,5};
b=int (input('enter item'))
if b in a:
    a.remove(b)
    print(a)

5.#max and min value in a set
seta= set([1,8,3,5,7])
print('max no.',max(seta))
print('min no.',min(seta))  

6.#shallowcopy
setp=set(["red","green"])
setq=set(["green","red"])
setr=setp.copy()
print(setr)

#7.sort ascending and descending  a dictionary by value
a={1:2,2:4,3:2,4:6,5:3}
b=set();
for i in a:
    b.add(a[i])
print(b)

#8.add a key to a dictionary
a={1:2,2:4,3:2,4:6,5:3}   
a[6]=22
print(a)

#9.concatenate dictionaries
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#10.check if a member already exists or not
d={1:10,2:20,3:30,4:40}
def is_key_present(x):
    if x in d:
        print('key is present')
    else:
        print('key not present')

is_key_present(5)
 
#11.iterate over dictionaries using for loops
squares = {x: x*x for x in range(6)}
print(squares)

sq={x:x*x for x in range(11) if x%2==1}
print(sq)