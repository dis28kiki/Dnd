# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_create2.ui'
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

class Ui_Form2(object):
    def setupUi(self, Form2):
        if not Form2.objectName():
            Form2.setObjectName(u"Form2")
        Form2.resize(1920, 1080)
        self.label = QLabel(Form2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"border-image: url(\"/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest5.jpg\") 0 0 0 0 stretch stretch")
        self.label_2 = QLabel(Form2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 100, 1720, 840))
        self.label_2.setStyleSheet(u"/*background-color: rgba(241, 243, 181, 55);*/\n"
"background-color: rgba(99, 113, 54, 75);\n"
"border-radius: 145px;")
        self.label_3 = QLabel(Form2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 170, 581, 441))
        self.label_3.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 115);\n"
"border-radius: 205px;\n"
"opacity: 0.5;")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.ptm_del_kvest = QPushButton(Form2)
        self.ptm_del_kvest.setObjectName(u"ptm_del_kvest")
        self.ptm_del_kvest.setGeometry(QRect(1270, 850, 451, 40))
        self.ptm_del_kvest.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_add_kvest = QPushButton(Form2)
        self.btm_add_kvest.setObjectName(u"btm_add_kvest")
        self.btm_add_kvest.setGeometry(QRect(820, 850, 421, 40))
        self.btm_add_kvest.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_kvest = QListWidget(Form2)
        self.list_kvest.setObjectName(u"list_kvest")
        self.list_kvest.setGeometry(QRect(230, 640, 531, 201))
        self.list_kvest.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_kvest.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_dalee = QPushButton(Form2)
        self.btm_dalee.setObjectName(u"btm_dalee")
        self.btm_dalee.setGeometry(QRect(1690, 970, 191, 40))
        self.btm_dalee.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_nazad = QPushButton(Form2)
        self.btm_nazad.setObjectName(u"btm_nazad")
        self.btm_nazad.setGeometry(QRect(20, 30, 191, 40))
        self.btm_nazad.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_4 = QLabel(Form2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 210, 451, 361))
        self.label_4.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.textEdit_sujet = QTextEdit(Form2)
        self.textEdit_sujet.setObjectName(u"textEdit_sujet")
        self.textEdit_sujet.setGeometry(QRect(820, 170, 901, 441))
        self.textEdit_sujet.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.textEdit_kvest = QTextEdit(Form2)
        self.textEdit_kvest.setObjectName(u"textEdit_kvest")
        self.textEdit_kvest.setGeometry(QRect(820, 640, 901, 201))
        self.textEdit_kvest.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")

        self.retranslateUi(Form2)

        QMetaObject.connectSlotsByName(Form2)
    # setupUi

    def retranslateUi(self, Form2):
        Form2.setWindowTitle(QCoreApplication.translate("Form2", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form2", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.ptm_del_kvest.setText(QCoreApplication.translate("Form2", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_kvest.setText(QCoreApplication.translate("Form2", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_dalee.setText(QCoreApplication.translate("Form2", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btm_nazad.setText(QCoreApplication.translate("Form2", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_4.setText(QCoreApplication.translate("Form2", u"<html><head/><body><p align=\"center\">\u0422\u044b \u0443\u0436\u0435 \u043d\u0430 \u0432\u0435\u0440\u043d\u043e\u043c \u043f\u0443\u0442\u0438, \u041c\u0430\u0441\u0442\u0435\u0440. \u0422\u0435\u043f\u0435\u0440\u044c, \u043f\u0440\u043e\u0448\u0443 \u043d\u0430\u043f\u0438\u0448\u0438 \u043e\u0441\u043d\u043e\u0432\u044b\u043d\u043e\u0439 \u0441\u044e\u0436\u0435\u0442 \u0438 \u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e \u0434\u043e\u0431\u0430\u0432\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043e\u0442\u0434\u0435\u043b\u044c\u043d\u044b\u0445 \u043a\u0432\u0435\u0441\u0442\u043e\u0432, \u0447\u0442\u043e \u043c\u043e\u0433\u0443\u0442 \u0432\u0441\u0442\u0440\u0435\u0447\u0430\u0442\u044c\u0441\u044f \u043d\u0430 \u043f\u0443\u0442\u0438 \u0443 \u0431\u0443\u0434\u0443\u0449\u0438\u0445 \u0433\u0435\u0440\u043e\u0435\u0432.</p></body></html>", None))
        self.textEdit_sujet.setPlaceholderText(QCoreApplication.translate("Form2", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0441\u044e\u0436\u0435\u0442", None))
        self.textEdit_kvest.setPlaceholderText(QCoreApplication.translate("Form2", u"\u041d\u0430\u043f\u0438\u0448\u0438 \u043e \u043a\u0432\u0435\u0441\u0442\u0435...", None))
    # retranslateUi

