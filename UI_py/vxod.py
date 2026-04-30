# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_vxod.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QSizePolicy, QWidget


class Ui_Vxod(object):
    def setupUi(self, Vxod):
        if not Vxod.objectName():
            Vxod.setObjectName("Vxod")
        Vxod.resize(1920, 1080)
        Vxod.setMinimumSize(QSize(1920, 1080))
        Vxod.setMaximumSize(QSize(1920, 1080))
        Vxod.setStyleSheet("background-color: rgb(63, 54, 43);")
        self.label = QLabel(Vxod)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(
            'border-image: url("/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest1.jpg") 0 0 0 0 stretch stretch'
        )
        self.btm_prodolj = QPushButton(Vxod)
        self.btm_prodolj.setObjectName("btm_prodolj")
        self.btm_prodolj.setGeometry(QRect(120, 340, 460, 50))
        self.btm_prodolj.setStyleSheet(
            "border: 3px solid;\n"
            "border-radius: 5px;\n"
            "border-color: rgba(192, 200, 115,100);\n"
            "background-color: rgba(23, 35, 25, 205);\n"
            "color: rgb(151, 202, 171);\n"
            'font: 500 italic 20pt "Z003 [urw]";'
        )
        self.btm_new_sessia = QPushButton(Vxod)
        self.btm_new_sessia.setObjectName("btm_new_sessia")
        self.btm_new_sessia.setGeometry(QRect(120, 440, 460, 50))
        self.btm_new_sessia.setStyleSheet(
            "border: 3px solid;\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "border-radius: 5px;\n"
            "border-color: rgba(192, 200, 115,100);\n"
            "background-color: rgba(23, 35, 25, 205);\n"
            "color: rgb(151, 202, 171);"
        )
        self.btm_exit = QPushButton(Vxod)
        self.btm_exit.setObjectName("btm_exit")
        self.btm_exit.setGeometry(QRect(120, 640, 460, 50))
        self.btm_exit.setStyleSheet(
            "border: 3px solid;\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "border-radius: 5px;\n"
            "border-color: rgba(192, 200, 115,100);\n"
            "background-color: rgba(23, 35, 25, 205);\n"
            "color: rgb(151, 202, 171);"
        )
        self.btm_zagruz_sessiu = QPushButton(Vxod)
        self.btm_zagruz_sessiu.setObjectName("btm_zagruz_sessiu")
        self.btm_zagruz_sessiu.setGeometry(QRect(120, 540, 460, 50))
        self.btm_zagruz_sessiu.setStyleSheet(
            "border: 3px solid;\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "border-radius: 5px;\n"
            "border-color: rgba(192, 200, 115,100);\n"
            "background-color: rgba(23, 35, 25, 205);\n"
            "color: rgb(151, 202, 171);"
        )
        self.label_2 = QLabel(Vxod)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(100, 240, 500, 530))
        self.label_2.setStyleSheet(
            "background-color: rgba(241, 243, 181, 55);\nborder-radius: 25px;"
        )
        self.label.raise_()
        self.label_2.raise_()
        self.btm_prodolj.raise_()
        self.btm_new_sessia.raise_()
        self.btm_zagruz_sessiu.raise_()
        self.btm_exit.raise_()

        self.retranslateUi(Vxod)

        QMetaObject.connectSlotsByName(Vxod)

    # setupUi

    def retranslateUi(self, Vxod):
        Vxod.setWindowTitle(QCoreApplication.translate("Vxod", "Form", None))
        self.label.setText("")
        self.btm_prodolj.setText(
            QCoreApplication.translate(
                "Vxod",
                "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c",
                None,
            )
        )
        self.btm_new_sessia.setText(
            QCoreApplication.translate(
                "Vxod",
                "\u041d\u043e\u0432\u0430\u044f \u0441\u0435\u0441\u0441\u0438\u044f",
                None,
            )
        )
        self.btm_exit.setText(
            QCoreApplication.translate("Vxod", "\u0412\u044b\u0445\u043e\u0434", None)
        )
        self.btm_zagruz_sessiu.setText(
            QCoreApplication.translate(
                "Vxod",
                "\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u044e",
                None,
            )
        )
        self.label_2.setText("")

    # retranslateUi
