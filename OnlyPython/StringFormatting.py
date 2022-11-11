'''''''''''''''
#String Formatting

name='Arnab {}'
surname='Das'
newname=name.format(surname)
print(newname)

print(f'Hello! {surname}')

phrase1 = 'Today is last week of {} and {}'
phase2 = phrase1.format('December','Friday')
print(phase2)

'''

#Take user inputs

x=int(input("Enter the number : "))
cube=x*x*x
print(f"The Cube is {cube}" )
print('The Cube is ', cube )




