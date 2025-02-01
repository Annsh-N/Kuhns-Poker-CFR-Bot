import random
import pickle
from cfr_trainer import KuhnNode

def deal_cards():
    cards = ['K', 'Q', 'J']
    random.shuffle(cards)
    return cards[:2]

def get_winner(card1, card2):
    card_ranks = {'K': 3, 'Q': 2, 'J': 1}
    return 1 if card_ranks[card1] > card_ranks[card2] else -1

def play_hand(strategy, cards):
    history = ''
    player_card, opponent_card = cards

    node = strategy.get(str(player_card) + history, KuhnNode())
    strategy_probs = node.get_average_strategy()

    #Uncomment to see strategy for imprving the model
    #print(f"AI Strategy for {player_card} ({history}): {strategy_probs}")

    if random.random() < strategy_probs[1]:  # Now accessing valid probabilities
        history += 'b'
        opponent_node = strategy.get(str(opponent_card) + history, KuhnNode())
        opponent_strategy_probs = opponent_node.get_average_strategy()

        if random.random() < opponent_strategy_probs[1]:
            return get_winner(player_card, opponent_card) * 2
    return get_winner(player_card, opponent_card)


def simulate(strategy, games=1000):
    results = [play_hand(strategy, deal_cards()) for _ in range(games)]
    return sum(results) / games

if __name__ == '__main__':
    with open('cfr_training_data.pkl', 'rb') as f:
        strategy = pickle.load(f)
    
    print('Expected value over 1000 games:', simulate(strategy, 1000))
