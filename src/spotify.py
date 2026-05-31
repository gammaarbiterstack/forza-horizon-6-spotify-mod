class SpotifyController:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Spotify connected (demo)")

    def play(self):
        if self.connected:
            print("Playing track...")
        else:
            print("Connect Spotify first")
