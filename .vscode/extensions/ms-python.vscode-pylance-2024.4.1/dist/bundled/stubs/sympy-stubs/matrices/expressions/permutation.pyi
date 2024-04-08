from typing import Any, Self
from sympy.core.basic import Basic
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.special import Identity, OneMatrix, ZeroMatrix

class PermutationMatrix(MatrixExpr):
    def __new__(cls, perm) -> Self:
        ...
    
    @property
    def shape(self) -> tuple[Any, Any]:
        ...
    
    @property
    def is_Identity(self):
        ...
    
    def doit(self, **hints) -> Identity | Self:
        ...
    
    _eval_adjoint = ...


class MatrixPermute(MatrixExpr):
    def __new__(cls, mat, perm, axis=...) -> Self:
        ...
    
    def doit(self, deep=..., **hints) -> Basic | PermutationMatrix | ZeroMatrix | OneMatrix | MatrixPermute | Self:
        ...
    
    @property
    def shape(self):
        ...
    


