from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive")

        self._attack = attack
        self.health = health
        self.max_health = health

        self.wins = 0
        self.losses = 0
        self.base_rating = 1200
        self.rating = self.base_rating

    def play(self, game_state: dict) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card entered battlefield",
        }

    def attack(self, target) -> dict:
        target_name = target if isinstance(target, str) else target.name

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self._attack,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:

        block_amount = min(self._attack // 2, incoming_damage)
        actual_damage = incoming_damage - block_amount

        self.health -= actual_damage
        self.health = max(0, self.health)

        return {
            "defender": self.name,
            "damage_taken": actual_damage,
            "damage_blocked": block_amount,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self._attack,
            "health": self.health,
            "max_health": self.max_health,
            "alive": self.health > 0,
        }

    def calculate_rating(self) -> int:
        win_bonus = self.wins * 16
        loss_penalty = self.losses * 8
        self.rating = self.base_rating + win_bonus - loss_penalty
        return self.rating

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("Wins cannot be negative")
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("Losses cannot be negative")
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}",
            "rating": self.calculate_rating(),
            "win_rate": (
                self.wins / (self.wins + self.losses) * 100
                if (self.wins + self.losses) > 0
                else 0
            ),
        }

    def get_tournament_stats(self) -> dict:
        info = self.get_card_info()
        info.update(
            {
                "attack": self._attack,
                "health": self.health,
                "wins": self.wins,
                "losses": self.losses,
                "rating": self.calculate_rating(),
                "record": f"{self.wins}-{self.losses}",
            }
        )
        return info
