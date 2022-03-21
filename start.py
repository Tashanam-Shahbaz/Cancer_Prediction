from Cancer_Prediction import DecisionTreeClassifier
import pandas as pd

##TRAIN AND SPLIT TREE
train = pd.read_csv("train.csv")

##FIT THE MODAL
classifier = DecisionTreeClassifier(min_samples_split=3, max_depth=3)
classifier.fit(train.iloc[:].values)


print("_____Enter Following Values for Tumour:_____")
mean_radius=float(input("Mean Radius: "))
mean_texture=float(input("Mean Texture:"))
mean_perimeter=float(input("Mean Perimeter : "))
mean_area=float(input("Mean Area: "))
mean_smoothness=float(input("Mean Smoothness: "))

data=[[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]]
# data=[[16.13,20.68,108.1,798.8,0.117]]
Y_pred = classifier.predict(data)

if Y_pred == [[1]]:
    print("Tumour is Malignant.")
elif Y_pred == [[0]] :
    print("Tumor is benign.")
