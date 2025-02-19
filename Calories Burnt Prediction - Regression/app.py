from flask import Flask, render_template, request, jsonify
from utils import Calories, load_dataset
df = load_dataset()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Gender_options')
def gender_options():
    return jsonify(list(df['Gender'].unique()))


@app.route('/predictions', methods=['POST'])
def predictions():
    data = request.form
    print(data)

    Gender = data['Gender']
    Age = data['Age']
    Height = data['Height']
    Weight = data['Weight']
    Duration = data['Duration']
    Heart_Rate = data['Heart_Rate']
    Body_Temp = data['Body_Temp']

    cal = Calories()
    predicted_cal = cal.predicted_calories(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)

    return jsonify({"Predictions of Calories Burnt": predicted_cal})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5050')