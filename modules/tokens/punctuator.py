from enum import Enum, unique
from .token import Token

class Punctuator(Token):
    @property
    def data(self):
        return self.punctuator

    def __init__(self, punctuator, position = None):
        self.punctuator = punctuator
        super().__init__(position)

    @classmethod
    def symbols(cls):
        return {punctuator.value for punctuator in Punc}

class Operator(Punctuator):
    def __repr__(self):
        return f"Operator: {self.punctuator.value}"

    @classmethod
    def symbols(cls):
        return {operator.value for operator in Op}

@unique
class Punc(Enum):
    LPAREN = "("
    RPAREN = ")"
    EOF = ""

@unique
class Op(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    POWER = "**"
    DIVIDE = "/"
    MODULO = "%"
