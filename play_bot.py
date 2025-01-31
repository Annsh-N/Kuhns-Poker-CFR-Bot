import pickle
import random

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
    
    if random.random() < strategy.get(str(ai_card) + history, [0.5, 0.5])[1]:
        history += 'b'
        print('AI bets')
        action = input("Enter 'b' to bet or 'p' to pass: ")
        if action == 'b':
            history += 'b'
            winner = 'AI' if ai_card > player_card else 'You'
            print(f'AI had {ai_card}. {winner} wins 2.')
        else:
            print(f'AI had {ai_card}. AI wins 1.')
    else:
        print('AI checks')
        action = input("Enter 'b' to bet or 'p' to pass: ")
        if action == 'b':
            history += 'bp'
            print(f'AI had {ai_card}. You win 1.')
        else:
            winner = 'AI' if ai_card > player_card else 'You'
            print(f'AI had {ai_card}. {winner} wins 1.')

if __name__ == '__main__':
    strategy = load_strategy()
    while True:
        play_ai(strategy)
        if input("Play again? (y/n): ") != 'y':
            break
