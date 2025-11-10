#list operations[ciarus3ln]
'''
-> list is an orderd data type
-> lis is an mutable(changable)
-> builtin data structure
'''
a=[1,2,3,4,5,6]
a.append('hello')
#print(a)
#tuple:
'''
-> it is an orderd data type
->it is immutable(cannot changable after creation)
-> it is a built-in data structure
-> tuple can be created in two ways
    1. variable= (data)
    2. variable= tuple() #when ever we want convert one data to another we use this
    '''


v=(1,2,3,4)
print(v)
print(v[2])
print(sum(v)) #we can able to perform aggreagte functions(sum,min,max)
print(type(v))


#v=[1,2,3,4]

b=list(v)
b.append('good morning')
v=tuple(b)
print(v)


'''
1. we will have tupe data
2. we need convert this tuple to list
3. now the data will be in list format
4. we can able to all operations by using ciarus3ln
5. convert this list to tuple'''


#list user input
'''a=input().split(",") #list data type inside tht list every data will combine as a  single str
print(a)
print(type(a))'''


#variable= list(map(datatype, input().split(",")))
var=set(map(int,input().split(",")))
#print(var)

q=1
e=2
r=3
print(id(q))
print(id(e))
print(id(r))


#user=list(map(int,input().split(",")))

a='hello'
b=input()
if  a==b:
    print("hi")


