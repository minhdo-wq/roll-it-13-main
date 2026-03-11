
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

# Main routine


# testing loop...
while True:
    want_instructions = yes_no ("do you want to see the instructions?")
    print(f"uhmm, you said {want_instructions}")
    want_coffe = yes_no ("Are you sure?")
    print(f"Hehe boy, you said {want_coffe}")
    want_instructions = yes_no ("do you want hear a joke?")
    print(f"oh, so you said {want_instructions}")
    break

print ("no or yes it's not meaning")
print ("nothing")
