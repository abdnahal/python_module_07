from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    fire_dragon = TournamentCard(
        name="Fire Dragon", cost=5, rarity="Legendary", attack=7, health=5
    )

    ice_wizard = TournamentCard(
        name="Ice Wizard", cost=4, rarity="Rare", attack=5, health=6
    )

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    # Display registration
    for card_id, card in [(dragon_id, fire_dragon), (wizard_id, ice_wizard)]:
        print(f"{card.name} (ID: {card_id}):")
        rank_info = card.get_rank_info()
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {rank_info['rating']}")
        print(f"- Record: {rank_info['record']}")
    print()

    print("Creating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(
        f"Match result: {{'winner': '{match_result['winner']}', "
        + f"'loser': '{match_result['loser']}', "
        + f"'winner_rating': {match_result['winner_rating']}, "
        + f"'loser_rating': {match_result['loser_rating']}}}"
    )
    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for rank, entry in enumerate(leaderboard, 1):
        print(
            f"{rank}. {entry['name']} - Rating: {entry['rating']} \
({entry['record']})"
        )
    print()

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(
        f"{{'total_cards': {report['total_cards']}, "
        + f"'matches_played': {report['matches_played']}, "
        + f"'avg_rating': {int(report['avg_rating'])}, "
        + f"'platform_status': '{report['platform_status']}'}}"
    )
    print()


if __name__ == "__main__":
    main()
