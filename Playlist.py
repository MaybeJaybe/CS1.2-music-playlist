from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None

  def add_song(self, title):
    new_song = Song(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

  def find_song(self, title):
    current_song = self.__first_song
    index = 0
    title_found = False

    while current_song != None:
        if title == current_song.get_title():
            return index
            title_found = True

        current_song = current_song.get_next_song()
        index += 1

    if title_found == False:
        return -1

  def remove_song(self, title):
    current_song = self.__first_song

    if current_song.get_title() == title:
        self.__first_song = self.__first_song.get_next_song()
        return f'Removed {current_song.get_title()}'

    else:
        while current_song.get_title() != title:
            if current_song.get_next_song().get_title == title:
                current_song.set_next_song(current_song.get_next_song())
                return f'Removed {current_song.get_title()}'
            else:
                current_song = current_song.get_next_song()

  def length(self):
    index = 0
    current_song = self.__first_song

    while current_song != None:
        index += 1
        current_song = current_song.get_next_song()

    return index

  def print_songs(self):
    index = 1
    current_song = self.__first_song

    while current_song != None:
        print(f'This is song # {index}, {current_song}')
        index += 1
        current_song = current_song.get_next_song()