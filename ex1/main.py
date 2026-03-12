from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")

    deck = Deck()

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2,
                            "Uncommon", 5, "+1 mana per turn")

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}\n")

    deck.shuffle()

    print("Drawing and playing cards:\n")

    for _ in range(3):
        if deck.is_empty():
            break

        card = deck.draw_card()
        card_type = card.__class__.__name__

        print(f"Drew: {card.name} ({card_type.replace('Card', '')})")
        result = card.play({})
        print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
