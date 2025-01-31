# Kuhns-Poker-CFR-Bot
# Kuhn Poker Bot with Counterfactual Regret Minimization (CFR)

## Overview

This project implements a poker-playing AI for Kuhn Poker using Counterfactual Regret Minimization (CFR). The bot is trained to make optimal decisions over thousands of iterations.

## Project Structure

```
/kuhn_poker_bot
│── cfr_trainer.py           # CFR Training Algorithm
│── kuhn_poker.py            # Kuhn Poker Game Engine
│── play_bot.py              # AI playing against a user
│── test_cfr.py              # Automated tests
│── cfr_training_data.pkl    # Trained strategy data
│── README.md                # Project documentation
```

## How to Train the AI

Run the training script to generate a trained strategy:

```
python cfr_trainer.py
```

This will generate `cfr_training_data.pkl`, which stores the trained AI strategy.

## Playing Against the AI

Once training is complete, play against the AI:

```
python play_bot.py
```

The AI will use the trained strategy to make optimal decisions.

## Running Tests

To ensure everything is working correctly, run the test suite:

```
python -m unittest test_cfr.py
```

## Explanation of CFR

Counterfactual Regret Minimization (CFR) is an iterative self-play algorithm where the AI learns optimal strategies by minimizing regret over many iterations.

- **Regret Tracking**: The bot tracks how much better an action could have performed.
- **Strategy Update**: The AI updates its strategy using the regret values.
- **Convergence**: Over time, the AI learns an optimal Nash equilibrium strategy.

## Future Improvements

- Implementing multiplayer variants.
- Adding reinforcement learning for deeper decision-making.
- Improving the UI for a better playing experience.

