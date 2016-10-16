from abc import ABCMeta
from abc import abstractmethod


class BaseGame(object):
    """The core Game object."""

    __meta__ = ABCMeta

    @abstractmethod
    def play(self):
        raise NotImplementedError

    def is_end_state(self):
        raise NotImplementedError
