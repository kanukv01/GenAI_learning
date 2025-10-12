# python features
# 1. Easy to read and write syntax
# 2. Dynamically typed language
# 3. Interpreted language
# 4. Supports multiple programming paradigms (OOP, procedural, functional)
# 5. Extensive standard library
# 6. Cross-platform compatibility
# 7. Large community support
# 8. Automatic memory management (garbage collection)
# 9. Support for modules and packages
# 10. Integration with other languages and tools

#Variables and Data Types
#Constant variables are usually written in uppercase
print("vinay")
a=1
b=2.5
print(a+b)
#commented this line
print(a*b)
name="testing strings"
print(name)
name="vinay"
print(name)
GRAVITY = 9.81
print(GRAVITY)
is_raining = True
print(is_raining)

#Classes and Objects
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())

class myNumber:
    def __init__(self, value):
        self.value = value      

    def add(self, num):
        return self.value + num     
    def multiply(self, num):
        return self.value * num 
    def divide(self, num):
        return self.value / num

my_num = myNumber(10)
print(my_num.add(5))
print(my_num.multiply(2))
print(my_num.divide(2))

class Addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b    
my_add = Addition(5,3)
print(my_add.add())

#Python Arrays implementation
arr = [1, 2, 3, 4, 5]
print(arr)
print(arr[0])
print(arr[1])
arr.append(6)
print(arr)

brands = ["Nike", "Adidas", "Puma"]
print(brands)
brands.append("Reebok")
print(brands)
print(brands[2])
brands.remove("Adidas")
print(brands)