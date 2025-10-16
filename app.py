from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = round(weight / ((height / 100) ** 2), 2)  # Convert cm to meters

    # Determine category
    if bmi < 18.5:
        category = "Underweight"
        category_class = "underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        category_class = "normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        category_class = "overweight"
    else:
        category = "Obese"
        category_class = "obese"

    return render_template('index.html', bmi=bmi, category=category, category_class=category_class)

if __name__ == '__main__':
    app.run(debug=True)
