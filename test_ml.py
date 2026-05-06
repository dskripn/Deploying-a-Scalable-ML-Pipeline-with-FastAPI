
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_random_forest():
    """
    Test that train_model returns a RandomForestClassifier instance.

    """
    # Your code here
    X_train = np.array([
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 0.0]
    ])
    y_train = np.array([0, 1, 1, 0])

    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_inference_output_shape_matches_input():
    """
    Test that inference returns one prediction for each input row.

    """
    # Your code here
    X_train = np.array([
        [0.0, 1.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 0.0]
    ])
    y_train = np.array([0, 1, 1, 0])

    model = train_model(X_train, y_train)
    preds = inference(model, X_train)

    assert len(preds) == X_train.shape[0]

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_range():
    """
    Test that precision, recall, and F1 score are all between 0 and 1.
    
    """
    # Your code here
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 1, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
