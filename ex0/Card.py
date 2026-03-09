from abc import abstractmethod, ABC


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if cost < 0:
            raise ValueError("Card cost cannot be negative")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
