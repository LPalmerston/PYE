
#This file is about "Strings"
a="Hello World"
print(a)

#Multiline string
b="""Hi, I'm Agustin, 
    and I'm studing for programming"""
print(b)

#Strings are arrays
print(a[0])

for x in a:
    print(x)

for x in "apple":
    print(x)

#Check strings with IN
txt = "The best things in life are free!"
print("free" in txt)

#Check strings with NOT
txt = "The open source is the future!"
print("free" not in txt)

#Modify strings
x="Yellow pear"
y=x.upper()
print(y)
print(x.replace("l", "x"))
print(x.strip("e"))
print(x.replace("e", ""))

x="My name is Agustin and I'm from Resistencia"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x+" "+y)