from random import sample

class Song:
    song_list =  []

    def __init__(self, song_name, song_file_path):
        self.song_name = song_name
        self.song_file_path = song_file_path
        
        Song.song_list.append((self, False))
    
    @classmethod
    def get_all_songs(cls):
        print(f"All songs: {[song[0].song_name for song in Song.song_list]}")

class Player:
   
    def __init__(self):
        self.song_que = []

    def shuffle_songs(self):
        print("Shuffling songs...")
        song_not_played = [song_obj for song_obj in Song.song_list if not song_obj[1]]
        self.song_que = sample(song_not_played, 2)

        for i in range(len(Song.song_list)):
            if Song.song_list[i] in self.song_que:
                Song.song_list[i] = (Song.song_list[i][0], True)

    def add_to_que(self, song_obj):
        print(f"adding song '{song_obj.song_name}' to queue")
        self.song_que.append((song_obj, True))

    def play_song(self):
        print(f"Play song - {self.song_que[0][0].song_name}")

    def get_songs_que(self):
        print(f"Songs in queue: {[song[0].song_name for song in self.song_que]}")


# initialize the songs
songs = [("abc", "/abc_path.mp3"), 
    ("def", "/def_path.mp3"),
    ("ghi", "/ghi_path.mp3"),
    ("jkl", "/jkl_path.mp3"),]
for song in songs:
    Song(song[0], song[1])
Song.get_all_songs()

ply = Player()

#shuffle songs
ply.shuffle_songs()
ply.get_songs_que()

#play song
ply.play_song()

#shuffle songs
ply.shuffle_songs()
ply.get_songs_que()

#adding song to queue
song_5 = Song("mno", "/mno_path")
Song.song_list.append((song_5, True))
ply.add_to_que(song_5)
ply.get_songs_que()
