#iterative statements:

'''
meanings:
=> iterative ==repeating
=> these statements execute a block of code multiple times until the condition
   becomes false
=> used when we want to do an execution again and again(eg: printing numb,processing items,etc)
=> 2: for,while loops
'''
#for loop:
'''
syntax: for variable in sequence:
                block of statements
                
for-> it is used when you already know many times that i neeed to repeat the statements
->  it goes through each element in a sequence [list,tuple,dictionary,set,range,etc]
-> when ever we are not using any[list,tuple,dict,set] and we want to iterate the
   integers then only we prefer range function
    for variable in range(integers)
'''
#print 1 to 5 numbers
'''for a in range(1,6): #6 will be excluded
    print(a)'''
    
'''
=> range(1,6)-> generates numbers 1 to 5 (6 is excluded)
-> a takeseach number one by one
-> print(a) it prints the current number
-> after all numbers are printed loop stops'''

print("=================================")

#ex:2- print each charecter in a word

'''for i in "PYTHON":
    print(i)'''
print("=======================")

#ex:3: sum of first 10numbers
'''c=0
for i in range(1,5): #10[10]
    c=c+i #6+4 =10
print(c)'''

#==========================================================

#while loop:
'''
syntax:
while  condition:
    block of statements
    
->  it is used when you dont know the number of iterations and how many times the loop should run
-> this loop continious as long as condition is true
'''


#print 1 to 5 numbers

i=1
while i<=5: #6<=5 False
    print(i) #1 2 3 4 5
    i=i+1 #5+1=6

print("=========================")

#print the numbers in reverse format


i=5 #0
while i>0: #0>0 False
    print(i) #5 4 3 2 1
    i=i-1 # 1-1=0
    
















