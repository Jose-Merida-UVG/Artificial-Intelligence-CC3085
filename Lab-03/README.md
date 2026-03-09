# Lab 3: Naive Bayes, SVM & Decision Trees

## Summary

This assignment explores three classical supervised learning algorithms through both engineering-oriented theoretical analysis and two practical implementations on real datasets.

- **Naive Bayes — The Independence Assumption**: Analysis of how treating correlated words as independent events causes the model to underestimate true joint probabilities. The practical consequence: a Bayesian spam filter built from scratch on real SMS data.

- **SVM — The Economics of Data**: Mathematical argument for why removing non-support-vector points does not change the decision boundary (only $\alpha_i > 0$ contribute to $w$), and the resulting memory efficiency advantage over KNN at scale.

- **Decision Trees — Greedy Myopia**: Discussion of how greedy tree construction does not guarantee a globally optimal tree, illustrated with a bank vault analogy showing how a sub-optimal initial split can lead to a more compact overall tree.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering the three theoretical topics above. |
| `Informe.tex` | Original LaTeX source for the report. |
| `SpamFilter.ipynb` | Naive Bayes spam classifier built from scratch on a real SMS dataset. |
| `League.ipynb` | SVM (linear + RBF) and Decision Tree classifiers applied to League of Legends match data. |
| `data/spam.txt` | SMS spam dataset — 5,565 messages, tab-separated label and text. |

## Datasets

- **SMS Spam Collection**: 5,565 SMS messages labeled `ham` or `légitime`. Included in `data/spam.txt`.
- **League of Legends Diamond Ranked Games (10 min)**: Kaggle dataset with 40 features from Diamond-rank matches at the 10-minute mark. Downloaded automatically at runtime via `kagglehub`.

## Key Results

**Spam Filter (Naive Bayes from scratch, Laplace smoothing k=1):**

| Model | Accuracy | Ham Precision | Spam Recall | False Positives |
| :---- | :------- | :------------ | :---------- | :-------------- |
| Baseline | 99% | 1.00 | 0.98 | 11 |
| Tuned (threshold = 10) | 98% | 0.98 | 0.89 | **1** |

Adding a classification threshold that only flags spam when `score_spam > score_ham + 10` reduces false positives from 11 to 1 — the correct trade-off for an email filter where losing a legitimate email is the costliest error.

**League of Legends (SVM + Decision Tree):**

| Model | Accuracy | Notes |
| :---- | :------- | :---- |
| SVM Linear | 72% | Simple, efficient, recommended |
| SVM RBF | 72% | Near-identical to linear — data is linearly separable |
| Decision Tree (depth=3) | 71% | Best for communicating results to analysts |

The near-identical Linear and RBF performance suggests a strong "snowball" effect in LoL: more gold, kills, and dragons at minute 10 proportionally and directly increases win probability. The Decision Tree root splits on `blueTotalGold`, and confirmed by real LoL players: early gold (items) is the dominant game factor.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook SpamFilter.ipynb
jupyter notebook League.ipynb
```
