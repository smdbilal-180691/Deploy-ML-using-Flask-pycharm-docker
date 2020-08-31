import pickle
from flask import Flask,request
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pickle_inp = open("classifier.pkl","rb")
classifier = pickle.load(pickle_inp)

@app.route("/")
def welcome():
    return "Welcome to my first flask- flasgger app"

@app.route("/predict",methods=["GET"])
def predict_note():
    """Let's Authenticate the Banks Note
        This is using docstrings for specifications.
        ---
        parameters:
          - name: variance
            in: query
            type: number
            required: true
          - name: skewness
            in: query
            type: number
            required: true
          - name: curtosis
            in: query
            type: number
            required: true
          - name: entropy
            in: query
            type: number
            required: true
        responses:
            200:
                description: The output values

        """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if str(prediction) == '[0]':
        return "Forged bank note"
    else:
        return "Genuine bank note"
    #return "The predicted value is" +str(prediction)

if __name__=='__main__':
    app.run(host='0.0.0.0')