#Example
x = 5
y = "John"
print(x)
print(y)

#Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Example
x = 5
y = "John"
print(type(x))
print(type(y))

#Example
x = "John"
# is the same as
x = 'John'

#Example
a = 4
A = "Sally"
#A will not overwrite a

#Names
#Example
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Multiple Variables
#Example1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example2
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Example1
x = "Python is awesome"
print(x)

#Example2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Example3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Example4
x = 5
y = 10
print(x + y)

#Example5
x = 5
y = "John"
print(x, y)

#Global Variables
#Example1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Example2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Example3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Example4
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
