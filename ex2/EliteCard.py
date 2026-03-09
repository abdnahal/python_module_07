from typing import List
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        mana_pool: int,
        spells: List[str],
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive")

        self.attack_power = attack
        self.health = health
        self.max_health = health

        if mana_pool < 0:
            raise ValueError("Mana pool cannot be negative")

        self.mana_pool = mana_pool
        self.max_mana = mana_pool
        self.spells = spells if spells else []

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card with combat and magic abilities summoned",
        }

    def attack(self, target) -> dict:

        target_name = target if isinstance(target, str) else target.name

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:

        block_amount = min(self.attack_power // 2, incoming_damage)
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
            "attack": self.attack_power,
            "health": self.health,
            "max_health": self.max_health,
            "alive": self.health > 0,
        }

    def cast_spell(self, spell_name: str, targets: List[str]) -> dict:
        if spell_name not in self.spells:
            return {"error": f"Cannot cast {spell_name} - not in spell list"}

        mana_cost = len(spell_name)

        if self.mana_pool < mana_cost:
            return {"error": "Insufficient mana to cast spell"}

        self.mana_pool -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:

        if amount < 0:
            return {"error": "Cannot channel negative mana"}

        self.mana_pool = min(self.mana_pool + amount, self.max_mana)

        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:

        return {
            "name": self.name,
            "mana_pool": self.mana_pool,
            "max_mana": self.max_mana,
            "spells": self.spells,
            "spell_count": len(self.spells),
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": "Elite",
                "attack": self.attack_power,
                "health": self.health,
                "mana_pool": self.mana_pool,
                "spells": self.spells,
            }
        )
        return info
