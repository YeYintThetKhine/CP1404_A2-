from song import Song


class SongList:
    def __init__(self, ):
        """
            Initialize an empty list for Song object
        """
        self.songs = []

    def add_song(self, title, artist, year):
        """
            This method adds single song object to songs list
        """
        self.songs.append([Song(title, artist, year, 'y')])

    def get_song(self, title):
        """
            Method to return a user selected single song object.
        """
        for song in self.songs:
            if song[0].title == title:
                return song[0]

    def load_songs(self):
        """
            load songs from songs.csv and create a Song object for each song
        """
        readfile = open('songs.csv', 'r')
        for song in readfile:
            song_string = song.split(",")
            self.songs.append(
                [Song(song_string[0], song_string[1], int(song_string[2]), song_string[3].strip())])

        readfile.close()

    def get_required_songs_count(self):
        """
        Loops through songs list and counts all the songs that needs to be learned and returns the count
        """
        required_songs = 0
        for song in self.songs:
            if song[0].status == 'y':
                required_songs += 1
        return required_songs

    def save_file(self):
        """
            saves all the changes made by the user to songs.csv file
        """
        writefile = open('songs.csv', 'w')
        for song in self.songs:
            writefile.write(
                song[0].title + "," + song[0].artist + "," + str(song[0].year) + "," + song[
                    0].status + "\n")

        writefile.close()

    def sort(self, sort_method):
        """
            Sort the list based on user spinner selection primarily then by the title
        """
        if sort_method == "Artist":
            self.songs.sort(key=lambda i: (i[0].artist, i[0].title))
        elif sort_method == "Title":
            self.songs.sort(key=lambda i: i[0].title)
        elif sort_method == "Year":
            self.songs.sort(key=lambda i: (i[0].year, i[0].title))
        else:
            self.songs.sort(key=lambda i: (i[0].status, i[0].title))

    def get_learned_songs_count(self):
        """
        Loops through songs list and counts all the songs that are learned and returns the count
        """
        learned_songs = 0
        for song in self.songs:
            if song[0].status == 'n':
                learned_songs += 1
        return learned_songs


