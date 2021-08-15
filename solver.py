from queue import PriorityQueue
import pygame as py


def h(p1, p2):  # manhattan dist calc
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, win):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        current.draw(win)
        py.display.update()


def algorithm(grid, start, end, win):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {sq: float("inf") for row in grid for sq in row}
    g_score[start] = 0
    f_score = {sq: float("inf") for row in grid for sq in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, win)
            return True

        neighbours = current.neighbours(grid)
        for neighbour in neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(
                    neighbour.get_pos(), end.get_pos()
                )
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
                    neighbour.draw(win)

        current.make_closed()
        current.draw(win)
        py.display.update()

    return False
