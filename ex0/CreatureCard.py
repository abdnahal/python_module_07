from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0:
            raise ValueError("Creature attack must be positive")
        if health <= 0:
            raise ValueError("Creature health must be positive")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        target_name = target if isinstance(target, str) else target.name
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({"type": "Creature", "attack": self.attack,
                     "health": self.health})
        return info
