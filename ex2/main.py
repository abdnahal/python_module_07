from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Legendary",
        attack=5,
        health=8,
        mana_pool=4,
        spells=["Fireball", "Heal", "Berserk"],
    )

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    print("Playing Arcane Warrior (Elite Card):")
    result = arcane_warrior.play({})
    print(f"Play result: {result}\n")

    print("Combat phase:")

    attack_result = arcane_warrior.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = arcane_warrior.defend(5)
    print(f"Defense result: {defense_result}")
    print()

    print("Magic phase:")

    spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = arcane_warrior.channel_mana(3)
    print(f"Mana channel: {mana_result}")
    print()

    print("Full Card Information:")
    print(arcane_warrior.get_card_info())
    print()

    print("Combat Stats:", arcane_warrior.get_combat_stats())
    print("Magic Stats:", arcane_warrior.get_magic_stats())
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
