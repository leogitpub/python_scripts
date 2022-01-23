class Dog:  

      

    # A simple class 

    # attribute 

    attr1 = "mamal"

    attr2 = "dog"

  

    # A sample method   

    def fun(self):  

        attr1 = "omkarrr"
        print("calling static method " + attr1)
        print("I'm a", self.attr1) 

        print("I'm a", self.attr2) 

  
# Driver code 
# Object instantiation 

Rodger = Dog() 

  
# Accessing class attributes 
# and method through objects
def fun():
    print("hello")

print(Rodger.attr1) 
fun()
Rodger.fun()
