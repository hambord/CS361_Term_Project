# Extra tools and odd bits to be used throughout main.py and generator.py
import time
from os import system, name


def press_enter_key():
    input("Press Enter to continue...")


def newline():
    print("\n", end='')


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#
#def write_to_file(front_data_inp):
#    file = open(front_data_inp.export_filename + ".txt", "w")
#    for each_line in front_data_inp.map_data.string_data:
#        file.writelines(each_line)
#    return


def a_star(start, goal):
    def distance(a, b):
        ax, ay = a
        bx, by = b
        return abs(ax - bx) + abs(ay - by)

    def reconstruct_path(n):
        if n == start:
            return [n]
        return reconstruct_path(cameFrom[n]) + [n]

    def neighbors(n):
        x, y = n
        return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    closed = set()
    open = set()

    open.add(start)
    cameFrom = {}

    gScore = {start: 0}
    fScore = {start: distance(start, goal)}

    while open:
        current = None
        for each in open:
            if current is None or fScore[each] < fScore[current]:
                current = each

        if current == goal:
            return reconstruct_path(goal)

        open.remove(current)
        closed.add(current)

        for neighbor in neighbors(current):
            if neighbor in closed:
                continue
            g = gScore[current] + 1

            if neighbor not in open or g < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = g
                fScore[neighbor] = gScore[neighbor] + distance(neighbor, goal)
                if neighbor not in open:
                    open.add(neighbor)
    return tuple


# Could do this with a text file, but having it in-application I believe applies usability heuristic number three,
#  as licensing information is readily available at all times to those users who need it or have questions about
#  the legal usability of the software. It is, albeit, very redundant and best served in a text file in this sense.
def license_information():
    print("Copyright 2024 Dan Hambor");
    newline()
    print("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated ")
    print("documentation files (the “Software”), to deal in the Software without restriction, including without limitation")
    print("the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software")
    print("and to permit persons to whom the Software is furnished to do so, subject to the following conditions:")
    newline()
    print("The above copyright notice and this permission notice shall be included in all copies or substantial")
    print("portions of the Software.")
    newline()
    print("THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO")
    print("THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS")
    print("OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR")
    print("OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")


# Keep receiving the appropriate segment until something interrupts it.
# Preferably finding the file in generator and exporter.
def cool_loopy_thing(loop_spinny):
    if loop_spinny == 0:
        print("|", end="\r")
        time.sleep(0.35)
        return 1
    elif loop_spinny == 1:
        print("\\", end="\r")
        time.sleep(0.35)
        return 2
    elif loop_spinny == 2:
        print("-", end="\r")
        time.sleep(0.35)
        return 3
    elif loop_spinny == 3:
        print("/", end="\r")
        time.sleep(0.35)
        return 0
