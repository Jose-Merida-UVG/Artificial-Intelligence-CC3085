# Lab 5: Reinforcement Learning

## Summary

This assignment explores reinforcement learning theory and practice, implementing Q-Learning on the stochastic FrozenLake environment.

- **Exploration vs. Exploitation**: Analysis of the restaurant analogy — a Greedy agent always returns to its first satisfactory option and risks never discovering a far better one. Epsilon-Greedy ($\varepsilon = 0.1$) balances this, but every exploratory step is a sub-optimal decision if the current best truly is optimal.

- **On-Policy vs. Off-Policy (SARSA vs. Q-Learning)**: In a robot-near-cliff scenario, SARSA (on-policy) is safer during training because it evaluates the policy it actually follows — including exploratory, risky actions and their penalties. Q-Learning (off-policy) assumes future optimal behavior, ignoring the real cost of exploration near danger.

- **Bootstrapping**: Explained via a driving analogy — correcting course while moving rather than waiting for a crash. Critical for continuous (non-episodic) tasks like server temperature control, where there is no episode end to trigger a Monte Carlo retrospective.

- **Q-Learning on FrozenLake**: From-scratch tabular Q-Learning implementation with epsilon-greedy exploration and exponential decay, trained on the stochastic (`is_slippery=True`) 4×4 grid.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering the three theoretical topics above. |
| `Informe.tex` | Original LaTeX source for the report. |
| `FrozenLake.ipynb` | Q-Learning implementation, training loop, evaluation, and GIF generation. |
| `gym-results/success.gif` | Animated GIF of a successful episode after training. |
| `gym-results/rl-video-episode-0.mp4` | Raw MP4 recording of the same episode. |

## Implementation Details

**Environment**: `FrozenLake-v1` from Gymnasium with `is_slippery=True` — each action has a 1/3 probability of sliding in each of the two perpendicular directions. 16 states, 4 actions.

**Q-Update rule**: $Q(s,a) \leftarrow Q(s,a) + \alpha [R + \gamma \max_{a'} Q(s',a') - Q(s,a)]$

**Hyperparameters**: $\alpha = 0.8$, $\gamma = 0.95$, $\varepsilon_0 = 1.0$, $\varepsilon_{\min} = 0.01$, decay = 0.999, episodes = 10,000.

The training and evaluation functions are the same — evaluation is triggered by passing `alpha=0, epsilon=0` to freeze the Q-table and disable exploration.

## Key Results

| Phase | Result |
| :---- | :----- |
| Training (last 1,000 episodes) | 48.3% win rate (includes exploration noise) |
| Greedy evaluation (10 episodes) | **6/10 wins (60%)** |

The optimal policy is counter-intuitive: from the starting state (0), the agent moves **left** — into the wall. With `is_slippery=True`, moving down or right carries a 1/3 chance of sliding into a hole, while bouncing off the left wall is safe and drifts the agent toward higher-value states. The emergent strategy involves hugging the left and bottom walls to exploit the stochastic sliding toward the goal.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook FrozenLake.ipynb
```
