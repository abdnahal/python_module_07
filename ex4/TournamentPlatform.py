from typing import Dict, List, Optional
from random import randint
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("Only TournamentCard objects can be registered")

        card_id = f"{card.name.lower().replace(' ', '_')}_\
{len(self.cards) + 1:03d}"
        self.cards[card_id] = card

        return card_id

    def get_rating(self, stat: dict) -> int:
        return stat["rating"]

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards:
            raise ValueError(f"Card {card1_id} not found")
        if card2_id not in self.cards:
            raise ValueError(f"Card {card2_id} not found")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        card1_power = card1.attack
        card2_power = card2.attack

        card1_roll = card1_power + randint(-2, 2)
        card2_roll = card2_power + randint(-2, 2)

        if card1_roll > card2_roll:
            winner_id = card1_id
            winner = card1
            loser = card2
        else:
            winner_id = card2_id
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": card2_id if winner_id == card1_id else card1_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> List[Dict]:
        leaderboard_data = []
        for card_id, card in self.cards.items():
            leaderboard_data.append(
                {
                    "card_id": card_id,
                    "name": card.name,
                    "rating": card.calculate_rating(),
                    "record": card.get_rank_info()["record"],
                }
            )

        leaderboard = sorted(leaderboard_data,
                             key=self.get_rating, reverse=True)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        if not self.cards:
            return {"total_cards": 0, "matches_played": 0,
                    "platform_status": "empty"}

        total_wins = sum(card.wins for card in self.cards.values())
        total_losses = sum(card.losses for card in self.cards.values())
        total_cards = len(self.cards)

        ratings = [card.calculate_rating() for card in self.cards.values()]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "total_wins": total_wins,
            "total_losses": total_losses,
            "avg_rating": round(avg_rating, 0),
            "platform_status": "active",
        }

    def get_card_by_id(self, card_id: str) -> Optional[TournamentCard]:
        return self.cards.get(card_id)

    def card_count(self) -> int:
        return len(self.cards)
