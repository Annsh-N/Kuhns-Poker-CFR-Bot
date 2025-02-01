import random
import pickle

class KuhnNode:
    def __init__(self):
        self.regret_sum = [0.0, 0.0]
        self.strategy = [0.5, 0.5]
        self.strategy_sum = [0.0, 0.0]
    
    def get_strategy(self):
        normalizing_sum = sum(max(r, 0) for r in self.regret_sum)
        if normalizing_sum > 0:
            self.strategy = [max(r, 0) / normalizing_sum for r in self.regret_sum]
        else:
            self.strategy = [0.5, 0.5]
        self.strategy_sum = [s + p for s, p in zip(self.strategy_sum, self.strategy)]
        return self.strategy
    
    def get_average_strategy(self):
        normalizing_sum = sum(self.strategy_sum)
        if normalizing_sum > 0:
            return [s / normalizing_sum for s in self.strategy_sum]
        return [0.5, 0.5]

def cfr(cards, history, prob1, prob2, nodes):
    plays = len(history)
    player = plays % 2
    opponent = 1 - player
    
    card_ranks = {'K': 3, 'Q': 2, 'J': 1}
    
    if plays > 1 and (history[-1] == 'p' or history[-2:] == 'bb'):
        if history == 'pp':
            return 1 if card_ranks[cards[player]] > card_ranks[cards[opponent]] else -1
        return 2 if history[-2:] == 'bb' and card_ranks[cards[player]] > card_ranks[cards[opponent]] else -2
    
    info_set = str(cards[player]) + history
    node = nodes.setdefault(info_set, KuhnNode())
    strategy = node.get_strategy()
    util = [0.0, 0.0]
    node_util = 0.0
    
    for i, action in enumerate(['p', 'b']):
        new_history = history + action
        prob = prob1 if player == 0 else prob2
        util[i] = -cfr(cards, new_history, prob * strategy[i], prob2 if player == 0 else prob1, nodes)
        node_util += strategy[i] * util[i]
    
    for i in range(2):
        regret = util[i] - node_util
        node.regret_sum[i] += (prob1 * regret) if player == 0 else (prob2 * regret)

    
    return node_util

def train(iterations=100000):
    nodes = {}
    cards = ['K', 'Q', 'J']
    for _ in range(iterations):
        random.shuffle(cards)
        cfr(cards, '', 1, 1, nodes)
    
    with open('cfr_training_data.pkl', 'wb') as f:
        pickle.dump(nodes, f)
    print("Training complete. Strategy saved.")

if __name__ == '__main__':
    train(1000000)
