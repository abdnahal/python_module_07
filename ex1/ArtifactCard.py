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
        self.active = True
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        if not self.active:
            return {"error": "Artifact is not active"}

        self.durability -= 1
        return {
            "artifact": self.name,
            "ability": self.effect,
            "activated": True,
            "durability_remaining": self.durability,
        }

    def take_damage(self, damage: int) -> dict:
        self.durability = max(0, self.durability - damage)

        return {
            "artifact": self.name,
            "damage_taken": damage,
            "durability_remaining": self.durability,
            "destroyed": self.durability == 0,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": "Artifact",
                "durability": self.durability,
                "effect": self.effect,
                "active": self.active,
            }
        )
        return info
