from PyQt6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from make_question import Ui_Suallar
import sys

class my_win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Suallar()
        self.ui.setupUi(self)
        self.setWindowTitle("Sual Hazırla")
        self.ui.question.setPlaceholderText("Sual")
        self.ui.options.currentItemChanged.connect(self.optionsChangedVariant)
        self.ui.reset_all.clicked.connect(self.reset_all_settings)
        self.ui.next.clicked.connect(self.nextQuestion)  
        self.questionIndex = 0

        # Radyo düğmelerini içerecek bir grup oluştur
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.ui.true_variant_a)
        self.button_group.addButton(self.ui.true_variant_b)
        self.button_group.addButton(self.ui.true_variant_c)
        self.button_group.addButton(self.ui.true_variant_d)
        self.button_group.addButton(self.ui.true_variant_e)

    def optionsChangedVariant(self, index):
        if "3" in index.text():
            self.ui.options.setDisabled(True)
            self.ui.true_variant_d.setDisabled(True)
            self.ui.true_variant_e.setDisabled(True)
            self.ui.d_choise.setDisabled(True)
            self.ui.e_choise.setDisabled(True)
            self.ui.e_choise.setStyleSheet("background-color: gray;")
            self.ui.d_choise.setStyleSheet("background-color: gray;")

        elif "4" in index.text():
            self.ui.options.setDisabled(True)
            self.ui.e_choise.setDisabled(True)
            self.ui.true_variant_e.setDisabled(True)
            self.ui.e_choise.setStyleSheet("background-color: gray;")
        
        else:
            self.ui.options.setDisabled(True)

    def reset_all_settings(self):
        self.ui.question.clear()
        self.ui.lesson_name.clear()
        self.ui.a_choise.clear()
        self.ui.b_choise.clear()
        self.ui.c_choise.clear()
        self.ui.d_choise.clear()
        self.ui.e_choise.clear()
        self.ui.options.reset()
        self.ui.options.setDisabled(False)
        self.ui.true_variant_d.setDisabled(False)
        self.ui.true_variant_e.setDisabled(False)
        self.ui.d_choise.setDisabled(False)
        self.ui.e_choise.setDisabled(False)
        self.ui.e_choise.setStyleSheet("background-color: white;")
        self.ui.d_choise.setStyleSheet("background-color: white;")
        self.questionIndex = 0
        self.ui.questionCounter.setText("0")
        # Tüm radyo düğmelerinin seçimini kaldır
        self.button_group.setExclusive(False)
        for button in self.button_group.buttons():
            button.setChecked(False)
        self.button_group.setExclusive(True)

    def checkTrueVariant(self):
        if None is self.button_group.checkedButton():
            self.status(msg="Doğru cavabı qeyd etməmisiniz", delay=2, type="Error")
            

    def nextQuestion(self):
        self.questionIndex += 1
        self.ui.questionCounter.setText(str(self.questionIndex))
        if len(self.ui.question.toPlainText()) < 5:
            self.status(msg="Sual qeyd edilməyib", delay=2, type="Error")  
        else:
            self.status(msg="Sual əlavə edildi", type="Success", delay=2)
        self.checkTrueVariant()

    
    def status(self, msg = "", type="Error", delay = 2):
        if("Error" in type):
            self.statusBar().setStyleSheet("color: red;")
        elif("Success" in type):
            self.statusBar().setStyleSheet("color: green;")
        else:
            self.statusBar().setStyleSheet("color: black;")

        self.statusBar().showMessage(msg, msecs=delay*1000)



app = QApplication(sys.argv)
pencere = my_win()
pencere.show()
sys.exit(app.exec())
