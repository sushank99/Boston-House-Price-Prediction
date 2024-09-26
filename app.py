import pickle
from flask import Flask, render_template, request, app, jsonify, url_for
import numpy as np
import json
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
## load the regression model
regmodel = pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))

    
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods= ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    
    print("Got Input From User")
    
    output = abs((regmodel.predict(final_input)[0])*1000)
    output = "%.2f" % (abs(output))
    
    print(f' Predicted Price of House : {output}')
    
    return render_template('result.html', predicted_text="The House Price Prediction is ${}".format(output))


if __name__=='__main__':
    app.run(debug=True)