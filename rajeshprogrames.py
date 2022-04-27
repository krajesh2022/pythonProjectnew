name = "sar"
name1 = name[0] + "too" + name[2]
print(name1)

#slicing programs
str_alphabets = "1a3b5c7d9e7f5g3h1"
print(str_alphabets[0:2])
print(str_alphabets[:4])
print(str_alphabets[0:-1])
print(str_alphabets[1:4])
#fllowing two commands does same thng ie prints whole numbers string
print(str_alphabets[0:])
print(str_alphabets[::])
#following programme for finding even numbers
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even number".format(num))
else:
   print("{0} is Odd number".format(num))

