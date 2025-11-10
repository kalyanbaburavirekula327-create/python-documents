
'''
list[orderd,mutable]
tuple[orderd,immutable]
dictionary[orderd,mutable]
set[unorderd,mutable]'''
#dictionary:
'''
->below the 3.7 the dictionary is unorderd
-> after 3.7 version dict is categorized into orderd format'''

''''
1. book is placing proper orderd
2. when ever we want to access the we prefer to use word [when ever i want meaning i search the word[index]]'''

#def: the combination of orderd word and meaning as a pair are storing inside a book it is called a dict
#def: the combination of orderd keys and values  as a pair are storing inside a {}   it is called a dict in python

#create a dict
'''
1st syntax:
variable= {'k':'v'} #if value is in integer format no need to declare the values inside the dict

2nd syntax:

variable= dict(k='v')
'''
#creation of dict
v={'k': 1,'a':'python','c':12.79}
print(v)
#k=dict(a=11,b='hello',c=23.67)
#print(k)

#v[ind]
#accessing the elements

print(v['a'])
print(v['c'])

#we need to update or add new elements into the dictionary
#update
'''
syntax update

v['key']=new data

syntax add new data

v['key']=new data
'''
#updating
sam={'a':1,'b':2,'c':3}
sam['b']='2'
print(sam)

#adding
sam['d']='i am new value'
print(sam)

#removing elements from the dictionary
'''
->pop()
->popitem()
->del
->clear()'''


hello={'what is the time':'8:47','age':25,'course':'python','shift':'morning'}
#pop()-> remove the data(value) by key
#syntax: variable.pop(key)
hello.pop('age')
print(hello)
#popitem():-> it just removes the last inserted item
#syntax: variable.popitem()
hello.popitem()
print(hello)

#del : 1. we can able to delete entire dictionary at a single time,2. only specific pair can be deleted also
#del variable['key']
del hello['course']
print(hello)
#{}
#clear: variable.clear()
hello.clear()
print(hello)

#==================================================================
#methods:
'''
keys
values
items
get
merge\copy
'''
method=dict(a=1,b=2,c=3,d=4)#keys=[a,b,c,d],values=[1,2,3,4],pair=[method]
print(method)
#only keys: variable.keys()
print("keys:=>",list(method.keys()))
#only values: variable.values()

print("values:=>",list(method.values()))

#pair value: variable.items()
print("items:=>",list(method.items()))
#copy: variable.copy()
newdict=method.copy()
print(newdict)

#merge 1st.update(2nd)
e={'key':'value'}
'''newdict.update(e)
print(newdict)'''
#merge:
r={**newdict,**e}
print(r)

#method :1st | 2nd

print(newdict | e)


