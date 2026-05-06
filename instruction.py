print("Welcome to the Area and Perimeter Quiz!")

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
import random

# Check that users have entered a valid
# option based on a list
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


# compared user / computer choice and returns
# result (win/ lose/ tie)
def rps_compare(user, comp):

   # If the user and computer choice is the same, it's a tie
   if user == comp:
       result = "tie"
   # There are three ways to win
   elif user == "paper" and comp == "rock":
       result = "win"
   elif user == "scissors" and comp == "paper":
       result = "win"
   elif user == "rock" and comp == "scissors":
       result = "win"
   # if it's not a win / tie, then it's a loss
   else:
       result = "lose"

   return result





# main routine

mode = "regular"
rounds_played = 0
rps_list = ("rock", "paper", "scissors", "xxx")

# Ask user for number of rounds / infinite mode
rounds_wanted = int_check("How many questions?<enter for infinite>: ", "")

if rounds_wanted == "":
    # change mode to infinite if users press <enter>
    mode = "infinite"
    print("you chose infinite")


    # set rounds_wanted to number for comparison later.
    rounds_wanted = 5

print("rounds_wanted", rounds_wanted)

# game loop starts here
while rounds_played < rounds_wanted:

# Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n💕 Round {rounds_played + 1} (Infinite Mode)💕 "
    else:
        rounds_heading = f"\n💕 Round {rounds_played + 1} of {rounds_wanted}💕"
    print(rounds_heading)
    # randomly choose from the rps list ( excluding the exit code)
    comp_choice = random.choice(rps_list[:-1])
    print()

    user_choice = string_checker("Choose:", rps_list)
    print("you chose", user_choice)

    if user_choice == "xxx":
        break



    result = rps_compare(user_choice, comp_choice)
    print(f"{user_choice} vs {comp_choice}, {result}")

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        rounds_wanted += 1

    # end of the round!!
    rounds_played += 1


