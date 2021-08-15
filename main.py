import pygame as py
import random
import solver

WIDTH = 1000
ROWS = 50
WIN = py.display.set_mode((WIDTH, WIDTH))
py.display.set_caption("Maze")

CONVERSIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
LINES = {
    "U": [[0, 0], [1, 0]],
    "D": [[0, 1], [1, 1]],
    "L": [[0, 0], [0, 1]],
    "R": [[1, 0], [1, 1]],
}
DIRECTIONS = ["U", "D", "L", "R"]
OPPOSITE_DIR = {"U": "D", "D": "U", "L": "R", "R": "L"}

COLOURS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "SEARCHED": (64, 224, 208),
    "BACKTRACKED": (128, 128, 128),
    "START": (52, 235, 113),
    "END": (52, 140, 235),
    "OPEN": (252, 177, 48),
    "CLOSED": (230, 62, 50),
    "PATH": (78, 49, 222),
}


class Sq:
    def __init__(self, row, col, width, colours):
        self.row = row
        self.col = col
        self.colour = colours["WHITE"]
        self.visited = False
        self.x = col * width
        self.y = row * width
        self.width = width
        self.sides = ["U", "D", "L", "R"]
        self.colours = colours

    def make_visited(self):
        self.visited = True

    def make_unvisited(self):
        self.visited = False

    def make_closed(self):
        self.colour = self.colours["CLOSED"]

    def make_open(self):
        self.colour = self.colours["OPEN"]

    def make_path(self):
        self.colour = self.colours["PATH"]

    def make_searched(self):
        self.colour = self.colours["SEARCHED"]

    def make_backtracked(self):
        self.colour = self.colours["BACKTRACKED"]

    def make_start(self):
        self.colour = self.colours["START"]

    def make_end(self):
        self.colour = self.colours["END"]

    def remove_border(self, line):
        self.sides.remove(line)

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.visited

    def reset(self):
        self.colour = self.colours["WHITE"]
        self.sides = ["U", "D", "L", "R"]

    def draw(self, win):
        py.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))
        for side in self.sides:
            start, end = LINES[side]
            py.draw.line(
                win,
                self.colours["BLACK"],
                (self.x + self.width * start[0], self.y + self.width * start[1]),
                (self.x + self.width * end[0], self.y + self.width * end[1]),
                2,
            )

    def neighbours(self, grid):
        neighbours = []
        for dire in DIRECTIONS:
            if dire not in self.sides:
                try:
                    row, col = CONVERSIONS[dire]
                    if row + self.row > -1 and col + self.col > -1:
                        neighbours.append(grid[row + self.row][col + self.col])
                except:
                    pass
        return neighbours


def show_start_end(start, end, win):
    start.make_start()
    end.make_end()
    start.draw(win)
    end.draw(win)
    py.display.update()


def draw_grid(grid, win, colours):
    win.fill(colours["WHITE"])
    for row in grid:
        for sq in row:
            sq.draw(win)
    py.display.update()


def make_grid(rows, width, colours):
    grid = []
    width_of_sq = width // rows
    for i in range(rows):
        row = []
        for j in range(rows):
            sq = Sq(i, j, width_of_sq, colours)
            row.append(sq)
        grid.append(row)
    return grid


def next_square(grid, curr, directions):
    r = curr.row
    c = curr.col
    # Loop through earch direction the next square could be
    for dire in directions:
        row, col = CONVERSIONS[dire]
        # Check if the indexes exists
        try:
            if not grid[row + r][col + c].is_visited() and row + r > -1 and col + c > -1:
                random.shuffle(DIRECTIONS)  # randomize next square selection
                return grid[row + r][col + c], dire
        except:
            pass
    return None, None


def create_maze(win, start, grid, directions):
    # reset maze
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

        next_sq, dire = next_square(grid, curr_sq, directions)
        if next_sq != None:
            stack.append(next_sq)
            next_sq.remove_border(OPPOSITE_DIR[dire])
            next_sq.draw(win)

            curr_sq.remove_border(dire)
        else:
            stack.pop()
            curr_sq.make_backtracked()

        curr_sq.draw(win)
        py.display.update()


def main(win, width, rows, colours, directions):
    print("To draw maze press Space")
    print("To solve maze press S")
    grid = make_grid(rows, width, colours)

    run = True
    drawn = False

    start = grid[0][0]
    end = grid[len(grid) - 1][len(grid) - 1]
    show_start_end(start, end, win)

    draw_grid(grid, win, colours)
    while run:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    create_maze(win, start, grid, directions)
                    show_start_end(start, end, win)
                    drawn = True

                if event.key == py.K_s:
                    if drawn:
                        solver.algorithm(grid, start, end, win)
                        show_start_end(start, end, win)
                        drawn = False

    py.quit()


main(WIN, WIDTH, ROWS, COLOURS, DIRECTIONS)
