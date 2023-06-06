import numpy as np
from pyexpat import model

operator = 'and'
#----------------


atributes = np.array([ [0, 0], [0, 1], [1, 0], [1, 1]])
atributes = np.array([
    [2.38522625552451,-2.3651502566768],
    [1.78131675892343,-2.51096188404183],
    [2.07450455993614,-2.64907887854061],
    [1.68010079641285,-1.92219612993337],
    [1.94269448933319,-2.11927461479238],
    [1.82769108089341,-1.84964742595465],
    [-0.226085609267856,10.2122638499433],
    [0.474377683294493,10.3387000590726],
    [-0.369616586230174,10.0139616612662],
    [-0.501451528802594,10.8795842526065],
    [0.28796382938741,10.2333344681027],
    [-0.194184067748596,10.23419618068],
    [2.11586840084,-1.89702365423267]
])
if operator == 'and':
    labels = np.array([0, 0, 0, 1])
elif operator == 'or':
    labels = np.array([0, 1, 1, 1])
elif operator == 'xor':
    labels = np.array

labels = np.array([1,1,1,1,1,1,2,2,2,2,2,2,1])
#----------------

w = [+15, +15] #initial random values for weights

threshold = 0.2
alpha = 0.5 #learning rate
epoch = 10000 #learning time
#----------------
print("learning rate: ", alpha,", threshold: ", threshold)
for i in range(0, epoch):
    print("epoch ", i + 1)
    global_delta = 0  # this variable is used to terminate the for loop if learning completed in early epoch
    for j in range(len(atributes)):
        actual = labels[j]
        sum = atributes[j][0] * w[0] + atributes[j][1] * w[1]
        if sum > threshold:  # then fire
            predicted = 2
        else:  # do not fire
            predicted = 1
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


print("Now test :")
test_x = input("Enter chem1:")
test_x = float(test_x)
test_y = input("Enter chem2:")
test_y = float(test_y)
print("Prediction: ")
pre = test_x * w[0] + test_y * w[1]
if pre > threshold:  # then fire
    pre = 2
else:  # do not fire
    pre = 1
print("Prediction:",pre)

