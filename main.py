import sys

from PySide6.QtWidgets import (
    QApplication,
    QHeaderView,
    QMainWindow,
    QMessageBox,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QWidget,
)

from db import db
from UI_py.create1 import Ui_Form1
from UI_py.create2 import Ui_Form2
from UI_py.create3 import Ui_Form3
from UI_py.create4 import Ui_Form4
from UI_py.create5 import Ui_Form5
from UI_py.maine import Ui_Form_main
from UI_py.vxod import Ui_Vxod


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.db = db

        self.vxod_widget = QWidget()
        self.vxod_ui = Ui_Vxod()
        self.vxod_ui.setupUi(self.vxod_widget)

        self.create1_widget = QWidget()
        self.create1_ui = Ui_Form1()
        self.create1_ui.setupUi(self.create1_widget)

        self.create2_widget = QWidget()
        self.create2_ui = Ui_Form2()
        self.create2_ui.setupUi(self.create2_widget)

        self.create3_widget = QWidget()
        self.create3_ui = Ui_Form3()
        self.create3_ui.setupUi(self.create3_widget)

        self.create4_widget = QWidget()
        self.create4_ui = Ui_Form4()
        self.create4_ui.setupUi(self.create4_widget)

        self.create5_widget = QWidget()
        self.create5_ui = Ui_Form5()
        self.create5_ui.setupUi(self.create5_widget)

        self.main_widget = QWidget()
        self.main_ui = Ui_Form_main()
        self.main_ui.setupUi(self.main_widget)

        self.stacked_widget.addWidget(self.vxod_widget)  # 0
        self.stacked_widget.addWidget(self.create1_widget)
        self.stacked_widget.addWidget(self.create2_widget)
        self.stacked_widget.addWidget(self.create3_widget)
        self.stacked_widget.addWidget(self.create4_widget)
        self.stacked_widget.addWidget(self.create5_widget)
        self.stacked_widget.addWidget(self.main_widget)

        self.stacked_widget.setCurrentIndex(0)
        # |||||                      подключение кнопок                             ||||
        # выход и выход между окнами

        # self.vxod_ui.btm_prodolj.clicked.connect()
        # self.vxod_ui.btm_zagruz_sessiu.clicked.connect()
        self.vxod_ui.btm_exit.clicked.connect(self.exit_)
        self.vxod_ui.btm_new_sessia.clicked.connect(self.go_to_create1)

        self.create1_ui.btm_nazad.clicked.connect(self.go_to_vxod)
        self.create1_ui.btm_dalee.clicked.connect(self.go_to_create2)

        self.create2_ui.btm_nazad.clicked.connect(self.go_to_create1)
        self.create2_ui.btm_dalee.clicked.connect(self.go_to_create3)

        self.create3_ui.btm_nazad.clicked.connect(self.go_to_create2)
        self.create3_ui.btm_dalee.clicked.connect(self.go_to_create4)

        self.create4_ui.btm_nazad.clicked.connect(self.go_to_create3)
        self.create4_ui.btm_dalee.clicked.connect(self.go_to_create5)

        self.create5_ui.btm_nazad.clicked.connect(self.go_to_create4)
        self.create5_ui.btm_dalee.clicked.connect(self.go_to_main)

        self.main_ui.btm_nazad.clicked.connect(self.go_to_vxod)

    def exit_(self):
        QApplication.quit()

    def go_to_vxod(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_create1(self):
        self.stacked_widget.setCurrentIndex(1)

    def go_to_create2(self):
        self.stacked_widget.setCurrentIndex(2)

    def go_to_create3(self):
        self.stacked_widget.setCurrentIndex(3)

    def go_to_create4(self):
        self.stacked_widget.setCurrentIndex(4)

    def go_to_create5(self):
        self.stacked_widget.setCurrentIndex(5)

    def go_to_main(self):
        self.stacked_widget.setCurrentIndex(6)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
