#!/usr/bin/python
# -*- coding: utf-8 -*-
# === funcs in explain =======================================================#


def requestInteger(message):
    """
    message: the message to display to the user in the dialog
    returns: the number as an integer

    This will allow the user to input an integer.
    The dialog will keep appearing until a valid integer is entered.
    The dialog box has a Cancel button. If the user clicks it, the function will return None.
    The dialog box also has a Stop button, which stops the program.
    (You can use this if you accidentally make an infinite loop.)

    Example:
    def printAge():
    age = requestInteger("How old are you?")
    print "You are " + str(age) + " years old!"

    This will open a dialog box asking the user's age and then print it back out.
    """


def requestIntegerInRange(message, min, max):
    """
    message: the message to display to the user in the dialog
    min: the smallest integer allowed
    max: the largest integer allowed

    Opens a message dialog to the user asking for an integer between a minimum and maximum (inclusive).
    The dialog will keep appearing until a valid integer is entered.
    The dialog box has a Cancel button.
    If the user clicks it, the function will return None.
    The dialog box also has a Stop button, which stops the program.
    (You can use this if you accidentally make an infinite loop.)

    Example:
    def guessingGame():
        import random
        r = random.randint(1,10)
        guess = requestIntegerInRange("Guess a number 1-10", 1, 10)
        if guess == r:
            print "You win!"
        else:
            print "You lose!"

    This will open a dialog box asking the user to pick a number from 1 to 10.
    If the chosen number is the same as the randomly generated one, you win)
    """


def requestNumber(message):
    """
    message: the message to display to the user in the dialog
    returns: the number as a double

    This will allow the user to input a number with a decimal.
    The dialog will keep appearing until a valid number is entered.
    The dialog box has a Cancel button.
    If the user clicks it, the function will return None.
    The dialog box also has a Stop button, which stops the program.
    (You can use this if you accidentally make an infinite loop.)

    Example:
    def printHeight():
        dec = requestNumber("How many feet tall are you?")
        feet = floor(dec)
        inch = (dec - feet)*12
        print "You are " + str(feet) + " feet and " + str(inch) + " inches tall."

    This will open a dialog box asking the user's height in feet (in decimal form)
    and then print out the equivalent number of feet and inches.
    """


def requestString(message):
    """
    message: the message to display to the user in the dialog
    returns: the input string This will allow the user to input any string.

    The dialog box has a Cancel button. If the user clicks it, the function will return None.
    The dialog box also has a Stop button, which stops the program.
    (You can use this if you accidentally make an infinite loop.)

    Example:
    def printName():
        name = requestString("What is your name?")
        print "Hello " + name + "!"
    This will open a dialog box asking the user's name and then print it back out.
    """


def printNow(output):
    """
    output: What we want to print
    Prints the specified output to the JES command area.
    In older versions of JES, if you wanted output to appear before the program finished running,
    you had to use printNow.
    But in JES 5 and later, printNow is no longer necessary
    – you can just use the normal print statement,
    and the message will appear as soon as possible. Example:

    import time

    def lineByLine():
        for x in range(1, 11, 2):
        printNow(x)
        time.sleep(0.5)
        print x + 1
        time.sleep(0.5)

    This will print the numbers 1 to 10 in order, with a half-second wait in between each.
    (So, you can see that printNow and print do the same thing now.)
    """


def showInformation(message):
    """
    message: the message to show to the user
    Opens a message dialog to the user showing information.
    """


# TODO -- functions that return user input (not shimmed)
'''
requestInteger
requestIntegerInRange
showWarning
showInformation
showError
printNow
'''

# === entities in globals but not explain ====================================#
