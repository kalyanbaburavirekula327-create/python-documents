#set
'''
-> it is a built in data type where we manage and manipulate the data
-> it is a mutable
-> it is unorderd
-> it removes duplicates automatically'''

#operations and methods
#creation of a set

#1st syntax of creation: variable= {}
#d={1,'h',23.95}
#print(type(d))

#2nd syntax of creation: variable = set()
a={1,2,3,4,5,6,'hello',12.98} #i want remove the element 'hello' by using list operations
#print(a)
b=list(a)
#print(b)
b.remove('hello')
a=set(b)
#print(a)

#why set is unorderd

r=[4,7,'hello',1,5,45.97] #list orderd
print(r[2])

r=(4,7,'hello',1,5,45.97) #tuple orderd
print(r[2])
r={'a':1,'b':2,'c':'hello'} #dict orderd
print(r['c'])
r={12.678,4,7,'hello','hi',5,45.97} #set unorderd,it is not having indexing
r.remove('hello')
print(r)
#loops

#set methods:
#list[more than 15 ],tuple[below 5],dict[relevent operations like list],set[some similarity to list but less operation]

#add,update,remove,discard,pop,clear,copy
hello={1,2,4}
#add: to add the data [single data] we use add
#syntax : variable.add(single new data)
hello.add('good morning everyone')
print(hello)
hello.add('nov 7th 2025')
print(hello)

#update(): we can able to add multiple data at a time
#syntax: variable.update([multiple data])
hello.update(['python','set','session'])
print(hello)

#remove the elements from the set
#remove :syntax:variable.remove()-> [if element is present it removes else throw error]

hello.remove('session')
print(hello)

#hello.remove('kalyan')
#print(hello)
#discard: if element is present it removes else it display current set instead of throwing errors
#variable.discard(data to be removed)
hello.discard('set')
print(hello)

hello.discard('gen ai testing')
print(hello)


#pop,clear,copy
#pop: no index ,=>remove the last data,else removes random data
#syntax : variable.pop()
hello.pop()
print(hello)
hello.pop()
print(hello)

#clear: just display the structure removes all the data

#hello.clear()
#print(hello)

#copy() we can able to copy entire set and assign to a new variable
#syntax: new_variable= oldvariable.copy()
ncpv=hello.copy()
print(ncpv)

#methods[union,intersection,difference,symmetric_difference]

#these methods perform the action on two sets

#set1=[1,2,3,4,5,6],set2=[4,3,4,7,8,9,10]

#output={1,2,3,4,5,6,7,8,9,10}
set1={1,2,3,4,5,6}
set2={4,3,4,7,8,9,10}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))





