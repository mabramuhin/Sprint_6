from enum import Enum

class OrderEntryPoint(Enum):
    HEADER = ("в шапке страницы", "header_order_button")
    ROADMAP = ("в roadmap", "roadmap_order_button")

    def __init__(self, value, locator_name):
        self._value_ = value
        self.locator_name = locator_name

class ScooterColor(Enum):
    BLACK = ("чёрный жемчуг", "color_checkbox_black")
    GREY = ("серая безысходность", "color_checkbox_grey")

    def __init__(self, value, locator_name):
        self._value_ = value
        self.locator_name = locator_name