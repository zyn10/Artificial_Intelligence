from pandas import read_csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

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
    Y[i] = Class[Y[i][0]]

X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)


models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))


print("O K ")