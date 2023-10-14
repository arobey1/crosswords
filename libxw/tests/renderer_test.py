import textwrap

from libxw.examples import ExampleLoader
from libxw.render import StringRenderer


def test_string_renderer() -> None:
    renderer = StringRenderer()
    loader = ExampleLoader.default()

    def check_legacy_json(filename: str, expected: str) -> None:
        legacy_json = loader.try_load_legacy_json(filename)
        assert legacy_json is not None
        puzzle = legacy_json.try_to_puzzle()
        assert puzzle is not None
        actual = renderer.render_puzzle(puzzle)
        assert actual == textwrap.dedent(expected).strip()

    check_legacy_json(
        filename="001.json",
        expected="""
            ARAS.SHARP.MOEN
            MENU.IAMSO.ORSO
            ASKS.GLITTERATI
            SALTINES.BARNES
            SWEATER.PERIGEE
            ..DIRT.HELLS...
            TEENY.MOLLY.GAB
            AWES.ZESTY.DORA
            REP.DINES.DEBIT
            ...SAMSA.GETA..
            TOSHIBA.LEMONDE
            IMPALA.SAYONARA
            BARRYBONDS.ANAS
            ENID.WHOLE.TAFT
            RIGS.EMBER.ESTS
        """
    )
