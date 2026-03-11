
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




# Main routine

# aks the user if they want instructions (check they say yes / no)
want_instructions = yes_no ("Do you want to see the instructions? ")

# Display the instruction if the user wants to see them...
if want_instructions == "yes":
 instructions()

print()
print("Program continues")




