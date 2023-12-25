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

    # Quitting from program

    file.seek(0)            # locating the pointer at the beginning of the file
    file.truncate()         # clearing everything in the file
    for song in songs:      # loop for adding data
        for index in song:
            file.write(index)
            if index != '' and index != '':
                file.write(',')
        file.write('\n')

    print("{} songs saved to {}".format(len(songs), file.name))
    print("Make some music!")
    file.close()
    quit()

def get_songs_status(no_of_songs,songs):
    """Add the statuses of songs into a list"""

    songs_status = []
    for row in range(no_of_songs):
        record = songs[row][3]
        songs_status.append(record)
    return songs_status

def display_menu():
    """Display menu options, get user input and return the input"""

    print("Menu: \n"
          "D - Display songs\n"
          "A - Add new song\n"
          "C - Complete a song\n"
          "Q - Quit")

def check_blank(input_prompt, error_message):
    """Check if the input user made is blank"""

    text = str(input("{} ".format(input_prompt)))
    while text == '' or text == ' ':    # checking if the input is blank or not
        print(error_message)
        text = str(input("{} ".format(input_prompt)))

    return text

def display_songs(songs):
    """List the songs the program has stored and number of songs required to learn when the user chose 'D' as
    the menu option."""
    count = len(songs)
    songs_learned = 0
    songs_to_learn = 0

    for row in range(count):
        title = songs[row]["title"]
        artist = songs[row]["artist"]
        year = songs[row]["year"]

        if songs[row]["status"] == 'r':
            print("{:2}. * {} - {} ({})".format(row + 1, title, artist, year))
            songs_to_learn += 1
        else:
            print("{:2}. {} - {} ({})".format(row + 1, title, artist, year))
            songs_learned += 1

    print("{} songs learned, {} songs still to learn.".format(songs_learned, songs_to_learn))



