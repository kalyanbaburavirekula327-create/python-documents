#scope&history
#variables,ids,memorey allocation
#keywords
#we learn about what types of data do we have
#user input functions
#we enterd into operators

#Strings: group of charecters that are enclosed within single or double quotations
#string is a immutable
time='8:11am'
print(time)

#string methods:
#upper,lower,title,capitalize,strip,replaced(old,new),split,join,count,isdigit,isalpha
'''upper: it just converts all letters to uppercase:'''
u='hello'
print(u.upper())

l='HEY'
print(l.lower())

#title: it makes first letter of each word capital

t='hello world'
print(t.title())

#capitalize:
c='hello world'
print(c.capitalize())


#strip:it is a most important method in the strings concept
'''
while using the strip function when ever we are having extra spaces at the begining
or ending it just remove

'''

s='  hello  '
print(s.strip())

#replace:
'''
when ever we wanted update the old /previous data to the new data we use this method'''

r='good afternoon'
print(r.replace(r,'good morning'))

#split:
'''
it is used to split the string in to list by spaces'''

s='hello how are you'
print(s.split())

#join : when ever the strings are stored in an array/list it again converts in to string


a='hello hi'
a=a.split()
a.append('bye')
print(" ".join(a))

#count:
'''
it is used to get the data that how many times the substring appears'''

c='apppple'
print(c.count('p'))


#isdigit,isalpha:
#isdigit: if the string contains only numbers it results true boolean value else false

i='123456'
print(i.isdigit())

iss='abc'
print(iss.isalpha())

#len: when ever we are having multiple lines of information then we can find the length
#of the entire information

l='hello how are you what you are doing have a nice day sir / mam'
print(len(l))




