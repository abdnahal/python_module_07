from typing import Dict, Optional
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from random import choice


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:

        if not isinstance(factory, CardFactory):
            raise TypeError("factory must be a CardFactory")
        if not isinstance(strategy, GameStrategy):
            raise TypeError("strategy must be a GameStrategy")

        self.factory = factory
        self.strategy = strategy
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> Dict:
        if not self.factory or not self.strategy:
            raise RuntimeError("Engine not configured. Call \
configure_engine() first.")

        hand_size = 3
        hand = []
        for _ in range(hand_size):
            card_type = choice(["creature", "spell", "artifact"])
            if card_type == "creature":
                hand.append(self.factory.create_creature())
            elif card_type == "spell":
                hand.append(self.factory.create_spell())
            else:
                hand.append(self.factory.create_artifact())
            self.cards_created += 1

        battlefield = [self.factory.create_creature(),
                       self.factory.create_creature()]
        self.cards_created += 2

        turn_result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += turn_result.get("damage_dealt", 0)

        turn_result["factory"] = self.factory.__class__.__name__
        turn_result["hand_size"] = len(hand)

        return turn_result

    def get_engine_status(self) -> Dict:
        return {
            "configured": self.factory is not None
            and self.strategy is not None,
            "factory": self.factory.__class__.__name__
            if self.factory else None,
            "strategy": self.strategy.get_strategy_name()
            if self.strategy else None,
            "turns_simulated": self.turns_simulated,
            "strategy_used": (
                self.strategy.get_strategy_name() if self.strategy else None
            ),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
