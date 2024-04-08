from types import NotImplementedType
from typing import Any, Callable, Generator, Iterator, Literal, Self
from sympy.core.kind import Kind
from sympy.core.basic import Basic
from sympy.core.decorators import sympify_method_args, sympify_return
from sympy.core.evalf import EvalfMixin
from sympy.core.expr import Expr
from sympy.core.logic import And, FuzzyBool, Not, Or
from sympy.core.operations import LatticeOp
from sympy.core.singleton import Singleton
from sympy.logic.boolalg import Boolean, BooleanFalse, BooleanTrue, Xor
from sympy.sets.contains import Contains
from sympy.sets.fancysets import ImageSet
from sympy.sets.powerset import PowerSet
from sympy.utilities.decorator import deprecated

tfn = ...
@sympify_method_args
class Set(Basic, EvalfMixin):
    __slots__ = ...
    is_number = ...
    is_iterable = ...
    is_interval = ...
    is_FiniteSet = ...
    is_Interval = ...
    is_ProductSet = ...
    is_Union = ...
    is_Intersection: FuzzyBool = ...
    is_UniversalSet: FuzzyBool = ...
    is_Complement: FuzzyBool = ...
    is_ComplexRegion = ...
    is_empty: FuzzyBool = ...
    is_finite_set: FuzzyBool = ...
    @property
    def is_EmptySet(self) -> None:
        ...
    
    def union(self, other) -> FiniteSet | Union:
        ...
    
    def intersect(self, other) -> FiniteSet | Intersection | Union | Complement:
        ...
    
    def intersection(self, other) -> FiniteSet | Intersection | Union | Complement:
        ...
    
    def is_disjoint(self, other):
        ...
    
    def isdisjoint(self, other):
        ...
    
    def complement(self, universe) -> Intersection | Complement:
        ...
    
    def symmetric_difference(self, other) -> SymmetricDifference:
        ...
    
    @property
    def inf(self):
        ...
    
    @property
    def sup(self):
        ...
    
    def contains(self, other) -> Contains:
        ...
    
    def is_subset(self, other) -> bool | None:
        ...
    
    def issubset(self, other) -> bool | None:
        ...
    
    def is_proper_subset(self, other) -> bool | None:
        ...
    
    def is_superset(self, other) -> bool | None:
        ...
    
    def issuperset(self, other) -> bool | None:
        ...
    
    def is_proper_superset(self, other) -> bool | None:
        ...
    
    def powerset(self) -> PowerSet:
        ...
    
    @property
    def measure(self):
        ...
    
    @property
    def kind(self) -> SetKind:
        ...
    
    @property
    def boundary(self):
        ...
    
    @property
    def is_open(self) -> FuzzyBool:
        ...
    
    @property
    def is_closed(self):
        ...
    
    @property
    def closure(self):
        ...
    
    @property
    def interior(self):
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __add__(self, other) -> FiniteSet | Union:
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __or__(self, other) -> FiniteSet | Union:
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __and__(self, other) -> FiniteSet | Intersection | Union | Complement:
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __mul__(self, other) -> FiniteSet | ProductSet:
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __xor__(self, other) -> SymmetricDifference:
        ...
    
    @sympify_return([('exp', Expr)], NotImplemented)
    def __pow__(self, exp) -> FiniteSet | ProductSet:
        ...
    
    @sympify_return([('other', 'Set')], NotImplemented)
    def __sub__(self, other) -> Intersection | Complement:
        ...
    
    def __contains__(self, other):
        ...
    


class ProductSet(Set):
    is_ProductSet = ...
    def __new__(cls, *sets, **assumptions) -> FiniteSet | Self:
        ...
    
    @property
    def sets(self) -> tuple[Basic, ...]:
        ...
    
    def flatten(self) -> FiniteSet | ProductSet:
        ...
    
    def as_relational(self, *symbols) -> And:
        ...
    
    @property
    def is_iterable(self) -> bool:
        ...
    
    def __iter__(self) -> Generator[tuple[()] | tuple[Any] | tuple[Any, Any] | Any, Any, None]:
        ...
    
    @property
    def is_empty(self) -> bool | None:
        ...
    
    @property
    def is_finite_set(self) -> bool | None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __bool__(self) -> bool:
        ...
    


class Interval(Set):
    is_Interval = ...
    def __new__(cls, start, end, left_open=..., right_open=...) -> FiniteSet | Self:
        ...
    
    @property
    def start(self) -> Basic:
        ...
    
    @property
    def end(self) -> Basic:
        ...
    
    @property
    def left_open(self) -> Basic:
        ...
    
    @property
    def right_open(self) -> Basic:
        ...
    
    @classmethod
    def open(cls, a, b) -> Self:
        ...
    
    @classmethod
    def Lopen(cls, a, b) -> Self:
        ...
    
    @classmethod
    def Ropen(cls, a, b) -> Self:
        ...
    
    @property
    def left(self) -> Basic:
        ...
    
    @property
    def right(self) -> Basic:
        ...
    
    @property
    def is_empty(self) -> bool | None:
        ...
    
    @property
    def is_finite_set(self):
        ...
    
    def as_relational(self, x) -> And:
        ...
    
    def to_mpi(self, prec=...) -> Any:
        ...
    
    @property
    def is_left_unbounded(self) -> NotImplementedType | bool:
        ...
    
    @property
    def is_right_unbounded(self) -> NotImplementedType | bool:
        ...
    


