import pandas as pd
import numpy as np
from Cancer_Prediction import DecisionTreeClassifier
##TRAIN AND SPLIT TREE

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

##FIT THE MODAL
classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(train.iloc[:].values)
classifier.print_tree()
Y_test = test.iloc[:, -1].values
Y_test = [[item] for item in Y_test]
Y_pred = classifier.predict(test.iloc[:, 0:5].values)


# ##TEST MODEL
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, Y_pred))