print("hello world!")
num = 5;
num2 = 0;
sum = num + num2
print(sum)
#If - else statement
if(sum > 10):
  print("Hey great!");
else:
  print('Ahh!!');
sentence = 'My name is Sanjit'
#Length of a string
print(len(sentence))
#slice a string
trim = slice(0,8)
print(sentence[trim])
#Slicing Shorthands
print(sentence[0:6])
print(sentence[:8])
print(sentence[4:8:13])
#Reverse a string
print(sentence[::-1])
#Find Method in String
x = sentence.find('name')
print(x)
print(sentence.find('s',3,10))
#Casting
a = str(3)
b = int(5)
c = float(10)
print(a)
print(b)
print(c)
print(type(a))
# Many Values to Multiple Variables
x, y,z = 'sanjit','sarvesh','Mohali'
print(x,y,z)
# One Value to Multiple Variables
a=b=c='Software Developer'
print(a)
print(b)
print(c)
# Unpack a Collection
fruits =['Banana','Apple','Orange']
x,y,z=fruits
print(x,y,z)