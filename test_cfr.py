import unittest
import pickle
import random
from cfr_trainer import cfr, KuhnNode, train

def load_strategy():
    with open('cfr_training_data.pkl', 'rb') as f:
        return pickle.load(f)

class TestCFR(unittest.TestCase):
    def setUp(self):
        self.nodes = {}
        self.cards = ['K', 'Q', 'J']
    
    def test_cfr_convergence(self):
        train(1000)
        strategy = load_strategy()
        self.assertTrue(isinstance(strategy, dict))
        self.assertTrue(all(isinstance(v, KuhnNode) for v in strategy.values()))
        
        for key, node in strategy.items():
            self.assertTrue(abs(sum(node.get_average_strategy()) - 1.0) < 0.01)

    def test_strategy_application(self):
        strategy = load_strategy()
        cards = ['K', 'Q', 'J']
        random.shuffle(cards)
        history = ''
        ai_card = cards[1]

        # Ensure we fetch the strategy from KuhnNode
        node = strategy.get(str(ai_card) + history, KuhnNode())
        strategy_used = node.get_average_strategy()  # Fix applied here

        self.assertEqual(len(strategy_used), 2)
        self.assertTrue(all(0 <= s <= 1 for s in strategy_used))

if __name__ == '__main__':
    unittest.main()
