from user_interface import Ui_BMI_Program as Bmi_Ui
import sys
from PyQt5 import QtWidgets


class Bmi_main(QtWidgets.QWidget,Bmi_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculate_button.clicked.connect(self.calculation)
    
    def calculation(self):
        height = float(self.height_info.text())
        weight = float(self.weight_info.text())
        bmi = weight / (height * height)
        self.label_3.setText(str(bmi.__round__(2)))


        if 0 <= bmi <= 18.4:
            self.result_section.setText("Underweight")
        elif 18.5 <= bmi <= 24.9:
            self.result_section.setText("Healthy Weight")
        elif 25.0 <= bmi <= 29.9:
            self.result_section.setText("Overweight")
        elif 30.0 <= bmi <= 34.9:
            self.result_section.setText("Overweight(Obesity)-I.Phase")
        elif 35.0 <= bmi <= 44.9:
            self.result_section.setText("Overweight(Obesity)-II.Phase")
        elif 45.0 >= bmi:
            self.result_section.setText("Overweight(Obesity)-III.Phase")

if __name__ == "__main__":
    uygulama = QtWidgets.QApplication(sys.argv)
    ekran = Bmi_main()
    ekran.show()
    sys.exit(uygulama.exec_())