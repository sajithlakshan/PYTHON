print("__________Create a Class__________")

class MyClass1:
  x = 5

p1 = MyClass1()
print(p1.x)

print("*****************The __init__() Function************")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("+++++++++++ Object Methods ++++++++++++")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

print("==================The self Parameter==============")


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print("@@@@@@@@@@@ Modify Object Properties @@@@@@@@@@@@")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

print(p1.age)

print("]]]]]]]]]]]]]]]]]] The pass Statement [[[[[[[[[[[[[[[[")


class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement
