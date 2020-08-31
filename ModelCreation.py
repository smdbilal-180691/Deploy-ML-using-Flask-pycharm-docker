import pandas as pd
import numpy as np

import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import struct

in_df = pd.read_csv(r"bank_note.csv")
#print(in_df.head())
X = in_df.iloc[:,:-1]
Y = in_df.iloc[:,-1]

#print(X.head())

#TrainTest Split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

#Classifier def
classifier = RandomForestClassifier()
classifier.fit(X_train,Y_train)

Y_pred = classifier.predict(X_test)
score = accuracy_score(Y_test,Y_pred)
print(score)

#Predicting using user input
print(classifier.predict([[-2,-3,-4,-1]]))

#Prints whether 32 bit or 64 bit of python used
print(struct.calcsize("P") * 8)

pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier,pickle_out)
pickle_out.close()





