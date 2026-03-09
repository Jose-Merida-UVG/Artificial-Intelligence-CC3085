# Lab 2: Data Preparation, KNN & Bias-Variance

## Summary

This assignment covers data preparation fundamentals, the convexity of logistic regression loss functions, and K-Nearest Neighbors classification with a strong focus on the bias-variance tradeoff.

- **Logistic Regression Convexity**: Theoretical analysis of why MSE cannot be used as the loss function for logistic regression with a sigmoid output — the gradient produces a transcendental equation with no closed-form solution, and the resulting loss surface is non-convex, riddled with local minima where gradient descent gets stuck. Binary cross-entropy is convex by contrast, guaranteeing a global minimum.

- **KNN & Bias-Variance Tradeoff**: Implementation and experimentation with K-Nearest Neighbors on a real phishing detection dataset, exploring how the choice of $k$ affects model complexity and generalization.

- **Data Preparation**: Feature selection via Pearson correlation, stratified train/test split, and MinMax scaling with outlier capping — applied before model training to avoid data leakage.

- **From-Scratch Benchmarking**: Custom implementations of both Logistic Regression (gradient descent) and KNN benchmarked against scikit-learn equivalents.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report covering theoretical questions on convexity, imbalanced KNN, and overfitting. |
| `Informe.tex` | Original LaTeX source for the report. |
| `Notebook.ipynb` | Jupyter notebook with Tasks 2–4: data preparation, from-scratch implementations, and benchmarking. |

## Dataset

**Web Page Phishing Detection Dataset** (via Kaggle) — 11,430 URLs with 87 extracted features, perfectly balanced between phishing and legitimate samples. Downloaded automatically at runtime via `kagglehub`.

- Top correlated features selected: `google_index` (r = 0.731) and `page_rank` (r = 0.511).

## Key Results

**Logistic Regression** (lr = 0.01, 25,000 epochs): Cost converges from 0.6927 → 0.3198, matching scikit-learn's output exactly (87% accuracy) — a direct consequence of the convex loss surface guaranteeing a unique global minimum.

**KNN** (K = 3) — Custom vs. scikit-learn on training data:

| Metric | Custom KNN | scikit-learn KNN |
| :----- | :--------- | :--------------- |
| Accuracy | **0.88** | 0.84 |
| Spam Recall | **0.93** | 0.79 |
| F1 (macro) | **0.88** | 0.84 |

The custom implementation outperforms scikit-learn by handling equidistant points ("hotspots") more fairly — averaging all points within the K-th neighbor radius rather than breaking ties by insertion order. In the context of phishing detection, **Recall is prioritized**: a false negative allows a user to submit credentials to a fake site; a false positive is just an IT ticket.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook Notebook.ipynb
```
