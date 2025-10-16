The BMI Calculator is a simple web-based application built using Python (Flask), HTML, and CSS.
It allows users to input their height (in cm) and weight (in kg) to calculate their Body Mass Index (BMI) and identify their health category (Underweight, Normal, Overweight, or Obese).
This project demonstrates basic Flask web development, form handling, and dynamic content rendering using templates.

->TECHNOLOGIES USED:
Frontend: HTML, CSS
Backend: Python (Flask)
Environment: Localhost / Linux Hosting

->HOW IT WORKS:
User enters height and weight in the form.
Flask processes the data and calculates BMI using:
BMI=(WEIGHT(kg))/(HEIGHT(m))^2

->The app displays both the BMI value and the health category:
BMI < 18.5 → Underweight
18.5 ≤ BMI < 24.9 → Normal
25 ≤ BMI < 29.9 → Overweight
BMI ≥ 30 → Obese
