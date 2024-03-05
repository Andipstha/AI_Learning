# import pandas as pd
# from sklearn.model_selection import train_test_split 
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics

# # Load the data
# dataset = pd.read_csv('/path/to/your/data.csv')

# # Prepare the data
# X = dataset['x'].values.reshape(-1,1)
# y = dataset['y'].values.reshape(-1,1)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# # Train the algorithm
# regressor = LinearRegression()  
# regressor.fit(X_train, y_train)

# # Make predictions using the testing set
# y_pred = regressor.predict(X_test)

# # Compare the actual output values with the predicted values
# df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
# print(df)

import numpy as np

class LinearRegression:
    def init(self):
        self.slope = None
        self.intercept = None
    
    def fit(self, X, y):
        # Calculate mean of X and y
        mean_x = np.mean(X)
        mean_y = np.mean(y)
        
        # Calculate the slope (m)
        numerator = np.sum((X - mean_x) * (y - mean_y))
        denominator = np.sum((X - mean_x) ** 2)
        self.slope = numerator / denominator
        
        # Calculate the intercept (b)
        self.intercept = mean_y - self.slope * mean_x
    
    def predict(self, X):
        if self.slope is None or self.intercept is None:
            raise Exception("Model has not been trained yet. Please fit the model first.")
        
        return self.slope * X + self.intercept

# Example usage:
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

model = LinearRegression()
model.fit(X, y)

print("Slope (m):", model.slope)
print("Intercept (b):", model.intercept)

new_X = 6
predicted_y = model.predict(new_X)
print("Predicted value for X =", new_X, ":",predicted_y)