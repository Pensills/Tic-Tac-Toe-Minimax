import copy

nodes = 0
winner = 0
team_x = "X"
team_o = "O"

#Prints out the Tic-Tac-Toe GameBoard
def print_gb(gb):
    for item in gb:
        print("\t" + item[0] + "\t|\t" + item[1] + "\t|\t" + item[2] + "\t")
        print("-------------------------------------------------")

#Resets the GameBoard
def reset_gb():
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

#Places the next move made onto the GameBoard
def move(gb, team, row, collumn):
    row_p = 0
    if (row == "A"):
        row_p = 0
    if (row == "B"):
        row_p = 1
    if (row == "C"):
        row_p = 2
    if (gb[row_p][collumn - 1] == "-"):
        gb[row_p][collumn - 1] = team

#Checks the GameBoard to see if either player has won
def is_winner(gb, player):
    if (gb[0][0] == gb[0][1] and gb[0][1] == gb[0][2] and gb[0][0] == player):
        return 1
    if (gb[1][0] == gb[1][1] and gb[1][1] == gb[1][2] and gb[1][0] == player):
        return 1
    if (gb[2][0] == gb[2][1] and gb[2][1] == gb[2][2] and gb[2][0] == player):
        return 1
    if (gb[0][0] == gb[1][0] and gb[1][0] == gb[2][0] and gb[0][0] == player):
        return 1
    if (gb[0][1] == gb[1][1] and gb[1][1] == gb[2][1] and gb[0][1] == player):
        return 1
    if (gb[0][2] == gb[1][2] and gb[1][2] == gb[2][2] and gb[0][2] == player):
        return 1
    if (gb[0][0] == gb[1][1] and gb[1][1] == gb[2][2] and gb[0][0] == player):
        return 1
    if (gb[0][2] == gb[1][1] and gb[1][1] == gb[2][0] and gb[0][2] == player):
        return 1
    return 0

#Search algorithm that starts the search by calling the maxscore function, which is the first half of the recursion
def minimax(gb, player):
    value, action = maxscore(gb, player)
    return (value, action)

#Minscore chooses an empty spot to play a move for the OPPONENT, if all spots on the GameBoard are filled, then the minscore determines if that moves was a winning, losing, or drawing move for the current player
def minscore(gb, player):
    global nodes
    if (is_end_state(gb)):
        return (end_state(gb, player), None)
    if (end_state(gb, team_x) == 1  or end_state(gb, team_o) == 1):
        return (end_state(gb, player), None)
    value = 1
    action = None
    if (player == team_x):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_x, a[0], a[1])
            value_2, a2 = maxscore(gb_copy, team_o)
            if (value_2 < value):
                value = value_2
                if a != None:
                    action = a
        return (value, action)

    if (player == team_o):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_o, a[0], a[1])
            value_2, a2 = maxscore(gb_copy, team_x)
            if (value_2 < value):
                value = value_2
                if a != None:
                    action = a
        return (value, action)
    
    return (None, None)

#Maxscore chooses an empty spot to play a move for the PLAYER, if all spots on the GameBoard are filled, then the minscore determines if that moves was a winning, losing, or drawing move for the current player
def maxscore(gb, player):
    global nodes
    if (is_end_state(gb)):
        return (end_state(gb, player), None)
    if (end_state(gb, team_x) == 1  or end_state(gb, team_o) == 1):
        return (end_state(gb, player), None)
    value = -1
    action = None
    if (player == team_x):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_x, a[0], a[1])
            if (end_state(gb_copy, team_x) == 1):
                return (1, a)
            value_2, a2 = minscore(gb_copy, team_o)
            if (value_2 > value):
                value = value_2
                if a != None:
                    action = a
        return (value, action)

    if (player == team_o):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_o, a[0], a[1])
            if (end_state(gb_copy, team_o) == 1):
                return (1, a)
            value_2, a2 = minscore(gb_copy, team_x)
            if (value_2 > value):
                value = value_2
                if a != None:
                    action = a
        return (value, action)
    
    return None

#Similar to the Minimax function above, however also checks for end states along the way
def alpha_beta_search(gb, player):
    value, action = maxscore_alpha(gb, player, -1, 1)
    return (value, action)

#The Maxscore and Minscore Alpha functions use Alpha Beta Pruning to check if a hypothetical moves brings an end state sooner than filling up the entire board

#i.e.
#  X | X | X
#    | O |
#    | O |
#This board would be considered an end state because player X has won before all board spots are filled
def maxscore_alpha(gb, player, alpha, beta):
    global nodes
    if (is_end_state(gb)):
        return (end_state(gb, player), None)
    if (end_state(gb, team_x) == 1  or end_state(gb, team_o) == 1):
        return (end_state(gb, player), None)
    value = -1
    action = None
    if (player == team_x):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_x, a[0], a[1])
            if (end_state(gb_copy, team_x) == 1):
                return (1, a)
            value_2, a2 = minscore_alpha(gb_copy, team_o, alpha, beta)
            if (value_2 > value):
                value = value_2
                if a != None:
                    action = a
                alpha = max(alpha, value)
            if (value >= beta):
                return(value, action)
        return (value, action)

    if (player == team_o):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_o, a[0], a[1])
            if (end_state(gb_copy, team_o) == 1):
                return (1, a)
            value_2, a2 = minscore_alpha(gb_copy, team_x, alpha, beta)
            if (value_2 > value):
                value = value_2
                if a != None:
                    action = a
                alpha = max(alpha, value)
            if (value >= beta):
                return(value, action)
        return (value, action)

