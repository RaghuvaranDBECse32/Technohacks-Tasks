class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_index = 0

    def load_playlist(self, directory):
        """Load MP3 files from a directory into the playlist."""
        files = os.listdir(directory)
        self.playlist = [os.path.join(directory, file) for file in files if file.endswith('.mp3')]
        print("Playlist loaded successfully.")

    def play(self):
        """Play the current song in the playlist."""
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            print(f"Now playing: {os.path.basename(self.playlist[self.current_index])}")
        else:
            print("No songs in the playlist.")

    def next_song(self):
        """Play the next song in the playlist."""
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play()

    def previous_song(self):
        """Play the previous song in the playlist."""
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play()

    def add_to_playlist(self, file):
        """Add a song to the playlist."""
        if file.endswith('.mp3'):
            self.playlist.append(file)
            print(f"Added '{os.path.basename(file)}' to the playlist.")
        else:
            print("Invalid file format. Only MP3 files can be added to the playlist.")

    def show_playlist(self):
        """Display the current playlist."""
        if self.playlist:
            print("Current Playlist:")
            for index, song in enumerate(self.playlist, start=1):
                print(f"{index}. {os.path.basename(song)}")
        else:
            print("No songs in the playlist.")

    def clear_playlist(self):
        """Clear the playlist."""
        self.playlist = []
        print("Playlist cleared.")

def main():
    player = MusicPlayer()
    print("Welcome to Simple Music Player!")

    while True:
        print("\nSelect operation:")
        print("1. Load Playlist")
        print("2. Play")
        print("3. Next Song")
        print("4. Previous Song")
        print("5. Add to Playlist")
        print("6. Show Playlist")
        print("7. Clear Playlist")
        print("8. Quit")

        choice = input("Enter choice (1-8): ")

        if choice == '1':
            directory = input("Enter directory path containing MP3 files: ")
            player.load_playlist(directory)
        elif choice == '2':
            player.play()
        elif choice == '3':
            player.next_song()
        elif choice == '4':
            player.previous_song()
        elif choice == '5':
            file = input("Enter MP3 file path to add to playlist: ")
            player.add_to_playlist(file)
        elif choice == '6':
            player.show_playlist()
        elif choice == '7':
            player.clear_playlist()
        elif choice == '8':
            print("Thank you for using Simple Music Player!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
