import numpy as np
import sklearn.datasets as skdata
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

'''
Name: shahid, zunair

Collaborators: khalid, maryam

Collaboration details:

All TODO function like fit fuction, update function, predict, score etc

Summary:

You should answer the questions:
1) What did you do in this assignment?
2) How did you do it?
3) What are the constants and hyper-parameters you used?

Scores:

Report your scores here. For example,

Results on the iris dataset using scikit-learn Perceptron model
Training set mean accuracy: 0.8512
Validation set mean accuracy: 0.7333
Testing set mean accuracy: 0.9286
Results on the iris dataset using our Perceptron model trained with 10 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Results on the iris dataset using our Perceptron model trained with 20 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Results on the iris dataset using our Perceptron model trained with 60 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Using best model trained with 10 steps and tolerance of 0.001
Testing set mean accuracy: 0.0
Results on the wine dataset using scikit-learn Perceptron model
Training set mean accuracy: 0.5625
Validation set mean accuracy: 0.4118
Testing set mean accuracy: 0.4706
Results on the wine dataset using our Perceptron model trained with 10 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Results on the wine dataset using our Perceptron model trained with 20 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Results on the wine dataset using our Perceptron model trained with 60 steps and tolerance of 0.001
Training set mean accuracy: 0.0
Validation set mean accuracy: 0.0
Using best model trained with 10 steps and tolerance of 0.001
Testing set mean accuracy: 0.0
'''

'''
Implementation of Perceptron for multi-class classification
'''


class PerceptronMultiClass(object):

    def __init__(self):
        # Define private variables, weights and number of classes
        self.__weights = None
        self.__n_class = -1
        self.weights = np.zeros(x_train.shape[1] + 1)

    def __update(self, x, y):
        threshold = 0.5 * np.ones([1, x.shape[1]])
        x = np.concatenate([threshold, x], axis=0)
        for n in range(x.shape[1]):
            x_n = np.expand_dims(x[:, n], axis=-1)
            prediction = np.matmul(self.__weights.T, x_n)
            # print('ARGMAX',np.argmax(prediction))
            prediction = np.argmax(np.amax(prediction))
            if prediction != y[n]:
                for c in range(self.__n_class):
                    weights_c = np.expand_dims(self.__weights[:, c], axis=0)
                    # print('dimensions before',weights_c.shape)
                    weights_c = weights_c
                    # print('dimensions after',weights_c.shape)
                    # print('shape of x_n',x_n.shape)
                    if c == prediction:
                        weights_c = weights_c - x_n
                        self.__weights[:, c] = weights_c[:, 0]
                    elif c == y[n]:
                        weights_c = weights_c + x_n
                        self.__weights[:, c] = weights_c[:, 0]
                    else:
                        continue
        # TODO: Implement the member update function


def fit(self, x, y, T=100, tol=1e-3):
    for n in range(y.shape[0]):
        self.__n_class = len(np.unique(y))  # number of classes
    # print(x.shape[0],x.shape[1],self.__n_class) #(d+1,C)
    self.__weights = np.zeros([x.shape[0] + 1, self.__n_class])
    for i in range(self.__n_class):
        self.__weights[0] = -1.0
    # print(self.__weights)
    # print(self.__weights.shape[0],self.__weights.shape[1])
    # finding misclassified examples
    # c_hat = h(x^n(t)) , c_star = y^n ---> unique values determine the __n_class
    # Initialize loss and weights
    prev_loss = 2.0
    pre_weights = np.copy(self.__weights)

    for t in range(T):
        predictions = self.predict(x)
        # loss = 1/N sum n^N
        loss = np.mean(np.where(predictions != y, 1.0, 0.0))
        # stopping convergence
        if loss == 0.0:
            break

        elif loss > prev_loss + tol and t > 2:
            self.__weights = pre_weights
            break
        prev_loss = loss
        pre_weights = np.copy(self.__weights)
        # updating weight vector and class
        self.__update(x, y)
    # TODO: Implement the fit function

def predict(self, x):
    threshold = 0.5 * np.ones((1, x.shape[1]))
    # print('threshold',threshold.shape)
    # x is (d,N), thus concatenate threshold and # X


    x = np.concatenate([threshold, x], axis=0)  # --> (d+1,N)
# print('Size of x',x.shape)
# predict w^T(d+1,N)^T . (d+1,N) --> (1,N)

    predictions = np.matmul(self.__weights.T, x)
# print(predictions.shape[0],predictions.shape[1])
# argmax of predcitions
# print('prediction of values',predictions)
    predictions = np.argmax(np.amax(predictions, axis=1))
