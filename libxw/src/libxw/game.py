from dataclasses import dataclass
from enum import Enum
from enum import auto
from typing import Sequence
from typing import Mapping

from .puzzle import CellIndex
from .puzzle import ClueDirection
from .puzzle import Puzzle


class CellCheckedness(Enum):
    NOT_CHECKED = auto()
    INCORRECT = auto()
    CORRECT = auto()


@dataclass
class CellState:
    guessed_chars: Sequence[str]
    checkedness: CellCheckedness


@dataclass
class Game:
    puzzle: Puzzle
    cursor: CellIndex
    direction: ClueDirection
    cell_states: Mapping[CellIndex, CellState]

    @classmethod
    def new(cls, puzzle: Puzzle) -> "Game":
        return cls(
            puzzle,
            cursor=(0, 0),
            direction=ClueDirection.ACROSS,
            cell_states={
                index: CellState(
                    guessed_chars=[],
                    checkedness=CellCheckedness.NOT_CHECKED,
                )
                for index, cell in puzzle.cells.items()
                if cell is not Puzzle.BLACK_SQUARE
            },
        )

    def change_direction(self) -> "Game":
        return Game(
            self.puzzle,
            self.cursor,
            self.direction.other(),
            self.cell_states,
        )

    def check_cell(self) -> "Game":
        raise NotImplementedError

    def check_game(self) -> "Game":
        raise NotImplementedError

    def make_guess(self, chars: Sequence[str]) -> "Game":
        return Game(
            self.puzzle,
            self.cursor,  # TODO: Move cursor after a guess!
            self.direction,
            {
                **self.cell_states,
                self.cursor: CellState(
                    guessed_chars=chars,
                    checkedness=CellCheckedness.NOT_CHECKED,
                ),
            },
        )

    def move_left(self) -> "Game":
        raise NotImplementedError

    def move_right(self) -> "Game":
        raise NotImplementedError

    def move_up(self) -> "Game":
        raise NotImplementedError

    def move_down(self) -> "Game":
        raise NotImplementedError
