import string
import pickle
import argparse
import time
from dataclasses import dataclass
from tools import newline, press_enter_key


@dataclass
class FrontData:
    map_instance: None
    export_filename: string
    export_filename_dict: dict
    export_custom_tiles: list

    parameters_generation_ready: int
    export_generation_ready: int

    desired_rooms_x: int
    desired_rooms_y: int
    desired_room_size: int


def menu():
    print("Randomized Dungeon Exporter [CS 361]")

    parser = argparse.ArgumentParser(description='Exporter script.')
    parser.add_argument('--arg1', type=str)
    args = parser.parse_args()
    infinite_sleep = True

    try:
        input_filename = args.arg1
        file = open(str(input_filename) + ".txt", "rb")
        input_object = pickle.load(file)
        file.close()

        newline()
        print("Exporting changes to current file: " + str(input_filename) + ".txt")
        change_tiles(input_object)
        write_to_file(input_filename, input_object)

        file_result = open(str(input_filename) + "_result.txt", "w")
        file_result.write("0")
        file_result.close()

        newline()
        print("Export successful! You may close this terminal window and return to the main application.")
        while infinite_sleep: time.sleep(0.1)
        return

    except pickle.UnpicklingError:
        # Will return the following on main.py:
        # print(str(input_filename) + ".txt loaded, but contains corrupted data. Please try again or regenerate your instance!")
        file_result = open(str(input_filename) + "_result.txt", "w")
        file_result.write("1")
        file_result.close()

        print("ERROR: Please see the main.py window for more information. You may close this terminal window.")
        newline()
        press_enter_key()
        while infinite_sleep: time.sleep(0.1)
        return

    except FileNotFoundError:
        # Will return the following on main.py:
        # print(str(input_filename) + ".txt is not a valid filename. Please try again or regenerate your instance!")
        file_result = open(str(input_filename) + "_result.txt", "w")
        file_result.write("2")
        file_result.close()

        print("ERROR: Please see the main.py window for more information. You may close this terminal window.")
        newline()
        press_enter_key()
        while infinite_sleep: time.sleep(0.1)
        return


def change_tiles(input_object):
    for row in range(0, len(input_object.map_instance.string_data)):
        temp = []
        for tile in range(0, len(input_object.map_instance.string_data[row])):
            if input_object.map_instance.string_data[row][tile] == "#":
                temp.append(input_object.export_custom_tiles[0])
            elif input_object.map_instance.string_data[row][tile] == ".":
                temp.append(input_object.export_custom_tiles[1])
            else:
                continue
        input_object.map_instance.string_data[row] = ''.join(temp)


def write_to_file(input_filename, input_object):
    file = open(input_filename + ".txt", "w")
    for each_line in input_object.map_instance.string_data:
        file.write(each_line + "\n")
    return


if __name__ == "__main__":
    menu()