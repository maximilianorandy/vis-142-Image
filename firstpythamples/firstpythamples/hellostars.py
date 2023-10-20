#! /usr/bin/python3

you = input("What is your name: ")
print("Hello " + you)
while(True):
    num = input("How many stars do you want: ")
    #print(type(num))
    num = int(num)
    #print(type(num))
    stars = ""
    for count in range(0, num):
        stars = stars + '*'
    print(stars)
    answer = input("Do you want more stars? ")
    if (answer != 'Y' and answer != 'y'):
        break




