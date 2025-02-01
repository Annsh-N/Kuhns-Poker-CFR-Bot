import pickle
import random
from cfr_trainer import KuhnNode

def load_strategy():
    with open('cfr_training_data.pkl', 'rb') as f:
        return pickle.load(f)

def play_ai(strategy):
    cards = ['K', 'Q', 'J']
    random.shuffle(cards)
    history = ''
    ai_card = cards[1]
    player_card = cards[0]
    print(f'Your card: {player_card}')
    
    node = strategy.get(str(ai_card) + history, KuhnNode())  # Get AI's KuhnNode
    strategy_probs = node.get_average_strategy()  # Extract strategy probabilities

    if random.random() < strategy_probs[1]:  # AI bets first
        history += 'b'
        print('AI bets')
    else:
        print('AI checks')

    action = input("Enter 'b' to bet or 'p' to pass: ")
    history += action

    # AI reacts after player's move
    node = strategy.get(str(ai_card) + history, KuhnNode())
    strategy_probs = node.get_average_strategy()

    if action == 'b':  # If the player bets, AI decides to call or fold
        if random.random() < strategy_probs[1]:  
            history += 'b'
            print('AI calls the bet.')

            # ✅ Corrected Winner Determination
            card_ranks = {'K': 3, 'Q': 2, 'J': 1}
            winner = 'AI' if card_ranks[ai_card] > card_ranks[player_card] else 'You'

            print(f'AI had {ai_card}. {winner} wins 2.')  # ✅ Now correct
        else:
            print('AI folds. You win 1.')
    else:  # If the player checks, game ends
        card_ranks = {'K': 3, 'Q': 2, 'J': 1}
        winner = 'AI' if card_ranks[ai_card] > card_ranks[player_card] else 'You'
        print(f'AI had {ai_card}. {winner} wins 1.')

    print(f'Game history: {history}')

if __name__ == '__main__':
    strategy = load_strategy()
    while True:
        play_ai(strategy)
        if input("Play again? (y/n): ") != 'y':
            break
