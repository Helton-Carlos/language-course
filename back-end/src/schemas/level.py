from typing import Literal, get_args

Level = Literal["A1", "A2", "B1", "B2", "C1", "C2"]

LEVELS: tuple[Level, ...] = get_args(Level)
