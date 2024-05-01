#Stack data type

s = ["Ravager",
     "Conqueror",
     "Fury",
     "Savage"]

#removing each element from stack
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.pop()
print(s)

#now adding the elements
x = "Havoc","Enforcer","Conqueror","Rampager"

s.append(list(x))

print(s)

d = []

for i in range (4):
    data = input("enter data:- ")
    d.append(data)

print(d)