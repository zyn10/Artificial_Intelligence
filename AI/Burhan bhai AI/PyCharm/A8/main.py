import numpy as np
import pandas
from pandas import read_csv
import random


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
            self.w.append(0.05)

    def sigmoid(self, y):
        sigma_s = 1.0 / (1.0 + np.exp(-y))
        return sigma_s

    def solve(self, x , y):

        epoch = 10000
        #self.w = [0.05, 0.05, 0.05, 0.03, 0.04, 0.02, 0.01, -0.02, 0.02]
        #x = [[0,0],[0,1],[1,0],[1,1]]
        #solution = [0,1,1,0]
        #solution = [[0,0],[0,1],[1,0],[1,1]]
        #dw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        dw = []
        for i in range(0, len(self.w)):
            dw.append(0)

        eta = 0.05
        thresh = 2


        for e in range(epoch):

            o1 = 1
            o2 = 1

            for sol in range(0, len(X)):
                count1 = 0
                count2 = 0

                actual = y[sol][0]

                h1 = self.sigmoid((self.w[0] * thresh) + self.w[1] * x[sol][0] + self.w[2] * x[sol][1] + self.w[3] * x[sol][2] + self.w[4] * x[sol][3] + self.w[5] * x[sol][4] + self.w[6] * x[sol][5] + self.w[7] * x[sol][6] + self.w[8] * x[sol][7] + self.w[9] * x[sol][8])
                h2 = self.sigmoid((self.w[10] * thresh) + self.w[11] * x[sol][0] + self.w[12] * x[sol][1] + self.w[13] * x[sol][2] + self.w[14] * x[sol][3] + self.w[15] * x[sol][4] + self.w[16] * x[sol][5] + self.w[17] * x[sol][6] + self.w[18] * x[sol][7] + self.w[19] * x[sol][8])

                output1 = self.sigmoid((self.w[20] * thresh) + self.w[21] * h1 + self.w[22] * h2)
                #output2 = self.sigmoid(self.w[9] * thresh + self.w[10] * h1 + self.w[11] * h2)


                if e %500 == 0:

                    if actual == 1 and o1 == 1:
                        print('epoch: ', e)
                        print(actual , ' --> ', output1)
                        o1 = 0
                    if actual == 0 and o2 == 1:
                        print(actual , ' --> ', output1)
                        o2 = 0
                        print('--------------------')

                sigma_h1 =0
                sigma_h2 =0
                sigma_output1 = 0
                if output1 == actual:
                    nulll = 0
                    #pcount += 1
                    #break
                else:
                    sigma_output1 = output1 * (1 - output1) * (actual - output1)
                    #sigma_output2 = output2 * (1 - output2) * (actual[1] - output2)
                    sigma_h1 = h1 * (1 - h1) * ((sigma_output1 * self.w[21]))
                    sigma_h2 = h2 * (1 - h2) * ((sigma_output1 * self.w[22]))


                for k in range(0, len(dw)-3):
                    if k == 0:
                        dw[k] = eta * (sigma_h1 * thresh)
                    elif k == 10:
                        dw[k] = eta * (sigma_h2 * thresh)
                    elif k < 10:
                        dw[k] = eta * (sigma_h1 * x[sol][k-1])
                    else:
                        dw[k] = eta * (sigma_h2 * x[sol][k-11])

                    self.w[k] += dw[k]

                dw[20] = eta * (sigma_output1) * thresh
                self.w[20] += dw[20]
                dw[21] = eta * (sigma_output1) * h1
                self.w[21] += dw[21]
                dw[22] = eta * (sigma_output1) * h2
                self.w[22] += dw[22]




    def test(self, x, y):

        thresh = 1

        r = random.randint(0, len(Y))

        print('Test: ')

        actual = y[r][0]

        h1 = self.sigmoid(
                    self.w[0] * thresh + self.w[1] * x[r][0] + self.w[2] * x[r][1] + self.w[3] * x[r][2] + self.w[
                        4] * x[r][3] + self.w[5] * x[r][4] + self.w[6] * x[r][5] + self.w[7] * x[r][6] + self.w[
                        8] * x[r][7] + self.w[9] * x[r][8])
        h2 = self.sigmoid(
                    self.w[10] * thresh + self.w[11] * x[r][0] + self.w[12] * x[r][1] + self.w[13] * x[r][2] +
                    self.w[14] * x[r][3] + self.w[15] * x[r][4] + self.w[16] * x[r][5] + self.w[17] * x[r][6] +
                    self.w[18] * x[r][7] + self.w[19] * x[r][8])

        output1 = self.sigmoid(self.w[20] * thresh + self.w[21] * h1 + self.w[22] * h2)
        # output2 = self.sigmoid(self.w[9] * thresh + self.w[10] * h1 + self.w[11] * h2)

        print(actual, ' --> ', output1)

        print('--------------------')


