# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_create4.ui'
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

class Ui_Form4(object):
    def setupUi(self, Form4):
        if not Form4.objectName():
            Form4.setObjectName(u"Form4")
        Form4.resize(1920, 1080)
        self.label = QLabel(Form4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"border-image: url(\"/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest5.jpg\") 0 0 0 0 stretch stretch")
        self.label_2 = QLabel(Form4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 100, 1720, 840))
        self.label_2.setStyleSheet(u"/*background-color: rgba(241, 243, 181, 55);*/\n"
"background-color: rgba(99, 113, 54, 75);\n"
"border-radius: 145px;")
        self.label_3 = QLabel(Form4)
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
        self.ptm_del_kvest = QPushButton(Form4)
        self.ptm_del_kvest.setObjectName(u"ptm_del_kvest")
        self.ptm_del_kvest.setGeometry(QRect(530, 840, 331, 40))
        self.ptm_del_kvest.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_add_kvest = QPushButton(Form4)
        self.btm_add_kvest.setObjectName(u"btm_add_kvest")
        self.btm_add_kvest.setGeometry(QRect(220, 840, 301, 40))
        self.btm_add_kvest.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_kvest = QListWidget(Form4)
        self.list_kvest.setObjectName(u"list_kvest")
        self.list_kvest.setGeometry(QRect(220, 610, 641, 221))
        self.list_kvest.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_kvest.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_dalee = QPushButton(Form4)
        self.btm_dalee.setObjectName(u"btm_dalee")
        self.btm_dalee.setGeometry(QRect(1690, 970, 191, 40))
        self.btm_dalee.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.btm_nazad = QPushButton(Form4)
        self.btm_nazad.setObjectName(u"btm_nazad")
        self.btm_nazad.setGeometry(QRect(20, 30, 191, 40))
        self.btm_nazad.setStyleSheet(u"color: rgb(14, 4, 5);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 175);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_4 = QLabel(Form4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 180, 451, 361))
        self.label_4.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.list_kvest_2 = QListWidget(Form4)
        self.list_kvest_2.setObjectName(u"list_kvest_2")
        self.list_kvest_2.setGeometry(QRect(920, 220, 800, 241))
        self.list_kvest_2.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.list_kvest_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.label_5 = QLabel(Form4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(910, 190, 431, 31))
        self.label_5.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(Form4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(160, 580, 291, 31))
        self.label_9.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btm_add_kvest_2 = QPushButton(Form4)
        self.btm_add_kvest_2.setObjectName(u"btm_add_kvest_2")
        self.btm_add_kvest_2.setGeometry(QRect(920, 840, 390, 40))
        self.btm_add_kvest_2.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.ptm_del_kvest_2 = QPushButton(Form4)
        self.ptm_del_kvest_2.setObjectName(u"ptm_del_kvest_2")
        self.ptm_del_kvest_2.setGeometry(QRect(1320, 840, 390, 40))
        self.ptm_del_kvest_2.setStyleSheet(u"color: rgb(188, 197, 163);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"background-color: rgba(21, 22, 17,200);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.textEdit = QTextEdit(Form4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(920, 500, 791, 331))
        self.textEdit.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 16pt \"Z003 [urw]\";\n"
"background-color: rgba(193, 204, 178, 195);\n"
"border-radius: 5px;\n"
"opacity: 0.5;")
        self.label_6 = QLabel(Form4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(880, 470, 431, 31))
        self.label_6.setStyleSheet(u"\n"
"color: rgb(14, 4, 5);\n"
"font: 500 italic 18pt \"Z003 [urw]\";\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Form4)

        QMetaObject.connectSlotsByName(Form4)
    # setupUi

    def retranslateUi(self, Form4):
        Form4.setWindowTitle(QCoreApplication.translate("Form4", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form4", u"<html><head/><body><p align=\"justify\"><br/></p></body></html>", None))
        self.ptm_del_kvest.setText(QCoreApplication.translate("Form4", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_kvest.setText(QCoreApplication.translate("Form4", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_dalee.setText(QCoreApplication.translate("Form4", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btm_nazad.setText(QCoreApplication.translate("Form4", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_4.setText(QCoreApplication.translate("Form4", u"<html><head/><body><p align=\"center\">\u0421\u0430\u043c\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043b\u043e\u043a\u0430\u0446\u0438\u0438! \u0420\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u044e \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043d\u0430\u0439\u0442\u0438 png, jpeg \u0444\u0430\u0439\u043b \u0441 \u0443\u0436\u0435 \u0433\u043e\u0442\u043e\u0432\u043e\u0439 \u0440\u0430\u0437\u043c\u0435\u0442\u043a\u043e\u0439 \u0434\u043b\u044f \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0439 \u0438\u0433\u0440\u044b. \u0420\u0430\u043d\u0435\u0435 \u0412\u044b \u0443\u0436\u0435 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u043b\u0438 \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0438 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0435\u0439. \u041a\u0430\u0436\u0434\u043e\u043c\u0443 \u0430\u0432\u0430\u043d\u0442\u044e\u0440\u0438\u0441\u0442\u0443 \u0441\u043e\u043f\u043e\u0441\u0442"
                        "\u0430\u0432\u044f\u0442\u0441\u044f \u043f\u043e \u0442\u043e\u043a\u0435\u043d\u0443 \u0441 \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u043c \u0446\u0432\u0435\u0442\u043e\u043c.<br/>\u0422\u0430\u043a \u0436\u0435 \u043d\u0430 \u044d\u0442\u043e\u043c \u044d\u0442\u0430\u043f\u0435, \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u0440\u0442\u0435\u0444\u0430\u043a\u0442\u044b, \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u044b \u0438 \u043f\u043e\u0434\u043e\u0431\u043d\u044b\u0435 \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u0435 \u0432\u0435\u0449\u0438.<br/>\u0412 \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u043c \u0412\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0430\u0442\u044c \u0442\u043e\u043a\u0435\u043d\u044b (\u0438\u0433\u0440\u043e\u043a\u043e\u0432) \u043d\u0430 \u0432\u044b\u0448\u0435\u0439 \u043a\u0430\u0440\u0442\u0435.</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form4", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432, \u0430\u0440\u0442\u0435\u0444\u0430\u043a\u0442\u043e\u0432 \u0438 \u0442\u0434", None))
        self.label_9.setText(QCoreApplication.translate("Form4", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043b\u043e\u043a\u0430\u0446\u0438\u0439", None))
        self.btm_add_kvest_2.setText(QCoreApplication.translate("Form4", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.ptm_del_kvest_2.setText(QCoreApplication.translate("Form4", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Form4", u"\u041e\u043a\u043e\u0448\u043a\u043e \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043e\u0432", None))
    # retranslateUi

