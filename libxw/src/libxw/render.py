from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar

from .puzzle import Cell
from .puzzle import Puzzle


OutputFormat = TypeVar("OutputFormat")


class Renderer(ABC, Generic[OutputFormat]):
    @abstractmethod
    def render_puzzle(self, puzzle: Puzzle) -> OutputFormat:
        ...


class StringRenderer(Renderer[str]):
    def render_puzzle(self, puzzle: Puzzle) -> str:

        # Set up a grid to dump characters into.  This is obviously not our final
        # approach here, but it should let us get some characters on the screen.
        height = puzzle.height
        width = puzzle.width
        grid = [["?" for _ in range(width)] for _ in range(height)]
        for index, cell in puzzle.cells.items():
            row, col = index
            match cell:
                case Puzzle.BLACK_SQUARE:
                    grid[row][col] = "."
                case Cell([char], _, _):
                    grid[row][col] = char
                case Cell(chars, _, _):
                    raise NotImplementedError(chars)  # rebus

        return "\n".join("".join(row) for row in grid)
