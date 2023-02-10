# print("hello world!")
# num = 5;
# num2 = 0;
# sum = num + num2
# print(sum)
#If - else statement
# if(sum > 10):
#   print("Hey great!");
# else:
#   print('Ahh!!');
# sentence = 'My name is Sanjit'
#Length of a string
# print(len(sentence))
#slice a string
# trim = slice(0,8)
# print(sentence[trim])
#Slicing Shorthands
# print(sentence[0:6])
# print(sentence[:8])
# print(sentence[4:8:13])
#Reverse a string
# print(sentence[::-1])
#Find Method in String
# x = sentence.find('name')
# print(x)
# print(sentence.find('s',3,10))
#Casting
a = str(3)
b = int(5)
c = float(10)
# print(a)
# print(b)
# print(c)
# print(type(a))
# Many Values to Multiple Variables
x, y,z = 'sanjit','sarvesh','Mohali'
# print(x,y,z)
# One Value to Multiple Variables
a=b=c='Software Developer'
# print(a)
# print(b)
# print(c)
# Unpack a Collection
fruits =['Banana','Apple','Orange']
x,y,z=fruits
# print(x,y,z)
# list
vegetable =['cabbage', 'potato','Tomato','pumkin','shimla mirch','zinger','Pea','apple', 'Apples']
# print(vegetable)
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# print(vegetable[2])
# print(vegetable[2:6])
# print(vegetable[:6])
# print(vegetable[2:])
# print(vegetable[3:5:7])
# print(vegetable)
#Reverse a list
# print(vegetable[::-1])
# print(vegetable[-4:-1])
# Check if Item Exists
# if 'apple' in vegetable:
#   print("Yes")
# Change Item Value
# vegetable[3]="Adrak"
# print(vegetable)
# Change a Range of Item Values
# vegetable[0:2]=["watermelon","Dhania","test"]
# print(vegetable)
# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# vegetable[0:1]=["testing"]
# print(len(vegetable))
# Insert Items
veg = vegetable
# print(veg)
# print(veg.insert(0,"new updated"))
# print(veg)
# Append Items
# veg.append("updhay")
# print(veg)
# Extend List
# fruits.extend(vegetable)
# print(fruits)
# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# tuple
# nonVeg = ("fish","Chicken")
# veg.extend(nonVeg)
print('veg =>',veg)
# Remove Specified Item
# veg.remove("Cabbage")
# Remove Specified Index
# veg.pop(3)
# veg.pop()
# The del keyword also removes the specified index:
# del veg[1]
# Delete the entire list:
# del veg
# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# veg.clear()
# print(veg)
# Loop Through a List
# for x in veg:
#   print(x)
# Loop Through the Index Numbers
# for i in range(len(veg)):
#   print(veg[i])
# Using a While Loop
# i=0
# while i < len(veg):
#   print(veg[i])
#   i = i+1
# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
# [print(x) for x in veg]
# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# newVeg =[]
# for x in veg:
#   if "a" in x:
#     newVeg.append(x)
# print(newVeg)
# With list comprehension you can do all that with only one line of code:
# newVeg = [x for x in veg if "a" in x]
# print(newVeg)
# The condition is like a filter that only accepts the items that valuate to True.
# newVeg =[x for x in veg if x != 'apple']
# print(newVeg)
# Sort List Alphanumerically
# veg.sort()
# Sort Descending
# veg.sort(reverse=True)
# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):
# numbers = [100, 12, 44, 30, 10, 50,80]
# def myFunct(n):
#   return abs(n-30)
# numbers.sort(key = myFunct)
# print(numbers)
# Case Insensitive Sort
# veg.sort(key=str.lower)
# Reverse Order
# veg.reverse()
# Copy a List
# newCopy = veg.copy()
# ake a copy of a list with the list() method:
# newVege = list(veg)
