from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}\n")

    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Simulating aggressive turn...")

    hand = [
        factory.create_creature("dragon"),
        factory.create_creature("goblin"),
        factory.create_spell("fireball"),
    ]

    print("Hand: [", end="")
    for i, card in enumerate(hand):
        if i > 0:
            print(", ", end="")
        print(f"{card.name} ({card.cost})", end="")
    print("]\n")

    turn_result = engine.simulate_turn()

    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(
        f"Actions: {{'cards_played': {turn_result['cards_played']}, "
        + f"'mana_used': {turn_result['mana_used']}, "
        + f"'targets_attacked': {turn_result['targets_attacked']}, "
        + f"'damage_dealt': {turn_result['damage_dealt']}}}"
    )
    print()

    print("Game Report:")
    status = engine.get_engine_status()
    print(
        f"{{'turns_simulated': {status['turns_simulated']}, "
        + f"'strategy_used': '{status['strategy_used']}', "
        + f"'total_damage': {status['total_damage']}, "
        + f"'cards_created': {status['cards_created']}}}"
    )
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
