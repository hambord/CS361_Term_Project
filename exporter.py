import string
import pickle
from dataclasses import dataclass
from tools import clear, newline, press_enter_key


@dataclass
class FrontData:
    map_data: None
    export_filename: string
    export_filename_dict: dict

    parameters_generation_ready: int
    export_generation_ready: int

    desired_rooms_x: int
    desired_rooms_y: int
    desired_room_size: int


def menu():
    clear()
    print("Randomized Dungeon Generator Exporter [CS 361]")
    newline()
    input_filename = input("What is the name of the text file you wish to process?: ")

    try:
        file = open(str(input_filename) + ".txt", "rb")
        input_object = pickle.load(file)
        file.close()
        input_change_tiles = input("Would you like to customize the tiles of the map? Enter Y to configure: ")

        if input_change_tiles == "Y" or input_change_tiles == "y":
            clear()
            print("Randomized Dungeon Generator Exporter [CS 361]")
            newline()
            change_tiles(input_object.map_data)

        newline()
        print("Exporting changes to current file: " + str(input_filename) + ".txt")
        write_to_file(input_filename, input_object)
        newline()
        print("Export successful! You may exit this application now!")
        press_enter_key()
        clear()
        return

    except pickle.UnpicklingError:
        print(str(input_filename) + ".txt loaded, but contains corrupted data. Please try again or regenerate your instance!")
        newline()
        press_enter_key()
        clear()
        return

    except FileNotFoundError:
        print(str(input_filename) + ".txt is not a valid filename. Please try again or regenerate your instance!")
        newline()
        press_enter_key()
        clear()
        return


def change_tiles(input_object):
    replacement_tiles = ["", ""]
    replacement_tiles[0] = input("What would you like to change the tile of the walls to?: ")
    replacement_tiles[1] = input("What would you like to change the tile of the floors to?: ")

    for row in range(0, len(input_object.string_data)):
        temp = []
        for tile in range(0, len(input_object.string_data[row])):
            if input_object.string_data[row][tile] == "#":
                temp.append(replacement_tiles[0])
            elif input_object.string_data[row][tile] == ".":
                temp.append(replacement_tiles[1])
            else:
                continue
        input_object.string_data[row] = ''.join(temp)


def write_to_file(input_filename, input_object):
    file = open(input_filename + ".txt", "w")
    for each_line in input_object.map_data.string_data:
        file.write(each_line + "\n")
    return


if __name__ == "__main__":
    menu()