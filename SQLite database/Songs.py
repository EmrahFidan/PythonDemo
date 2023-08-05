import sqlite3

import time

class song():

    def __init__(self,song_name,singer,album,where_listen,type,song_long):
        self.song_name = song_name
        self.singer = singer
        self.album = album
        self.where_listen = where_listen
        self.type = type
        self.song_long = song_long

    def __str__(self):
        return "Song Name : {}\nSinger : {}\nAlbum : {}\nWhere Can Listen : {}\nType : {}\nSong Long : {}\n".format(self.song_name,self.singer,self.album,self.where_listen,self.type,self.song_long)

class Music():
    def __init__(self):

        self.create_link()

    def create_link(self):

        self.link = sqlite3.connect("music.db")
        self.cursor = self.link.cursor()

        command = "Create Table If not exists Songs (song_name TEXT,singer TEXT,album TEXT,where_listen TEXT,type TEXT,song_long FLOAT)"
        self.cursor.execute(command)
        self.link.commit()

    def disconnect(self):

        self.link.close()

    def show_songs(self):

        command = "Select * From Songs"
        self.cursor.execute(command)

        music = self.cursor.fetchall()

        if(len(music) == 0):
            print("Song doesn't exists")
        else:
            for demet in music:
                data = song(demet[0],demet[1],demet[2],demet[3],demet[4],demet[5])
                print(data)

    def search_the_song(self,song_name):

        command = "Select * From Songs where song_name = ?"
        self.cursor.execute(command,(song_name,))

        music = self.cursor.fetchall()

        if (len(music) == 0):
            print("This song doesn't exist")
        else:
            for demet in music:
                data = song(demet[0], demet[1], demet[2], demet[3], demet[4], demet[5])
                print(data)

    def add_song(self,song):

        command ="INSERT INTO Songs VALUES(?,?,?,?,?,?)"
        self.cursor.execute(command,(song.song_name,song.singer,song.album,song.where_listen,song.type,song.song_long))

        self.link.commit()

    def delete_song(self,song_name):

        command = "Delete From Songs where song_name = ?"
        self.cursor.execute(command,(song_name,))
        self.link.commit()

    def search_album(self,album):

        command = "Select * From Songs where album = ?"
        self.cursor.execute(command, (album,))

        music = self.cursor.fetchall()

        if (len(music) == 0):
            print("This album doesn't exist")
        else:
            for demet in music:
                    data = song(demet[0], demet[1], demet[2], demet[3], demet[4], demet[5])
                    print(data)
                    print("\n")

    def increase_song_long(self,song_name):

        command = "Select * From Songs where song_name = ?"
        self.cursor.execute(command,(song_name,))

        music = self.cursor.fetchall()

        if (len(music) == 0):
            print("This song don't exist")
        else:
            song_long = music[0][5]
            song_long += 0.10

            command2 = "Update songs set song_long = ? where song_name = ?"
            self.cursor.execute(command2,(song_long,song_name))

            self.link.commit()

    def collect_song_times(self,song_name):

        command = "Select * From songs where song_name = ?"
        self.cursor.execute(command, (song_name,))

        liste = self.cursor.fetchall()

        if (len(liste) == 0):
            print("This product don't exist")
        else:
            song_long = liste[0][5]
            return song_long
