import os
import string
import pickle
import time
from pathlib import Path
from dataclasses import dataclass
from tools import clear, newline, press_enter_key, license_information, cool_loopy_thing


# For exporting to both display and game data
@dataclass
class export_data:
    map_data: None
    string_data: list


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

    generated: bool
    exported: bool


def main_menu(front_data_inp):
    print("Randomized Dungeon Generator [CS 361]")
    newline()
    # Parameters configuration.
    if front_data_inp.parameters_generation_ready == 0:
        print("Parameters status: NOT CONFIGURED! Generator will not run without configuration!")
    else:
        print("Parameters status: Configured to generate a " +
              str(front_data_inp.desired_rooms_x) + " x " + str(front_data_inp.desired_rooms_y) +
              " map with room size of " + str(front_data_inp.desired_room_size) + " tiles!")

    # Export filenames configuration.
    if front_data_inp.export_generation_ready == 0:
        print("Export status: NOT CONFIGURED! Generator will run, but cannot export, without configuration!")
    else:
        print("Export status: Configured to export as " + str(front_data_inp.export_filename) + ".txt!")
    newline()

    print("1: Generate/regenerate a dungeon instance.")
    print("2: Set parameters for dungeon generation.")
    print("3: Configure exporter for the dungeon instance.")
    print("4: View complete credits and licensing information.")
    print("5: Exit")
    newline()


def option_one(front_data_inp):
    print("Randomized Dungeon Generator [CS 361]")
    print("1. Generate/regenerate a dungeon instance.")
    newline()

    if front_data_inp.parameters_generation_ready == 1:
        print("Parameters have been configured! Ready to generate?")
        print("Enter 'Y' to generate")
        print("Enter 'N' to go back to the main menu.")

        newline()
        inner_loop_input = input("Enter your selection here: ")
        while inner_loop_input is not None:
            if inner_loop_input == "Y" or inner_loop_input == "y":
                file = open("working/current_instance.txt", "wb")
                pickle.dump(front_data_inp, file)
                file.close()

                seeking_segment = 0
                while os.listdir('./working'):
                    print("Now generating the instance! Please wait... ", end='')
                    seeking_segment = cool_loopy_thing(seeking_segment)

                file_current = open("current_instance.txt", "rb")
                front_data_inp = pickle.load(file_current)
                file_current.close()
                os.remove("current_instance.txt")

                if front_data_inp.export_generation_ready == 1:
                    print("Generated successfully! Currently exporting as " + front_data_inp.export_filename + ".txt")
                    print("Export successful! Located in root as " + front_data_inp.export_filename + ".txt")
                    break
                else:
                    newline()
                    print("Generation was successful, but export settings were not configured!")
                    break
            elif inner_loop_input == "N" or inner_loop_input == "n":
                break
            else:
                input("You entered an invalid option! Try again!")
    newline()
    inner_loop_opt = input("View the instance now? Enter 'Y' to view or 'N' to return: ")
    if inner_loop_opt == "Y" or inner_loop_opt == "y":
        clear()
        print("Randomized Dungeon Generator [CS 361]")
        print("1. Generate/regenerate a dungeon instance.")
        newline()
        for each in front_data_inp.map_instance.string_data:
            print(each)
        newline()
        input("Press the Enter key to return to the main menu...")
    else:
        newline()
        input("Press the Enter key to return to the main menu...")
        return


