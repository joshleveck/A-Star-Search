import pygame as py
import random
from constants import (
    WIDTH,
    ROWS,
    COLOURS,
    DIRECTIONS,
    CONVERSIONS,
    OPPOSITE_DIR,
    LINES,
)
import Algorithm.solver as solver
from Helpers import initial, visual, input


def main(width, rows, colours, directions, conversions, oppositeDir, lines):
    win = initial.winInitial(width)
    grid = initial.makeGrid(rows, width, colours, lines, conversions, directions)

    run = True
    drawn = False

    start = grid[0][0]
    end = grid[len(grid) - 1][len(grid) - 1]
    visual.showStartEnd(start, end, win)

    visual.drawGrid(grid, win, colours)
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                drawn = input.keydown(
                    event.key,
                    start,
                    end,
                    win,
                    grid,
                    directions,
                    drawn,
                    conversions,
                    oppositeDir,
                )

    py.quit()


main(WIDTH, ROWS, COLOURS, DIRECTIONS, CONVERSIONS, OPPOSITE_DIR, LINES)
