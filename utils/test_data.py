from dataclasses import dataclass
from utils.enums import ScooterColor


@dataclass(frozen=True)
class OwnerData:
    name: str
    surname: str
    address: str
    metro_index: int
    phone: str

@dataclass(frozen=True)
class RentData:
    delivery_date: str
    period_index: int
    scooter_color: ScooterColor
    comment: str

@dataclass(frozen=True)
class OrderData:
    owner: OwnerData
    rent: RentData

HEADER_ORDER_DATA = OrderData(
    owner=OwnerData("Иван", "Первый", "г. Москва", 0, "89046666666"),
    rent=RentData("05.02.2026", 0, ScooterColor.GREY, "Комментарий для курьера")
)

ROADMAP_ORDER_DATA = OrderData(
    owner=OwnerData("Пётр", "Второй", "г. Санкт-Петербург", -1, "89047777777"),
    rent=RentData("06.02.2026", -1, ScooterColor.BLACK, "Комментарий для курьера")
)