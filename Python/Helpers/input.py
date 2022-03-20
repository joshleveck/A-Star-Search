from matplotlib.pyplot import draw
import pygame as py
from Helpers import visual
from Algorithm import solver, mazeDraw


def keydown(key, start, end, win, grid, directions, drawn, conversions, oppositeDir):
    if key == py.K_SPACE:
        mazeDraw.createMaze(win, start, grid, directions, conversions, oppositeDir)
        visual.showStartEnd(start, end, win)
        drawn = True

    if key == py.K_s:
        if drawn:
            solver.algorithm(grid, start, end, win)
            visual.showStartEnd(start, end, win)
            drawn = False
    return drawn
