WIDTH = 700
ROWS = 50

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
