from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Mapping
from typing import Sequence
from typing import Tuple
from typing import TypeAlias
from typing import Union
from typing import cast


CellIndex: TypeAlias = Tuple[int, int]


class CellBackground(Enum):
    WHITE = auto()
    GRAY = auto()


@dataclass
class Cell:
    chars: Sequence[str]  # Unless this is a rebus, this should be a singleton list.
    is_circled: bool  # Some puzzles have letters inside of circles like ⓣⓗⓘⓢ.
    background: CellBackground

    @property
    def is_rebus(self) -> bool:
        return len(self.chars) > 1


class ClueDirection(Enum):
    ACROSS = auto()
    DOWN = auto()


@dataclass
class Clue:
    text: str


class BlackSquare:
    pass


_POSITIVE_INFINITY = float("inf")
_NEGATIVE_INFINITY = float("-inf")


@dataclass
class Puzzle:
    BLACK_SQUARE = BlackSquare()

    cells: Mapping[CellIndex, Union[Cell, BlackSquare]]
    clues: Mapping[ClueDirection, Mapping[CellIndex, Clue]]

    @property
    def width(self) -> int:
        # TODO: This is *slow*! We should store this data some other way.
        xmin = _POSITIVE_INFINITY
        xmax = _NEGATIVE_INFINITY
        for x, _ in self.cells.keys():
            xmin = min(x, xmin)
            xmax = max(x, xmax)
        dx = xmax - xmin + 1  # Offset by one because we include both endpoints.
        if _NEGATIVE_INFINITY < x < _POSITIVE_INFINITY:
            return cast(int, dx)
        return 0  # There were no cells.

    @property
    def height(self) -> int:
        # TODO: This is *slow*! We should store this data some other way.
        ymin = _POSITIVE_INFINITY
        ymax = _NEGATIVE_INFINITY
        for _, y in self.cells.keys():
            ymin = min(y, ymin)
            ymax = max(y, ymax)
        dx = ymax - ymin + 1  # Offset by one because we include both endpoints.
        if _NEGATIVE_INFINITY < y < _POSITIVE_INFINITY:
            return cast(int, dx)
        return 0  # There were no cells.
