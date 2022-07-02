from libxw.examples import ExampleLoader


def test_clue_indexes_map_to_real_puzzle_cells() -> None:
    loader = ExampleLoader.default()
    legacy_json = loader.try_load_legacy_json("001.json")
    assert legacy_json is not None

    puzzle = legacy_json.try_to_puzzle()
    assert puzzle is not None

    for clues in puzzle.clues.values():
        for index in clues.keys():
            assert index in puzzle.cells
