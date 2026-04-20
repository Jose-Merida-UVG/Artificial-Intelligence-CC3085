# Lab 9: Bayesian Networks & Markov Networks

## Summary

This assignment explores probabilistic graphical models through theoretical analysis and practical implementation of Bayesian Networks and Markov Networks, with focus on exact inference and causal reasoning.

- **Bayes' Rule & Diagnostic Reasoning**: Understanding how Bayes' Rule transforms diagnostic reasoning (from effect to cause) into causal reasoning. In credit card fraud detection, it's computationally easier to estimate $P(\text{Observable Evidence} \mid \text{Cause})$ in production than the inverse $P(\text{Cause} \mid \text{Observable Evidence})$, since fraudulent transactions produce specific observable patterns that can be learned directly from data.

- **Bayesian Networks vs. Markov Networks**: Comparative analysis of when to use each model. Bayesian Networks excel in modeling causal relationships and directed dependencies (e.g., engine faults causing sensor anomalies), while Markov Networks are ideal for symmetric undirected relationships (e.g., pixel segmentation in medical imaging where neighboring pixels influence each other symmetrically).

- **Computational Intractability of Normalization**: Analysis of why computing the normalization constant $Z$ in Markov Networks is NP-hard. With $n=50$ boolean variables, the joint space has $2^{50}$ assignments — a computationally prohibitive $1.1 \times 10^{15}$ combinations. Exact inference becomes infeasible at scale, motivating the use of approximate algorithms like MCMC (Gibbs Sampling) to explore the state space stochastically without computing $Z$ explicitly.

- **Exact Inference by Enumeration**: Implementation of Bayesian Network inference using the chain rule: $P(B, E, A) = P(B) \cdot P(E) \cdot P(A \mid B, E)$. Enumeration over all $2^3 = 8$ assignments allows marginal inference via Bayes' Rule: $P(\text{query} \mid \text{evidence}) = \frac{P(\text{query}, \text{evidence})}{P(\text{evidence})}$.

- **Explain Away Effect**: Practical demonstration of d-separation in Bayesian Networks. Two independent causes (Burglary and Earthquake) become dependent when conditioned on their shared effect (Alarm). Confirming the earthquake as cause reduces the probability of burglary from $\approx 0.50$ back to its prior $\epsilon = 0.01$, as the earthquake "explains away" the alarm, eliminating the need to invoke the alternative cause.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering Bayes' Rule application, Markov vs. Bayesian network comparison, and computational intractability analysis. |
| `Informe.tex` | Original LaTeX source for the report. |
| `Inference.ipynb` | Jupyter notebook with Bayesian Network modeling, exact inference by enumeration, marginal probability calculation, and Explain Away effect demonstration. |

## Key Results

**Burglar-Earthquake-Alarm Network** (discrete variables with uniform priors $\epsilon = 0.01$):

| Query | Result | Interpretation |
| :--- | :------ | :---------- |
| $P(A=1)$ | 0.0199 | Prior probability that alarm sounds (robo OR earthquake) |
| $P(B=1 \mid A=1)$ | 0.5025 | After alarm triggers, robo and earthquake are equally likely |
| $P(B=1 \mid A=1, E=1)$ | 0.0100 | Confirming earthquake "explains away" the alarm; robo probability collapses to prior |

The Explain Away effect shows how causal knowledge restructures probability: confirming one cause decreases the posterior of independent alternative causes, despite those causes being marginally independent before observing the effect.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook Inference.ipynb
```
