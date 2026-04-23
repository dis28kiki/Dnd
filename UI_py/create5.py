# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_create5.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form5(object):
    def setupUi(self, Form5):
        if not Form5.objectName():
            Form5.setObjectName(u"Form5")
        Form5.resize(1920, 1080)
        self.label = QLabel(Form5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"border-image: url(\"/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest5.jpg\") 0 0 0 0 stretch stretch")
        self.label_2 = QLabel(Form5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 100, 1720, 840))
        self.label_2.setStyleSheet(u"/*background-color: rgba(241, 243, 181, 55);*/\n"
"background-color: rgba(99, 113, 54, 75);\n"
"border-radius: 145px;")
        self.label_3 = QLabel(Form5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 170, 661, 381))
        self.label_3.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 95);\n"
"border-radius: 150px;\n"
"opacity: 0.5;")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.list_files_zamenki = QListWidget(Form5)
        self.list_files_zamenki.setObjectName(u"list_files_zamenki")
        self.list_files_zamenki.setGeometry(QRect(220, 610, 641, 271))
        self.list_files_zamenki.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_files_zamenki.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_dalee = QPushButton(Form5)
        self.btm_dalee.setObjectName(u"btm_dalee")
        self.btm_dalee.setGeometry(QRect(1690, 970, 191, 40))
        self.btm_dalee.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_nazad = QPushButton(Form5)
        self.btm_nazad.setObjectName(u"btm_nazad")
        self.btm_nazad.setGeometry(QRect(20, 30, 191, 40))
        self.btm_nazad.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_4 = QLabel(Form5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 180, 451, 361))
        self.label_4.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_9 = QLabel(Form5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 580, 291, 31))
        self.label_9.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btm_add_zamentk = QPushButton(Form5)
        self.btm_add_zamentk.setObjectName(u"btm_add_zamentk")
        self.btm_add_zamentk.setGeometry(QRect(920, 840, 390, 40))
        self.btm_add_zamentk.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.ptm_del_zamenki = QPushButton(Form5)
        self.ptm_del_zamenki.setObjectName(u"ptm_del_zamenki")
        self.ptm_del_zamenki.setGeometry(QRect(1320, 840, 390, 40))
        self.ptm_del_zamenki.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.textEdit_zamenki = QTextEdit(Form5)
        self.textEdit_zamenki.setObjectName(u"textEdit_zamenki")
        self.textEdit_zamenki.setGeometry(QRect(920, 180, 791, 651))
        self.textEdit_zamenki.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_6 = QLabel(Form5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(870, 150, 431, 31))
        self.label_6.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Form5)

        QMetaObject.connectSlotsByName(Form5)
    # setupUi

    def retranslateUi(self, Form5):
        Form5.setWindowTitle(QCoreApplication.translate("Form5", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form5", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.btm_dalee.setText(QCoreApplication.translate("Form5", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btm_nazad.setText(QCoreApplication.translate("Form5", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_4.setText(QCoreApplication.translate("Form5", u"<html><head/><body><p align=\"center\">\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u044d\u0442\u0430\u043f \u043f\u0435\u0440\u0435\u0434 \u043d\u0430\u0447\u0430\u043b\u043e\u043c \u0432\u0430\u0448\u0435\u0433\u043e \u0443\u0432\u043b\u0435\u043a\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f. \u0412 \u044d\u0442\u043e\u043c \u043c\u0435\u043d\u044e \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u044e\u0431\u0443\u044e \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043c\u043e\u0436\u0435\u0442 \u043f\u043e\u043d\u0430\u0434\u0438\u0442\u044c\u0441\u044f \u0432 \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u043c. \u0412\u044b \u0441\u043c\u043e\u0436\u0435\u0442\u0435 \u0435\u0433\u043e \u0440\u0435\u0434\u0430\u043a"
                        "\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438 \u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u043b\u044e\u0431\u044b\u0435 \u0437\u0430\u043c\u0435\u0442\u043a\u0438.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Form5", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043c\u0435\u0442\u043e\u043a", None))
        self.btm_add_zamentk.setText(QCoreApplication.translate("Form5", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ptm_del_zamenki.setText(QCoreApplication.translate("Form5", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Form5", u"\u041e\u043a\u043e\u0448\u043a\u043e \u0434\u043b\u044f \u0432\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438", None))
    # retranslateUi

