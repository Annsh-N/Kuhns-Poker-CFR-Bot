import random

def deal_cards():
    cards = [1, 2, 3]
    random.shuffle(cards)
    return cards[:2]

def get_winner(card1, card2):
    return 1 if card1 > card2 else -1

def play_hand(strategy, cards):
    history = ''
    player_card, opponent_card = cards
    
    if strategy.get((player_card, history), [0.5, 0.5])[1] > 0.5:
        history += 'b'
        if strategy.get((opponent_card, history), [0.5, 0.5])[1] > 0.5:
            return get_winner(player_card, opponent_card) * 2
    return get_winner(player_card, opponent_card)

def simulate(strategy, games=1000):
    results = [play_hand(strategy, deal_cards()) for _ in range(games)]
    return sum(results) / games

if __name__ == '__main__':
    with open('cfr_training_data.pkl', 'rb') as f:
        import pickle
        strategy = pickle.load(f)
    
    print('Expected value:', simulate(strategy))
