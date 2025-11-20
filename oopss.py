'''20-> basic oops ideas,inheritance,polymorphism,abstraction,
encapsulation,file handling,exception handling'''

#additional things-> numpy,pandas,imports and modules

#oop:

#2 ways : function base code,class base coding(oop)

#class- blue print of an object
#object- instance of a class



#class class_name:
'''def method:
        logics
        print() #method

object= class_name()
object.methodname()'''
    
    
'''class python_session:
    #method1
    def participant1(hello,a,b):
        print(a+b)
    #method 2
    def participant2(bye):
        print("annaveerappa")
    #method 3
    def participant3(a):
        print("avinash")
    #method 4
    def participant4(a):
        print("manikumar")
#he wants avinash       
management=python_session()
management.participant1(10,5)
management.participant2()'''

'''class nandra: 
   def test(hello):
      print("Hello from test method!")
   def test3(aroppdxkjbv,c,d):
      print(f"{c},{d},Hello from test3 function!")
#nandra.test3('how are you')
kalyan=nandra()
kalyan.test3('session','python')'''


#================================================================

#inheritance ->types[single,multiple,multilevel,hierarchieal,hybrid]


#def:aquiring properties from one class to the another class so the first class is named as parent
#and the other classes is named as child classes







#single inheritance:

'''
->aquiring properties from one parent to one child
-> we always create object for the child class only'''
'''class mother:
    def cooks(self):
        print("cooks well")
class child(mother):
    def plays(self):
        print("plays well")
o=child()
o.plays()
o.cooks()'''
#multiple inheritance

#the child class can able to inherit multiple parent classes

'''class father:
    def news(self):
        print("watches news")
class mother:
    def serials(self):
        print("watches serials")
class child(father,mother):
    def cricket(self):
        print("watches cricket")
k=child()
k.cricket()
k.serials()
k.news()'''

#multilevel: can able to inherit properties level by level

'''class grandfather:
    def aggriculture(self):
        print(' i know aggriculture')
class father(grandfather):
    def bussiness(self):
        print('i know business')
class son(father):
    def software(self):
        print('i know developing apps')
obj=son()
obj.software()'''

#hierarchieal,hybrid

#hierarchieal: we have only one parent class but multiple child clasess

'''class parent:
    def mother(self):
        print("cooks well")
class child1(parent):
    def daughter(self):
        print("quick learner")
class child2(parent):
    def daughter1(self):
        print("studies well")
o1=child1()
o2=child2()

o2.daughter1()
o2.mother()
print("===============")

o1.daughter()
o1.mother()'''

#hybrid inheritance:

#[single,multiple,multi level,hierarchieal,hybrid]
#hybrid inheritance is a combination of two or more types of inheritance
#python supports multiple inheritance
'''class A:
    def a(self):
        print("this is class A")
class B(A): #single inheritance
    def b(self):
        print("this is class B")
class C(A): #hirearchieal
    def c(self):
        print("this is class C")
class D(B,C): #multiple inheritance
    def d(self):
        print("this is class D")

obj=D()

obj.d()
obj.c()
obj.b()
obj.a()'''

#================================================================

#POLYMORPHISM:manyforms,

# two techiques[overriding,overloading]
#same method and diffrent classes
'''class home_before_2025:
    def fridge(self):
        print("this is old fridge")
class home_after_2025(home_before_2025):
    def fridge(self):
        super().fridge()
        print("this is new fridge")
o=home_after_2025()
o.fridge()'''


#overloading concept:same classes, same methods,different parameters
'''class home:
    def __init__(self,a):
        print(a)
    def __init__(self,a,b,c):
        print(a,b)
obj=home('python')
obj=home('python','session')'''


'''obj.normal('python')
obj.normal('python','session','hello')'''
#same classes, same methods,different parameters
#1.default,args,kwargs

#1.using default
class demo:
    def same(self,a=hi,b=None,c=0): #none==0
        if c!=0: #c  is not equals to zero
            print(a,b,c)
        elif (a!=None and b!=None):
            print(a,b)
        else:
            print(a)
o=demo()
o.same('hi')
o.same('hi','hello')
o.same('hi','hello','good morning')
            













































    