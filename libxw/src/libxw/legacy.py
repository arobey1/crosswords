import json
import logging
from dataclasses import dataclass
from typing import Dict
from typing import IO
from typing import Optional
from typing import Sequence
from typing import Union

from .puzzle import Cell
from .puzzle import CellBackground
from .puzzle import CellIndex
from .puzzle import Clue
from .puzzle import BlackSquare
from .puzzle import ClueDirection
from .puzzle import Puzzle


# TODO: Configure actual logging...
logger = logging.getLogger(__name__)


@dataclass
class LegacyJson:
    spots: str
    ans: str
    aClues: Sequence[str]
    dClues: Sequence[str]

    @classmethod
    def try_load(cls, buf: IO[str]) -> Optional["LegacyJson"]:
        try:
            # Lots of stuff could go wrong here (EOF, invalid JSON,
            # missing keys, etc.).
            as_dict = json.load(buf)
            return cls(
                spots=as_dict["spots"],
                ans=as_dict["ans"],
                aClues=[clue for clue in as_dict["aClues"]],
                dClues=[clue for clue in as_dict["dClues"]],
            )
        except Exception as e:
            logger.info("Failed to load LegacyJson: %s", e)
            return None

    def try_to_puzzle(self) -> Optional[Puzzle]:
        try:
            # It's possible that even though we got a "valid" LegacyJson
            # object, it might not actually encode a valid Puzzle object.

            cells: Dict[CellIndex, Union[Cell, BlackSquare]] = {}
            clues: Dict[ClueDirection, Dict[CellIndex, Clue]] = {}

            # Assume 15x15.
            across_clue_index = 0
            down_clue_index = 0
            height = 15
            width = 15
            for row in range(height):
                for col in range(width):
                    index = (row, col)

                    # TODO: Handle rebus parsing.
                    offset = row * width + col
                    char = self.ans[offset]

                    if char == ".":
                        cells[index] = Puzzle.BLACK_SQUARE
                    else:
                        cells[index] = Cell(
                            chars=[char],
                            is_circled=False,
                            background=CellBackground.WHITE,
                        )

                    # TODO: Actually detect if we should enter either of these branches.

                    starting_new_across_clue = False
                    if starting_new_across_clue:
                        across_clue = Clue(self.aClues[across_clue_index])
                        across_clue_index += 1
                        across_clues = clues.setdefault(ClueDirection.ACROSS, {})
                        across_clues[index] = across_clue

                    starting_new_down_clue = False
                    if starting_new_down_clue:
                        down_clue = Clue(self.dClues[down_clue_index])
                        down_clue_index += 1
                        down_clues = clues.setdefault(ClueDirection.DOWN, {})
                        down_clues[index] = down_clue

            return Puzzle(cells, clues)

        except Exception as e:
            logger.info("Failed to convert LegacyJson into Puzzle: %s", e)
            return None
