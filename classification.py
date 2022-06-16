import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import confusion_matrix, f1_score, silhouette_score
from sklearn.metrics import precision_score, classification_report, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier
from warnings import filterwarnings
import pickle

filterwarnings('ignore')
np.set_printoptions(suppress=True)

# Import model

# Dataset loading
class_data = pd.read_csv('target.csv', index_col = 0)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def Prediction(pred):
    prediction = classifier.predict(pred)
    return prediction

# Features and label sets
target = pd.read_csv('target.csv')
X = target.drop('Clusters', axis = 1).values
y = target.iloc[:,-1].values.reshape(-1,1)
# Training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

# Random Forest Classification Model
def TrainEvaluateTuned(X_train,y_train, X_test):
    
    # Standard scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    # Model training
    classifier = RandomForestClassifier(n_estimators = 200, min_samples_split= 4,
                                        min_samples_leaf = 4, max_features = 'sqrt',
                                        max_depth = 30, random_state = 100)
    classifier.fit(X_train, y_train)

    # Predicting the test set results
    y_pred = classifier.predict(X_test)

    return y_pred

