# Getting Started with BMI Calculator

![Example BMI](https://user-images.githubusercontent.com/53980530/198906142-52ef7a69-82ea-4c1d-b37e-f85ffe28e3ba.jpg)

The project is a simple Body Mass Index (BMI) Calculator that takes your height and weight and gives you a result.
- The result is "Underweight" if your BMI is between 0 and 18.4
- The result is "Healthweight" if your BMI is between 18.5 and 24.9
- The result is "Overweight" if your BMI is between 25 and 29.9
- The result is "Overweight(Obesity)-I. Phase" if your BMI is between 30.0 and 34.9
- The result is "Overweight(Obesity)-II. Phase" if your BMI is between 35 and 44.9
- The result is "Overweight(Obesity)-III. Phase" if your BMI is over 45.

## **INSTRUCTIONS TO USE THE PROGRAM**

1. Download the repository and open it with your favorite IDE.
2. Open `bmi_main.py` and run the program.
3. Enter your height in terms of meters.
4. Enter your weight in terms of kilograms.
5. Click **Calculate**.
6. See your result.


### **DEVELOPMENT PROCESS**
1. The user interfaces are developed with QtDesigner and turned to code by the command:

`pyuic5 -o user_interface.ui -o user_interface.py`

2. Necessary functions are developed in `bmi_main.py`

3. The Main function is developed in `bmi_main.py`

# Learn More

[Qt Designer Manual](https://doc.qt.io/qt-6/qtdesigner-manual.html)
