import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .legacy import LegacyJson


logger = logging.getLogger(__name__)


@dataclass
class ExampleLoader:
    root: Path

    @classmethod
    def default(cls) -> "ExampleLoader":
        # Ignore the jankiness here ...
        return cls(root=Path(__file__).parent / "../../examples")

    def try_load_legacy_json(self, filename: str) -> Optional[LegacyJson]:
        path = self.root / filename
        try:
            with open(path) as f:
                return LegacyJson.try_load(f)
        except FileNotFoundError as e:
            logger.info("Failed to load LegacyJson at %s: %s", filename, e)
            return None