# print('predictions after argmax',predictions)
    return predictions

# TODO: Implement the predict function

def getPredictedLabels(self, x):
    '''
            Predicts labels based on feature vector x and computes the mean accuracy
            of the predictions

            Args:
                x : numpy
                    d x N feature vector

            Returns:
                labels
    '''
    # TODO: Implement the score function

def score(self, x, y):
    predcitions = self.predict(x)

    # accuracy score
    scores = np.where(predcitions == y, 1.0, 0.0)
    return np.mean(scores)

    # TODO: Implement the score function

def split_dataset(x, y, n_sample_train_to_val_test=8):
    '''
    Helper function to splits dataset into training, validation and testing sets

    Args:
        x : numpy
            d x N feature vector
        y : numpy
            1 x N ground-truth label
        n_sample_train_to_val_test : int
            number of training samples for every validation, testing sample

    Returns:
        x_train : numpy
            d x n feature vector
        y_train : numpy
            1 x n ground-truth label
        x_val : numpy
            d x m feature vector
        y_val : numpy
            1 x m ground-truth label
        x_test : numpy
            d x m feature vector
        y_test : numpy
            1 x m ground-truth label
    '''
    n_sample_interval = n_sample_train_to_val_test + 2

    train_idx = []
    val_idx = []
    test_idx = []
    for idx in range(x.shape[0]):
        if idx and idx % n_sample_interval == (n_sample_interval - 1):
            val_idx.append(idx)
        elif idx and idx % n_sample_interval == 0:
            test_idx.append(idx)
        else:
            train_idx.append(idx)

    x_train, x_val, x_test = x[train_idx, :], x[val_idx, :], x[test_idx, :]
    y_train, y_val, y_test = y[train_idx], y[val_idx], y[test_idx]

    return x_train, y_train, x_val, y_val, x_test, y_test


if __name__ == '__main__':

    iris_data = skdata.load_iris()
    wine_data = skdata.load_wine()

    datasets = [iris_data, wine_data]
    tags = ['iris', 'wine']
    last_score = 0
    id_ = 0
    models = []
    # TODO: Experiment with 3 different max training steps (T) for each dataset
    train_steps_iris = [10, 20, 60]
    train_steps_wine = [10, 20, 60]

    train_steps = [train_steps_iris, train_steps_wine]

    # TODO: Set a tolerance for each dataset
    tol_iris = 0.001
    tol_wine = 0.001

    tols = [tol_iris, tol_wine]

    for dataset, steps, tol, tag in zip(datasets, train_steps, tols, tags):
        # Split dataset into 80 training, 10 validation, 10 testing
        x = dataset.data
        y = dataset.target
        x_train, y_train, x_val, y_val, x_test, y_test = split_dataset(
            x=x,
            y=y,
            n_sample_train_to_val_test=8)

        '''
        Trains and tests Perceptron model from scikit-learn
        '''
        model = Perceptron(penalty=None, alpha=0.0, tol=1e-3)
        # Trains scikit-learn Perceptron model
        model.fit(x_train, y_train)

        print('Results on the {} dataset using scikit-learn Perceptron model'.format(tag))

        # Test model on training set
        scores_train = model.score(x_train, y_train)
        print('Training set mean accuracy: {:.4f}'.format(scores_train))

        # Test model on validation set
        scores_val = model.score(x_val, y_val)
        print('Validation set mean accuracy: {:.4f}'.format(scores_val))

        # Test model on testing set
        scores_test = model.score(x_test, y_test)
        print('Testing set mean accuracy: {:.4f}'.format(scores_test))

        '''
        Trains, validates, and tests our Perceptron model for multi-class classification
        '''
        # TODO: obtain dataset in correct shape (d x N)

        # Initialize empty lists to hold models and scores
        models = []
        scores = []
        for T in steps:
            # TODO: Initialize PerceptronMultiClass model

            print(
                'Results on the {} dataset using our Perceptron model trained with {} steps and tolerance of {}'.format(
                    tag, T, tol))
            # TODO: Train model on training set

            # TODO: Test model on training set

            # scores_train.append(score_train)
            print('Training set mean accuracy: {:.4f}'.format(scores_train))

            # TODO: Test model on validation set

            print('Validation set mean accuracy: {:.4f}'.format(scores_val))

            # TODO: Save the model and its score

            # TODO: Select the best performing model on the validation set
            best_idx = 0

        print('Using best model trained with {} steps and tolerance of {}'.format(steps[best_idx], tol))

        # Test model on testing set

        score_test = 0.0

        print('Testing set mean accuracy: {:.4f}'.format(score_test))
