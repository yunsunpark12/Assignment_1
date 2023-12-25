"""
Name: Yunsun Park
Date started: 19_Dec_2023
GitHub URL: https://github.com/yunsunpark12/Assignment_1
"""

def main():
    """
    To call get_menu function to display the menu options, deciding which function to execute
    and quitting from the program by showing the number of songs saved in the program.
    """

    file = open('songs.csv', 'r+')
    data = file.read()

    print("Song List 1.0 - by Yunsun Park")

    songs = [r.split(",") for r in [r for r in data.split("\n")]]   # converting string into 2D array
    songs.pop(-1)                                                   # removing the empty string caused by \n from the list
    no_of_songs = len(songs)
    print("{} songs loaded.".format(no_of_songs))
    display_menu()

    # Determining which function to execute depending on the choice the user made

    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'D':
            display_songs(songs)
        elif choice == 'A':
            new_song = add_new_song()           # getting new song
            songs.append(new_song)
        elif choice == 'C':
            check_to_mark_as_completed(songs)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input('>>> ').upper()


    print("{} songs saved to {}".format(len(songs), file.name))
    print("Make some music!")
    file.close()
    quit()

def display_menu():
    """Display menu options, get user input and return the input"""

    print("Menu: \n"
          "D - Display songs\n"
          "A - Add new song\n"
          "C - Complete a song\n"
          "Q - Quit")