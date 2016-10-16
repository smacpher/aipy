import logging

from aipy.game.core import BaseGame

def get_pretty_game_state(game_state):
    """Outputs a nicely formatted game state"""
    return _prettify_game_state(game_state)


def _prettify_game_state(game_state):
    """Returns a nicely formatted 2-d array for logging purposes"""
    result = ''
    rows = len(game_state)
    for row_index in range(rows):
        row = game_state[row_index]
        result += '\n'
        row_str = map(lambda x: str(x) if x != None else ' ', row)
        result += ' | '.join(row_str)
        result += '\n'
        if row_index < rows - 1:  # don't print on last iteration
            result += '--  --  --'
    return result


class TurnBasedGame(BaseGame):
    """TODO"""

    LOGGER = logging.getLogger(self.__class__.__name__).setLevel(
        logging.INFO,
    )

    def __init__(self, ai, initial_state):
        self.ai = ai

        self._initial_state = initial_state
        self._state = None

    @property
    def state(self):
        if self._state is None:
            self._state = self._initial_state
        return self._state

    def play(self):
        heuristic_fn = self.ai.heuristic_fn

        is_user_turn = self._prompt_user_starts()
        while heuristic_fn(self.state) is None:
            self.LOGGER.info(get_pretty_game_state(self.state))

            if is_user_turn:

    def _prompt_user_starts(self):
        user_starts = None
        while user_starts is None:
            user_input = raw_input('Do you want to go first? (y/n)')\
                .strip()\
                .upper()
            if user_input == 'Y':
                user_starts = True
            elif user_input == 'N':
                user_starts = False
            else:
                self.LOGGER.info('Input (y)es or (n)o.')
        return user_starts
