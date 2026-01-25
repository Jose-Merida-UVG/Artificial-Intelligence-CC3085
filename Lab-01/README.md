# Lab 1: Performance Metrics

## 📖 Summary

This assignment explores the selection and application of performance metrics in AI models, ranging from business logic
dilemmas to technical implementation of data cleaning pipelines and regression metrics.

- **Business Dilemma Analysis**: Evaluation of Precision, Recall, Accuracy, and Adjusted R-Squared in real-world scenarios (Medical screening, Spam filtering, and Real Estate valuation)

- **Data Engineering Pipeline**: Manual implementation of a data processing pipeline in Python, including synthetic dataset generation, mean-based imputation, and manual undersampling
  for class imbalance—built without "black-box" cleaning libraries.

- **Regression Metrics & Norms**: From-scratch implementation of MAE and RMSE to analyze the mathematical sensitivity of L1, L2, and Chebyshev (bonus) norms when dealing with
  catastrophic outliers in critical contexts like medicine.

## 📂 Deliverables

- **Informe.pdf**: In-depth analysis of performance metrics, business case justifications, and code excerpts.

- **Informe.tex**: Original LaTeX file used for writing the report.

- **task_2.py**: Python script containing the manual data cleaning logic (Artificial DF creation, NaN handling and undersampling).

- **task_3.py**: Python script featuring the manual implementations of RMSE/MAE and the comparison analysis printed to the console.

The 'juice' of the assignment is all in Informe.pdf, however, you're still welcome to execute the Python scripts.

## 🚀 Execution

Before running the scripts, you must have [python](https://www.python.org) installed.

Requirement installation

```bash
pip install -r requirements.txt
```

Task 2

```bash
python3 task_2.py
```

Task 3

```bash
python3 task_3.py
```
