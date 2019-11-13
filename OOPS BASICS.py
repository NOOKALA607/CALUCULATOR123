
#CLASS LEVEL:
                #HOW TO ACCESS CLASS LEVEL MEMBERS OR VARIABLES?
                #     answer========>BY USING CLASS NAME
                #HOW TO ACCESS OBJECT LEVEL MEMBERS OR VARIABLES?
                #       answer=======>BY OBJECT REFERENCE VARIABLE

#OBJECT LEVEL:
                #HOW TO ACCESS CLASS LEVEL MEMBERS OR VARIABLES?
                #      answer========>BY USING CLASS NAME
                #HOW TO ACCESS OBJECT LEVEL MEMBERS OR VARIABLES?
                #       answer========>BY USING SELF KEYWORD




class Manohar:
    a=100#class level variable or member
    def manu(self,x,y,z):#INSTANCE METHOD
        print(Manohar.a)#access class level variable in object level by using class name
        print(self.a)#access class level variable in object level by using self argument
        self.b=1#instance variable or object level variables
        self.x=x#instance variable or object level variables
        self.y=y#instance variable or object level variables
        self.z=z#instance variable or object level variables
    
    
    def main(self):#INSTANCE METHOD
        print(self.b)
        
        
        print(self.x)#access object level variables in object level
        print(self.y)#access object level variables in object level
        print(self.z)#access object level variables in object level

    def nook():#CLASS LEVEL METHOD
        m=Manohar()#OBJECT REFERENCE VARIABLE
        m.manu(1,2,3)#passing arguments Through object level methods
        print(m.x)#access object level members in the class level members
        print(m.y)#access object level members in the class level members
        print(m.z)#access object level members in the class level members
        Manohar.e=500000
        print(Manohar.e)
#NOTE1:if we want to access variables outside
#of the class we consider that clouser as CLASS LEVEL

m=Manohar()#OBJECT REFERENCE VARIABLE
m.manu(10,20,30)#passing arguments Through object level methods
m.main()
print(m.x)#access object level members in the class level members
print(Manohar.a)#access class level variable in
                                #class level for this we can using
                                    #class name or object reference variable
print(m.a)#access class level variable in   class level
print(m.b)#access class level variable in   class level
Manohar.nook()

Manohar.d=12345
print(Manohar.d)
print(Manohar.e)


class Manohar:
    a=10
    @classmethod
    def manu(cls):#if your passing any arguments
                                #through this class level method the we have to
                                #mention "@classmethod on the top of that method
        print(cls.a)
print(Manohar.a)
Manohar.manu()


class Test:
    a=10
print(Test.a)

#NOTE2:
#ONE THING WE SHOULD  REMEMBER THAT
class Test:
    def manu(self):
        a=10#we can access with in the method only not out side of the method
        self.b=20# we can access it at anywhere in the program
        print(a)#can access
        print(self.b)
    def hello(self):
        print(self.b)
        #print(a)#can't access
    @staticmethod#OPTIONAL NOT MANDATORY
    def hoe():
       t=Test()
       t.manu()
       print(t.b)
        #print(a)#can't access
    @classmethod# ITS MANDATORY
    def hiii(cls):
        t=Test()
        t.manu()
        print(t.b)
        #print(cls.a)#can't access

t=Test()
t.manu()
t.hello()
Test.hoe()#remember dont take object reference variable for class level members
t.hiii()

class Manu:
    @staticmethod#not mandatory but optional
    def main(x,y):
       print(x+y)
Manu.main(10,20)

class Employee:
    def main(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def how(self):
        print(self.x)
        print(self.y)
        print(self.z)


class Manu:
    def oh(self):
        print(self.x+self.y*self.z)
e=Employee()
e.main(10,20,30)
Manu.oh(e)#if we want to access variables from one class to another class we have to follow this.

class Manu:
    a=20
    @classmethod
    def could(cls,y):#this class method is used
                                   #when you accessing class level
                                    #variables at the time of passing some arguments through method
                                    #at that time @classmethod is mandatory
        print(cls.a+y)

Manu.could(20)
