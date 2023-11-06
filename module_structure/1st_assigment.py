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


op = Operations

op.zeros(2)

op.ones(2)

op.random(3)

tensor1 = torch.tensor([[3, 2, 5], [2, 4, 5]])
tensor2 = torch.tensor([[1, 5, 7], [6, 3, 1]])

op.sum(tensor1, tensor2)

op.mult(tensor1, tensor2)
