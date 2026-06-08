import random

print("Welcome to the Perimeter Quiz!")
print()
def instructions():
    print()
    print("~~~𝓘𝓝𝓢𝓣𝓡𝓤𝓒𝓣𝓘𝓞𝓝~~~")

    print()

    print(" Find the Perimeter!, try to answer correctly.")

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

# compared user/ computer choice and returns
    # result (correct / wrong)

def quiz_compare(user, comp):
# there is one way to get correct answer
 if user == comp:
     result = "correct"
# if it's not correct then it's wrong
 else:
     result = "wrong"

 return result

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
comp=0
round_correct = 0
round_wrong =0

quiz_list = user=comp
game_history = []

# ask users for number of rounds / quizzes
rounds_wanted = int_check("How many rounds?", "")



# game loop starts here

print("rounds_wanted", rounds_wanted)
while rounds_played < rounds_wanted:

# Rounds headings

    rounds_heading = f"\n💕 Round {rounds_played + 1} of {rounds_wanted}💕"
    print(rounds_heading)





    # Generate random length and width

    length = random.randint(1,20)
    width = random.randint(1,20)

    print("Rectangle dimension:")
    print("Length =", length )
    print("Width =", width)

    # equations


    perimeter = 2 * (length + width)


    user_perimeter = int(input("Enter the Perimeter :"))

    result = quiz_compare(user_perimeter, perimeter)
    print(f" your answer:{user_perimeter} correct answer:{perimeter}, result: {result}")



    # Adjust quiz correct/ wrong counters and add results to quiz history

    if result == "wrong":
       round_wrong +=1
       feedback = "😒😒 wrong. 😒😒"

    else:
        feedback = "🎉🎉 correct. 🎉🎉"


    # Set up round feedback and output it user.
    # Add it to the quiz history list (include the round number)

    round_feedback = f"{user_perimeter} vs {perimeter}, {feedback}"
    history_item = f"Round: {rounds_played + 1} - {result}"
    print(result)
    game_history.append(history_item)

    # end of the round!!
    rounds_played += 1
# Game loop ends here



# Calculate statistics
rounds_won = rounds_played - round_correct - round_wrong
percent_won = rounds_won / rounds_played * 100
percent_lost = round_wrong / rounds_played * 100



# Output Game Statistics
print("📊📊📊 Game Statistics 📊📊📊")
print(f"🎉 correct: {percent_won:.2f}\t"
     f" 😢 wrong: {percent_lost:.2f} \t")


# ask user if they want to see their quiz history and output it if requested.
see_history = string_checker("\nDo you want to see your results? ")
if see_history == "yes":
    for item in game_history:
        print(item)

    print()
    print("Thanks for taking the quiz. ")




