# Linear Regression From Scratch

import numpy as np


class LinearRegression:

    def __init__(self, lr=0.01, epochs=1000):

        # 👶 Baby model
        self.w = 0
        self.b = 0

        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):

        n = len(X)

        for epoch in range(self.epochs):

            # 🔮 Prediction
            y_pred = self.w * X + self.b

            # 😭 How badly did we fail?
            dw = (-2/n) * np.sum(X * (y - y_pred))
            db = (-2/n) * np.sum(y - y_pred)

            # 🧠 Learning from mistakes
            self.w -= self.lr * dw
            self.b -= self.lr * db

            if epoch % 100 == 0:

                loss = np.mean((y - y_pred)**2)

                print(
                    f"Epoch {epoch} | Loss {loss:.4f}"
                )

    def predict(self, X):

        return self.w * X + self.b