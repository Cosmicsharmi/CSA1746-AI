# Evaluation: +10 if X wins, -10 if O wins, else 0
def evaluate(state):
    if state == 0:
        return 10  
    return 0
def game_over(state):
    return state == 0
def get_possible_moves(state):
    return [i for i in [1, 2] if state - i >= 0]
def make_move(state, move, player):
    return state - move
def alpha_beta_pruning(state, depth, alpha, beta, player):
    if depth == 0 or game_over(state):
        return evaluate(state)
    if player == "X":
        best_score = float('-inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "O")
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, "X")
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score
initial_state = 4
depth = 4

result = alpha_beta_pruning(initial_state, depth, float('-inf'), float('inf'), "X")

print("Optimal score for Player X starting at state 4:", result)
