import random

class Playlist:
  def __init__(self, songs, shuffle=False):
    self.songs = songs
    self.index = 0
    
    if shuffle:
      random.shuffle(self.songs)
    
  def __iter__(self):
    return self
  
  # Define a magic method to iterate through songs
  def __next__(self):
    if self.index >= len(self.songs):
      raise StopIteration
    
    # Pull the next song, increment index, and return
    song = self.songs[self.index]
    self.index += 1
    return song
  
# Shuffle a Playlist, use for loop to iterate through
favorite_songs = Playlist(["Ticking", "Tiny Dancer"], shuffle=True)
for song in favorite_songs:
  print(song)