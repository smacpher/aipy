import copy

from aipy.ai.minimax_ai import MinimaxAI


def get_score(game_state, max_player):
    """Gets the score of the given state based on the given player."""
    if check_win(game_state, max_player):
        return 10
    elif check_win(game_state, not max_player):
        return -10
    elif no_more_moves(game_state):  # tie
        return 0
    else:  # not an end state
        return None


def no_more_moves(game_state):
    rows, cols = len(game_state), len(game_state[0])
    for row in range(rows):
        for col in range(cols):
            if game_state[row][col] is None:
                return False
    return True


def check_win(game_state, player):
    """Checks if the given player has a winning combo."""
    rows, cols = len(game_state), len(game_state[0])
    for row in range(rows):
        for col in range(cols):
            start_row = row
            start_col = col
            if _check_win_from_cell(game_state,
                                   start_row,
                                   start_col,
                                   player):
                return True
    return False


def _check_win_from_cell(game_state, start_row, start_col, player):
    rows, cols = len(game_state), len(game_state[0])
    one_d_dirs = [-1, 0, +1]
    for d_row in one_d_dirs:
        for d_col in one_d_dirs:
            plausible_end_row = start_row + d_row * (rows - 1)
            plausible_end_col = start_col + d_col * (cols - 1)
            # staying in place
            if d_row == 0 and d_col == 0:
                continue
            # index out of range
            elif (plausible_end_row < 0 or plausible_end_row >= rows or
                          plausible_end_col < 0 or plausible_end_col >= cols):
                continue
            # valid direction
            else:
                if (_check_win_from_cell_in_dir(game_state,
                                                start_row,
                                                start_col,
                                                d_row,
                                                d_col,
                                                player)):
                    return True
    return False


def _check_win_from_cell_in_dir(game_state, start_row, start_col, d_row, d_col, player):
    win_length = len(game_state)
    for i in range(win_length):
        row = start_row + i * d_row
        col = start_col + i * d_col
        if game_state[row][col] != player:
            return False
    return True


def _is_valid_move(state, move):
    """
    Returns True if a move (represented by a '(row, col)' tuple) is valid.
    """
    (row, col) = move
    rows, cols = len(state), len(state[0])
    if (row >= rows or row < 0 or
        col >= cols or col < 0 or
        state[row][col] is not None):
        return False
    else:
        return True


def get_possible_states(state, player):
    """Returns an array of all possible game states one move away"""
    rows, cols = len(state), len(state[0])
    possible_game_states = []
    for row in range(rows):
        for col in range(cols):
            if _is_valid_move(state, (row, col)):
                temp_state = copy.deepcopy(state)
                temp_state[row][col] = player
                possible_game_states.append(temp_state)
    return possible_game_states


def pprint_list(a):
    for elem in a:
        print(elem)
        print('\n')


state = [[True, False, True],

         [None, True, None],

         [False, False, None]]

# print(get_score(state, max_player=True))

ai = MinimaxAI(heuristic_fn=get_score,
               state_fn=get_possible_states)

choice = ai.compute(state=state)

pprint_list(choice)

a = [[True, False, True],
     [None, True, None],
     [False, False, True]]


