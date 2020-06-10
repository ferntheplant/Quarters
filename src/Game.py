import time
import GameItem as gi
import EventQueue as eq

from Log import inject_logging, register_source


LOG_SOURCE = register_source("GAME")


class GameState:
    PREGAME = 1
    ONGOING = 2
    PAUSED = 3
    COMPLETE = 4
    EMPTY = 5


class Game(gi.GameItem):
    """
    Game object code should handle:
    - popping events
    - ensuring events are valid for the game
    - checking/validating game state
    Interesting case:
    - Player A and B racing to make shot first. A->B
    - event 1 says player A made shot
    - edit game state to reflect player A winning
    - event 2 says player B made shot
    - need game to understand that event 2 is invalid due to gamestate after event 1

    """
    def __init__(self):
        super(gi.GameItem).__init__()

        self.event_queue = eq.EventQueue()
        self.clients = []

        self.game_state = None
        self.game_start_time = None

        self.table = None

        inject_logging(self, LOG_SOURCE)

    def main_loop(self):
        while True:
            event = self.event_queue.pop()
            if event.typeID == eq.EventType.USER_INPUT:
                self.parse_user_input(event)
            elif event.typeID == eq.EventType.CLIENT_STATUS:
                self.process_client_event(event)

    def get_player(self, player_id):
        """
        Returns player object corresponding to the provided player id. Intended to be used at start
        of processing of user input to find the player who submitted input. Catches errors to
        return gracefully if player ID does not exist.
        :param player_id:
        :return: already existing player object or None
        """
        try:
            return self.table.player_id_to_player_map[player_id]
        except KeyError as e:
            self.warning("Player id {} does not exist in this game.")
            return None
