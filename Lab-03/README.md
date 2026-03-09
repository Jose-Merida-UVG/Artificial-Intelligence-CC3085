# Lab 3: Naive Bayes, SVM & Decision Trees

## Summary

This assignment explores three classical supervised learning algorithms through both theoretical analysis and practical implementation.

- **Naive Bayes -- The Independence Assumption**: Analysis of the consequences of assuming feature independence, and practical application to a spam filtering task.

- **Support Vector Machines**: Classification applied to a sports league dataset, examining kernel selection and margin behavior.

- **Decision Trees**: Discussion of tree-based model design decisions and their impact on generalization.

## Deliverables

- **Informe.pdf**: Written report with theoretical analysis, model comparisons, and discussion.

- **Informe.tex**: Original LaTeX source for the report.

- **SpamFilter.ipynb**: Jupyter notebook implementing a Naive Bayes spam classifier.

- **League.ipynb**: Jupyter notebook implementing SVM-based classification on a sports league dataset.

- **data/**: Directory containing the datasets used by the notebooks.

## Execution

Before running the notebooks, make sure [Python](https://www.python.org) is installed.

```bash
pip install -r requirements.txt
jupyter notebook SpamFilter.ipynb
jupyter notebook League.ipynb
```
