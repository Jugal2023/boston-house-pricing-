import pickle
from Flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd



app=Flask(__name__)
## load the model
regmodel=pickle.load(open('regmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['post'])
def predict_api():
    data=request.json['data']
    print(data)
