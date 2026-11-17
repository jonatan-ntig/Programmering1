from items.påsitem import Item
import vizdoom as vzd
import os
import secrets

class DoomItem(Item):
    def __init__(self):
        game = vzd.DoomGame()
        game.load_config(os.path.join(vzd.scenarios_path, "basic.cfg")) 
        game.set_mode(vzd.Mode.SPECTATOR)
        unique_identifier = secrets.token_hex(8)
        game.add_available_button(vzd.Button.MOVE_FORWARD)
        game.add_available_button(vzd.Button.MOVE_BACKWARD)
        game.add_available_button(vzd.Button.TURN_LEFT)
        game.add_available_button(vzd.Button.TURN_RIGHT)
        game.init()
        game.new_episode(unique_identifier+".lmp")
        while not game.is_episode_finished():
            game.advance_action()
        game.new_episode()
        game.close()    
        
        with open(unique_identifier+".lmp", "rb") as f:
            episode_data = f.read()
        os.remove(unique_identifier+".lmp")

        super().__init__("doom", episode_data)

    def __str__(self):
        return f"ID: {self.id}, Typ: Doom, Storlek: {len(self.innehåll)} bytes"

    def open(self):
        game = vzd.DoomGame()
        game.load_config(os.path.join(vzd.scenarios_path, "basic.cfg"))
        game.set_mode(vzd.Mode.SPECTATOR)
        game.init()
        with open(self.id +".lmp", "wb") as f:
            f.write(self.innehåll)
        game.replay_episode(self.id +".lmp")
        while not game.is_episode_finished():
            game.advance_action()
        game.new_episode()
        game.close()