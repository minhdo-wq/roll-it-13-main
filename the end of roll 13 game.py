# function go here 

def yes_no(question):

    """ checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response =input (question).lower()

        # check the user says yes ? no
        if response == "yes"or response == "y":
            return "yes'"
        elif response == "no"or response == "n"or response =="nooo":
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

print ("i will start the game")
print (" ")
print (" ")
print ("no or yes it's not meaning")
print ("good luck")


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

# Main routine
make_statement("roll to win","🎲")
make_statement("start the game","***")

# Main starts here...

# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0
rounds_played = 0

game_history = []

game_goal = int(input("Game Goal: "))    # should be a function call!

#play multiple rounds until a winner has been found 
while comp_score < game_goal and user_score < game_goal:

    rounds_played += 1

    # Start of round loop
    make_statement(f"Round {rounds_played}", "🎲")

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
    while player_1_points < 13 and player_2_points < 13:
        print()
        input("Press <enter> to continue this round\n")
        
        # first person rolls the dice ans score is updated 
        player_1_roll = random.randint (1,6)
        player_1_points += player_1_roll

        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")

        # if the first person's score is over 13, end the round 
        if player_1_points >= 13:
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

    # work out who won and set the loser's points to zero...
    if user_points > comp_points:
        winner = "user"
        loser = "computer"
        comp_points = 0
    else:
        winner = "computer"
        loser = "user"
        user_points = 0

    round_feedback = f"The {winner} won.   The {loser}'s points have been reset to zero"

    # double user points if eligible
    if winner == "user" and double_user == "yes":
        
        user_points = user_points * 2

    # Output round results
    make_statement("Round Results","📢")
    print(f"User Points: {user_points} | Computer Point: {comp_points}")
    print(round_feedback)
    print()

    # Outside rounds loop - Update score with round points, only add points to the score of the round
    comp_score += comp_points
    user_score += user_points

    # Generate round results and add it to the game history list
    game_results = (f"Round {rounds_played}: User points {user_points} | "
                    f"Computer Points {comp_points}, {winner} wins "
                    f"({user_score} | {comp_score})")
    
    game_history.append(game_results)

    # show overall scores (add this to rounds loop)
    print("*** Game Update ***")    # replace with call to statment generator
    print(f"User score: {user_score} | Computer Score {comp_score}")


# end of entire game, output final results

make_statement("Game Over", "🎬")

print()
if user_score > comp_score:
    print()
    make_statement("Human won","💂")

else:
    make_statement("HAHHAHAH LOL","🤪")


while True:

    want_banana =input ("do you want to see game history? ").lower()
    # check the user says yes ? no
    if want_banana == "yes"or want_banana == "y":
        print("you said yes")
        break
    else:
        want_banana == "no"or want_banana == "n"
        print("omg dude, but i sitll show you see!!")
        break

print()
make_statement("game history","📄")

for item in game_history:
    print(item)
        






