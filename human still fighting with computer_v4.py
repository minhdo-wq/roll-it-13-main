
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
    want_instructions = yes_no ("Are you ready?")
    print(f"oh, so you said {want_instructions}")
    break

print ("no or yes it's not meaning")
print ("i will start the game")
print (" ")
print (" ")
print ("good luck")


def make_statement(statement, decoration):
    """Adds emoji / additional charaters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main routine
make_statement("roll to win","🎲")
make_statement("start the game","***")





import random

def initial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    # Roll the dice for the user note if they got a double
    roll_one = random.randint(1,6)
    roll_two = random.randint(1,6)

    if roll_one == roll_two:
        double = "yes"

    total = roll_one + roll_two
    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t|: Total: {total} ")

    return total, double

def make_statement(statement, decoration):
    """Adds emoji / additional charaters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main starts here...


# Roll the dice for the user and note if they got a double
initial_user = initial_points("User")
initial_comp = initial_points("Comp")

# Retriave user points (first item returned from function)
user_points = initial_user[0]
comp_points = initial_comp[0]

double_user = initial_user[1]

# let the user know if they qualify for double points
if double_user == "yes":
    print("Great news - if you win, you will earn double points!")

# assume user goes firsrt...
first = "user"
second = "Computer"
player_1_points = user_points
player_2_points = comp_points

# if user has fewer points, they start the game
if user_points < comp_points:
    ("You start because your initial roll was less than the computer\n")

# if the user and computer roll equal points, the users is player 1...
elif user_points == comp_points:
    print("The initial rolls were the same, the user starts!")
    
# if the computer has fewer points, switch the computer to 'player 1'
else:
    player_1_points, player_2_points = player_2_points, player_1_points
    first, second = second, first

# loop until we have a winner...
while player_1_points < 20 and player_2_points < 20:
    print()
    input("Press <enter> to continue this round\n")
    
    # first person rolls the dice ans score is updated 
    player_1_roll = random.randint (1,6)
    player_1_points += player_1_roll

    print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

    # if the first person's score is over 20, end the round 
    if player_1_points >= 20:
        break
    
# second person rolls the dice (and score is updated)
    player_2_roll = random.randint (1,6)
    player_2_points += player_2_roll

    print(f"{second}: Rolled a {player_2_roll} - has {player_2_points} points")

    print(f"{first}: {player_1_points} | {second} {player_2_points}")

# end of round

# associate player points with either the user or the computer 
user_points = player_1_points
comp_points = player_2_points

# switch the user and computer points if the computer went first 
if first == "Computer":
    user_points, comp_points = comp_points, user_points

# work out who won...
if user_points > comp_points:
    winner = "user"
else:
    winner = "computer"

round_feedback = f"The {winner} won."

# double user points if eligible
if winner == "user" and double_user == "yes":
    
    user_points = user_points * 2

# Output round results
make_statement("Round Results","📢")
print(f"User Points: {user_points} | Computer Point: {comp_points}")
print(round_feedback)
print()

