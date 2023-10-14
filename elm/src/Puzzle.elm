type CellBackground
  = Gray
  | White

type BlackSquare = ()  -- unit

type Cell
  = BlackSquare
  | WhiteSquare
      { chars: List String
      , isCircled: Bool
      , background: CellBackground
      }

isRebus cell =
  case cell of
    BlackSquare -> False
    WhiteSquare whiteSquare ->
      (List.length whiteSquare.chars) > 1

type alias CellIndex =
  { row: Int
  , col: Int
  }

type ClueDirection = Across | Down

otherDirection clueDirection =
  case ClueDirection of
    Across -> Down
    Down -> Across

Clue = { text: String }

type alias Puzzle =
  { cells: Map CellIndex Cell
  , clues: Map ClueDirection (Map CellIndex Clue)
  }

width : Puzzle -> Int
height : Puzzle -> Int
