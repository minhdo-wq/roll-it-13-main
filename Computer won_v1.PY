
def initial_points(which_player):...
def make_statement(statement, decoration):
    """Adds emoji / additional charaters to the start and end of headings"""

    ends = decoration * 3
    print(f"\n{ends} {statement} {ends}")

# Main starts here...

# At the start of the game, the computer / user score are both zero 
comp_score = 0
user_score = 0
round_played = 0

game_goal = int(input("Game Goal "))  # should be a function call!

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    #Start of round loop
    # For testing purposes, ask the user what the points for the user / computer were
    # Roll the dice for the user and note if they got a double
    initial_user = initial_points("user")
    initial_comp = initial_points("comp")

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
    loser = "computer"
    comp_points = 0
else:
    winner = "computer"
    loser = "user"
    user_points = 0

round_feedback = f"The {winner} won. The  {loser}'s points have been reset to zero"

# double user points if eligible
if winner == "user" and double_user == "yes":
    user_points = user_points * 2
      
 # Outside rounds loop - Update score with round points, only add points to the score of the end
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to rounds loop)
    print("*** Game stopped Update ***")   # replace with call to statement generator
    print(f"User Score: {user_score} | Computer score {comp_score}")


# end of entire game, output final results
print()
if user_score > comp_score:
    print("!!! No way, you won !!!")  # replace this with statement generator call 
else:
    print("you're unlucky")




