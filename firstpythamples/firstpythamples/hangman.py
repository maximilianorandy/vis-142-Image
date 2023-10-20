#! /usr/bin/python3.4

# hangman - taken from "Programming the Raspberry Pi: getting started with python"
# Simon Monk

import random

# normally, you declare variables and assign them values (instantiate) early
# arachnids
words = ['spider', 'scorpion', 'tarantula', 'solifugid', 'vinegaroon']
lives_remaining = 10
guessed_letters = ''

#main() # can not call this before it is defined, see comments and last
# line of the program for why

# def play: Instead of calling this function "play" (as the book does),
# I am calling it "main".
# Why? Because having a main function where the program starts is
# traditonal in other programming languages. So it lends familiarity as
# "the place where the program starts" (kind of!), and is the nominal 
# first function to be listed in your program. This is not required, 
# it is only a convention and is not necessarily "pythonic"
def main():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("A winner to the core")
            break
        if lives_remaining == 0:
            print("Hanging you, loser")
            print("The word was " + word + ", you thick head.")
            break
    exit()

# Because python is "scripty" the program can be used as if being
# being interpreted one line at a time. In fact, see the python command line.
# But actually, python is also compiled, first into byte code.
# Unlike shell scripts, when there is an error, a python program will exit
# by "throwing and exception".
# Function declarations usually follow variable declarations as a 
# matter of style. In python functions also need to be declared lexically,
# or in order, such that they are declared before they are referenced
# or "called" on.
# This is why the call to main() is the last line of the script. If we 
# called it before "def main()" then we would be calling a function
# before it was declared, which is a syntactical violation in Python
# Howerver, functions are compiled lexically on the first pass.
# So we can use process_guess in the main function,
# because process_guess will be compiled *before* main is called
# at the bottom of the program.

# Bottom line? Functions can call other functions regardless of what
# order they are declared in.
# But functions must be declared before they are executed.
# Best practice: Use an object oriented sytle, or if using a procedural
# style (or mix of procedural and object oriented as is common)
# use the conventions of declaring global variables after your imports,
# followed in whatever order you choose, functions and object declarations.
def pick_a_word():
#    return random.choice(words);
    rand = random.random();
    return words[int(rand * len(words))]

def get_guess(word):
    print_word_with_blanks(word)
    print("Lives remaining " + str(lives_remaining));
    guess = input("Guess a letter or whole word: ")
    return guess;

def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

def whole_word_guess(guess, word):
    global lives_remaining
    if guess == word:
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

def single_letter_guess(guess, word):
    global lives_remaining
    global guessed_letters
    if word.find(guess) == -1:
        # incorrect guess
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True
                

# testing pick_a_word()
#print(pick_a_word());

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # found
            display_word = display_word + letter
        else:
            # not found
            display_word = display_word + '_'
    print(display_word)

# running main()
main()
    

