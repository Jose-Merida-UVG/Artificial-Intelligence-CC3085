# Lab 6: Minimax & Adversarial Search

## Summary

This assignment explores adversarial search and game-playing AI through both theoretical analysis and practical implementation of a Connect Four agent using the Minimax algorithm with Alpha-Beta pruning.

- **The Minimax Algorithm**: Implementation of the classic adversarial search technique for two-player zero-sum games. Core recursive strategy where the maximizing player (AI) selects moves that maximize score while the minimizing player (opponent) selects moves that minimize score. Includes theoretical analysis showing that depth-10 search on chess ($b=30$) would take 18.7 years without optimization.

- **Alpha-Beta Pruning**: Critical optimization that reduces the search space from $O(b^d)$ to $O(b^{d/2})$ in the best case without changing the algorithm's result. Maintains alpha (best MAX can guarantee) and beta (best MIN can guarantee) bounds to prune branches when `alpha >= beta`. Achieves **93.86% node reduction** in practice at depth 4.

- **Strategic Heuristic Evaluation**: Custom evaluation function that scores board positions using center column preference (+6 per piece), asymmetric defensive priority (opponent threats -80 vs. own opportunities +50), and sliding window analysis across all 69 possible winning lines (horizontal, vertical, diagonal). The asymmetry reflects that blocking an opponent's 3-in-a-row is more urgent than creating your own second opportunity.

- **Interactive Game Application**: Full-featured Streamlit web app with two modes — play against the AI agent (depth-6 search) or watch the agent play against a random baseline. Includes auto-play showcase, move-by-move controls, and clean minimal UI.

## Deliverables

| File                | Description                                                                                                          |
| :------------------ | :------------------------------------------------------------------------------------------------------------------- |
| `Informe.pdf`       | Written report covering Minimax complexity analysis, Alpha-Beta effectiveness, and evaluation function design.       |
| `Informe.tex`       | Original LaTeX source for the report.                                                                                |
| `ConnectFour.ipynb` | Jupyter notebook with three tasks: game logic & Minimax, Alpha-Beta pruning, and strategic heuristic implementation. |
| `app.py`            | Streamlit web application for interactive gameplay with agent vs. human and agent vs. random modes.                  |
| `connect4_game.py`  | Core game logic: 6×7 board representation, move validation, win detection, and terminal state checking.              |
| `agent.py`          | Agent implementations: `RandomAgent`, `MinimaxAgent`, `AlphaBetaAgent`, and `MyAgent` wrapper.                       |
| `README.md`         | Quick start guide with installation instructions and agent customization methods.                                    |

> The Streamlit app (`app.py`) provides the best demonstration of the agent's capabilities. The notebook contains the step-by-step implementation and performance analysis.

## Game Rules & Implementation

**Environment**: Connect Four on a 6×7 grid (rows × columns). Players alternate dropping pieces into columns; gravity pulls pieces to the lowest available row. First player to get 4 pieces in a row (horizontal, vertical, or diagonal) wins.

**Board Representation**: NumPy array with values `0` (empty), `1` (human/red), `2` (AI/yellow).

**Agent Configuration**: `AlphaBetaAgent` with depth-6 search and multi-criteria heuristic evaluation. The agent explores ~172 nodes per move (vs. ~2,800 for pure Minimax) thanks to Alpha-Beta pruning.

## Key Results

**Alpha-Beta Pruning Efficiency** (depth=4, empty board):

| Algorithm    | Nodes Explored | Reduction  |
| :----------- | :------------- | :--------- |
| Pure Minimax | ~2,800         | —          |
| Alpha-Beta   | ~172           | **93.86%** |

This 16.3× speedup enables the agent to search 2 plies deeper in the same time budget — a critical advantage in real-time gameplay.

**Heuristic Evaluation Function** — Scores positions across 69 possible 4-cell windows:

- **Center column preference**: +6 per piece (column 3 participates in the most winning lines)
- **Threat detection**: Own 3-in-a-row with empty space (+50), opponent 3-in-a-row (-80)
- **Development potential**: Own 2-in-a-row with 2 empty (+10), opponent 2-in-a-row (-15)
- **Terminal states**: Victory (+100,000), defeat (-100,000), draw (0)

The asymmetric defensive priority (-80 vs. +50) implements "paranoid conservatism" — blocking opponent threats is more urgent than creating redundant winning opportunities. This reflects game theory: one opponent win ends the game; multiple own winning lines don't compound.

**Strategic Insight**: At depth 6, the agent frequently makes counter-intuitive opening moves (e.g., moving left into the wall) because with `is_slippery=False` in Connect Four, the deterministic physics allow precise setup of winning forks 5-6 moves ahead. Against intermediate human players, the agent wins consistently by forcing the opponent into zugzwang-like positions where all moves lead to defeat.

## Video Demo

Watch the agent in action: **[Connect Four AI Demo](https://youtu.be/wat_djyqZK4)**

## Execution

```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app (recommended)
streamlit run app.py

# Or explore the notebook implementation
jupyter notebook ConnectFour.ipynb
```

**Game Modes**:

- **Play vs Agent**: Human (red) vs. AI (yellow) — click column buttons to drop pieces
- **Watch: Agent vs Random**: Automated showcase with auto-play and step-through controls
