from aipy.base_ai import BaseAi


class MinimaxAi(BaseAi):
    """The MinimaxAi class. Implements the minimax algorithm to compute
    the best possible move.  See the 'compute' method for the actual
    minimax algorithm.
    
    Args:
        depth (int): The maximum recursive depth the minimax algorithm can
            hit before returning a game state's heuristic.
    """
    def __init__(self, heuristic_fn, state_fn, depth=100):
        self.depth = depth

        # Verify attribute types.
        if self._is_function(heuristic_fn):
            self.heuristic_fn = heuristic_fn
        else:
            raise ValueError('heuristic_fn needs to be a function.')

        if self._is_function(state_fn):
            self.state_fn = state_fn
        else:
            raise ValueError('state_fn needs to be a function.')

    def _is_function(self, fn):
        return hasattr(fn, '__call__')

    def compute(self, state):
        """Serves as a wrapper for the core minimax algorithm.  The best move --
        represented as a state -- is stored in the 'choice' variable.  The 
        'choice' variable is accessed in the inner function's scope by using
        the 'nonlocal' identifier.
        """
        depth = self.depth
        choice = None
        state_fn = self.state_fn
        heuristic_fn = self.heuristic_fn

        def _minimax(state, max_player, depth):
            """The core minimax algorithm."""

            # Refer to these variable in the nearest enclosing scope,
            # excluding the global scope.
            nonlocal choice
            nonlocal state_fn
            nonlocal heuristic_fn

            # Base case.
            score = heuristic_fn(state, not max_player)

            # If score is None, then the game is not in an end state. 
            if score or depth == 0:
                return score
            else:
                states = []
                scores = []

                # Populate moves and scores.
                for child_state in state_fn(state, max_player):
                    score = _minimax(child_state, not max_player, depth - 1)
                    scores.append(score)
                    states.append(child_state)

                #  Based on the player, choose the best move.
                if max_player:
                    #  We want to maximize AI's score.
                    max_score_index = scores.index(max(scores))
                    choice = states[max_score_index]
                    return scores[max_score_index]
                else:
                    #  Opponent wants to minimize AI's score.
                    min_score_index = scores.index(min(scores))
                    choice = states[min_score_index]
                    return scores[min_score_index]
        
        # Call minimax to update 'choice'.
        _minimax(state, max_player=True, depth=depth)
        return choice