def option_two(front_data_inp):
    configured1 = 0  # flag for rooms_x
    configured2 = 0  # flag for rooms_y
    configured3 = 0  # flag for rooms_size

    print("Randomized Dungeon Generator [CS 361]")
    print("2. Set parameters for dungeon generation.")
    newline()
    print("Please enter each entry as integers between 5 and 25.")
    newline()

    int_check = -1
    while int_check < 1:
        input_number_x = input("Enter the amount of rooms you would like going north to south: ")
        try:
            int(input_number_x)
            front_data_inp.desired_rooms_x = int(input_number_x)
            int_check = 1
            configured1 = 1
        except ValueError:
            print("ERROR: Invalid input made! Please try again!")
            int_check = -1

    int_check = -1
    while int_check < 1:
        input_number_y = input("Enter the amount of rooms you would like going east to west: ")
        try:
            int(input_number_y)
            front_data_inp.desired_rooms_y = int(input_number_y)
            int_check = 1
            configured2 = 1
        except ValueError:
            print("ERROR: Invalid input made! Please try again!")
            int_check = -1

    int_check = -1
    while int_check < 1:
        input_number_rooms = input("Enter the size of each room by number of square tiles: ")
        try:
            int(input_number_rooms)
            front_data_inp.desired_room_size = int(input_number_rooms)
            int_check = 1
            configured3 = 1
        except ValueError:
            print("ERROR: Invalid input made! Please try again!")
            int_check = -1
    newline()

    # A lot of repeated code for now, like everything else, but provides early error-correcting for users by specifying
    #  the specific problem field before allowing generation to commence.
    did_the_bad = 0
    if 5 < int(input_number_x) > 25:
        did_the_bad = 1
        print("Input for of x-column number of rooms is not between [5, 25]! Please review before generating.")
    if 5 < int(input_number_y) > 25:
        did_the_bad = 1
        print("Input for number of y-column number of rooms is not between [5, 25]! Please review before generating.")
    if 5 < int(input_number_rooms) > 25:
        did_the_bad = 1
        print("Input for tile size of each room is not between [5, 25]! Please review before generating.")

    if did_the_bad == 1:
        newline()
        front_data_inp.parameters_generation_ready = 0
        press_enter_key()
        return

    if configured1 == 1 and configured2 == 1 and configured3 == 1:
        front_data_inp.parameters_generation_ready = 1
        print("Configured successfully! ", end='')
        press_enter_key()
        return


def option_three(front_data_inp):
    filename_set_flag = 0

    clear()
    print("Randomized Dungeon Generator [CS 361]")
    print("3. Configure exporter for the dungeon instance.")
    newline()
    print("Current filename selected: " + str(front_data_inp.export_filename))

    filename_dictionary_flag = input("Would you like to view the dictionary of previously used names? "
                                     "Enter 'Y' to view or 'N' to continue: ")
    while filename_dictionary_flag != "N" or filename_dictionary_flag != "Y":
        if filename_dictionary_flag == "Y" or filename_dictionary_flag == "y":
            newline()
            print(front_data_inp.export_filename_dict)
            newline()
            press_enter_key()
            break
        elif filename_dictionary_flag == "N" or filename_dictionary_flag == "n":
            break
        else:
            filename_dictionary_flag = input("ERROR: Invalid character. Enter 'Y' to view or 'N' to continue: ")

    while filename_set_flag == 0:
        clear()
        print("Randomized Dungeon Generator [CS 361]")
        print("3. Configure exporter for the dungeon instance.")
        newline()

        print("NOTE: Your chosen name will be forced into lowercase for compatibility reasons.")
        filename = input("What name would you like for the exported text file containing the generated dungeon?: ")
        filename = filename.lower()
        # If it exists both in dictionary and directory. There is almost definitely a duplicate.
        if filename in front_data_inp.export_filename_dict and os.path.exists(filename):
            newline()
            print("CAUTION! " + str(filename) + " exists both in generated dictionary and directory.")
            filename_set_flag = _option_three_confirmation(front_data_inp, filename)
        # If it exists only in the current directory.
        elif os.path.exists(filename):
            newline()
            print("CAUTION! " + str(filename) + " exists in the generator's directory.")
            filename_set_flag = _option_three_confirmation(front_data_inp, filename)
        # Exists only in generated dictionary. Courtesy warning to check project files for duplicate map.
        elif filename in front_data_inp.export_filename_dict:
            newline()
            print("CAUTION! " + str(filename) + " exists in generated dictionary. "
                                                "Check your individual project files for a duplicate map.")
            filename_set_flag = _option_three_confirmation(front_data_inp, filename)
        # Otherwise, just set the name and move on
        else:
            front_data_inp.export_filename = filename
            _option_three_increment(front_data_inp, filename)
            break
    front_data_inp.export_generation_ready = 1
    clear()
    print("Randomized Dungeon Generator [CS 361]")
    print("3. Configure exporter for the dungeon instance.")
    newline()

    print("Filename successfully set! Would you like to customize the tiles in the exported map?")
    custom_tiles_set = input("Enter Y to customize, or N to keep the default tiles: ")
    if custom_tiles_set == "Y" or custom_tiles_set == "y":
        newline()
        front_data_inp.export_custom_tiles[0] = input("What would you like to change the tile of the walls to: ")
        front_data_inp.export_custom_tiles[1] = input("What would you like to change the tile of the floors to: ")
    else:
        front_data_inp.export_custom_tiles[0] = "#"
        front_data_inp.export_custom_tiles[1] = "."

    newline()

    print("Exporter customization complete! Your instance will export as " + filename + ".txt with '" +
          front_data_inp.export_custom_tiles[0] + "' for walls and '" + front_data_inp.export_custom_tiles[1] +
          "' for floors!")

    press_enter_key()
    return 1


