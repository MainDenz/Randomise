import random

#A variable to save the number of people
number = int(input("How many people?" ))

#Emptylist to save the names
names_input=[]

#for loop to save the names
while number==0:
    print("Invalid Choice")
    break
if number>0:
    print("Type your names")
for i in range(number):
    names_input.append(input())

#A variable to save a random name
random_name = random.choice(names_input)

print("The random person is ", random_name)
#print(names_input)