# Hoja de Trabajo 2: Markov Decision Processes

## Summary

This assignment explores the theoretical foundations of Markov Decision Processes and implements Value Iteration on the stochastic FrozenLake environment.

- **The Gambler's Fallacy & the Markov Property**: Mathematical argument for why including a win/loss history in a Blackjack agent's state is irrelevant (or a violation) of the Markov Property. In a truly random game, $P(s_{t+1} | s_t, a_t) = P(s_{t+1} | s_0, \ldots, s_t, a_t)$ — history provides no additional information over the current state. What IS critical: available actions, transition distributions, and termination conditions.

- **The Discount Factor Dilemma ($\gamma$)**: Two contrasting scenarios — a rescue robot in a burning building (requires $\gamma \approx 0$: act now, nearby victims first) vs. a pension fund investment agent over 30 years (requires $\gamma \approx 1$: sacrifice short-term gains for long-term stability). Each extreme of $\gamma$ leads to pathological behavior in the wrong context.

- **Stochastic vs. Deterministic Policies**: Argues that even in stochastic environments, a deterministic policy is sufficient for optimality. The Bellman equation computes the *expected value* over all transitions — the best action is always the one with the highest expected value, with no mathematical incentive to randomize.

- **Living Penalty ($r$) Analysis**: Traces how the step reward shapes agent behavior. $r = 0$ produces an infinitely patient agent that avoids all risk even at extreme cost (hugging walls indefinitely). $r = -10$ produces a panicked agent that crosses minefields to save 2 steps. The FrozenLake results in Task 2 directly validate this.

- **Value Iteration on FrozenLake**: From-scratch MDP model with stochastic transitions, Bellman-optimal value iteration, policy extraction, and visualization.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering all four theoretical topics above. |
| `Informe.tex` | Original LaTeX source for the report. |
| `FrozenLake.ipynb` | MDP implementation, value iteration, policy extraction, and heatmap visualization. |

## Implementation Details

**MDP Model (`FrozenLakeMDP` class)**:
- 4×4 grid, 16 states, 4 actions (N/S/E/W).
- Grid: `S F F F / F H F H / F F F H / H F F G` — 4 holes (states 5, 7, 11, 12) and 1 goal (state 15).
- Stochastic transitions: each action has 1/3 probability of moving in the intended direction and 1/3 each of the two perpendicular directions.
- Rewards: +1.0 at goal, 0.0 elsewhere. All terminal states absorbing.

**Value Iteration**: Bellman optimality equation iterated until $\max_s |V_{k+1}(s) - V_k(s)| < \varepsilon$.
Hyperparameters: $\gamma = 0.9$, $\varepsilon = 10^{-5}$.

**Visualization**: Side-by-side — optimal policy grid (arrow symbols per state) and V(s) heatmap using the `mako` colormap.

## Key Results

The optimal policy is counter-intuitive: from the starting state (0), the optimal action is to move **left** — into the wall.

- Moving **down** or **right**: 1/3 chance of sliding into hole (state 5).
- Moving **left**: 2/3 chance of staying in place (wall bounce) + 1/3 chance of reaching state 4, which has higher value than state 1.

This wall-bouncing strategy is a direct result of the stochastic slippery mechanic and a living penalty of 0 — the agent is willing to be patient as long as it avoids holes. State 14 has the highest non-terminal value: it cannot directly fall into a hole and carries a 1/3 probability of reaching the goal on any action.

## Execution

```bash
pip install numpy matplotlib seaborn jupyter
jupyter notebook FrozenLake.ipynb
```
