import numpy as np

class LinearRegression:
    
    def __init__(self, learning_rate=0.01, epcohs=100):
        self.lr = learning_rate
        self.epcohs = epcohs 
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        # number of samples and features
        n_samples, n_features = X.shape
        
        # Initial weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient Descent 
        for _ in range(self.epcohs):
            # Predict 
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # Gradient computation
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            # Update weights and bias
            self.weights -= self.lr * dw
            self.bias -= self.lr * db
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
    
