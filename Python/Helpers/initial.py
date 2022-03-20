import pygame as py
import Classes.Square as Square


def winInitial(width):
    win = py.display.set_mode((width, width))
    py.display.set_caption("Maze")
    return win


def makeGrid(rows, width, colours, lines, conversions, directions):
    grid = []
    widthOfSq = width // rows
    for i in range(rows):
        row = []
        for j in range(rows):
            sq = Square.Square(i, j, widthOfSq, colours, lines, conversions, directions)
            row.append(sq)
        grid.append(row)
    return grid
