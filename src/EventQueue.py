class EventQueue:
    """
    Async event queue to process incoming client/user events
    """
    def __init__(self):
        pass


class EventType:
    CLIENT_STATUS = 1
    USER_INPUT = 2


class Event:
    """
    Standard event type to package/process events.
    TODO: API for event shape
    """
    def __init__(self):
        self.typeID = None
