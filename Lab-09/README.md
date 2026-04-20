# Lab 9: Bayesian Networks & Markov Networks

## Summary

This assignment explores probabilistic graphical models through theoretical analysis and practical implementation of Bayesian Networks and Markov Networks, with focus on causal reasoning, model selection, and computational tractability.

- **Bayes' Rule & Diagnostic Reasoning**: Understanding how Bayes' Rule transforms causal reasoning into diagnostic inference. In credit card fraud detection systems, $P(\text{Observable Evidence} \mid \text{Fraud})$ is easier to estimate from historical data (observing fraud patterns), while $P(\text{Fraud} \mid \text{Observable Evidence})$ must be derived via Bayes' Rule using the fraud base rate prior. Production systems leverage this asymmetry: estimate the causal direction from labeled data, then invert using Bayes' Rule to obtain the diagnostic probability the system needs.

- **Bayesian Networks vs. Markov Networks**: Comparative analysis of directed vs. undirected graphical models. Bayesian Networks model causal hierarchies with directed edges (e.g., broken engine parts → sensor anomalies); factorization follows the chain rule respecting causal order. Markov Networks model symmetric undirected relationships (e.g., medical image segmentation where neighboring pixels influence each other symmetrically); they use factors on cliques rather than conditional probabilities.

- **Computational Intractability of Normalization**: Analysis of why exact inference on Markov Networks becomes prohibitive at scale. With $n=50$ boolean variables, computing the normalization constant $Z$ requires summing over $2^{50} \approx 10^{15}$ assignments — at one nanosecond per evaluation, this takes ~11 days of continuous computation. For industrial-scale networks with hundreds or thousands of variables, exact inference is completely infeasible. Solution: approximate algorithms like MCMC (Gibbs Sampling) stochastically explore the state space without explicit enumeration of $Z$.

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
| $P(A=1)$ | 0.0199 | Prior probability that alarm sounds (burglary OR earthquake) |
| $P(B=1 \mid A=1)$ | 0.5025 | After alarm triggers, burglary and earthquake are equally likely |
| $P(B=1 \mid A=1, E=1)$ | 0.0100 | Confirming earthquake "explains away" the alarm; burglary probability collapses to prior |

The Explain Away effect shows how causal knowledge restructures probability: confirming one cause decreases the posterior of independent alternative causes, despite those causes being marginally independent before observing the effect.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook Inference.ipynb
```
