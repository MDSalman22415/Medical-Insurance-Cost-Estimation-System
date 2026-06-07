from flask import Flask, render_template, request
import pickle
import pandas as pd
app = Flask(__name__, static_folder="static", template_folder="templates")
# Load dataset
data = pd.read_csv('Cleaned_data.csv')

# Load model
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))


@app.route('/')
def index():
    region = sorted(data['region'].unique())
    smoker = sorted(data['smoker'].unique())
    sex = sorted(data['sex'].unique())

    return render_template('index.html',sex=sex, smoker=smoker, region=region)


@app.route('/predict', methods=['POST'])
def predict():

    age = int(request.form.get('age'))
    sex = request.form.get('sex')
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = request.form.get('smoker')
    region = request.form.get('region')

    input_df = pd.DataFrame(
        [[age, sex, bmi, children, smoker, region]],
        columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region']
    )

    prediction = pipe.predict(input_df)[0]

    return str(round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True, port=5001)

import os
print("RUNNING FROM:", os.getcwd())