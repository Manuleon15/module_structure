import torch

class Operations:
    def __init__(self):
        pass

    @staticmethod
    def zeros(shape):
        return torch.zeros(shape)

    @staticmethod
    def ones(shape):
        return torch.ones(shape)

    @staticmethod
    def random(shape):
        return torch.rand(shape)

    @staticmethod
    def sum(t1, t2):
        return t1 + t2

    @staticmethod
    def mult(t1, t2):
        return t1 * t2


__all__ = ['Operations']

