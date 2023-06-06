from random import random
import numpy as np
import pandas
from pandas import read_csv

class nural_network:
    def __init__(self):
        self.inputs = 0
        self.layers = 1
        self.neurons = [1]
        self.w = []
        self.total_neuron = 1

    def set_layer(self, layers):
        self.layers = layers
        self.neurons = []
        for n in range(0, layers):
            self.neurons.append(1)

    def set_inputs(self, input):
        self.inputs = input

    def add_neurons(self, neurons, layer_number):
        self.neurons[layer_number - 1] = neurons
        self.set_weight()

    def set_weight(self):
        self.total_neuron = self.neurons[0]
        total_weight = self.inputs * self.neurons[0]
        for n in range(1, len(self.neurons)):
            self.total_neuron += self.neurons[n]
            total_weight += self.neurons[n-1] * self.neurons[n]

        self.w = []
        total_weight += self.total_neuron
        for n in range(0, total_weight):
            self.w.append(0.02)

    def sigmoid(self, y):
        sigma_s = 1.0 / (1.0 + np.exp(-y))
        return sigma_s

    def solve(self, x , y):

        epoch = 10000
        #self.w = [0.05, 0.05, 0.05, 0.03, 0.04, 0.02, 0.01, -0.02, 0.02]
        #x = [[0,0],[0,1],[1,0],[1,1]]
        #solution = [0,1,1,0]
        solution = [[0,0],[0,1],[1,0],[1,1]]
        dw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        eta = 0.02
        thresh = 1


        for e in range(epoch):

            o1 = 1
            o2 = 1
            o3 = 1
            print('epoch: ',e )
            for sol in range(0, len(X)):
                count1 = 0
                count2 = 0
                ind = y[sol][0]
                actual = solution[ind-1]

                h1 = self.sigmoid((self.w[0] * thresh)  + self.w[1] * x[sol][0] + self.w[3] * x[sol][1])
                h2 = self.sigmoid((self.w[5] * thresh)  + self.w[2] * x[sol][0] + self.w[4] * x[sol][1])

                output1 = self.sigmoid((self.w[6] * thresh)  + self.w[7] * h1 + self.w[8] * h2)
                output2 = self.sigmoid((self.w[9] * thresh)  + self.w[10] * h1 + self.w[11] * h2)


                if (ind == 1 and o1 == 1):
                    print(actual[0] ,' + ', actual[1],' : ind:', ind , ' --> ', output1, ' + ', output2)
                    o1 = 0
                if (ind == 2 and o2 == 1):
                    print(actual[0] ,' + ', actual[1],' : ind:', ind , ' --> ', output1, ' + ', output2)
                    o2 = 0
                if (ind == 3 and o3 == 1):
                    print(actual[0] ,' + ', actual[1],' : ind:', ind , ' --> ', output1, ' + ', output2)
                    o3 = 0


                if output1 == actual[0]:
                    nulll =0
                    #pcount += 1
                    #break
                else:
                    sigma_output1 = output1 * (1 - output1) * (actual[0] - output1)
                    sigma_output2 = output2 * (1 - output2) * (actual[1] - output2)
                    sigma_h1 = h1 * (1 - h1) * ((sigma_output1 * self.w[7]) + (sigma_output2 * self.w[10]))
                    sigma_h2 = h2 * (1 - h2) * ((sigma_output1 * self.w[8]) + (sigma_output2 * self.w[11]))


                for k in range(0, len(dw)-6):
                    if k == 0:
                        dw[k] = eta * (sigma_h1 * thresh)
                    elif k == 5:
                        dw[k] = eta * (sigma_h2 * thresh)
                    elif k % 2 != 0:
                        dw[k] = eta * (sigma_h1 * x[sol][count1])
                        if count1 == 0:
                            count1 = 1
                        else:
                            count1 = 0
                    else:
                        dw[k] = eta * (sigma_h2 * x[sol][count2])
                        if count2 == 1:
                            count2 = 1
                        else:
                            count2 = 0
                    self.w[k] += dw[k]

                dw[6] = eta * (sigma_output1) * thresh
                self.w[6] += dw[6]
                dw[7] = eta * (sigma_output1) * h1
                self.w[7] += dw[7]
                dw[8] = eta * (sigma_output1) * h2
                self.w[8] += dw[8]

                dw[9] = eta * (sigma_output2) * thresh
                self.w[9] += dw[9]
                dw[10] = eta * (sigma_output2) * h1
                self.w[10] += dw[10]
                dw[11] = eta * (sigma_output2) * h2
                self.w[11] += dw[11]

            print('--------------------')

    def test(self, x , y):

        epoch = 10000
        #self.w = [0.05, 0.05, 0.05, 0.03, 0.04, 0.02, 0.01, -0.02, 0.02]
        #x = [[0,0],[0,1],[1,0],[1,1]]
        #solution = [0,1,1,0]
        solution = [[0,0],[0,1],[1,0],[1,1]]
        thresh = 1

        r = random.randint(0,len(y))

        ind = y[r][0]
        actual = solution[ind - 1]

        h1 = self.sigmoid((self.w[0] * thresh) + self.w[1] * x[r][0] + self.w[3] * x[r][1])
        h2 = self.sigmoid((self.w[5] * thresh) + self.w[2] * x[r][0] + self.w[4] * x[r][1])

        output1 = self.sigmoid((self.w[6] * thresh) + self.w[7] * h1 + self.w[8] * h2)
        output2 = self.sigmoid((self.w[9] * thresh) + self.w[10] * h1 + self.w[11] * h2)

        print(actual[0], ' + ', actual[1], ' : ind:', ind, ' --> ', output1, ' + ', output2)

        print('--------------------')

url = 'SpiralData_Clean_Spread.csv'
names = ['Chem1', 'Chem2', 'Clnum']
dataset = read_csv(url, names=names)
array = dataset.values
X = array[1:,0:2]
Y = array[1:,2:]
for i in range(0,len(X)):
    X[i][0] = float(X[i][0])
    X[i][1] = float(X[i][1])
    Y[i][0] = int(Y[i][0])


ANN = nural_network()
ANN.set_inputs(2)
ANN.set_layer(2)
ANN.add_neurons(2,1)
ANN.add_neurons(2,2)
ANN.solve(X, Y)

ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)


print("O K ")


"""
operator = 'and'
#----------------
atributes = np.array([ [0, 0], [0, 1], [1, 0], [1, 1]])

if operator == 'and':
    labels = np.array([0, 0, 0, 1])
elif operator == 'or':
    labels = np.array([0, 1, 1, 1])
elif operator == 'xor':
    labels = np.array([0, 1, 1, 0])
#----------------

w = [+9, +9] #initial random values for weights

threshold = 5
alpha = 0.5 #learning rate
epoch = 1000 #learning time
#----------------
print("learning rate: ", alpha,", threshold: ", threshold)
for i in range(0, epoch):
    print("epoch ", i + 1)
    global_delta = 0  # this variable is used to terminate the for loop if learning completed in early epoch
    for j in range(len(atributes)):
        actual = labels[j]
        sum = atributes[j][0] * w[0] + atributes[j][1] * w[1]
        if sum > threshold:  # then fire
            predicted = 1
        else:  # do not fire
            predicted = 0
        delta = actual - predicted
        global_delta = global_delta + abs(delta)

        # update weights with respect to the error
        for k in range(0, 2):
            w[k] = w[k] + delta * alpha

        print(atributes[j][0], " ", operator, " ", atributes[j][1], " -> actual: ", actual, ", predicted: ", predicted,
              " (w: ", w[0], ")")

    if global_delta == 0:
        break
    print("------------------------------")

"""
