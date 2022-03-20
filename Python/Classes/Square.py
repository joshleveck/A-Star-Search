import pygame as py


class Square:
    def __init__(self, row, col, width, colours, lines, conversions, directions):
        self.row = row
        self.col = col
        self.colour = colours["WHITE"]
        self.visited = False
        self.x = col * width
        self.y = row * width
        self.width = width
        self.sides = ["U", "D", "L", "R"]
        self.colours = colours
        self.lines = lines
        self.conversions = conversions
        self.directions = directions

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
            start, end = self.lines[side]
            py.draw.line(
                win,
                self.colours["BLACK"],
                (self.x + self.width * start[0], self.y + self.width * start[1]),
                (self.x + self.width * end[0], self.y + self.width * end[1]),
                2,
            )

    def neighbours(self, grid):
        neighbours = []
        for dire in self.directions:
            if dire not in self.sides:
                try:
                    row, col = self.conversions[dire]
                    if row + self.row > -1 and col + self.col > -1:
                        neighbours.append(grid[row + self.row][col + self.col])
                except:
                    pass
        return neighbours
