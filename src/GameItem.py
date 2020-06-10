class GameItem:
    def __init__(self, display_name=None):
        self.unique_id = self.generate_id()
        if not display_name:
            self.display_name = str(self.unique_id)

    def generate_id(self):
        """
        TODO: mechanism for ensuring every generated ID is unique/psuedorandom
        :return:
        """
        return 0


class PLayerStatus:
    ON_DECK = 1
    SHOOTING = 2
    REDEMPTION = 3
    SOLIDARITY = 4
    SITTING_OUT = 5


class Player(GameItem):
    """
    Represents a user/player. Maps to any objects it uses for easy access
    """
    def __init__(self, display_name):
        super(GameItem).__init__(display_name)

        self.table = None
        self.original_seat = None
        self.current_seat = None

        self.player_status = None

        self.num_turns = None
        self.num_win = None
        self.num_loss = None
        self.num_drink = None
        self.num_redemptions = None


class Table(GameItem):
    """
    Represents a table. Maps to any objects it uses for easy access
    """
    def __init(self, display_name):
        super(GameItem).__init__(display_name)

        self.players = []
        self.seats = []
        self.player_id_to_player_map = {}
        self.player_seat_map = {}
        self.shot_player_map = {}

        self.num_shots = None

        self.round_count = None
        self.current_streak_count = None


class Seat(GameItem):
    """
    Represents a seat at a table. Maps to any objects it uses for easy access
    """
    def __init__(self):
        super(GameItem).__init__()

        self.left = None
        self.right = None

        self.cur_player = None

