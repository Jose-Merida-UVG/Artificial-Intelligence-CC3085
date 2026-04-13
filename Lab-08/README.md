# Lab 8: Constraint Satisfaction Problems

## Summary

This assignment explores Constraint Satisfaction Problems (CSPs) through both theoretical analysis and practical implementation of a microservice-to-server allocation problem.

- **MCV & LCV Heuristics**: Analysis of why MCV (Most Constrained Variable) forces early failures by targeting variables with the fewest remaining options, while LCV (Least Constraining Value) maximizes success by preserving neighbors' flexibility. The two operate at different levels — variable selection vs. value selection — and together make Backtracking efficient in practice.

- **CSP Factor Modeling**: Design of a conditional anti-affinity factor for hospital shift scheduling (Dr. Perez and Dr. Gomez cannot share weekday shifts but may share weekend shifts), formalized with variables per doctor-day pair, shift domains, and a piecewise factor function.

- **Backtracking vs. Local Search**: Comparative analysis applied to a videogame matchmaking scenario with millions of users, arguing that ICM's real-time "good enough" solutions outweigh Backtracking's optimal but computationally infeasible guarantees at scale.

- **CSP Formulation**: Formal modeling of the allocation as a CSP triple $(\mathcal{X}, \mathcal{D}, \mathcal{F})$ with 8 variables (microservices), shared domain $\{S_1, S_2, S_3\}$, binary anti-affinity factors for pairs $(M_1,M_2)$, $(M_3,M_4)$, $(M_5,M_6)$, $(M_1,M_5)$, and a global capacity factor limiting each server to at most 3 microservices.

- **Backtracking Search**: Systematic depth-first exploration of the assignment tree ($3^8 = 6{,}561$ possible states). A recursive implementation assigns servers sequentially and backtracks on constraint violations.

- **Optimized Backtracking (MRV + Forward Checking)**: Extends basic backtracking with Minimum Remaining Values heuristic (fail-first variable ordering) and Forward Checking (proactive domain pruning of anti-affine neighbors). Detects dead ends earlier by eliminating empty domains before recursing.

- **Beam Search**: Maintains the $K$ best partial assignments at each level, scored by a violation-counting heuristic. Not complete — small beam widths may discard all paths to a valid solution.

- **Local Search (ICM)**: Iterated Conditional Modes starts from a random complete assignment and greedily reassigns each microservice to the server minimizing total violations. Terminates on a valid solution, a local optimum, or an iteration limit.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering CSP formulation, algorithm analysis, and comparative results. |
| `Informe.tex` | Original LaTeX source for the report. |
| `ConstraintSatisfaction.ipynb` | Jupyter notebook with CSP modeling, four solver implementations, and a comparative performance analysis with timing and visualization. |

## Key Results

All four algorithms find a valid (zero-violation) solution on this small instance. The search space is only $3^8 = 6{,}561$ assignments, so execution times are sub-millisecond. The optimized backtracking with MRV + Forward Checking explores fewer nodes than plain backtracking by detecting dead ends earlier, while Beam Search and ICM offer alternative trade-offs between completeness and efficiency.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook ConstraintSatisfaction.ipynb
```
