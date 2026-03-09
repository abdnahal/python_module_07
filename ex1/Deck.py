from typing import List
from random import shuffle
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card objects can be added to the deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")

        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creature_count = 0
        spell_count = 0
        artifact_count = 0
        total_cost = 0

        for card in self.cards:
            card_type = card.__class__.__name__

            if card_type == "CreatureCard":
                creature_count += 1
            elif card_type == "SpellCard":
                spell_count += 1
            elif card_type == "ArtifactCard":
                artifact_count += 1

            total_cost += card.cost

        total_cards = len(self.cards)
        avg_cost = total_cost / total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": round(avg_cost, 1),
        }

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def card_count(self) -> int:
        return len(self.cards)