class Union(Set, LatticeOp):
    is_Union = ...
    @property
    def identity(self):
        ...
    
    @property
    def zero(self):
        ...
    
    def __new__(cls, *args, **kwargs) -> FiniteSet | Union | Self:
        ...
    
    @property
    def args(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def is_empty(self) -> bool | None:
        ...
    
    @property
    def is_finite_set(self) -> bool | None:
        ...
    
    def is_subset(self, other) -> bool | None:
        ...
    
    def as_relational(self, symbol) -> And | Or:
        ...
    
    @property
    def is_iterable(self) -> bool:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    


class Intersection(Set, LatticeOp):
    is_Intersection = ...
    @property
    def identity(self):
        ...
    
    @property
    def zero(self):
        ...
    
    def __new__(cls, *args, **kwargs) -> FiniteSet | Intersection | Union | Complement | Self:
        ...
    
    @property
    def args(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def is_iterable(self) -> bool:
        ...
    
    @property
    def is_finite_set(self) -> Literal[True] | None:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def as_relational(self, symbol) -> And:
        ...
    


class Complement(Set):
    is_Complement = ...
    def __new__(cls, a, b, evaluate=...) -> Intersection | Complement | Self:
        ...
    
    @staticmethod
    def reduce(A, B) -> Intersection | Complement:
        ...
    
    def as_relational(self, symbol) -> And:
        ...
    
    @property
    def is_iterable(self) -> Literal[True] | None:
        ...
    
    @property
    def is_finite_set(self) -> bool | None:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    


class EmptySet(Set, metaclass=Singleton):
    is_empty = ...
    is_finite_set = ...
    is_FiniteSet = ...
    @property
    def is_EmptySet(self) -> Literal[True]:
        ...
    
    def as_relational(self, symbol) -> BooleanFalse:
        ...
    
    def __len__(self) -> Literal[0]:
        ...
    
    def __iter__(self) -> Iterator[Any]:
        ...
    


class UniversalSet(Set, metaclass=Singleton):
    is_UniversalSet = ...
    is_empty = ...
    is_finite_set = ...
    def as_relational(self, symbol) -> BooleanTrue:
        ...
    


class FiniteSet(Set):
    is_FiniteSet = ...
    is_iterable = ...
    is_empty = ...
    is_finite_set = ...
    def __new__(cls, *args, **kwargs) -> Self:
        ...
    
    def __iter__(self) -> Iterator[Basic]:
        ...
    
    @property
    def measure(self) -> Literal[0]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def as_relational(self, symbol) -> Or:
        ...
    
    def compare(self, other) -> int:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    __hash__: Callable[[Basic], Any] = ...


class SymmetricDifference(Set):
    is_SymmetricDifference = ...
    def __new__(cls, a, b, evaluate=...) -> SymmetricDifference | Self:
        ...
    
    @staticmethod
    def reduce(A, B) -> SymmetricDifference:
        ...
    
    def as_relational(self, symbol) -> BooleanFalse | Not | Xor:
        ...
    
    @property
    def is_iterable(self) -> Literal[True] | None:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    


class DisjointUnion(Set):
    def __new__(cls, *sets) -> Self:
        ...
    
    @property
    def sets(self) -> tuple[Basic, ...]:
        ...
    
    @property
    def is_empty(self) -> bool | None:
        ...
    
    @property
    def is_finite_set(self) -> bool | None:
        ...
    
    @property
    def is_iterable(self) -> bool:
        ...
    
    def __iter__(self) -> Generator[Any, Any, None]:
        ...
    
    def __len__(self) -> int:
        ...
    


def imageset(*args) -> Basic | ImageSet | FiniteSet:
    ...

def is_function_invertible_in_set(func, setv) -> Literal[True] | None:
    ...

def simplify_union(args) -> FiniteSet | Union:
    ...

def simplify_intersection(args) -> FiniteSet | Intersection | Union | Complement:
    ...

def set_add(x, y) -> Any | FiniteSet | ImageSet | Union:
    ...

def set_sub(x, y) -> Any | FiniteSet | ImageSet | Union:
    ...

def set_mul(x, y) -> Any | FiniteSet | ImageSet | Union:
    ...

def set_div(x, y) -> Any | FiniteSet | ImageSet | Union:
    ...

def set_pow(x, y) -> Any | FiniteSet | ImageSet | Union:
    ...

def set_function(f, x):
    ...

class SetKind(Kind):
    def __new__(cls, element_kind=...) -> Self:
        ...
    
    def __repr__(self) -> Literal['SetKind()']:
        ...
    


