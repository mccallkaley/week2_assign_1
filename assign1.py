#Question 1 
#Cube Number Test... Print out all cubed numbers up to the
#  total value 1000, so if the cubed number is over 1000 break the loop.

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)


#Question 2  #print prime numbers 1 to 100
Number = 1

while(Number <= 100):
    count = 0
    i = 2
    
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1


#Question 3
#Take in a users input for their age,
# if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


age = int(input("How old are you? "))

if age < 18:
    print("kids")
elif age >= 18 and age <= 65:
    print("adults")
elif age > 65: 
    print("seniors")


    



