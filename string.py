#Example1
print("Hello")
print('Hello')

#Example2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Example3
a = "Hello"
print(a)

#Example4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Example5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Example6
a = "Hello, World!"
print(a[1])

#Example7
for x in "banana":
  print(x)

#Example8
a = "Hello, World!"
print(len(a))

#Example9
txt = "The best things in life are free!"
print("free" in txt)

#Example10
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Example11
txt = "The best things in life are free!"
print("expensive" not in txt)
      
#Example12

#Example13
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
# type: ignore #Example
#Python - Slicing Strings
#Example1
b = "Hello, World!"
print(b[2:5])

#Example2
b = "Hello, World!"
print(b[:5])

#Example3
b = "Hello, World!"
print(b[2:])

#Example4
b = "Hello, World!"
print(b[-5:-2])
#Python - Modify Strings
#Example1
a = "Hello, World!"
print(a.upper())

#Example2
a = "Hello, World!"
print(a.lower())

#Example3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Example4
a = "Hello, World!"
print(a.replace("H", "J"))

#Example5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
#Example1
a = "Hello"
b = "World"
c = a + b
print(c)

#Example2
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Python - Format - Strings
#Example1
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Example2
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Example3
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Example4
txt = f"The price is {20 * 59} dollars"
print(txt)

#Python - Escape Characters
#Example1
txt = "We are the so-called \"Vikings\" from the north."

#Example2
"""""
Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value	
"""
#Python - String Methods
