# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


# =======================
# Código generado por pyuic5 (train.ui)
# =======================
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(904, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 911, 661))
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap("Revolucion-Ferroviaria-en-Mexico-Alejandro-Armenta.jpg")
        )
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.s1 = QtWidgets.QPushButton(self.centralwidget)
        self.s1.setGeometry(QtCore.QRect(70, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.s1.setFont(font)
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QPushButton(self.centralwidget)
        self.s2.setGeometry(QtCore.QRect(70, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.s2.setFont(font)
        self.s2.setObjectName("s2")
        self.s4 = QtWidgets.QPushButton(self.centralwidget)
        self.s4.setGeometry(QtCore.QRect(740, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.s4.setFont(font)
        self.s4.setObjectName("s4")
        self.s5 = QtWidgets.QPushButton(self.centralwidget)
        self.s5.setGeometry(QtCore.QRect(740, 350, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.s5.setFont(font)
        self.s5.setObjectName("s5")
        self.s3 = QtWidgets.QPushButton(self.centralwidget)
        self.s3.setGeometry(QtCore.QRect(410, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.s3.setFont(font)
        self.s3.setObjectName("s3")
        self.u1 = QtWidgets.QPushButton(self.centralwidget)
        self.u1.setGeometry(QtCore.QRect(110, 170, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u1.setFont(font)
        self.u1.setObjectName("u1")
        self.l1 = QtWidgets.QPushButton(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(110, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l1.setFont(font)
        self.l1.setObjectName("l1")
        self.u2 = QtWidgets.QPushButton(self.centralwidget)
        self.u2.setGeometry(QtCore.QRect(180, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u2.setFont(font)
        self.u2.setObjectName("u2")
        self.l2 = QtWidgets.QPushButton(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(180, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l2.setFont(font)
        self.l2.setObjectName("l2")
        self.u3 = QtWidgets.QPushButton(self.centralwidget)
        self.u3.setGeometry(QtCore.QRect(270, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u3.setFont(font)
        self.u3.setObjectName("u3")
        self.l3 = QtWidgets.QPushButton(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(270, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l3.setFont(font)
        self.l3.setObjectName("l3")
        self.u7 = QtWidgets.QPushButton(self.centralwidget)
        self.u7.setGeometry(QtCore.QRect(330, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u7.setFont(font)
        self.u7.setObjectName("u7")
        self.u8 = QtWidgets.QPushButton(self.centralwidget)
        self.u8.setGeometry(QtCore.QRect(490, 180, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u8.setFont(font)
        self.u8.setObjectName("u8")
        self.u5 = QtWidgets.QPushButton(self.centralwidget)
        self.u5.setGeometry(QtCore.QRect(630, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u5.setFont(font)
        self.u5.setObjectName("u5")
        self.l4 = QtWidgets.QPushButton(self.centralwidget)
        self.l4.setGeometry(QtCore.QRect(540, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l4.setFont(font)
        self.l4.setObjectName("l4")
        self.u4 = QtWidgets.QPushButton(self.centralwidget)
        self.u4.setGeometry(QtCore.QRect(540, 260, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u4.setFont(font)
        self.u4.setObjectName("u4")
        self.l5 = QtWidgets.QPushButton(self.centralwidget)
        self.l5.setGeometry(QtCore.QRect(630, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l5.setFont(font)
        self.l5.setObjectName("l5")
        self.l6 = QtWidgets.QPushButton(self.centralwidget)
        self.l6.setGeometry(QtCore.QRect(690, 400, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.l6.setFont(font)
        self.l6.setObjectName("l6")
        self.u6 = QtWidgets.QPushButton(self.centralwidget)
        self.u6.setGeometry(QtCore.QRect(690, 170, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.u6.setFont(font)
        self.u6.setObjectName("u6")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(770, 560, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Monocraft")
        font.setPointSize(10)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.s1.setText(_translate("MainWindow", "S1"))
        self.s2.setText(_translate("MainWindow", "S2"))
        self.s4.setText(_translate("MainWindow", "S4"))
        self.s5.setText(_translate("MainWindow", "S5"))
        self.s3.setText(_translate("MainWindow", "S3"))
        self.u1.setText(_translate("MainWindow", "U1 ->"))
        self.l1.setText(_translate("MainWindow", "L1 ->"))
        self.u2.setText(_translate("MainWindow", "<- U2"))
        self.l2.setText(_translate("MainWindow", "<- L2"))
        self.u3.setText(_translate("MainWindow", "U3 ->"))
        self.l3.setText(_translate("MainWindow", "L3->"))
        self.u7.setText(_translate("MainWindow", "<- U7"))
        self.u8.setText(_translate("MainWindow", "U8 ->"))
        self.u5.setText(_translate("MainWindow", "U5->"))
        self.l4.setText(_translate("MainWindow", "<- L4"))
        self.u4.setText(_translate("MainWindow", "<- U4"))
        self.l5.setText(_translate("MainWindow", "L5->"))
        self.l6.setText(_translate("MainWindow", "<- L6"))
        self.u6.setText(_translate("MainWindow", "<- U6"))
        self.clear.setText(_translate("MainWindow", "CLEAR"))


# =======================
# Lógica adicional para evaluar reglas, actualizar la interfaz y hacer backtracking
# =======================

# Reglas definidas (en formato Python)
rules = [
    {"id": 1, "operator": "AND", "premises": ["U1 = green"], "conclusion": "L1 = red"},
    {"id": 2, "operator": "AND", "premises": ["U6 = green"], "conclusion": "L6 = red"},
    {"id": 3, "operator": "AND", "premises": ["S1 = busy"], "conclusion": "U2 = red"},
    {"id": 4, "operator": "AND", "premises": ["S2 = busy"], "conclusion": "L2 = red"},
    {"id": 5, "operator": "AND", "premises": ["S3 = busy"], "conclusion": "U3 = red"},
    {"id": 6, "operator": "AND", "premises": ["S3 = busy"], "conclusion": "U4 = red"},
    {"id": 7, "operator": "AND", "premises": ["S4 = busy"], "conclusion": "U5 = red"},
    {"id": 8, "operator": "AND", "premises": ["S5 = busy"], "conclusion": "L5 = red"},
    {
        "id": 9,
        "operator": "OR",
        "premises": [["U3 = red", "L3 = red"], ["U5 = red", "L5 = red"]],
        "conclusion": "U1 = red",
    },
    {
        "id": 10,
        "operator": "OR",
        "premises": [["U3 = red", "L3 = red"], ["U5 = red", "L5 = red"]],
        "conclusion": "L1 = red",
    },
    {
        "id": 11,
        "operator": "OR",
        "premises": [["U2 = red", "L2 = red"], ["U4 = red", "L4 = red"]],
        "conclusion": "U6 = red",
    },
    {
        "id": 12,
        "operator": "OR",
        "premises": [["U2 = red", "L2 = red"], ["U4 = red", "L4 = red"]],
        "conclusion": "L6 = red",
    },
    {
        "id": 13,
        "operator": "AND",
        "premises": ["U2 = red", "L2 = red"],
        "conclusion": "U7 = red",
    },
    {
        "id": 14,
        "operator": "AND",
        "premises": ["U5 = red", "L5 = red"],
        "conclusion": "U8 = red",
    },
    {
        "id": 15,
        "operator": "AND",
        "premises": ["U3 = green"],
        "conclusion": "U4 = green",
    },
    {
        "id": 16,
        "operator": "AND",
        "premises": ["L3 = green"],
        "conclusion": "L4 = green",
    },
    {"id": 17, "operator": "AND", "premises": ["U2 = green"], "conclusion": "L2 = red"},
    {"id": 18, "operator": "AND", "premises": ["U3 = green"], "conclusion": "L3 = red"},
    {"id": 19, "operator": "AND", "premises": ["U4 = green"], "conclusion": "L4 = red"},
    {"id": 20, "operator": "AND", "premises": ["U5 = green"], "conclusion": "L5 = red"},
    {
        "id": 21,
        "operator": "OR",
        "premises": ["U1 = green", "L1 = green"],
        "conclusion": "U7 = red",
    },
    {
        "id": 22,
        "operator": "OR",
        "premises": ["U6 = green", "L6 = green"],
        "conclusion": "U8 = red",
    },
]


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.buttons = {
            "S1": self.s1,
            "S2": self.s2,
            "S3": self.s3,
            "S4": self.s4,
            "S5": self.s5,
            "U1": self.u1,
            "U2": self.u2,
            "U3": self.u3,
            "U4": self.u4,
            "U5": self.u5,
            "U6": self.u6,
            "U7": self.u7,
            "U8": self.u8,
            "L1": self.l1,
            "L2": self.l2,
            "L3": self.l3,
            "L4": self.l4,
            "L5": self.l5,
            "L6": self.l6,
        }

        self.states = {key: "" for key in self.buttons.keys()}

        self.manual = {key: False for key in self.buttons.keys()}

        self.history = []
        self.push_history()

        for name, button in self.buttons.items():
            if name.startswith("U") or name.startswith("L"):
                button.clicked.connect(
                    lambda checked, n=name: self.set_state(n, "green")
                )
            elif name.startswith("S"):
                button.clicked.connect(
                    lambda checked, n=name: self.set_state(n, "busy")
                )

        self.clear.clicked.connect(self.clear_states)

    def push_history(self):
        self.history.append(self.states.copy())

    def backtrack(self):
        if len(self.history) > 1:
            self.history.pop()
            self.states = self.history[-1].copy()
            self.manual = {key: False for key in self.buttons.keys()}
            self.update_ui()

    def clear_states(self):
        for key in self.states:
            self.states[key] = ""
        self.history = []
        self.push_history()
        self.manual = {key: False for key in self.buttons.keys()}
        self.update_ui()

    def set_state(self, name, new_state):
        if not self.manual.get(name, False) and self.states.get(name, "") != "":
            self.backtrack()
            return

        self.manual[name] = True
        self.states[name] = new_state
        self.push_history()
        self.evaluate_rules()
        self.update_ui()

    def update_ui(self):
        for key, button in self.buttons.items():
            state = self.states[key]
            if state == "green":
                color = "green"
            elif state == "red":
                color = "red"
            elif state == "busy":
                color = "yellow"
            else:
                color = ""
            if color:
                button.setStyleSheet("background-color: " + color)
            else:
                button.setStyleSheet("")

    def evaluate_rules(self):
        changed = True
        while changed:
            changed = False
            for rule in rules:
                if rule["operator"] == "AND":
                    premises = rule["premises"]
                    all_true = True
                    for cond in premises:
                        if not self.check_condition(cond):
                            all_true = False
                            break
                    if all_true:
                        if self.apply_conclusion(rule["conclusion"]):
                            changed = True
                elif rule["operator"] == "OR":
                    premises = rule["premises"]
                    satisfied = False
                    for cond in premises:
                        if isinstance(cond, list):
                            if all(self.check_condition(c) for c in cond):
                                satisfied = True
                                break
                        else:
                            if self.check_condition(cond):
                                satisfied = True
                                break
                    if satisfied:
                        if self.apply_conclusion(rule["conclusion"]):
                            changed = True

    def check_condition(self, condition):
        try:
            key, value = condition.split("=")
            key = key.strip()
            value = value.strip()
            return self.states.get(key, "") == value
        except Exception as e:
            print("Error evaluando condición:", condition, e)
            return False

    def apply_conclusion(self, conclusion):
        key, value = conclusion.split("=")
        key = key.strip()
        value = value.strip()
        if self.states.get(key, "") != value:
            self.states[key] = value
            return True
        return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
