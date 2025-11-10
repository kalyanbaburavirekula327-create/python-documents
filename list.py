#transfer statements:[break,continue ,pass]
a=[1,2,3,4,5,6,7]
t=5
for i in a:
    if i==t: #5==5?
        pass
    #print(i)
    
    
#built-in data types/data structures[list,tuple,dict,set]:
    
'''
list built in data type/structure:
#CIARUS-3LN'''
'''
->C: creating a list types
->I: indexing and slicing
->A: adding the elements into the list[append,insert,extend]
->R: removing the elements from the list[pop,del,remove,clear]
->U: updating the elements inside the list
->s: searching and counting the data inside the list
->3L: list operations,list functions,list comprehensions
->N: nested lists'''




#c-creating a list
'''
list can be created by two ways:
=> using squre brackets
=> using list function

syntax for creating a list:

=> variable=[data]
=> variable=list((data))'''

a=[1,2,3,'hi',23.198]
#print(a)
#print(id(a))
#print(type(a))

b=list((1,2,3,'hi'))
#print(b)



#int arr=[]
 #3-1=2

#indexing and slicing

#indexing:
'''
=> the indexing always start from 0
=> we can able easily find out the indexes values [n-1]'''
#slicing:
#start:stop:step
samp=[1,'hello',34.67,900,'python']

#printing the last data[-1]
print(samp[-1])

#print(from user start point and upto ending)

print(samp[1:-1:2])
#print (list in reverse order)
print(samp[::-1])
print(samp[1::])


#CIARU[s-3ln]

#A: adding the elements into the list

#[append,insert,extend,add(+)]

lis=[1,2,3,4,5]

#append:when ever we want to add the data into the list by using this append function we can only insert single data
#and that data will be placed at the end of the list

#variable.append(new data)
lis.append('hello')
print(lis)

#insert syntax: variable.insert(index,data)
lis.insert(0,'goodmorning')
print(lis)

#add(+): concatination => adding up of two similar data types

b=[1,2,3]
c=['hi','hello','bye']

print(b+c)


new1=[8,6,5]
new2=[1,2,3]

#extend: firstlist.extend(second list)

new1.extend(new2)
print(new1)

new2.extend(new1)
print(new2)


#how to remove the elements/data from the list[pop,remove,clear,del]
#pop and del can be used based on index value
#remove : can be delete the elements based on data
#pop:
'''
-> it is used to remove the elements from the list
-> when  ever we want to get back the deleted element it is possible
-> the data can be removed based on indexing value
'''

#syntax : pop:> variable.pop(index value/number)

sam=[1,2,3,4,5,6]
#3
b=sam.pop(2)
print(b)


#remove:
'''
it is also used to remove the element from the list
once data got deleted we cant get back the deleted data
the data got deleted directly providing the value
'''

#syntax: variable.remove(data)



sam.remove(5)
print(sam)

n=[1,2,3,4,5,5,5,6,7,8,9,10] #[]
#del to delete elemets from the list directly
#syntax: del variable[index]
del n[7]
print(n)

# clear it removes all the data and gives just structure

#syntax: variable.clear()
n.clear()
print(n)


print(n)

#update: we already have some data that data will be modifed with new data
#**variable[index value]=new data

u=[1,2,3,4,1,5,5,7,7,7,]

#s: searching and counting

user='7'
a=10
print(user in u and a in u) #7==7? in u?

#count

us=1

#syntax: variable.count(data)

print(u.count(us))

#3LN(list operations/methods, list functions,list comprehensions,nested list)

#nested list:
#a thing within another one[list is hoilding another list]
b=[1,2,3,4,5,['a','b','v'],[10,'2.3']]
print(b)

#list methods:
#sum,add,multiplication(only with integers)

d=[1,2,3,'4']
#print(sum(d))

e=[1,2,3]
print(e*2)
print(sum(e*2))
#print(d+e)

#aggregate functions
'''
-> min
->max
->avg
-> count
-> sum'''


samp=[2,3,4,5,6]
print(min(samp))
print(max(samp))
#+,-,*,/,%,//,**
#avg=sum of all the numbers /total numbers
hi=sum(samp)
hello=len(samp)
#print(hello)
b=sum(samp)//len(samp)
print(b)

#list comprehensions:
#squre each number in a list
num=[1,2,3,4]
s=[] #[1,4,9,16]
for i in num:  #i=4
    s.append(i*i) #4*4=16 #4
print(s)

#list comprehensions:
'''
it is a single line expression [expression]

var=[expresion iterations]


'''
uss=int(input())
k=[i*uss for i in num ]
print(k)

























