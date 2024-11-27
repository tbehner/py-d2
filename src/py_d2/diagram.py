# -*- coding: utf-8 -*-
from typing import List
from typing import Optional

from py_d2.connection import D2Connection
from py_d2.grid import Grid
from py_d2.shape import D2Shape


class D2Diagram:
    def __init__(
        self,
        shapes: Optional[List[D2Shape]] = None,
        connections: Optional[List[D2Connection]] = None,
        grid: Optional[Grid] = None,
    ):
        self.shapes = shapes or []
        self.connections = connections or []
        self.grid = grid

    def add_shape(self, shape: D2Shape):
        self.shapes.append(shape)

    def add_connection(self, connection: D2Connection):
        self.connections.append(connection)

    def __repr__(self) -> str:
        out = ""
        if self.grid:
            out = "\n".join(self.grid.lines())

        shapes = [str(shape) for shape in self.shapes]
        connections = [str(connection) for connection in self.connections]

        return out + "\n".join(shapes + connections)
