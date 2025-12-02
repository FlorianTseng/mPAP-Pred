# Repository Overview

This repository contains two main directories: **`SISSO`** and **`XGB-TabNet-Results`**.  
They correspond to the symbolic regression workflow based on SISSO and the machine-learning regression results using XGBoost and TabNet, respectively.

---

## 📁 SISSO

The **`SISSO`** directory includes:

- **`SISSO.in`** – the input file used in our implementation  
- **`SISSO.out`** – the corresponding SISSO output

Due to privacy considerations, the original experimental dataset cannot be distributed.  
However, we provide a **toy dataset** generated via **bootstrap sampling + noise injection**, ensuring that the distributions of both targets and features resemble those of the original data while containing no identifiable information.

For details regarding the hyperparameter configuration in `SISSO.in`, we strongly recommend consulting the official guide:

👉 [**SISSO Guide v3.5**](https://github.com/rouyang2017/SISSO/blob/master/SISSO_Guide_v3.5.pdf)

---

## 📁 XGB-TabNet-Results

The **`XGB-TabNet-Results`** directory showcases:

- The performance of **XGBoost** on the task  
- The performance of **TabNet** under different learning-rate settings

These results highlight the comparative behaviour of tree-based and deep-learning-based tabular models in the same prediction scenario.

---
