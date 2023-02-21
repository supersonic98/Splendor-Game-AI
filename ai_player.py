import copy
import time
import random
import math
import numpy as np
MAX_DEPTH = 4
MAX_TIME = 10
C = math.sqrt(2)  # exploration vs exploitation constant in monte carlo

def heuristic(State, Player):
    score = Player.score + (Player.bonus_diamond + Player.bonus_emerald + Player.bonus_onyx + Player.bonus_sapphire + Player.bonus_ruby)/2
    for move in State.getLegalMoves(Player):
        if move[0] == "Buy" or move[0] == "Buy_reserve":
            score += 0.25
            break
    return score

def minmax(State, Player, otherPlayer, turn, depth, alpha = -100000, beta = 10000):
    curPlayer = Player if turn == 0 else otherPlayer
    if(depth >= MAX_DEPTH):
        return heuristic(State, Player), None
    if(State.game_state == 'Terminal'):
        if(State.win(Player)):
            return 100, None
        else:
            return -100, None
    actions = State.getLegalMoves(curPlayer)
    #print("Depth: ", depth, " Scanning ", len(actions), " States.")
    value = -1000 if turn == 0 else 1000
    if len(actions) == 0:
        State.switch_turns()
        return minmax(State, Player, otherPlayer, State.turn, depth + 1, alpha, beta)

    best_action = None
    for action in actions:
        action2 = copy.deepcopy(action)
        playerCopy = curPlayer.copyPlayer()
        action[1] = playerCopy
        NextStates = State.SimulateMove(action)
        #print("Depth: ", depth, " Scanning ", len(NextStates), " Possible resulting states.")
        score = 0
        for NextState in NextStates:
            NextState.switch_turns()
            nextScore, _ = minmax(NextState, playerCopy if turn == 0 else Player, otherPlayer if turn == 0 else playerCopy, NextStates[0].turn, depth + 1, alpha, beta)
            score += nextScore/len(NextStates)
        if turn == 0:
            value = max(value, score)
            if value == score:
                best_action = action2
            if value >= beta:
                break
            alpha = max(alpha, value)
        else:
            value = min(value, score)
            if value == score:
                best_action = action2
            if value <= alpha:
                break
            beta = min(beta, value)
    return value, best_action

# main function for the Monte Carlo Tree Search
def monte_carlo_tree_search(State, Player, otherPlayer):
    time_passed = 0
    root = { "State": State, "Players": [Player, otherPlayer], "Action": None, "Turn": 0, "Children": [] , "Stats": [0, 0], "Root": True, "Parent": None, "RandomIndex": 0}
    while time_passed < MAX_TIME:
        start = time.time()
        leaf = traverse(root)
        if len(leaf["Children"]) != 0:
            print("non-zero child count!")
            return -1
        simulation_result = rollout(leaf)
        backpropagate(leaf, simulation_result)
        end = time.time()
        time_passed += end - start
    selectedChild = best_child(root)
    #print("root Stats:")
    #print(root["Stats"])
    #print(len(root["Children"]))
    #print("Selected Node Stats:")
    #print(selectedChild["Stats"])

    return selectedChild["Action"]

def fullyExpanded(node):
    numberOfStates = 0
    numberOfChildren = len(node["Children"])
    for move in node["State"].getLegalMoves(node["Players"][node["Turn"]]):
        Players = [node["Players"][0].copyPlayer(), node["Players"][1].copyPlayer()]
        move[1] = Players[node["Turn"]]
        nextState = node["State"].SimulateMove(move)
        numberOfStates += len(nextState)
        if numberOfStates > numberOfChildren:
            return False
    return numberOfStates == numberOfChildren



# function for node traversal
def traverse(node):
    while fullyExpanded(node):
        if len(node["State"].getLegalMoves(node["Players"][node["Turn"]])) == 0 or node["State"].game_state == 'Terminal':
           break
        node = best_uct(node)

    # in case no children are present / node is terminal
    return pick_unvisited(node)

def best_uct(node):
    best = 0
    bestnode = None
    for child in node["Children"]:
        if child["Stats"][1] == 0:
            print("Something went wrong")
            print(child["Action"])
            print(child["Stats"])
            print(len(child["Children"]))
        score = child["Stats"][0] / child["Stats"][1]
        score += C*math.sqrt(np.log(node["Stats"][1])/child["Stats"][1])
        if score >= best:
            best = score
            bestnode = child
    return bestnode


def pick_unvisited(node):
    moves = node["State"].getLegalMoves(node["Players"][node["Turn"]])
    if len(moves) == 0 or node["State"].game_state == 'Terminal':
        return node
    random.shuffle(moves)
    for move in moves:
        numberFound = 0
        for child in node["Children"]:
            if child["Action"] == move:
                numberFound += 1
                break
        Players = [node["Players"][0].copyPlayer(), node["Players"][1].copyPlayer()]
        move[1] = Players[node["Turn"]]
        nextState = node["State"].SimulateMove(move)
        if numberFound == len(nextState):
            continue
        nextState[numberFound].switch_turns()
        node1 = { "State": nextState[0], "Players": Players, "Action": move, "Turn": nextState[0].turn, "Children": [] , "Stats": [0, 0], "Root": False, "Parent": node, "RandomIndex": numberFound}
        if node1["State"] == None:
            print ("error")
        node["Children"].append(node1)
        return node1
    print("something went wrong")
    print(len(moves))
    print(len(node["Children"]))



# function for the result of the simulation
def rollout(node):
    while not (len(node["State"].getLegalMoves(node["Players"][node["Turn"]])) == 0 or node["State"].game_state == 'Terminal'):
        node = rollout_policy(node)
    return node["Players"][0].score / 15.0

# function for randomly selecting a child node
def rollout_policy(node):
    moves = node["State"].getLegalMoves(node["Players"][node["Turn"]])
    move = random.randint(0, len(moves)-1)
    Players = [node["Players"][0].copyPlayer(), node["Players"][1].copyPlayer()]
    moves[move][1] = Players[node["Turn"]]
    nextState = node["State"].SimulateMove(moves[move])
    randState = random.randint(0, len(nextState)-1)
    nextState[randState].switch_turns()
    node1 = { "State": nextState[randState], "Players": Players, "Action": moves[move], "Turn": nextState[randState].turn, "Children": [] , "Stats": [0, 0], "Root": False, "Parent": node, "RandomIndex": randState}
    if node1["State"] == None:
        print("error")
    #node["Children"].append(node1)
    return node1



# function for backpropagation
def backpropagate(node, result):
    node["Stats"][0] += result
    node["Stats"][1] += 1
    if node["Root"]:
        return
    backpropagate(node["Parent"], result)

# function for selecting the best child
# node with highest number of visits
def best_child(node):
    best = 0
    bestchild = None
    for child in node["Children"]:
        if child["Stats"][1] > best:
            best = child["Stats"][1]
            bestchild = child
    return bestchild
