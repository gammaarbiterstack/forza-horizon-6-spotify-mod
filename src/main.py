from spotify import SpotifyController
from hotkeys import HotkeyManager
from config import Config

def main():
    config = Config()
    spotify = SpotifyController()
    hotkeys = HotkeyManager()

    spotify.connect()
    spotify.play()
    hotkeys.trigger("play_pause")

if __name__ == "__main__":
    main()
