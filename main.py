"""
Name: Ye Yint Thet Khine
Date: 23/05/2018
Brief Project Description:
A program that keeps a record of songs the user has learnt
and a record of songs to learn
GitHub URL: https://github.com/CP1404-2018-51/a2-YeYintThetKhine
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from songlist import SongList


class SongsList(App):
    def __init__(self, **kwargs):

        """
            Installing all the required widgets for the layout of kivy app
        """
        super().__init__(**kwargs)
        self.song_list = SongList()

        #   Bottom status label and Top count label
        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")

        # layout widget left part
        self.sort_label = Label(text="Sort by:")
        # Putting default sort method as Artist
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Required'))
        self.add_song_label = Label(text="Add New Song...")
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)

        # To add and clear for the bottom widget
        self.add_song_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

    def songs_sort(self, *args):
        """
        The code that handle the sorts base on the click of the spinner
        """
        self.song_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def build(self):
        """
            opening the kivy app and putting a little object
        """
        self.title = "Songs List 2.0"
        self.root = Builder.load_file('app.kv')
        self.song_list.load_songs()
        self.song_list.sort('Artist')
        self.building_widgets()
        self.right_widgets()
        return self.root

    def building_widgets(self):
        """
            left layout creation base on widgets created in an order
        """
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_song_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.add_song_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)

        # Setting on click for sorting spinner, add button and clear button
        self.spinner.bind(text=self.songs_sort)
        self.add_song_button.bind(on_release=self.add_song_handler)
        self.clear_button.bind(on_release=self.clear_fields)

    def right_widgets(self):
        """
            Building right layout with widgets based on the list we created.
        """
        # Sets the count label
        self.top_label.text = "To Learn: " + str(self.song_list.get_required_songs_count()) + ". Learned: " + str(
            self.song_list.get_learned_songs_count())

        # Goes through each song in the list and check if it learned or required and setts color based on that
        for song in self.song_list.songs:
            # n = Learned
            if song[0].status == 'n':
                song_button = Button(text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(
                    song[0].year) + ") " "(Learned)", id=song[0].title)

                song_button.background_color = [88, 89, 0, 0.3]
            # y = required to learn
            else:
                song_button = Button(
                    text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(song[0].year) + ")",
                    id=song[0].title)

                song_button.background_color = [0, 88, 88, 0.3]

            # Setting on click for the buttons created
            song_button.bind(on_release=self.click_handler)
            self.root.ids.rightLayout.add_widget(song_button)

    def click_handler(self, button):
        """
            Handles on click for each song button created
        """

        # if button user clicked is learned change it to required to learn and update the status bar
        if self.song_list.get_song(button.id).status == 'n':
            self.song_list.get_song(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "You need to learn " + str(self.song_list.get_song(button.id).title)

        # if button user clicked is Required to learn change it to learned and update the status bar
        else:
            self.song_list.get_song(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_song(button.id).title)

        # Update the sorting and reloads the right layout
        self.songs_sort()
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def clear_fields(self, *args):
        """
            Handles clearing up all the text fields and status bar
        """
        self.title_text_input.text = ""
        self.artist_text_input.text = ""
        self.year_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def add_song_handler(self, *args):
        """
            This method handles all the error checking for user input on text field and creates a Song object
        """
        # Checks if all the input fields are complete if not error text will be displayed
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:
                # If year is negative
                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Please enter a valid number"
                # If all the criteria matches it creates a Song object in song_list class
                else:
                    self.song_list.add_song(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sort(self.spinner.text)
                    self.clear_fields()
                    self.root.ids.rightLayout.clear_widgets()
                    self.right_widgets()
            # String Error checking for year input
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def stop(self):
        # By closing, all the data form the list will be saved to to songs.csv file
        self.song_list.save_file()


if __name__ == '__main__':
    app = SongsList()
    app.run()
