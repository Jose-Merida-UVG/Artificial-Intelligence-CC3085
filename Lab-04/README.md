# Lab 4: SGD & Neural Networks

## Summary

This assignment dives into optimization with Stochastic Gradient Descent and introduces neural network fundamentals through the Perceptron, with theoretical analysis of common failure modes.

- **The Step Size Dilemma**: Geometric explanation of SGD oscillation on the error surface when the learning rate is too large, and why learning rate decay ($\eta = 1/\sqrt{t}$) is strictly better than a constant small rate — it escapes local minima aggressively at first, then settles with fine-tuned precision.

- **Vanishing Gradients**: Mathematical walkthrough of why stacking Sigmoid activations kills the gradient signal during backpropagation. Each layer multiplies by $\sigma'(z) \leq 0.25$, causing the gradient to decay exponentially. ReLU (derivative = 1 for positive inputs) is the fix.

- **Depth vs. Width**: Analysis of why a 10-layer network with 10 neurons each outperforms a 1-layer network with 100 neurons at similar parameter counts — depth enables hierarchical compositionality; width must learn the global function all at once.

- **Gradient Descent Variants**: From-scratch implementation of Batch GD, SGD, and Mini-Batch GD on a noisy cubic polynomial, benchmarked against each other.

- **Perceptron**: From-scratch implementation on the Iris dataset (Setosa vs. Versicolor), with discussion of its limitations vs. SVM.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Written report with TikZ diagrams of the error surface, sigmoid derivative, and backpropagation chain rule. |
| `Informe.tex` | Original LaTeX source for the report. |
| `SGD.ipynb` | Gradient descent variants (Batch, SGD, Mini-Batch) on a synthetic noisy cubic polynomial. |
| `Perceptron.ipynb` | Perceptron classifier on Iris (Setosa vs. Versicolor) with decision boundary visualization. |

## Key Results

**SGD.ipynb** — Synthetic dataset: $y = 2x^3 - 3x^2 + 5x + 3$ with Gaussian noise, 1,000 points, normalized. Hyperparameters: lr = 0.001, 500 epochs.

| Method | Final MSE Loss | Notes |
| :----- | :------------- | :---- |
| Batch GD | 0.1845 | Only 500 weight updates total — not enough to converge |
| SGD | 0.0218 | 500,000 weight updates — fast but noisy near minimum |
| Mini-Batch (32) | **0.0217** | Best balance of stability and convergence speed |

The comparison-by-epoch is inherently unfair (BGD makes 1 update per epoch vs. SGD's 1,000). The interesting result is how dramatically more updates per epoch affects convergence even with a small epoch budget.

**Perceptron.ipynb** — Iris dataset, 2 features (sepal length/width), 100 samples. lr = 0.001, 10,000 epochs.
- Final accuracy: **100%** — expected, since Setosa and Versicolor are cleanly linearly separable.
- The decision boundary stops updating the moment zero training errors are achieved, meaning multiple runs produce different valid boundaries. Unlike SVM, the Perceptron has no notion of margin maximization, so it would generalize worse on unseen data.

## Execution

```bash
pip install -r requirements.txt
jupyter notebook SGD.ipynb
jupyter notebook Perceptron.ipynb
```
