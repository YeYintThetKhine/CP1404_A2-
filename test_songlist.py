"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print(song_list)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs

# test adding a new Song

# test get_song()

# test getting the number of required and learned songs (separately)

# test saving songs (check CSV file manually to see results)
