#Tuples: (), ordered, NOT changeable, duplicate

tuple1=(1, 2, 3)
print(type(tuple1))
print(tuple1)

tuple2=(1, 2, 3, 3, 4, 5, 5)
print(type(tuple2))
print(tuple2)
print(tuple2[0])

for x in tuple2:
    print(x)

setter=[1,2,3]
setter.append(4)
print(setter)