
# function go here 


def yes_no(question):

    """ checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response =input (question).lower()

        # check the user says yes ? no
        if response == "yes"or response == "y":
            return "yes'"
        elif response == "no"or response == "n":
            return "no"
        elif response == "maybe"or response == "idk":
            return "NUH UH BOY"
        else:
            print("OMG, ENTER YES / NO")

def instructions():...
"""Prints instructions"""

print("""
 *** Instruction***
          
Roll the the dice and try to win!
    """)

def int_check():
    """Checks users enter an integer more than / equal to 20"""

    error = "Please enter an integer more than / equal to 20. "

    while True:
        try:
            response = int(input("what is the game goal "))

            if response  < 20 :
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine

# aks the user if they want instructions (check they say yes / no)
want_instructions = yes_no ("Do you want to see the instructions? ")

# Display the instruction if the user wants to see them...
if want_instructions == "yes":
 instructions()

print()
game_goal = int_check()
print(game_goal)