"""
Name: Yunsun Park
Date started: 19_Dec_2023
GitHub URL: https://github.com/yunsunpark12/Assignment_1
"""

def main():
    """
    Displays stored songs.
    Calls get_menu function to display the menu options, deciding which function to execute
    and quitting from the program by showing the number of songs saved in the program.
    """

    file = open('songs.csv', 'r+')
    data = file.read()

    print("Song List 1.0 - by Yunsun Park")

    songs = [r.split(",") for r in [r for r in data.split("\n")]]   # converts string into 2D array
    songs.pop(-1)                                                   # removes the empty string caused by \n from the list
    no_of_songs = len(songs)
    print("{} songs loaded.".format(no_of_songs))
    display_menu()

    # Determines which function to execute depending on the choice the user made

    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'D':
            display_songs(songs)
        elif choice == 'A':
            new_song = add_new_song()           # gets new song
            songs.append(new_song)              # appends new songs to songs
        elif choice == 'C':
            check_to_mark_as_completed(songs)
        else:
            print("Invalid menu choice")
        display_menu()
        choice = input('>>> ').upper()


    # Quit from program
    file.seek(0)            # locates the pointer at the beginning of the file
    file.truncate()         # clears everything in the file
    for song in songs:      # loops for adding data
        for index in song:
            file.write(index)
            if index != 'r' and index != 'c':
                file.write(',')
        file.write('\n')

    print("{} songs saved to {}".format(len(songs), file.name))
    print("Make some music!")
    file.close()
    quit()

def get_songs_status(no_of_songs,songs):
    """Adds the statuses of songs into a list"""

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
    while text == '' or text == ' ':    # checks if the input is blank or not
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

def add_new_song():
    """Adding a new song to the program by asking for user input"""

    print("Enter details for a new song.")
    new_song_title = check_blank('Title:', 'Input can not be blank')    # checks if the title is blank or not
    new_artist = check_blank('Artist:', 'Input can not be blank')       # checks if the artist is blank or not

    # Error checking for the 'Year' input
    while True:
        new_year = input('Year: ')
        if not new_year:
            print('Input can not be blank.')
        elif not new_year.isdigit():
            print('Invalid input; enter a valid number.')
        elif int(new_year) <= 0:
            print('Number must be > 0.')
        else:
            break

    status = 'r'  # the newly added song is considered as required to learn ('r')

    song_info = [new_song_title, new_artist, int(new_year), status]  # convert 'new_year' to an integer
    print("{} by {} ({}) added to song list.".format(new_song_title, new_artist, new_year))

    return song_info

def check_to_mark_as_completed(songs):
    """
    Checks if the user input is blank and if the input has alphabets and special characters.
    if the user input is less than or equal to 0,if the user input is greater than the number of songs
    the program has stored, or if the song user chose is already completed or not.
    """

    no_of_songs = len(songs)
    song_statuses = get_song_status(no_of_songs, songs)  # getting the status of songs from get_songs_status function

    if 'r' in song_statuses:                # if one or more songs are still required to learn
        list_songs(songs)
        print("Enter the number of a song to mark as learned")
        learned_song_no = check_blank(">>>", "Invalid input; enter a valid number")
        check = False
        while check is not True:
            try:
                int_completed_song_no = int(completed_song_no)  # converting string to integer
                if completed_song_no <= 0:                  # if the user input is less than or equal to zero
                    print("Number must be > 0")
                    completed_song_no = check_blank(">>>", "Invalid input; enter a valid number")
                elif int_completed_song_no > no_of_songs:   # if the user input is greater than the number of songs the program hold
                    print("Invalid song number")
                    completed_song_no = check_blank(">>>", "Invalid input; enter a valid number")
                elif song_statuses[int_completed_song_no - 1] == 'c':  # if the song user chose is already completed ('c')
                    print(f"You have already learned {songs[int_completed_song_no - 1]}")
                    check = True                            # breaking from while loop
                else:                                       # if the song user chose is not marked as completed
                    check = True                            # breaking from while loop
                    mark_as_completed(int_completed_song_no, songs)  # go to mark_as_competed function to mark the song
            except ValueError:
                print("Invalid input; enter a valid number")
                completed_song_no = check_blank(">>>", "Invalid input; enter a valid number")
    else:  # if all the songs are completed learning
        print('No required songs!')


def mark_as_completed(completed_song_no, songs):
    """Marks the song user chose as completed."""

    print("{} learned!".format(songs[completed_song_no - 1][0]))
    songs[completed_song_no - 1].pop(3)         # removes 'r' from the list
    songs[completed_song_no - 1].append('c')    # replaces 'r' with 'c' to mark as completed


main()



