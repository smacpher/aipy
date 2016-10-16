from abc import ABCMeta
from abc import abstractmethod

class BasePlayer(object):
    """TODO"""

    __meta__ = ABCMeta

    def __init__(self, get_user_move):
        self.get_user_move = get_user_move

    def update_state(self, state):
        raise NotImplementedError