def minscore_alpha(gb, player, alpha, beta):
    global nodes
    if (is_end_state(gb)):
        return (end_state(gb, player), None)
    if (end_state(gb, team_x) == 1  or end_state(gb, team_o) == 1):
        return (end_state(gb, player), None)
    value = 1
    action = None
    if (player == team_x):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_x, a[0], a[1])
            value_2, a2 = maxscore_alpha(gb_copy, team_o, alpha, beta)
            if (value_2 < value):
                value = value_2
                if a != None:
                    action = a
                beta = min(beta, value)
            if (value <= alpha):
                return (value, action)
        return (value, action)

    if (player == team_o):
        states = available_states(gb)
        for a in states:
            nodes += 1
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_o, a[0], a[1])
            value_2, a2 = maxscore_alpha(gb_copy, team_x, alpha, beta)
            if (value_2 < value):
                value = value_2
                if a != None:
                    action = a
                beta = min(beta, value)
            if (value <= alpha):
                return(value, action)
        return (value, action)
    
    return (None, None)

#Returns all empty positions on the GameBoard
def available_states(gb):
    states = []
    count = 0
    for item in gb:
        if (item[0] == '-'):
            if (count == 0):
                states.append(["A", 1])
            if (count == 1):
                states.append(["B", 1])
            if (count == 2):
                states.append(["C", 1])
        if (item[1] == '-'):
            if (count == 0):
                states.append(["A", 2])
            if (count == 1):
                states.append(["B", 2])
            if (count == 2):
                states.append(["C", 2])
        if (item[2] == '-'):
            if (count == 0):
                states.append(["A", 3])
            if (count == 1):
                states.append(["B", 3])
            if (count == 2):
                states.append(["C", 3])
        count += 1

    return states

        
#Checks if the current state of the GameBoard is an end state (i.e. there are no empty spots remainging)
def is_end_state(gb):
    for item in gb:
        if item[0] == '-':
            return False
        if item[1] == '-':
            return False
        if item[2] == '-':
            return False
    return True

#Checks to see if either player has won, or if there was a draw
def end_state(gb, player):
    if (player == team_x):
        if (is_winner(gb, "X")):
            return 1
        if (is_winner(gb, "O")):
            return -1
    if (player == team_o):
        if (is_winner(gb, "X")):
            return -1
        if (is_winner(gb, "O")):
            return 1
    return 0

#Checks all possible moves to see if possible moves result in blocking the opponent from making a winning move on their immediately following turn
def block(gb, player):
    if (player == team_x):
        states = available_states(gb)
        for a in states:
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_o, a[0], a[1])
            if is_winner(gb_copy, team_o):
                return (-1, a)
    if (player == team_o):
        states = available_states(gb)
        for a in states:
            gb_copy = copy.deepcopy(gb)
            move(gb_copy, team_x, a[0], a[1])
            if is_winner(gb_copy, team_x):
                return (-1, a)




#Main function that the user interacts with to play the game
game_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

print("Welcome to Tic-Tac-Toe")
print_gb(game_board)
pruning = 0
while(not winner):
    input_string = input()
    input_list = input_string.split()
    if (input_string == "show"):
        print_gb(game_board)
    elif (input_string == "reset"):
        game_board = reset_gb()
        print_gb(game_board)
    elif (input_list[0] == "move"):
        move(game_board, input_list[1].upper(), input_list[2], int(input_list[3]))
        print_gb(game_board)
    elif (input_list[0] == "quit"):
        break
    elif (input_list[0] == "choose"):
        nodes = 0
        if (pruning):
            gb_copy = copy.deepcopy(game_board)
            value, action = alpha_beta_search(gb_copy, input_list[1])

            if action == None:
                value_1, action_1 = block(game_board, input_list[1])
                move(game_board, input_list[1].upper(), action_1[0], action_1[1])
            else:
                move(game_board, input_list[1].upper(), action[0], action[1])
            
            print_gb(game_board)
            print("Number of nodes searched:")
            print(nodes)
        else:
            gb_copy = copy.deepcopy(game_board)
            value, action = minimax(gb_copy, input_list[1])

            if action == None:
                value_1, action_1 = block(game_board, input_list[1])
                move(game_board, input_list[1].upper(), action_1[0], action_1[1])
            else:
                move(game_board, input_list[1].upper(), action[0], action[1])
            
            print_gb(game_board)
            print("Number of nodes searched:")
            print(nodes)
    elif (input_list[0] == "pruning"):
        if (len(input_list) == 1):
            if (pruning):
                print("Pruning is on")
            else:
                print("Pruning is off")
        else:
            if (input_list[1] == "on"):
                pruning = 1
                print("Pruning is now on")
            if (input_list[1] == "off"):
                pruning = 0
                print("Pruning is now off")

    if (is_end_state(game_board)):
        if (end_state(game_board, "X")):
            print("X is the Winner")
            break
        elif (end_state(game_board, "O")):
            print("O is the Winner")
            break
        else:
            print("It is a draw")
            break
    if (len(input_list) > 1):
        winner = is_winner(game_board, input_list[1])
        if (winner == 1):
                print(input_list[1] + " is the Winner")
                break

    