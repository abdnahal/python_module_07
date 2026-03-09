from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:\n")

    # Create a creature card
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    # Test 1: Get card info
    print("CreatureCard Info:")
    info = fire_dragon.get_card_info()
    print(info)
    print()

    # Test 2: Check if playable with sufficient mana
    print("Playing Fire Dragon with 6 mana available:")
    available_mana = 6
    is_playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {is_playable}")

    if is_playable:
        result = fire_dragon.play({})
        print(f"Play result: {result}")
    print()

    # Test 3: Attack with the creature
    print("Fire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack_target("Goblin Warrior")
    print(f"Attack result: {attack_result}")
    print()

    # Test 4: Check if playable with insufficient mana
    print("Testing insufficient mana (3 available):")
    available_mana = 3
    is_playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {is_playable}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
