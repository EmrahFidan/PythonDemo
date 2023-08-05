from Songs import *

print("""
----------------------------------------------------------------
WELCOME TO THE MUSİC PROGRAM

Processing: 
1- Show me to musics
2- Search for Music
3- Add Music
4- Delete Music
5- Search for Album
6- İncrease Music Time
7- Collect Song Time

Press "q" to exit
----------------------------------------------------------------
""")

music = Music()

while True:
    process = input("process you do: ")

    if (process == "q"):
        print("Checking OUT...")
        time.sleep(1)
        print("Come Again")
        break

    elif(process == "1"):

        music.show_songs()

    elif(process == "2"):

        song_name = input("which song do you want to search ")
        print("Searching for song...")
        time.sleep(1)

        music.search_the_song(song_name)

    elif (process == "3"):

        song_name = input("Song Name: ")
        singer = input("Singer: ")
        album = input("Album: ")
        where_listen = input("Where Listen: ")
        type = input("Type: ")
        song_long = float(input("Song long: "))

        new_song = song(song_name,singer,album,where_listen,type,song_long)
        print("Adding song")
        time.sleep(1)

        music.add_song(new_song)
        print("Song added")

    elif (process == "4"):

        song_name = input("Which song do you want to delete the song ? ")
        print("Searching for song...")
        time.sleep(1)

        solution = input("Are you sure ? (Y/N)")
        if (solution == "Y"):
            print("Deleting Song...")
            time.sleep(1)

            music.delete_song(song_name)
            print("Song Deleted")

    elif (process == "5"):

        album = input("which song do you want to album ")
        print("Searching for album...")
        time.sleep(1)

        music.search_album(album)

    elif (process == "6"):

        name = input("Which song do you want to increase time of the song ? :")
        print("İncreasing Song time...")
        time.sleep(1)

        music.increase_song_long(name)
        print("Song time increased")

    elif (process == "7"):
        print("Press 'q' to exit")

        a = 0
        while True:
            song_name = input("Name :")

            if (song_name == "q"):
                print("Calculating...")
                time.sleep(1)
                print("SUM SONGS LONG= ", a)
                break

            else:
                a = music.collect_song_times(song_name) + a

    else:

        print("illegal process")


