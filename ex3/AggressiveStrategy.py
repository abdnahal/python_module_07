from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self.name = "Aggressive"
        self.damage_dealt = 0
        self.cards_played_this_turn = []

    def _card_cost(self, card):
        return card.cost

    def _target_threat(self, target):
        return getattr(target, "attack", 0)

    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        self.cards_played_this_turn = []
        self.damage_dealt = 0
        mana_used = 0
        cards_played = []
        targets_attacked = []

        sorted_hand = sorted(hand, key=self._card_cost)

        available_mana = 10

        for card in sorted_hand:

            card_type = card.__class__.__name__

            if card_type == "CreatureCard" and available_mana >= card.cost:
                available_mana -= card.cost
                mana_used += card.cost
                cards_played.append(card.name)
                self.cards_played_this_turn.append(card)

            elif card_type == "SpellCard" and card.effect_type == "damage":
                if available_mana >= card.cost:
                    available_mana -= card.cost
                    mana_used += card.cost
                    cards_played.append(card.name)

        total_damage = 0
        for card in self.cards_played_this_turn:
            if hasattr(card, "attack"):
                total_damage += card.attack
                targets_attacked.append("Enemy Player")

        self.damage_dealt = total_damage

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": total_damage,
        }

    def get_strategy_name(self) -> str:
        return self.name

    def prioritize_targets(self, available_targets: List) -> List:
        t = self._target_threat
        prioritized = sorted(available_targets, key=t, reverse=True)
        return prioritized
