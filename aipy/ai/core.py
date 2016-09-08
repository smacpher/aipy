from abc import ABCMeta
from abc import abstractmethod


class BaseAI(object):

    __meta__ = ABCMeta

    @abstractmethod
    def compute(self):
        raise NotImplementedError
