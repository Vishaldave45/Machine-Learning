# 🚨 Edge Cases

## 1. Outliers

Normal Data

1000 sqft → 50L

1200 sqft → 60L

1500 sqft → 70L

Outlier

1000 sqft → 500 Crore

Problem:

Line shifts dramatically.

Solution:

Remove outliers.

Use Robust Regression.

---

## 2. Non Linear Data

Linear Regression only fits straight lines.

Solution:

Polynomial Regression.

---

## 3. Multicollinearity

Area in sqft

Area in square meter

Both represent same thing.

Problem:

Unstable coefficients.

Solution:

Remove correlated features.