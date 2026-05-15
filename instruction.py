import random


print("Welcome to the Area and Perimeter Quiz!")

def instructions():
    print(" Find the Area and the Perimeter!")

def string_checker(question, valid_ans = ('yes', 'no')):

    """Check that users enter a valid word / first
    letter of the word based on the list of options. Defaults to yes / no."""


    error = f"Please enter a valid option from the following list:{valid_ans}"

    while True:

        # Gets user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # checker if user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)



# Instructions
# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (no)
if want_instructions == "yes":
    instructions()

