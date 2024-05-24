from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

class SimplePerceptron:
    def __init__(self, input_dim):
        self.weights = np.random.rand(input_dim)
        self.bias = np.random.rand()

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

perceptron = SimplePerceptron(input_dim=2)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.json
    X = np.array(data["input"])
    prediction = perceptron.predict(X)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
