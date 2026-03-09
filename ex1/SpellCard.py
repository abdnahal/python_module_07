from ..ex0.Card import Card
from typing import List


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect = effect_type

    def play(self, game_state: dict) -> dict:
        effects = {
            'damage': 'Deal damage to target',
            'heal': 'Restore health to target',
            'buff': "Increase target's stats",
            'debuff': "Decrease target's stats",
            'draw': 'Draw cards from deck',
            'discard': "Discard opponent's cards"
        }

        effect_description = effects.get(self.effect_type, 'Unknown effect')

        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_description
        }

    def resolve_effect(self, targets: List[str]) -> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            'type': 'Spell',
            'effect_type': self.effect_type
        })
        return info
