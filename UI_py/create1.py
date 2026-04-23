# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_create1.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Form1(object):
    def setupUi(self, Form1):
        if not Form1.objectName():
            Form1.setObjectName(u"Form1")
        Form1.resize(1920, 1080)
        self.label = QLabel(Form1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"border-image: url(\"/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest5.jpg\") 0 0 0 0 stretch stretch")
        self.label_2 = QLabel(Form1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 100, 1720, 840))
        self.label_2.setStyleSheet(u"/*background-color: rgba(241, 243, 181, 55);*/\n"
"background-color: rgba(99, 113, 54, 75);\n"
"border-radius: 145px;")
        self.label_3 = QLabel(Form1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 270, 681, 601))
        self.label_3.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 125);\n"
"border-radius: 205px;\n"
"opacity: 0.5;")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.ptm_del_musik = QPushButton(Form1)
        self.ptm_del_musik.setObjectName(u"ptm_del_musik")
        self.ptm_del_musik.setGeometry(QRect(1340, 820, 380, 40))
        self.ptm_del_musik.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_add_musik = QPushButton(Form1)
        self.btm_add_musik.setObjectName(u"btm_add_musik")
        self.btm_add_musik.setGeometry(QRect(940, 820, 380, 40))
        self.btm_add_musik.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_musik = QListWidget(Form1)
        self.list_musik.setObjectName(u"list_musik")
        self.list_musik.setGeometry(QRect(940, 520, 781, 291))
        self.list_musik.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 14pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_musik.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_del_seting = QPushButton(Form1)
        self.btm_del_seting.setObjectName(u"btm_del_seting")
        self.btm_del_seting.setGeometry(QRect(1340, 420, 381, 40))
        self.btm_del_seting.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_add_srtting = QPushButton(Form1)
        self.btm_add_srtting.setObjectName(u"btm_add_srtting")
        self.btm_add_srtting.setGeometry(QRect(940, 420, 381, 40))
        self.btm_add_srtting.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_seting = QListWidget(Form1)
        self.list_seting.setObjectName(u"list_seting")
        self.list_seting.setGeometry(QRect(940, 180, 781, 231))
        self.list_seting.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 14pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 205px;\n"
"opacity: 0.5;")
        self.list_seting.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_dalee = QPushButton(Form1)
        self.btm_dalee.setObjectName(u"btm_dalee")
        self.btm_dalee.setGeometry(QRect(1690, 970, 191, 40))
        self.btm_dalee.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_nazad = QPushButton(Form1)
        self.btm_nazad.setObjectName(u"btm_nazad")
        self.btm_nazad.setGeometry(QRect(20, 30, 191, 40))
        self.btm_nazad.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_4 = QLabel(Form1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 210, 571, 641))
        self.label_4.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(Form1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(940, 140, 331, 31))
        self.label_5.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_6 = QLabel(Form1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(940, 480, 331, 31))
        self.label_6.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.lineEdit = QLineEdit(Form1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 180, 681, 61))
        self.lineEdit.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")

        self.retranslateUi(Form1)

        QMetaObject.connectSlotsByName(Form1)
    # setupUi

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(QCoreApplication.translate("Form1", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form1", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.ptm_del_musik.setText(QCoreApplication.translate("Form1", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_musik.setText(QCoreApplication.translate("Form1", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btm_del_seting.setText(QCoreApplication.translate("Form1", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_srtting.setText(QCoreApplication.translate("Form1", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.btm_dalee.setText(QCoreApplication.translate("Form1", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btm_nazad.setText(QCoreApplication.translate("Form1", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_4.setText(QCoreApplication.translate("Form1", u"<html><head/><body><p align=\"center\">\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c, \u041c\u0430\u0441\u0442\u0435\u0440!</p><p align=\"center\">\u0412\u043f\u0435\u0440\u0435\u0434\u0438 \u0442\u0435\u0431\u044f \u0436\u0434\u0435\u0442 \u0443\u0432\u043b\u0435\u043a\u0430\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u0433\u0440\u0430, \u043d\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u044d\u043c\u043e\u0446\u0438\u044f\u043c\u0438, \u043d\u043e \u043f\u0435\u0440\u0435\u0434 \u043d\u0430\u0447\u0430\u043b\u0430\u043c \u0442\u0435\u0431\u0435 \u043d\u0443\u0436\u043d\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0441\u0432\u043e\u044e \u043e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0443\u044e \u0441\u0440\u0435\u0434\u0443, \u0447\u0442\u043e \u0431\u044b \u043b\u043e\u0432\u043a\u043e \u0443\u043f\u0440\u0430\u0432\u043b\u044f\u0442\u044c \u0432\u0441\u0435\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435"
                        "\u0439 \u0432 \u0438\u0433\u0440\u0435 \u0438 \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u0443\u043f\u0443\u0441\u0442\u0438\u0442\u044c.</p><p align=\"center\">\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0431\u0435 \u0441\u0442\u043e\u0438\u0442 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0435\u0442\u0442\u0438\u043d\u0433, \u0432 \u043f\u043e\u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c \u0434\u043b\u044f \u0442\u0435\u0431\u044f \u044d\u0442\u043e \u0431\u0443\u0434\u0443\u0442 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438, \u0433\u0434\u0435 \u0442\u044b \u043c\u043e\u0436\u0435\u0448\u044c \u043d\u0430\u0439\u0442\u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043f\u043e \u044d\u0442\u043e\u0439 \u0432\u0441\u0435\u043b\u0435\u043d\u043d\u043e\u0439. \u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e \u0431\u0443\u0434\u0443\u0442 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u044b \u043a\u043d"
                        "\u0438\u0433\u0438 \u043f\u043e 5-\u043c\u0443 \u0438\u0437\u0434\u0430\u043d\u0438\u044e Dungeon &amp; Dragons. \u041f\u0440\u0438 \u0436\u0435\u043b\u0430\u043d\u0438\u0438 \u043c\u043e\u0436\u0435\u0448\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u0432\u043e\u0438 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 PDF, TXT \u0438 \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0432 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u043e\u043c \u0441\u043f\u0438\u0441\u043a\u0435. \u0422\u0430\u043a \u0436\u0435 \u0432\u044b\u0431\u0435\u0440\u0438 \u043c\u0443\u0437\u044b\u043a\u0443, \u0447\u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0430\u0442\u044c \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u043d\u0430 \u043f\u0440\u043e\u0442\u044f\u0436\u0435\u043d\u0438\u0438 \u0432\u0441\u0435\u0433\u043e \u043f\u0440\u0438\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f"
                        ". \u0411\u0430\u0437\u043e\u0432\u044b\u0435 \u043c\u0435\u043b\u043e\u0434\u0438\u0438 \u0443\u0436\u0435 \u0432\u0441\u0442\u0440\u043e\u0435\u043d\u044b.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form1", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043f\u0440\u0430\u0432\u043e\u043a", None))
        self.label_6.setText(QCoreApplication.translate("Form1", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0438\u0439", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form1", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438\u0433\u0440\u044b...", None))
    # retranslateUi

