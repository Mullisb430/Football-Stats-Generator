import sys, os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

screen = resource_path("footballGUI.ui")

class Football(QMainWindow):
    def __init__(self):
        self.counter = 1
        super(Football, self).__init__()
        uic.loadUi(screen, self)
        self.playButton.clicked.connect(self.play)
        self.playButton.clicked.connect(self.seasonTotals)
        self.resetButton.clicked.connect(self.reset)
    
    # Resets the game to be played again as if just opened.
    def reset(self):
        self.counter = 0

        self.touchdown1.setText(str(000))
        self.touchdown2.setText(str(000))
        self.touchdown3.setText(str(000))
        self.touchdown4.setText(str(000))
        self.touchdown5.setText(str(000))
        self.touchdown6.setText(str(000))
        self.touchdown7.setText(str(000))
        self.touchdown8.setText(str(000))
        self.touchdown9.setText(str(000))
        self.touchdown10.setText(str(000))
        self.touchdown11.setText(str(000))
        self.touchdown12.setText(str(000))
        self.touchdown13.setText(str(000))
        self.touchdown14.setText(str(000))
        self.touchdown15.setText(str(000))
        self.touchdown16.setText(str(000))

        self.interception1.setText(str(000))
        self.interception2.setText(str(000))
        self.interception3.setText(str(000))
        self.interception4.setText(str(000))
        self.interception5.setText(str(000))
        self.interception6.setText(str(000))
        self.interception7.setText(str(000))
        self.interception8.setText(str(000))
        self.interception9.setText(str(000))
        self.interception10.setText(str(000))
        self.interception11.setText(str(000))
        self.interception12.setText(str(000))
        self.interception13.setText(str(000))
        self.interception14.setText(str(000))
        self.interception15.setText(str(000))
        self.interception16.setText(str(000))

        self.yard1.setText(str(00000))
        self.yard2.setText(str(00000))
        self.yard3.setText(str(00000))
        self.yard4.setText(str(00000))
        self.yard5.setText(str(00000))
        self.yard6.setText(str(00000))
        self.yard7.setText(str(00000))
        self.yard8.setText(str(00000))
        self.yard9.setText(str(00000))
        self.yard10.setText(str(00000))
        self.yard11.setText(str(00000))
        self.yard12.setText(str(00000))
        self.yard13.setText(str(00000))
        self.yard14.setText(str(00000))
        self.yard15.setText(str(00000))
        self.yard16.setText(str(00000))

        self.completion1.setText(str(000))
        self.completion2.setText(str(000))
        self.completion3.setText(str(000))
        self.completion4.setText(str(000))
        self.completion5.setText(str(000))
        self.completion6.setText(str(000))
        self.completion7.setText(str(000))
        self.completion8.setText(str(000))
        self.completion9.setText(str(000))
        self.completion10.setText(str(000))
        self.completion11.setText(str(000))
        self.completion12.setText(str(000))
        self.completion13.setText(str(000))
        self.completion14.setText(str(000))
        self.completion15.setText(str(000))
        self.completion16.setText(str(000))

        self.seasonTD.setText(str(000))
        self.seasonINT.setText(str(000))
        self.seasonYard.setText(str(00000))
        self.seasonCompletion.setText(str(000))

        self.playButton.setEnabled(True)
   
    # Adds up the season totals, and places them in the appropriate label
    def seasonTotals(self):
        tdTot = [int(self.touchdown1.text()), int(self.touchdown2.text()), int(self.touchdown3.text()), int(self.touchdown4.text()), int(self.touchdown5.text()), int(self.touchdown6.text()), int(self.touchdown7.text()), int(self.touchdown8.text()), int(self.touchdown9.text()), int(self.touchdown10.text()), int(self.touchdown11.text()), int(self.touchdown12.text()), int(self.touchdown13.text()), int(self.touchdown14.text()), int(self.touchdown15.text()), int(self.touchdown16.text())]

        intTot = [int(self.interception1.text()), int(self.interception2.text()), int(self.interception3.text()), int(self.interception4.text()), int(self.interception5.text()), int(self.interception6.text()), int(self.interception7.text()), int(self.interception8.text()), int(self.interception9.text()), int(self.interception10.text()), int(self.interception11.text()), int(self.interception12.text()), int(self.interception13.text()), int(self.interception14.text()), int(self.interception15.text()), int(self.interception16.text())]

        yardTot = [int(self.yard1.text()), int(self.yard2.text()), int(self.yard3.text()), int(self.yard4.text()), int(self.yard5.text()), int(self.yard6.text()), int(self.yard7.text()), int(self.yard8.text()), int(self.yard9.text()), int(self.yard10.text()), int(self.yard11.text()), int(self.yard12.text()), int(self.yard13.text()), int(self.yard14.text()), int(self.yard15.text()), int(self.yard16.text())]

        completionTot = [int(self.completion1.text()), int(self.completion2.text()), int(self.completion3.text()), int(self.completion4.text()), int(self.completion5.text()), int(self.completion6.text()), int(self.completion7.text()), int(self.completion8.text()), int(self.completion9.text()), int(self.completion10.text()), int(self.completion11.text()), int(self.completion12.text()), int(self.completion13.text()), int(self.completion14.text()), int(self.completion15.text()), int(self.completion16.text())]

        self.seasonTD.setText(str(sum(tdTot)))
        self.seasonINT.setText(str(sum(intTot)))
        self.seasonYard.setText(str(sum(yardTot)))

        # 'try and except' function avoids the 'zero division' error
        actual = list(filter(lambda num: num>0, completionTot))
        try:
            self.seasonCompletion.setText(str(f'.{str((sum(actual)/len(actual)))[0:2]}'))
        except Exception:
            self.seasonCompletion.setText(str(000))

    # Statistic Generating Functions
    def touchDowns(self):
        key = random.randint(0, 100)
        if key <= 10:
            return random.randint(4, 5)
        elif key > 10 and key <=25:
            return 3
        elif key > 25 and key <=45:
            return random.randint(2, 3)
        elif key > 45 and key <=70:
            return random.randint(1, 2)
        elif key > 70:
            return 0

    def interceptions(self):
        key = random.randint(0, 100)
        if key <= 10:
            return 0
        elif key > 10 and key <=75:
            return 1
        elif key > 75:
            return random.randint(0, 3)

    def yards(self):
        key = random.randint(0, 100)
        if key <= 10:
            return random.randint(375, 499)
        elif key > 10 and key <=25:
            return random.randint(320, 374)
        elif key > 25 and key <=45:
            return random.randint(275, 319)
        elif key > 45 and key <=70:
            return random.randint(220, 274)
        elif key > 70:
            return random.randint(140, 219)

    def completions(self):
        key = random.randint(0, 100)
        if key <= 10:
            return random.randint(67, 73)
        elif key > 10 and key <=25:
            return random.randint(62, 66)
        elif key > 25 and key <=45:
            return random.randint(55, 61)
        elif key > 45 and key <=70:
            return random.randint(50, 54)
        elif key > 70:
            return random.randint(44, 49)

    # Filling the weeks with generated statistics
    def play(self):

        if self.counter == 1:
            self.touchdown1.setText(str(self.touchDowns()))
            self.interception1.setText(str(self.interceptions()))
            self.yard1.setText(str(self.yards()))
            self.completion1.setText(str(self.completions()))

        elif self.counter == 2:
            self.touchdown2.setText(str(self.touchDowns()))
            self.interception2.setText(str(self.interceptions()))
            self.yard2.setText(str(self.yards()))
            self.completion2.setText(str(self.completions()))

        elif self.counter == 3:
            self.touchdown3.setText(str(self.touchDowns()))
            self.interception3.setText(str(self.interceptions()))
            self.yard3.setText(str(self.yards()))
            self.completion3.setText(str(self.completions()))

        elif self.counter == 4:
            self.touchdown4.setText(str(self.touchDowns()))
            self.interception4.setText(str(self.interceptions()))
            self.yard4.setText(str(self.yards()))
            self.completion4.setText(str(self.completions()))

        elif self.counter == 5:
            self.touchdown5.setText(str(self.touchDowns()))
            self.interception5.setText(str(self.interceptions()))
            self.yard5.setText(str(self.yards()))
            self.completion5.setText(str(self.completions()))

        elif self.counter == 6:
            self.touchdown6.setText(str(self.touchDowns()))
            self.interception6.setText(str(self.interceptions()))
            self.yard6.setText(str(self.yards()))
            self.completion6.setText(str(self.completions()))

        elif self.counter == 7:
            self.touchdown7.setText(str(self.touchDowns()))
            self.interception7.setText(str(self.interceptions()))
            self.yard7.setText(str(self.yards()))
            self.completion7.setText(str(self.completions()))

        elif self.counter == 8:
            self.touchdown8.setText(str(self.touchDowns()))
            self.interception8.setText(str(self.interceptions()))
            self.yard8.setText(str(self.yards()))
            self.completion8.setText(str(self.completions()))

        elif self.counter == 9:
            self.touchdown9.setText(str(self.touchDowns()))
            self.interception9.setText(str(self.interceptions()))
            self.yard9.setText(str(self.yards()))
            self.completion9.setText(str(self.completions()))

        elif self.counter == 10:
            self.touchdown10.setText(str(self.touchDowns()))
            self.interception10.setText(str(self.interceptions()))
            self.yard10.setText(str(self.yards()))
            self.completion10.setText(str(self.completions()))

        elif self.counter == 11:
            self.touchdown11.setText(str(self.touchDowns()))
            self.interception11.setText(str(self.interceptions()))
            self.yard11.setText(str(self.yards()))
            self.completion11.setText(str(self.completions()))

        elif self.counter == 12:
            self.touchdown12.setText(str(self.touchDowns()))
            self.interception12.setText(str(self.interceptions()))
            self.yard12.setText(str(self.yards()))
            self.completion12.setText(str(self.completions()))

        elif self.counter == 13:
            self.touchdown13.setText(str(self.touchDowns()))
            self.interception13.setText(str(self.interceptions()))
            self.yard13.setText(str(self.yards()))
            self.completion13.setText(str(self.completions()))

        elif self.counter == 14:
            self.touchdown14.setText(str(self.touchDowns()))
            self.interception14.setText(str(self.interceptions()))
            self.yard14.setText(str(self.yards()))
            self.completion14.setText(str(self.completions()))

        elif self.counter == 15:
            self.touchdown15.setText(str(self.touchDowns()))
            self.interception15.setText(str(self.interceptions()))
            self.yard15.setText(str(self.yards()))
            self.completion15.setText(str(self.completions()))

        elif self.counter == 16:
            self.touchdown16.setText(str(self.touchDowns()))
            self.interception16.setText(str(self.interceptions()))
            self.yard16.setText(str(self.yards()))
            self.completion16.setText(str(self.completions()))
        
        elif self.counter > 16:
            self.playButton.setEnabled(False)

        self.counter += 1



app = QApplication(sys.argv)
football = Football()
football.show()
football.setFixedSize(1487, 990)
app.exec_()
