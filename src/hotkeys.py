class HotkeyManager:
    def __init__(self):
        self.hotkeys = {"play_pause": "Ctrl+P", "next_track": "Ctrl+N"}

    def trigger(self, action):
        if action in self.hotkeys:
            print(f"{action} triggered via {self.hotkeys[action]}")
        else:
            print("Hotkey not found")
