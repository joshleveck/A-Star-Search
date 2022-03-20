import random
import pygame as py


def nextSquare(grid, curr, directions, conversions):
    r = curr.row
    c = curr.col
    for dire in directions:
        row, col = conversions[dire]
        try:
            if (
                not grid[row + r][col + c].is_visited()
                and row + r > -1
                and col + c > -1
            ):
                random.shuffle(directions)
                return grid[row + r][col + c], dire
        except:
            pass
    return None, None


def createMaze(win, start, grid, directions, conversions, oppositeDir):
    for row in grid:
        for sq in row:
            sq.make_unvisited()
            sq.reset()
            sq.draw(win)

    stack = []
    stack.append(start)

    while len(stack) > 0:
        curr_sq = stack[-1]
        curr_sq.make_visited()
        curr_sq.make_searched()

        next_sq, dire = nextSquare(grid, curr_sq, directions, conversions)
        if next_sq != None:
            stack.append(next_sq)
            next_sq.remove_border(oppositeDir[dire])
            next_sq.draw(win)

            curr_sq.remove_border(dire)
        else:
            stack.pop()
            curr_sq.make_backtracked()

        curr_sq.draw(win)
        py.display.update()
