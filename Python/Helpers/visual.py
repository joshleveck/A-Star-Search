import pygame as py


def drawGrid(grid, win, colours):
    win.fill(colours["WHITE"])
    for row in grid:
        for sq in row:
            sq.draw(win)
    py.display.update()

def showStartEnd(start, end, win):
    start.make_start()
    end.make_end()
    start.draw(win)
    end.draw(win)
    py.display.update()
