#basics of python
#loops,and conditionals
#organizing and manipulating the data based on categories
#functions

#additon of two numbers program
#when ever we are performing same logical operations we need to create the same structure
#multiple times
a=10
b=20
#print(a+b)

'''a=int(input())
b=int(input())
print(a+b)'''

a=100
b=50
#print(a+b)


#functions:
'''def function_name(parameters):
    write my logic
call function_name(arguments)

->we do not want to create multiple structure for same logic[once creation is enough] '''

#27 even or odd

def add_two(a):
    for i in range(1,a+1):#10+20
        print(i)
#add_two(10)

#in how many ways we can able to write this functions
'''
4 types
1. function with parameters with return value
2. function with parameters without return value
3. function without parameters with return value
4.  function without parameters without return value
'''
#anonymous functions

#using functions only
'''
1.write a program that prints 1 to 10 numbers
2. write a program that prints first 5 prime numbers
3. write a program that prints no of even and odd numbers count [1 to 10]
4. write a program that prints addition of two strings
5. write a program that prints user string input to be displayed in capital format'''


'''4 types
1. function with parameters with return value
2. function with parameters without return value
3. function without parameters with return value
4.  function without parameters without return value
'''

#with parameters with return value

#add of two nums

def func_name(a,b):
    return (a+b) #2+5=7
#print(func_name(2,5))



#function with parameters without return value
'''def python(a,b):
    print(a+b) #10+5
    print(a-b) #10-5
    print(a*b) #10*5
    print(a//b) #10//5
#python(10,5)'''

#function without parameters with return value
'''def sample():
    return ("please fill all the details")
print(sample())
    '''
#function without parameters without return value

'''def final():
    a=int(input())
    if a%2==0:
        print("even")
    else:
        print("odd")
final()'''


#step-1:

'''a=10
b=20
c=a+b
print(c)'''


#step:2
'''def two(a,b):
    print(a+b)
two(10,5)'''

#step 3 : anonymous functions-> they do not have function name
#the anonymous functions are single line expressions [lambda]

#syntax: [lambda parameters : expression(logic)]

c=lambda  a,b :a=b
#print(c(10,34))
#write a program that gives squre of a number using lambda
sq= lambda a : a*a #a=6 : 6*6=36=a
#print(sq(int(input("enter a number to get square of it: "))))

#using lambda inside the function:

#def func_name(f,v):
    #return f//v
#res=func_name(7,8)
#print(res)
#by using lambda we can able to use map,filter,reduce

s=list(map(int,input().split(",")))

lis=[1,2,3,4,5] #[1,4,9,16,25], [1, 4,9,16,25]
#syntax for map:datatype(map(lambda parameters : expression ,variable))

#each and every number to be displayed as a square
sqq=list(map(lambda x:x**2,lis ))
#print(sqq)
#filter functions
morning=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,4,15]
for i in morning:
    if i%3==0:
        print(i)



# for i in morning:
#     if i%3==0:
#         print(i,end=" ")


#syntax  for filter:data structure( filter((lambda expression)))
#res=list(filter(lambda loan,a : loan=='processing', ))
# print(res)

#reduce

variable=[12,34,56,12,54,34,87,90]
 #10

#sum of all numbers/data from the list 
#->map,filter?
#reduce func
#algorithm
'''

-> we need to import the reduce from func tools
-> we do not want to store the data or reduce function inside side any data type
-> reduce(lambda expression)
'''

from functools import reduce
s=[1,2,3,4] #s=[10]
v=reduce(lambda a,b : a+b,s) #a=3,b=7 =>a+b=10
print(v)