def _option_three_confirmation(front_data_inp, filename):
    confirmation = None
    while confirmation is None:
        confirmation = input("Are you sure? Enter 'Y' to overwrite or 'N' to choose a new name: ")
        if confirmation == "Y" or confirmation == "y":
            front_data_inp.export_filename = filename
            _option_three_increment(front_data_inp, filename)
            return 1
        elif confirmation == "N" or confirmation == "n":
            return 0
        else:
            input("You have entered an invalid character. Enter 'Y' to overwrite or 'N' to choose a new name: ")


def _option_three_increment(front_data_inp, filename):
    if filename not in front_data_inp.export_filename_dict:
        front_data_inp.export_filename_dict[filename] = 1
    else:
        front_data_inp.export_filename_dict[filename] += 1
    return


def option_four():
    print("Randomized Dungeon Generator [CS 361]")
    print("4. View complete credits and licensing information.")
    newline()
    print("Main project by: Dan Hambor")
    print("Additional microservice implementation by: (PARTNER HERE)")
    newline()
    print("This project was made for Professor Letaw's Systems Programming course at Oregon State University, SEC. 400")
    print(
        "Special thanks to u/mizipzor, Kuoi.org, and RogueBasin for the learning material on the algorithm's implementation!")
    newline()
    print("This software is open source and licensed under the MIT License. Would you like to view it now?")

    temp = input("Enter 'Y' to view the entire license or 'N' to go back to the main menu: ")
    if temp == "Y" or temp == "y":
        clear()
        print("Randomized Dungeon Generator [CS 361]")
        print("4. View complete credits and licensing information.")
        newline()
        license_information()
        newline()
        press_enter_key()
        return
    else:
        return


if __name__ == "__main__":
    main_menu_option = ""
    main_menu_data = FrontData(None, None, {}, ["#", "."], 0, 0, 0, 0, 0, 0, 0)

    clear()
    while main_menu_option != "5":
        main_menu(main_menu_data)
        main_menu_option = input("Please select from the menu above: ")
        if main_menu_option == "1":
            clear()
            option_one(main_menu_data)
            clear()
        if main_menu_option == "2":
            clear()
            option_two(main_menu_data)
            clear()
        elif main_menu_option == "3":
            clear()
            option_three(main_menu_data)
            clear()
        elif main_menu_option == "4":
            clear()
            option_four()
            clear()
        elif main_menu_option == "5":
            newline()
            print("Thank you for using the random dungeon generator application! Bye for now!")
            break
        else:
            print("Entered an invalid option! Please select from the menu above: ")
        main_menu_option = ""
