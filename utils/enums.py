from enum import Enum

class OrderEntryPoint(Enum):
    HEADER = ("header", "шапке страницы")
    ROADMAP = ("roadmap", "низу страницы")

    def __init__(self, value, description):
        self._value_ = value
        self.description = description

class ScooterColor(Enum):
    BLACK = ("black", "чёрный жемчуг")
    GREY = ("grey", "серая безысходность")

    def __init__(self, value, description):
        self._value_ = value
        self.description = description