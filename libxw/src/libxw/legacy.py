import json
import logging
from dataclasses import dataclass
from typing import IO
from typing import Optional
from typing import Sequence


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
