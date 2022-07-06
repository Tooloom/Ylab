import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from random import choice


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = None
        self.matrix = [['-' for _ in range(10)] for _ in range(10)]
        self.matrix_ai = [i for i in range(1, 101)]
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi('Task_2_2.ui')
        self.ui.show()

    # ----------------------- signals handler -----------------------
    # здесь не получилось пройтись циклом. в интернете тоже не нашёл ответа
    def set(self):
        # self.ui.cell_1.setStyleSheet("background-image : url(cross.png);")
        # self.ui.cell_2.setStyleSheet("background-image : url(circle.png);")
        # for i in range(1, 5):
        #     button = getattr(self.ui, f'cell_{i}')
        #     button.clicked.connect(lambda: self.click(sign=i))
        self.ui.btn_retry.clicked.connect(lambda: self.click(sign='retry'))
        self.ui.cell_1.clicked.connect(lambda: self.click(sign=1))
        self.ui.cell_2.clicked.connect(lambda: self.click(sign=2))
        self.ui.cell_3.clicked.connect(lambda: self.click(sign=3))
        self.ui.cell_4.clicked.connect(lambda: self.click(sign=4))
        self.ui.cell_5.clicked.connect(lambda: self.click(sign=5))
        self.ui.cell_6.clicked.connect(lambda: self.click(sign=6))
        self.ui.cell_7.clicked.connect(lambda: self.click(sign=7))
        self.ui.cell_8.clicked.connect(lambda: self.click(sign=8))
        self.ui.cell_9.clicked.connect(lambda: self.click(sign=9))
        self.ui.cell_10.clicked.connect(lambda: self.click(sign=10))
        self.ui.cell_11.clicked.connect(lambda: self.click(sign=11))
        self.ui.cell_12.clicked.connect(lambda: self.click(sign=12))
        self.ui.cell_13.clicked.connect(lambda: self.click(sign=13))
        self.ui.cell_14.clicked.connect(lambda: self.click(sign=14))
        self.ui.cell_15.clicked.connect(lambda: self.click(sign=15))
        self.ui.cell_16.clicked.connect(lambda: self.click(sign=16))
        self.ui.cell_17.clicked.connect(lambda: self.click(sign=17))
        self.ui.cell_18.clicked.connect(lambda: self.click(sign=18))
        self.ui.cell_19.clicked.connect(lambda: self.click(sign=19))
        self.ui.cell_20.clicked.connect(lambda: self.click(sign=20))
        self.ui.cell_21.clicked.connect(lambda: self.click(sign=21))
        self.ui.cell_22.clicked.connect(lambda: self.click(sign=22))
        self.ui.cell_23.clicked.connect(lambda: self.click(sign=23))
        self.ui.cell_24.clicked.connect(lambda: self.click(sign=24))
        self.ui.cell_25.clicked.connect(lambda: self.click(sign=25))
        self.ui.cell_26.clicked.connect(lambda: self.click(sign=26))
        self.ui.cell_27.clicked.connect(lambda: self.click(sign=27))
        self.ui.cell_28.clicked.connect(lambda: self.click(sign=28))
        self.ui.cell_29.clicked.connect(lambda: self.click(sign=29))
        self.ui.cell_30.clicked.connect(lambda: self.click(sign=30))
        self.ui.cell_31.clicked.connect(lambda: self.click(sign=31))
        self.ui.cell_32.clicked.connect(lambda: self.click(sign=32))
        self.ui.cell_33.clicked.connect(lambda: self.click(sign=33))
        self.ui.cell_34.clicked.connect(lambda: self.click(sign=34))
        self.ui.cell_35.clicked.connect(lambda: self.click(sign=35))
        self.ui.cell_36.clicked.connect(lambda: self.click(sign=36))
        self.ui.cell_37.clicked.connect(lambda: self.click(sign=37))
        self.ui.cell_38.clicked.connect(lambda: self.click(sign=38))
        self.ui.cell_39.clicked.connect(lambda: self.click(sign=39))
        self.ui.cell_40.clicked.connect(lambda: self.click(sign=40))
        self.ui.cell_41.clicked.connect(lambda: self.click(sign=41))
        self.ui.cell_42.clicked.connect(lambda: self.click(sign=42))
        self.ui.cell_43.clicked.connect(lambda: self.click(sign=43))
        self.ui.cell_44.clicked.connect(lambda: self.click(sign=44))
        self.ui.cell_45.clicked.connect(lambda: self.click(sign=45))
        self.ui.cell_46.clicked.connect(lambda: self.click(sign=46))
        self.ui.cell_47.clicked.connect(lambda: self.click(sign=47))
        self.ui.cell_48.clicked.connect(lambda: self.click(sign=48))
        self.ui.cell_49.clicked.connect(lambda: self.click(sign=49))
        self.ui.cell_50.clicked.connect(lambda: self.click(sign=50))
        self.ui.cell_51.clicked.connect(lambda: self.click(sign=51))
        self.ui.cell_52.clicked.connect(lambda: self.click(sign=52))
        self.ui.cell_53.clicked.connect(lambda: self.click(sign=53))
        self.ui.cell_54.clicked.connect(lambda: self.click(sign=54))
        self.ui.cell_55.clicked.connect(lambda: self.click(sign=55))
        self.ui.cell_56.clicked.connect(lambda: self.click(sign=56))
        self.ui.cell_57.clicked.connect(lambda: self.click(sign=57))
        self.ui.cell_58.clicked.connect(lambda: self.click(sign=58))
        self.ui.cell_59.clicked.connect(lambda: self.click(sign=59))
        self.ui.cell_60.clicked.connect(lambda: self.click(sign=60))
        self.ui.cell_61.clicked.connect(lambda: self.click(sign=61))
        self.ui.cell_62.clicked.connect(lambda: self.click(sign=62))
        self.ui.cell_63.clicked.connect(lambda: self.click(sign=63))
        self.ui.cell_64.clicked.connect(lambda: self.click(sign=64))
        self.ui.cell_65.clicked.connect(lambda: self.click(sign=65))
        self.ui.cell_66.clicked.connect(lambda: self.click(sign=66))
        self.ui.cell_67.clicked.connect(lambda: self.click(sign=67))
        self.ui.cell_68.clicked.connect(lambda: self.click(sign=68))
        self.ui.cell_69.clicked.connect(lambda: self.click(sign=69))
        self.ui.cell_70.clicked.connect(lambda: self.click(sign=70))
        self.ui.cell_71.clicked.connect(lambda: self.click(sign=71))
        self.ui.cell_72.clicked.connect(lambda: self.click(sign=72))
        self.ui.cell_73.clicked.connect(lambda: self.click(sign=73))
        self.ui.cell_74.clicked.connect(lambda: self.click(sign=74))
        self.ui.cell_75.clicked.connect(lambda: self.click(sign=75))
        self.ui.cell_76.clicked.connect(lambda: self.click(sign=76))
        self.ui.cell_77.clicked.connect(lambda: self.click(sign=77))
        self.ui.cell_78.clicked.connect(lambda: self.click(sign=78))
        self.ui.cell_79.clicked.connect(lambda: self.click(sign=79))
        self.ui.cell_80.clicked.connect(lambda: self.click(sign=80))
        self.ui.cell_81.clicked.connect(lambda: self.click(sign=81))
        self.ui.cell_82.clicked.connect(lambda: self.click(sign=82))
        self.ui.cell_83.clicked.connect(lambda: self.click(sign=83))
        self.ui.cell_84.clicked.connect(lambda: self.click(sign=84))
        self.ui.cell_85.clicked.connect(lambda: self.click(sign=85))
        self.ui.cell_86.clicked.connect(lambda: self.click(sign=86))
        self.ui.cell_87.clicked.connect(lambda: self.click(sign=87))
        self.ui.cell_88.clicked.connect(lambda: self.click(sign=88))
        self.ui.cell_89.clicked.connect(lambda: self.click(sign=89))
        self.ui.cell_90.clicked.connect(lambda: self.click(sign=90))
        self.ui.cell_91.clicked.connect(lambda: self.click(sign=91))
        self.ui.cell_92.clicked.connect(lambda: self.click(sign=92))
        self.ui.cell_93.clicked.connect(lambda: self.click(sign=93))
        self.ui.cell_94.clicked.connect(lambda: self.click(sign=94))
        self.ui.cell_95.clicked.connect(lambda: self.click(sign=95))
        self.ui.cell_96.clicked.connect(lambda: self.click(sign=96))
        self.ui.cell_97.clicked.connect(lambda: self.click(sign=97))
        self.ui.cell_98.clicked.connect(lambda: self.click(sign=98))
        self.ui.cell_99.clicked.connect(lambda: self.click(sign=99))
        self.ui.cell_100.clicked.connect(lambda: self.click(sign=100))

    # ----------------------- buttons handler -----------------------
    def click(self, sign):
        if sign == 'retry':
            self.retry()

        if sign in range(1, 101):
            self.logic(sign)

    # -------------------------- main logic --------------------------
    def logic(self, sign):
        self.attempt_operations(sign, 'player')
        if self.win_lose_draw(sign, 'x'):
            return None

        sign_ai = choice(self.matrix_ai)
        self.attempt_operations(sign_ai, 'ai')
        if self.win_lose_draw(sign_ai, 'o'):
            return None

    # -------------------------- UI & matrix changes --------------------------
    def attempt_operations(self, sign, who):
        y = (sign - 1) // 10
        x = sign % 10 - 1

        if who == 'player':
            self.matrix[y][x] = 'x'
            getattr(self.ui, f'cell_{sign}').setStyleSheet("background-image : url(cross.png);")
        elif who == 'ai':
            self.matrix[y][x] = 'o'
            getattr(self.ui, f'cell_{sign}').setStyleSheet("background-image : url(circle.png);")
        self.matrix_ai.remove(sign)

        getattr(self.ui, f'cell_{sign}').setChecked(True)
        getattr(self.ui, f'cell_{sign}').setEnabled(False)

    # ----------------------- win lose draw -----------------------
    def win_lose_draw(self, sign, who):

        y = (sign - 1) // 10
        x = sign % 10 - 1

        for i in range(5):
            a = sorted([0, x - 4 + i, 9])[1]
            b = sorted([0, x + i + 1, 10])[1]
            ar = sorted([-1, x + 4 - i, 9])[1]
            br = sorted([-1, x - i - 1, 10])[1]
            c = sorted([0, y - 4 + i, 9])[1]
            d = sorted([0, y + i + 1, 10])[1]

            temp = self.matrix[y][a:b]
            if set(temp) == set(who) and len(temp) == 5:
                self.end_game(who)
                return True

            temp = []
            for t in range(c, d):
                temp.append(self.matrix[t][x])
            if set(temp) == set(who) and len(temp) == 5:
                self.end_game(who)
                return True

            temp = []
            for t, l in zip(range(c, d), range(a, b)):
                temp.append(self.matrix[t][l])
            if set(temp) == set(who) and len(temp) == 5:
                self.end_game(who)
                return True

            temp = []
            for t, l in zip(range(c, d), range(ar, br, -1)):
                temp.append(self.matrix[t][l])
            if set(temp) == set(who) and len(temp) == 5:
                self.end_game(who)
                return True

        if not self.matrix_ai:
            self.end_game('DRAW')
            return True

    # ----------------------- blocking cells after the end -----------------------
    def end_game(self, text):
        if text == 'x':
            text = 'You lose'
        elif text == 'o':
            text = 'You win'

        for i in range(1, 101):
            getattr(self.ui, f'cell_{i}').setEnabled(False)
            getattr(self.ui, f'cell_{i}').setChecked(True)
        self.ui.label.setText(text)

    # ----------------------- refreshing the game -----------------------
    def retry(self):
        for i in range(1, 101):
            getattr(self.ui, f'cell_{i}').setStyleSheet("background-image : None;")
            getattr(self.ui, f'cell_{i}').setEnabled(True)
            getattr(self.ui, f'cell_{i}').setChecked(False)
        self.matrix = [['-' for _ in range(10)] for _ in range(10)]
        self.matrix_ai = [i for i in range(1, 101)]
        self.ui.btn_retry.setText('Retry')
        self.ui.label.setText(None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
