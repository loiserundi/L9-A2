# import necessary packages
from abc import ABC, abstractmethod
# create a base class
class animal(ABC):

    # abstact method
       #should be implemented by all sub-classes
       def move(self):
              pass
       
# sub classes
class Human(animal):
       
       def move(self):
              print("I can walk and run")

class Snake(animal):
       def move(self):
              print("I can crawl")

class Dog(animal):
       
       def move(self):
              print("I can bark")

class Lion(animal):
       
       def move(self):
              print("I can roar")

#Driver Code
R = Human()
R.move()

K= Snake()
K.move()

R =Dog()
R.move()

K = Lion()
K.move()