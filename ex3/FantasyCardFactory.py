from typing import Optional, Dict, List
from random import choice
from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def __init__(self) -> None:
        self.creatures = {
            'dragon':
            {"cost": 5, "attack": 7,
             "health": 5, "rarity": "Legendary"},
            'goblin': {"cost": 2, "attack": 2,
                       "health": 1, "rarity": "Common"},
            'elf': {"cost": 3, "attack": 3,
                    "health": 3, "rarity": "Uncommon"},
            'dwarf': {"cost": 4, "attack": 4,
                      "health": 6, "rarity": "Uncommon"},
        }

        self.spells = {
            "fireball": {"cost": 3, "effect_type": "damage",
                         "rarity": "Common"},
            "heal": {"cost": 2, "effect_type": "heal",
                     "rarity": "Common"},
            "frost_storm": {"cost": 4, "effect_type": "damage",
                            "rarity": "Uncommon"},
            "berserk": {"cost": 2, "effect_type": "buff",
                        "rarity": "Uncommon"},
        }

        self.artifacts = {
            "mana_ring": {
                "cost": 2,
                "durability": 5,
                "effect": "+1 mana per turn",
                "rarity": "Uncommon",
            },
            "staff_of_power": {
                "cost": 4,
                "durability": 3,
                "effect": "+2 spell damage",
                "rarity": "Rare",
            },
            "excalibur": {
                "cost": 5,
                "durability": 10,
                "effect": "+3 attack",
                "rarity": "Legendary",
            },
        }

    def create_creature(self,
                        name_or_power: Optional[str | int] = None) -> Card:
        if isinstance(name_or_power, str):
            creature_type = name_or_power.lower()
            if creature_type not in self.creatures:
                raise ValueError(f"Unknown creature type: {creature_type}")
        else:
            creature_type = choice(list(self.creatures.keys()))

        stats = self.creatures[creature_type]

        creature_name = creature_type.capitalize()
        return CreatureCard(
            name=creature_name,
            cost=stats["cost"],
            rarity=stats["rarity"],
            attack=stats["attack"],
            health=stats["health"],
        )

    def create_spell(self, name_or_power: Optional[str | int] = None) -> Card:
        if isinstance(name_or_power, str):
            spell_type = name_or_power.lower()
            if spell_type not in self.spells:
                raise ValueError(f"Unknown spell type: {spell_type}")
        else:
            spell_type = choice(list(self.spells.keys()))

        stats = self.spells[spell_type]

        spell_name = spell_type.capitalize().replace("_", " ")
        return SpellCard(
            name=spell_name,
            cost=stats["cost"],
            rarity=stats["rarity"],
            effect_type=stats["effect_type"],
        )

    def create_artifact(self,
                        name_or_power: Optional[str | int] = None) -> Card:
        if isinstance(name_or_power, str):
            artifact_type = name_or_power.lower()
            if artifact_type not in self.artifacts:
                raise ValueError(f"Unknown artifact type: {artifact_type}")
        else:
            artifact_type = choice(list(self.artifacts.keys()))

        stats = self.artifacts[artifact_type]

        artifact_name = artifact_type.capitalize().replace("_", " ")
        return ArtifactCard(
            name=artifact_name,
            cost=stats["cost"],
            rarity=stats["rarity"],
            durability=stats["durability"],
            effect=stats["effect"],
        )

    def create_themed_deck(self, size: int) -> Dict:
        creatures_count = int(size * 0.4)
        spells_count = int(size * 0.4)
        artifacts_count = size - creatures_count - spells_count

        cards: List = []

        for _ in range(creatures_count):
            cards.append(self.create_creature())

        for _ in range(spells_count):
            cards.append(self.create_spell())

        for _ in range(artifacts_count):
            cards.append(self.create_artifact())

        return {
            "theme": "Fantasy",
            "total_cards": len(cards),
            "cards": cards,
            "composition": {
                "creatures": creatures_count,
                "spells": spells_count,
                "artifacts": artifacts_count,
            },
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys()),
        }
