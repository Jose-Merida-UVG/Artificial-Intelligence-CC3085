# Lab 1: Performance Metrics

## Summary

This assignment explores the selection and application of performance metrics in AI models — from business logic dilemmas to hands-on data engineering and from-scratch implementations of regression error metrics.

- **Business Dilemma Analysis**: Three case studies requiring metric selection justification for real-world AI products. Covers why Accuracy alone is dangerous for imbalanced datasets, when to prioritize Recall over Precision (and vice versa), and why Adjusted $R^2$ is the correct metric when adding features to a regression model.

- **Data Engineering Pipeline**: Manual implementation of a data processing pipeline in Python — synthetic dataset generation, mean-based imputation for missing values, and manual undersampling for class imbalance — built without any "black-box" cleaning libraries.

- **Regression Metrics & Norms**: From-scratch implementation of MAE and RMSE to analyze the mathematical sensitivity of $L_1$ and $L_2$ norms when dealing with catastrophic outliers, with a discussion of the Chebyshev ($L_\infty$) norm as a bonus.

## Deliverables

| File | Description |
| :--- | :---------- |
| `Informe.pdf` | Full written report: business case justifications, code excerpts, and mathematical analysis of each metric. |
| `Informe.tex` | Original LaTeX source for the report. |
| `task_2.py` | Data engineering script: synthetic DataFrame creation, NaN imputation, and manual undersampling. |
| `task_3.py` | Regression metrics script: from-scratch RMSE and MAE implementations with outlier sensitivity analysis. |

> The core of this assignment lives in `Informe.pdf`. The Python scripts are self-contained and runnable.

## Key Results

- Given `y_real = [100, 150, 200, 250, 300]` and `y_pred = [110, 140, 210, 240, 500]` (one catastrophic outlier):
  - **MAE = 48.0**
  - **RMSE = 89.89** — nearly **1.87×** the MAE, illustrating how $L_2$ aggressively penalizes large errors.
- The medication dosage analogy in the report makes the case for RMSE in safety-critical contexts: one patient receiving 3× the intended dose is fundamentally different from ten patients each receiving a small over/under-dose.

## Execution

Dependencies for this lab are `numpy` and `pandas` (task_2 only) and the standard library `math` (task_3).

```bash
pip install numpy pandas
```

```bash
python3 task_2.py
python3 task_3.py
```
