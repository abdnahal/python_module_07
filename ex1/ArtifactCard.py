from typing import Dict
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, 
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("Durability must be positive")
        self.durability = durability
        self.effect = effect
        self.active = True

    def play(self, game_state: dict) -> dict:
        """
        Put this artifact into play. Implements abstract play() method.
        """
        self.active = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}'
        }

    def activate_ability(self) -> dict:
        if not self.active:
            return {'error': 'Artifact is not active'}

        self.durability -= 1
        return {
            'artifact': self.name,
            'ability': self.effect,
            'activated': True,
            'durability_remaining': self.durability
        }
