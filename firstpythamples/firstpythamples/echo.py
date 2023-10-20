# this is a rude program
import random

dismiss = ["Talk to the hand", "I don't care", "Just walk away", "Please, not you.", "Take a long walk off a short pier", "Go away"]

while True:
    word = input("$ ")
    #print(dismiss[1]) # uncomment this line and play with the index
    print(random.choice(dismiss))
    if word == 'quit':
        break
    
