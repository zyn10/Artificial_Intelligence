import numpy as np
import pandas as pd
import math as mp
import copy

#Data
# data = pd.read_csv('SpiralData_Clean_Spread.csv', usecols=[0, 1], header=0)
# #print(data)
# X = data.values
# atributes = X
#
# data = pd.read_csv('SpiralData_Clean_Spread.csv', usecols=[2], header=0)
# Y = data.values
# labels = Y

atributes = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# print(atributes)
#Target Values
operator = 'xor'

#--------------------------------
if operator == 'and':
    labels = np.array([0, 0, 0, 1])
elif operator == 'or':
    labels = np.array([0, 1, 1, 1])
elif operator == 'xor':
    labels = np.array([0, 1, 1, 0])

spiral_output = [[0,0],[0,1],[1,0],[1,1]]
#--------------------------------

w = [0.05, 0.05, 0.05, 0.03, 0.04, 0.02, 0.01, -0.02, 0.02]
dw = [0, 0, 0, 0, 0, 0, 0, 0, 0]
threshold = 2
pcount = 0
alpha = 0.5


h1 = h2 = output = sigma_output = sigma_h1 = sigma_h2 = 0
def sigmid(x):
    #y = (mp.exp(x)-mp.exp(-x))/(mp.exp(x)+mp.exp(-x))
    y = 1.0 / (1 + mp.exp(-x))
    return y


for i in range(10000):
    print('epoch', i, " :")
    for j in range(0, len(atributes)):
        count1 = 0
        count2 = 0
        actual = labels[j]
        h1 = sigmid(w[0]*threshold + w[1]*atributes[j][0] + w[3]*atributes[j][1])
        h2 = sigmid(w[5]*threshold + w[2]*atributes[j][0] + w[4]*atributes[j][1])

        output = sigmid(w[6]*threshold + w[7]*h1 + w[8]*h2)

        print(actual, ' --> ', output)

        if output == actual:
            pcount += 1
            break
        else:
            sigma_output = output*(1-output)*(actual - output)
            sigma_h1 = h1 * (1 - h1) * (sigma_output * w[7])
            sigma_h2 = h2 * (1 - h2) * (sigma_output * w[8])

            for k in range(0, len(dw)-3):
                if k == 0:
                    dw[k] = alpha * (sigma_h1 * threshold)
                elif k == 5:
                    dw[k] = alpha * (sigma_h2 * threshold)
                elif k % 2 != 0:
                    dw[k] = alpha * (sigma_h1 * atributes[j][count1])
                    if count1 == 0:
                        count1 = 1
                    else:
                        count1 = 0
                else:
                    dw[k] = alpha * (sigma_h2 * atributes[j][count2])
                    if count2 == 1:
                        count2 = 1
                    else:
                        count2 = 0
                w[k] += dw[k]

            dw[6] = alpha * (sigma_output) * threshold
            w[6] += dw[6]
            dw[7] = alpha * (sigma_output) * h1
            w[7] += dw[7]
            dw[8] = alpha * (sigma_output) * h2
            w[8] += dw[8]
    print('--------------------')

    if pcount == 4:
        print('done')
        break


print('pcount: ', pcount)

