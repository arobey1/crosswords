from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Mapping
from typing import Sequence
from typing import Tuple
from typing import TypeAlias
from typing import Union


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


@dataclass
class Puzzle:
    BLACK_SQUARE = BlackSquare()

    cells: Mapping[CellIndex, Union[Cell, BlackSquare]]
    clues: Mapping[ClueDirection, Mapping[CellIndex, Clue]]
