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
        return torch.add(t1, t2)

    @staticmethod
    def mult(t1, t2):
        return torch.mul(t1, t2)

    @staticmethod
    def cambio_forma(new_shape):
        return torch.ones(new_shape)

    @staticmethod
    def transpose(t, dim1, dim2):
        return torch.transpose(t, dim1, dim2)
