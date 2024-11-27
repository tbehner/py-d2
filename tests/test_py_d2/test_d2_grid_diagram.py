# -*- coding: utf-8 -*-
from py_d2.connection import D2Connection
from py_d2.diagram import D2Diagram
from py_d2.shape import D2Shape
from py_d2.style import D2Style
from py_d2.grid import Grid, GridDirection


def test_d2_diagram_with_grid_rows():
    diagram = D2Diagram(grid=Grid(rows=4))
    assert str(diagram) == """grid-rows: 4"""

def test_d2_diagram_with_grid_columns():
    diagram = D2Diagram(grid=Grid(columns=4))
    assert str(diagram) == """grid-columns: 4"""

def test_d2_diagram_with_grid_columns_and_rows():
    diagram = D2Diagram(grid=Grid(rows=4, columns=4))
    assert str(diagram) == "\n".join([
    "grid-rows: 4",
    "grid-columns: 4",
    ])

def test_d2_diagram_with_grid_columns_and_rows_in_specific_orientation():
    dominant_direction = GridDirection.COLUMNS
    diagram = D2Diagram(grid=Grid(rows=4, columns=4, dominant_direction=dominant_direction))

    assert str(diagram) == "\n".join([
    "grid-columns: 4",
    "grid-rows: 4",
    ])

def test_d2_diagram_with_grid_gap():
    diagram = D2Diagram(grid=Grid(gap=0))
    assert str(diagram) == """grid-gap: 0"""

def test_d2_diagram_with_horizontal_gap():
    diagram = D2Diagram(grid=Grid(horizontal_gap=0))
    assert str(diagram) == """horizontal-gap: 0"""

def test_d2_diagram_with_vertical_gap():
    diagram = D2Diagram(grid=Grid(vertical_gap=0))
    assert str(diagram) == """vertical-gap: 0"""

def test_d2_diagram_grid_gab_over_oriented_gap():
    diagram = D2Diagram(grid=Grid(vertical_gap=4, gap=0))
    assert str(diagram) == """grid-gap: 0"""

def test_d2_shape_with_grid():
    shape = D2Shape(name="shape_name", grid=Grid(gap=0))
    assert str(shape) ==  "\n".join([
        "shape_name: {",
        "  grid-gap: 0",
        "}",
        ])
