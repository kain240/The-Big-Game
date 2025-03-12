from enum import Enum

class Status(Enum):
    Waiting = 'waiting'
    Started = 'started'
    Ended = 'ended'
    Running = 'running'
