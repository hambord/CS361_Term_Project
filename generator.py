import random
import itertools
from dataclasses import dataclass
from tools import a_star, newline, press_enter_key


# For exporting to both display and game data
@dataclass
class export_data:
    map_data: None
    string_data: list


def generate(rooms_x, rooms_y, cell_size=5):
    # Makes up all the tile data in the generator.
    class Cell(object):
        def __init__(self, rooms_x, rooms_y, input_id):
            self.x_coord = rooms_x
            self.y_coord = rooms_y
            self.cell_id = input_id

            self.connected = False
            self.connectedTo = []
            self.room = None

        def connect(self, other):
            self.connectedTo.append(other)
            other.connectedTo.append(self)
            self.connected = True
            other.connected = True

        def __str__(self):
            return "(%i,%i)" % (self.x_coord, self.y_coord)

    cells = {}
    for y in range(rooms_y):
        for x in range(rooms_x):
            current = Cell(x, y, len(cells))
            cells[(current.x_coord, current.y_coord)] = current

    # Mark random cells as connected.
    current = random.choice(list(cells.values()))
    current.connected = True

    # Operation while cell remains unconnected
    def get_neighbor_cells(cell):
        for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            try:
                yield cells[(cell.x_coord + x, cell.y_coord + y)]
            except KeyError:
                continue

    while True:
        unconnected = list(filter(lambda x: not x.connected, get_neighbor_cells(current)))
        if not unconnected:
            break
        neighbor = random.choice(unconnected)
        current.connect(neighbor)
        current = neighbor

    while True:  # Repeat all this while there are unconnected cells.
        unconnected = list(filter(lambda x: not x.connected, cells.values()))

        if not unconnected:
            break

        possibilities = []
        for cell in filter(lambda x: x.connected, cells.values()):
            neighbors = list(filter(lambda x: not x.connected, get_neighbor_cells(cell)))

            if not neighbors:
                continue

            possibilities.append((cell, neighbors))

        if possibilities:
            cell, neighbors = random.choice(possibilities)
            cell.connect(random.choice(neighbors))

    max_retries = 16
    while max_retries > 0:
        cell = random.choice(list(cells.values()))
        neighbor = random.choice(list(get_neighbor_cells(cell)))

        if cell in neighbor.connectedTo:
            max_retries -= 1
            continue
        cell.connect(neighbor)

    # Create rooms of random shapes here.
    rooms = []
    connections = {}
    for cell in cells.values():
        width = random.randint(3, cell_size-2)
        height = random.randint(3, cell_size-2)

        x = (cell.x_coord * cell_size) + random.randint(1, (cell_size-width)-1)
        y = (cell.y_coord * cell_size) + random.randint(1, (cell_size-height)-1)

        floor_tiles = []
        for i in range(width):
            for j in range(height):
                floor_tiles.append((x + i, y + j))
        cell.room = floor_tiles
        rooms.append(floor_tiles)

    # For each connection between two cells:
    for c in cells.values():
        for other in c.connectedTo:
            connections[tuple(sorted((c.cell_id, other.cell_id)))] = (c.room, other.room)

    for a, b in connections.values():
        # Create a random corridor between the rooms in each cell.
        start = random.choice(a)
        end = random.choice(b)

        corridor = []
        for tile in a_star(start, end):
            if tile not in a and tile not in b:
                corridor.append(tile)
        rooms.append(corridor)

    # create tiles
    final_tiles = {}
    tiles_x = rooms_x * cell_size
    tiles_y = rooms_y * cell_size

    for x in range(tiles_x):
        for y in range(tiles_y):
            final_tiles[(x, y)] = "#"  # Fill the void with tiles per objectives.
    for xy in itertools.chain.from_iterable(rooms):
        final_tiles[xy] = "."

    def get_neighbor_tiles(xy):
        temp_x, temp_y = xy
        for x, y in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
            try:
                yield final_tiles[(temp_x + x, temp_y + y)]
            except KeyError:
                continue

    for xy, tile in final_tiles.items():
        if not tile == "." and "." in get_neighbor_tiles(xy):
            final_tiles[xy] = "#"

    for_export = export_data(map_data=final_tiles, string_data=[])
    for_export.map_data = final_tiles

    for y in range(tiles_y):
        temp_string = ""
        for x in range(tiles_x):
            temp_string += str(final_tiles[(x, y)])
        for_export.string_data.append(temp_string)
    return for_export


# Implementation of usability heuristic seven, as power users are prompted to remove this bit below. It also protects
# low-risk, end-users from awkward operation of the application via renaming or incomplete files.
if __name__ == "__main__":
    print("Randomized Dungeon Generator [CS 361]")
    newline()
    print("ERROR: Please use main.py as the entry point to the generator! Do not run this independently.")
    print("If you are an advanced and/or knowledgeable user, remove or comment out this section of generator.py!")
    newline()
    press_enter_key()
