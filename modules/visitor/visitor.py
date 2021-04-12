from abc import ABC
from abc import abstractmethod
from .symbol_table import SymbolTable
from .helpers import convert_to_camel_case
from ..visitor import errors

class Visitor(ABC):
    vocab_base = None

    def __init__(self, output_stream):
        self.output_stream = output_stream
        self.symbol_table = SymbolTable(type(self))
        self.add_global_vars()

    def traverse(self, root):
        self.output_stream.write(f"{self.visit(root)}\n")

    def visit(self, node):
        method_name = f"visit{convert_to_camel_case(node.__name__)}"
        method = getattr(self, method_name, Visitor.no_visit_method)

        return method(node)

    @classmethod
    def no_visit_method(cls, node):
        raise errors.UndefinedVisitMethod(node)

    def add_global_vars(self):
        self.symbol_table["null"] = ("int", 0, True)
        self.symbol_table["true"] = ("bool", 1, True)
        self.symbol_table["false"] = ("bool", 0, True)

    @abstractmethod
    def visit_eof_node(self, node):
        pass

    @abstractmethod
    def visit_number_node(self, node):
        pass

    @abstractmethod
    def visit_variable_access_node(self, node):
        pass

    @abstractmethod
    def visit_variable_assign_node(self, node):
        pass

    @abstractmethod
    def visit_binary_operation_node(self, node):
        pass

    @abstractmethod
    def visit_unary_operation_node(self, node):
        pass