Class ={
    'no-recurrence-events': 1,
    'recurrence-events': 0
}
age ={ '10-19' : 1,
       '20-29' : 2,
       '30-39' : 3,
       '40-49' : 4,
       '50-59' : 5,
       '60-69' : 6,
       '70-79' : 7,
       '80-89' : 8,
       '90-99' : 9,
       '?' : 0
}
menopause ={ 'lt40' :1,
             'ge40' :2,
             'premeno' :3,
             '?' : 0
}
tumor_size = { '0-4' : 1,
               '5-9' : 2,
               '10-14' : 3,
               '15-19' : 4,
               '20-24' : 5,
               '25-29' : 6,
               '30-34' : 7,
               '35-39' : 8,
               '40-44' : 9,
               '45-49' : 10,
               '50-54' : 11,
               '55-59' : 12,
               '?' : 0
}
inv_nodes ={ '0-2' : 1,
             '3-5' : 2,
             '6-8' : 3,
             '9-11' : 4,
             '12-14' : 5,
             '15-17' : 6,
             '18-20' : 7,
             '21-23' : 8,
             '24-26' : 9,
             '27-29' : 10,
             '30-32' : 11,
             '33-35' : 12,
             '36-39' : 13,
             '?' : 0
}
node_caps ={ 'yes' : 1,
             'no' : 0,
             '?' : 2
}
deg_malig ={ '1' : 1,
             '2' : 2,
             '3' : 3,
             '?' : 0
}
breast ={ 'left' : 1,
          'right' : 2,
          '?' : 0
          }
breast_quad ={ 'left_up' : 1,
               'left_low' : 2,
               'right_up' : 3,
               'right_low' : 4,
               'central' : 5,
               '?' : 0
               }
irradiat ={ 'yes' : 1,
            'no' : 0,
            '?' : 2
}


url = 'breast-cancer.csv'
names = ['Class','age','menopause','tumor-size','inv-nodes','node-caps','deg-malig','breast','breast-quad','irradiat']
dataset = read_csv(url, names=names)
array = dataset.values
X = array[1:,1:10]
Y = array[1:,0:1]
for i in range(0,len(X)):
    X[i][0] = age[X[i][0]]
    X[i][1] = menopause[X[i][1]]
    X[i][2] = tumor_size[X[i][2]]
    X[i][3] = inv_nodes[X[i][3]]
    X[i][4] = node_caps[X[i][4]]
    X[i][5] = deg_malig[X[i][5]]
    X[i][6] = breast[X[i][6]]
    X[i][7] = breast_quad[X[i][7]]
    X[i][8] = irradiat[X[i][8]]
    Y[i][0] = Class[Y[i][0]]


ANN = nural_network()
ANN.set_inputs(9)
ANN.set_layer(2)
ANN.add_neurons(2,1)
ANN.add_neurons(1,2)
ANN.solve(X, Y)

ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)
ANN.test(X,Y)

print("O K ")



"""
1. Class: no-recurrence-events, recurrence-events
2. age: 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99.
3. menopause: lt40, ge40, premeno.
4. tumor-size: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59.
5. inv-nodes: 0-2, 3-5, 6-8, 9-11, 12-14, 15-17, 18-20, 21-23, 24-26, 27-29, 30-32, 33-35, 36-39.
6. node-caps: yes, no.
7. deg-malig: 1, 2, 3.
8. breast: left, right.
9. breast-quad: left-up, left-low, right-up, right-low, central.
10. irradiat: yes, no.

"""

