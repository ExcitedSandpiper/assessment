import random

print("Welcome to the Area and Perimeter Quiz!")
print()
def instructions():
    print()
    print("~~~𝓘𝓝𝓢𝓣𝓡𝓤𝓒𝓣𝓘𝓞𝓝~~~")

    print()

    print(" Find the Area and the Perimeter!, try to answer correctly.")

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

def int_check(question, exit_code=None):
    """ checks for an integer more than 0(allows <enter>)"""
    while True :
        error = "Please enter an integer that is 1 or more."

        # ask the question
        response = input(question)

        # check for infinite mode / exit code
        if response == exit_code:
            return exit_code

        try:

            # tries to make the response into integer
            response = int(response)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            # if the response is not an integer, displays an error
            print(error)


# Instructions
# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker(" 𝓓𝓸 𝔂𝓸𝓾 𝔀𝓪𝓷𝓽 𝓽𝓸 𝓻𝓮𝓪𝓭 𝓽𝓱𝓮 𝓲𝓷𝓼𝓽𝓻𝓾𝓬𝓽𝓲𝓸𝓷𝓼? ")

# checks users enter yes (y) or no (no)
if want_instructions == "yes":

    instructions()


# main routine

mode = "regular"
rounds_played = 0

# Choose number between two integers
random_integer = random.randint(1,100)

# ask users for number of rounds / quizzes
rounds_wanted = int_check("How many rounds?", "")

# set rounds_wanted to number
rounds_wanted = 5

print("𝓻𝓸𝓾𝓷𝓭𝓼_𝔀𝓪𝓷𝓽𝓮𝓭", rounds_wanted)

