"""
TODO: Actual documentation of intent goes here ...
"""

import argparse
import os
import pdb
import sys
from pathlib import Path

from libxw.legacy import LegacyJson
from libxw.render import StringRenderer


class _HelpFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


def main() -> None:
    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description=__doc__,
        formatter_class=_HelpFormatter,
    )
    # TODO: --log-file
    # TODO: --verbose
    parser.add_argument(
        "--with-pdb",
        action="store_true",
        help="If passed, drop into a debugger immediately after parsing arguments",
    )
    parser.add_argument(
        "--legacy-json",
        type=Path,
        required=True,
    )
    args = parser.parse_args()

    if args.with_pdb:
        pdb.set_trace()

    with open(args.legacy_json) as f:
        json = LegacyJson.try_load(f)
    assert json is not None

    puzzle = json.try_to_puzzle()
    assert puzzle is not None

    renderer = StringRenderer()
    rendered = renderer.render_puzzle(puzzle)

    print(rendered)
