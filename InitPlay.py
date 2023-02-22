# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:19:03 2023

@author: fben-eghan
"""

class BMI:
    def __init__(self, height, mass):
        self.height = height
        self.mass = mass
        self.BMI = height/((0.01*mass)**2)
        
Person1 = BMI(80, 180)
print(r'Height is {}cm and mass is {}kg'.format(Person1.height, Person1.mass))
print(r'Hence BMI is: {}'.format(Person1.BMI)) 



class Person:
    def __init__(self, name, age):
        self.name = name
        if type(age) != int or age < 0:
            raise ValueError("Age must be a positive integer")
        self.age = age

#person1 = Person("John", -30) '''Raises ValueError'''
#person2 = Person("Jane", "Twenty") '''Raises ValueError'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius*2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2
        
circle1 = Circle(5)
print(circle1.diameter)

circle1.radius = 7
print(circle1.diameter)

circle1.diameter = 20
print(circle1.radius)


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car('Toyota', 'Camry', 2022, 'Silver')

class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

class Car(Vehicle):
    def __init__(self, make, model, year, color, doors):
        super().__init__(make, model, year, color)
        self.doors = doors

car1 = Car('Toyota', 'Camry', 2022, 'Silver', 4)

class LazyCar:
    def __init__(self):
        self.make = None
        self.model = None
        self.year = None
        self.color = None

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

car1 = LazyCar()
car1.set_make('Toyota')
car1.set_model('Camry')



import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken: {end - start:.6f} seconds')
        return result
    return wrapper

@timer
def my_function():
    time.sleep(1)

my_function()


import os

class TempFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        os.remove(self.file_name)

with TempFile('temp.txt') as f:
    f.write('Hello, World!')
    
    
#####################    
    
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    @classmethod
    def from_dict(cls, data):
        return cls(data['make'], data['model'], data['year'], data['color'])

car1 = Car('Toyota', 'Camry', 2022, 'Silver')
data = {'make': 'Honda', 'model': 'Civic', 'year': 2021, 'color': 'Red'}
car2 = Car.from_dict(data)


class Car:
    def __init__(self, make, model, year, color):
        if not isinstance(make, str):
            raise TypeError('Make must be a string')
        if not isinstance(model, str):
            raise TypeError('Model must be a string')
        if not isinstance(year, int) or year < 1900:
            raise ValueError('Year must be an integer greater than or equal to 1900')
        if not isinstance(color, str):
            raise TypeError('Color must be a string')
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car('Toyota', 'Camry', 2022, 'Silver')
car2 = Car('Honda', 'Accord', '2021', 'Red')  # raises TypeError


class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 2:
            return 1
        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        return result

fibonacci = Fibonacci()
fibonacci.fib(50)  # computes the 50th Fibonacci number and caches the result in memo dict


class A:
    def __init__(self):
        print('A')

class B(A):d
    def __init__(self):
        print('B')
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super().__init__()

class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()

d = D()  # prints D, B, C, A

