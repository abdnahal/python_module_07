from typing import List, Dict
from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    """
    Concrete strategy that prioritizes offense and damage.
    
    Aggressive strategy characteristics:
    - Plays low-cost creatures first to build board presence
    - Attacks immediately with available creatures
    - Favors direct damage spells
    - Targets enemy creatures and the opponent directly
    """
    
    def __init__(self) -> None:
        """Initialize the aggressive strategy."""
        self.name = "Aggressive"
        self.damage_dealt = 0
        self.cards_played_this_turn = []
    
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        """
        Execute an aggressive turn.
        
        Steps:
        1. Sort hand by cost (play cheap cards first)
        2. Play low-cost creatures for board presence
        3. Play damage spells
        4. Attack with all available creatures
        
        Args:
            hand: Cards in player's hand
            battlefield: Cards currently in play
        
        Returns:
            Dictionary describing turn execution
        """
        self.cards_played_this_turn = []
        self.damage_dealt = 0
        mana_used = 0
        cards_played = []
        targets_attacked = []
        
        # Step 1: Sort hand by cost (ascending)
        sorted_hand = sorted(hand, key=lambda card: card.cost)
        
        # Step 2: Play creatures from lowest cost
        available_mana = 10  # Simplified: assume 10 mana per turn
        
        for card in sorted_hand:
            # Check card type
            card_type = card.__class__.__name__
            
            # Play creatures first (most aggressive)
            if card_type == 'CreatureCard' and available_mana >= card.cost:
                available_mana -= card.cost
                mana_used += card.cost
                cards_played.append(card.name)
                self.cards_played_this_turn.append(card)
            
            # Then play damage spells
            elif card_type == 'SpellCard' and card.effect_type == 'damage':
                if available_mana >= card.cost:
                    available_mana -= card.cost
                    mana_used += card.cost
                    cards_played.append(card.name)
        
        # Step 3: Calculate damage from all creatures
        total_damage = 0
        for card in self.cards_played_this_turn:
            if hasattr(card, 'attack'):  # It's a creature
                total_damage += card.attack
                targets_attacked.append('Enemy Player')
        
        self.damage_dealt = total_damage
        
        return {
            'strategy': self.get_strategy_name(),
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': total_damage
        }
    
    def get_strategy_name(self) -> str:
        """Get this strategy's name."""
        return self.name
    
    def prioritize_targets(self, available_targets: List) -> List:
        """
        Aggressive strategy: prioritize high-threat targets.
        
        Targets with high attack value are dangerous and should
        be eliminated first.
        
        Args:
            available_targets: List of potential targets
        
        Returns:
            Targets sorted by threat level (descending)
        """
        # Sort by attack power (descending) - highest threat first
        prioritized = sorted(
            available_targets,
            key=lambda target: getattr(target, 'attack', 0),
            reverse=True
        )
        return prioritized
