from __future__ import annotations

from enum import Enum
from typing import List
from typing import Optional


class GridDirection(Enum):
    ROWS = 0
    COLUMNS = 1


class Grid:
    def __init__(
        self,
        rows: Optional[int] = None,
        columns: Optional[int] = None,
        gap: Optional[int] = None,
        vertical_gap: Optional[int] = None,
        horizontal_gap: Optional[int] = None,
        dominant_direction: Optional[GridDirection] = None,
    ):
        self.rows = rows
        self.columns = columns

        # gap superseeds vertical and horizontal gap
        self.gap = gap
        if gap:
            self.vertical_gap = None
            self.horizontal_gap = None

        self.horizontal_gap = horizontal_gap
        self.vertical_gap = vertical_gap
        self.dominant_direction = dominant_direction

    def lines(self) -> List[str]:
        grid = []

        if self.dominant_direction == GridDirection.COLUMNS:
            if self.columns:
                grid.append(f"grid-columns: {self.columns}")
            if self.rows:
                grid.append(f"grid-rows: {self.rows}")
        else:
            if self.rows:
                grid.append(f"grid-rows: {self.rows}")
            if self.columns:
                grid.append(f"grid-columns: {self.columns}")

        if self.gap is not None:
            grid.append(f"grid-gap: {self.gap}")
        else:
            if self.horizontal_gap is not None:
                grid.append(f"horizontal-gap: {self.horizontal_gap}")

            if self.vertical_gap is not None:
                grid.append(f"vertical-gap: {self.vertical_gap}")

        return grid
