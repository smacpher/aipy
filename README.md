# aipy -- Python artificial intelligence wrapper

## Purpose
- The purpose of this package is to provide an easy, black-box API for creating game AIs.

## Background
- The Minimax Algorithm
    - The minimax algorithm is a decision rule used in game AIs for computing the best
possible move a player can take.
    - It is necessary to know 1) how to come up with a list of possible moves given
the current game state and 2) how to calculate a heuristic for any given game
state.

## Usage
- The package can be applied to any 'perfect information' game, or a game in
which it is possible to compute all possible moves.
    -  An example of a perfect information game is tic-tac-toe since it is
    possible to know all of the possible moves based off a given game state.
    -  An example of a game that wouldn't be considered a perfect information
    game would be blackjack, since while it is possible to probabalisticly 
    predict the next move a player might make, it is impossible to be sure
    of any next move based off of a given game state.

## Coverage
- As of now, the package can only use the core minimax algorithm, with no
optimizations. In the future, I plan to add support for alpha-beta pruning
and Monte Carlo tree search (MCTS). Even further down the line, it would
be cool to add machine-learning AI algorithms such as reinforcement
learning, neural-nets, etc.


## API

    import aipy
    import Game
    import Player

    # Define your heuristic function.
    def heuristic(game_state):
        return score(game_state)

    # Define your future state calculating function.
    def next_states(game_state, player):
        possible_states = []
        for state in get_possible_states(game_state, player):
            possible_states.append(state)
        return possible_states


    player = Player()
    # Instantiate a new MinimaxAI object.
    AI = aipy.MinimaxAI(depth=10, heuristic=heuristic, future_state_fn=next_states)
    game_state = Game()


    def main():
        while not is_end_state(game_state):
            if turn == player:
                move = player.get_move()
                new_state = update_game_state(game_state, move)
            elif turn == AI:
                move = AI.get_move()
                new_state = update_game_state(game_state, move)

        print 'GAME OVER!'

    if __name__ == '__main__':
        main()

