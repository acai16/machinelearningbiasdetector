import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

class calculator:
    text = ''

    def __init__(self, text):
        self.text = [f'''
                        {text}
                    '''
                    ]


    global tfidf 
    tfidf = joblib.load("tfidf.joblib")
    global pac
    pac = joblib.load("pac.joblib")

    def calc(this):
        new_vec = tfidf.transform(this.text)
        return pac.predict(new_vec)


    

        

    