#Declaring a Dictionary
D={1:'Arnab,Supratim',2:'31,27',3:'80,85'}

#print Dictionary
print(D)

#Print Individual values of dictionary
print(D[1])
print(D[2])
print(D[3])

#Iterating Through .keys()
keys = D.keys()
for i in keys:
    print(i)

#Iterating Through .keys()
values = D.values()
for i in values:
    print(i)

#Creating Dictionary using lists of Keys and Values dict(zip(keys,values))
keys =['Rahul', 'Rohit', 'Raj']
values =['Roshni', 'Ronika', 'Reshma']
D1=dict(zip(keys,values))
print(D1)

#Entering New values to an existing Dictionary
#suppose we want to enter values in D1 DIctionary
D1['Ranjan']='Ranjana'
print(D1)

#Delete Key from a Dictionary
del D1['Ranjan']
print(D1)

#Multiple values for individual keys





