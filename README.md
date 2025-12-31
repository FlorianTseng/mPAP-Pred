# Repository Overview

This repository contains three main directories: **`SISSO`**, **`XGB-TabNet-Results`**, and **`Pred`**. These components provide the inputs, outputs, performance evaluations, and prediction utilities used in our study [*Artificial intelligence-driven multivariate integration for pulmonary arterial pressure prediction in pulmonary hypertension*](http://dx.doi.org/10.1038/s41746-025-02233-6).

---

## 📁 SISSO

The `SISSO` directory includes:

- **SISSO.in** – the input file used in our SISSO implementation  
- **SISSO.out** – the corresponding output file  

For privacy reasons, the original clinical dataset cannot be released. However, we provide a **toy dataset** generated using a *bootstrap + noise* strategy to approximate the distributions of both the target variable and the features.

For details regarding the hyperparameter settings in `SISSO.in`, we recommend consulting the official [SISSO Guide](https://github.com/rouyang2017/SISSO/blob/master/SISSO_Guide_v3.5.pdf).

---

## 📁 XGB-TabNet-Results

The `XGB-TabNet-Results` directory presents:

- The performance of **XGBoost**
- The performance of **TabNet** under different learning-rate settings  

These results illustrate how various model configurations behave on our dataset.

---

## 📁 Pred

The `Pred` directory provides a utility for predicting **mPAP** of new cases using the symbolic SISSO formulas.  

To generate predictions:

1. Fill in the **`new-patients.csv`** file according to the variable definitions described in the paper.
2. Run **`pred-new.py`** to compute predictions.
3. The results will be saved in **`new-results.csv`**.

---

If you need further guidances, feel free to ask!
