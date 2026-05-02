# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextEdit,
    QWidget)

class Ui_Form_main(object):
    def setupUi(self, Form_main):
        if not Form_main.objectName():
            Form_main.setObjectName(u"Form_main")
        Form_main.resize(1920, 1080)
        self.label = QLabel(Form_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(u"border-image: url(\"/home/dis/\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438/background/trav1.jpeg\") 0 0 0 0 stretch stretch")
        self.btm_nazad = QPushButton(Form_main)
        self.btm_nazad.setObjectName(u"btm_nazad")
        self.btm_nazad.setGeometry(QRect(1670, 10, 231, 40))
        self.btm_nazad.setStyleSheet(u"color: rgb(30, 23, 20);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,200);\n"
"")
        self.tabWidget_predmets = QTabWidget(Form_main)
        self.tabWidget_predmets.setObjectName(u"tabWidget_predmets")
        self.tabWidget_predmets.setGeometry(QRect(10, 10, 1031, 1021))
        self.tabWidget_predmets.setStyleSheet(u"font: 500 italic 20pt \"Z003 [urw]\";\n"
"color: rgb(197, 212, 141);\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgb(27, 30, 18);\n"
"")
        self.tabWidget_predmets.setTabPosition(QTabWidget.TabPosition.West)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.listWidget_musik = QListWidget(self.tab)
        self.listWidget_musik.setObjectName(u"listWidget_musik")
        self.listWidget_musik.setGeometry(QRect(20, 10, 951, 881))
        self.listWidget_musik.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_2 = QPushButton(self.tab)
        self.btm_nazad_2.setObjectName(u"btm_nazad_2")
        self.btm_nazad_2.setGeometry(QRect(20, 960, 461, 40))
        self.btm_nazad_2.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_3 = QPushButton(self.tab)
        self.btm_nazad_3.setObjectName(u"btm_nazad_3")
        self.btm_nazad_3.setGeometry(QRect(490, 960, 481, 40))
        self.btm_nazad_3.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_4 = QPushButton(self.tab)
        self.btm_nazad_4.setObjectName(u"btm_nazad_4")
        self.btm_nazad_4.setGeometry(QRect(20, 910, 261, 40))
        self.btm_nazad_4.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_5 = QPushButton(self.tab)
        self.btm_nazad_5.setObjectName(u"btm_nazad_5")
        self.btm_nazad_5.setGeometry(QRect(770, 910, 201, 40))
        self.btm_nazad_5.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_6 = QPushButton(self.tab)
        self.btm_nazad_6.setObjectName(u"btm_nazad_6")
        self.btm_nazad_6.setGeometry(QRect(490, 910, 271, 40))
        self.btm_nazad_6.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_nazad_7 = QPushButton(self.tab)
        self.btm_nazad_7.setObjectName(u"btm_nazad_7")
        self.btm_nazad_7.setGeometry(QRect(290, 910, 191, 40))
        self.btm_nazad_7.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.textEdit_sujet = QTextEdit(self.tab_5)
        self.textEdit_sujet.setObjectName(u"textEdit_sujet")
        self.textEdit_sujet.setGeometry(QRect(20, 20, 941, 921))
        self.textEdit_sujet.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_redact = QPushButton(self.tab_5)
        self.btm_redact.setObjectName(u"btm_redact")
        self.btm_redact.setGeometry(QRect(20, 960, 941, 40))
        self.btm_redact.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.textEdit_kvests = QTextEdit(self.tab_6)
        self.textEdit_kvests.setObjectName(u"textEdit_kvests")
        self.textEdit_kvests.setGeometry(QRect(20, 300, 941, 641))
        self.textEdit_kvests.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.listWidget_kvests = QListWidget(self.tab_6)
        self.listWidget_kvests.setObjectName(u"listWidget_kvests")
        self.listWidget_kvests.setGeometry(QRect(20, 60, 941, 231))
        self.listWidget_kvests.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_redact_2 = QPushButton(self.tab_6)
        self.btm_redact_2.setObjectName(u"btm_redact_2")
        self.btm_redact_2.setGeometry(QRect(20, 960, 941, 40))
        self.btm_redact_2.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add = QPushButton(self.tab_6)
        self.btm_add.setObjectName(u"btm_add")
        self.btm_add.setGeometry(QRect(20, 10, 461, 40))
        self.btm_add.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_del = QPushButton(self.tab_6)
        self.btm_del.setObjectName(u"btm_del")
        self.btm_del.setGeometry(QRect(490, 10, 471, 40))
        self.btm_del.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.listWidget_player = QListWidget(self.tab_7)
        self.listWidget_player.setObjectName(u"listWidget_player")
        self.listWidget_player.setGeometry(QRect(20, 70, 941, 211))
        self.listWidget_player.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.widget_playerpdf = QWidget(self.tab_7)
        self.widget_playerpdf.setObjectName(u"widget_playerpdf")
        self.widget_playerpdf.setGeometry(QRect(20, 300, 941, 691))
        self.btm_del_2 = QPushButton(self.tab_7)
        self.btm_del_2.setObjectName(u"btm_del_2")
        self.btm_del_2.setGeometry(QRect(490, 20, 471, 40))
        self.btm_del_2.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add_2 = QPushButton(self.tab_7)
        self.btm_add_2.setObjectName(u"btm_add_2")
        self.btm_add_2.setGeometry(QRect(20, 20, 461, 40))
        self.btm_add_2.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.listWidget_nps = QListWidget(self.tab_8)
        self.listWidget_nps.setObjectName(u"listWidget_nps")
        self.listWidget_nps.setGeometry(QRect(20, 60, 941, 221))
        self.listWidget_nps.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.widget_nps_pdf = QWidget(self.tab_8)
        self.widget_nps_pdf.setObjectName(u"widget_nps_pdf")
        self.widget_nps_pdf.setGeometry(QRect(20, 300, 941, 691))
        self.btm_del_3 = QPushButton(self.tab_8)
        self.btm_del_3.setObjectName(u"btm_del_3")
        self.btm_del_3.setGeometry(QRect(490, 10, 471, 40))
        self.btm_del_3.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add_3 = QPushButton(self.tab_8)
        self.btm_add_3.setObjectName(u"btm_add_3")
        self.btm_add_3.setGeometry(QRect(20, 10, 461, 40))
        self.btm_add_3.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.listWidget_predmet = QListWidget(self.tab_9)
        self.listWidget_predmet.setObjectName(u"listWidget_predmet")
        self.listWidget_predmet.setGeometry(QRect(20, 60, 941, 231))
        self.listWidget_predmet.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.textEdit = QTextEdit(self.tab_9)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 300, 941, 651))
        self.textEdit.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);")
        self.btm_del_4 = QPushButton(self.tab_9)
        self.btm_del_4.setObjectName(u"btm_del_4")
        self.btm_del_4.setGeometry(QRect(490, 10, 471, 40))
        self.btm_del_4.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add_4 = QPushButton(self.tab_9)
        self.btm_add_4.setObjectName(u"btm_add_4")
        self.btm_add_4.setGeometry(QRect(20, 10, 461, 40))
        self.btm_add_4.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_save_predmet = QPushButton(self.tab_9)
        self.btm_save_predmet.setObjectName(u"btm_save_predmet")
        self.btm_save_predmet.setGeometry(QRect(20, 960, 941, 40))
        self.btm_save_predmet.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.graphicsView_location = QGraphicsView(self.tab_10)
        self.graphicsView_location.setObjectName(u"graphicsView_location")
        self.graphicsView_location.setGeometry(QRect(20, 200, 941, 801))
        self.listWidget_lokation = QListWidget(self.tab_10)
        self.listWidget_lokation.setObjectName(u"listWidget_lokation")
        self.listWidget_lokation.setGeometry(QRect(20, 20, 941, 121))
        self.listWidget_lokation.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_del_5 = QPushButton(self.tab_10)
        self.btm_del_5.setObjectName(u"btm_del_5")
        self.btm_del_5.setGeometry(QRect(490, 150, 471, 40))
        self.btm_del_5.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add_5 = QPushButton(self.tab_10)
        self.btm_add_5.setObjectName(u"btm_add_5")
        self.btm_add_5.setGeometry(QRect(20, 150, 461, 40))
        self.btm_add_5.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.textEdit_zametki = QTextEdit(self.tab_11)
        self.textEdit_zametki.setObjectName(u"textEdit_zametki")
        self.textEdit_zametki.setGeometry(QRect(20, 300, 941, 661))
        self.textEdit_zametki.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);")
        self.listWidget_zametki = QListWidget(self.tab_11)
        self.listWidget_zametki.setObjectName(u"listWidget_zametki")
        self.listWidget_zametki.setGeometry(QRect(20, 70, 941, 221))
        self.listWidget_zametki.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_del_6 = QPushButton(self.tab_11)
        self.btm_del_6.setObjectName(u"btm_del_6")
        self.btm_del_6.setGeometry(QRect(490, 20, 471, 40))
        self.btm_del_6.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_add_6 = QPushButton(self.tab_11)
        self.btm_add_6.setObjectName(u"btm_add_6")
        self.btm_add_6.setGeometry(QRect(20, 20, 461, 40))
        self.btm_add_6.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.btm_del_7 = QPushButton(self.tab_11)
        self.btm_del_7.setObjectName(u"btm_del_7")
        self.btm_del_7.setGeometry(QRect(20, 970, 941, 40))
        self.btm_del_7.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 20pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,90);\n"
"")
        self.tabWidget_predmets.addTab(self.tab_11, "")
        self.pushButton = QPushButton(Form_main)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1680, 770, 181, 171))
        self.pushButton.setStyleSheet(u"color: rgb(30, 23, 20);\n"
"font: 500 italic 40pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgba(125, 121, 54,200);\n"
"")
        self.label_2 = QLabel(Form_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1060, 710, 571, 311))
        self.label_2.setStyleSheet(u"border-image: url(\"/home/dis/\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438/background/listttt.png\") 0 0 0 0 stretch stretch")
        self.gridLayoutWidget = QWidget(Form_main)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(1110, 730, 461, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.radioButton_14 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_14.setObjectName(u"radioButton_14")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_14.sizePolicy().hasHeightForWidth())
        self.radioButton_14.setSizePolicy(sizePolicy)
        self.radioButton_14.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_14, 2, 0, 1, 1)

        self.radioButton_15 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_15.setObjectName(u"radioButton_15")
        sizePolicy.setHeightForWidth(self.radioButton_15.sizePolicy().hasHeightForWidth())
        self.radioButton_15.setSizePolicy(sizePolicy)
        self.radioButton_15.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_15, 1, 3, 1, 1)

        self.radioButton_11 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_11.setObjectName(u"radioButton_11")
        sizePolicy.setHeightForWidth(self.radioButton_11.sizePolicy().hasHeightForWidth())
        self.radioButton_11.setSizePolicy(sizePolicy)
        self.radioButton_11.setBaseSize(QSize(10, 10))
        self.radioButton_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.radioButton_11.setAutoFillBackground(False)
        self.radioButton_11.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")
        self.radioButton_11.setIconSize(QSize(16, 16))
        self.radioButton_11.setChecked(True)

        self.gridLayout.addWidget(self.radioButton_11, 0, 0, 1, 1)

        self.radioButton_16 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_16.setObjectName(u"radioButton_16")
        sizePolicy.setHeightForWidth(self.radioButton_16.sizePolicy().hasHeightForWidth())
        self.radioButton_16.setSizePolicy(sizePolicy)
        self.radioButton_16.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_16, 2, 3, 1, 1)

        self.radioButton_13 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_13.setObjectName(u"radioButton_13")
        sizePolicy.setHeightForWidth(self.radioButton_13.sizePolicy().hasHeightForWidth())
        self.radioButton_13.setSizePolicy(sizePolicy)
        self.radioButton_13.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_13, 1, 0, 1, 1)

        self.radioButton_12 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_12.setObjectName(u"radioButton_12")
        sizePolicy.setHeightForWidth(self.radioButton_12.sizePolicy().hasHeightForWidth())
        self.radioButton_12.setSizePolicy(sizePolicy)
        self.radioButton_12.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_12, 0, 3, 1, 1)

        self.radioButton_17 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_17.setObjectName(u"radioButton_17")
        sizePolicy.setHeightForWidth(self.radioButton_17.sizePolicy().hasHeightForWidth())
        self.radioButton_17.setSizePolicy(sizePolicy)
        self.radioButton_17.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_17, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_18.setObjectName(u"radioButton_18")
        sizePolicy.setHeightForWidth(self.radioButton_18.sizePolicy().hasHeightForWidth())
        self.radioButton_18.setSizePolicy(sizePolicy)
        self.radioButton_18.setStyleSheet(u"color: rgb(197, 212, 141);\n"
"font: 500 italic 28pt \"Z003 [urw]\";\n"
"border-radius: 5px;\n"
"background-color: rgba(40, 32, 25, 135);\n"
"opacity: 0.5;\n"
"")

        self.gridLayout.addWidget(self.radioButton_18, 3, 3, 1, 1)

        self.widget_3 = QWidget(Form_main)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(1070, 60, 831, 621))
        self.widget_3.setStyleSheet(u"font: 500 italic 20pt \"Z003 [urw]\";\n"
"color: rgb(197, 212, 141);\n"
"border-radius: 5px;\n"
"opacity: 0.5;\n"
"background-color: rgb(27, 30, 18);\n"
"")
        self.label.raise_()
        self.tabWidget_predmets.raise_()
        self.btm_nazad.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.widget_3.raise_()

        self.retranslateUi(Form_main)

        self.tabWidget_predmets.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Form_main)
    # setupUi

    def retranslateUi(self, Form_main):
        Form_main.setWindowTitle(QCoreApplication.translate("Form_main", u"Form", None))
        self.label.setText("")
        self.btm_nazad.setText(QCoreApplication.translate("Form_main", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u043c\u0435\u043d\u044e", None))
        self.btm_nazad_2.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_nazad_3.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_nazad_4.setText(QCoreApplication.translate("Form_main", u"\u0412\u043e\u0441\u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0441\u0442\u0438", None))
        self.btm_nazad_5.setText(QCoreApplication.translate("Form_main", u"\u0421\u0442\u043e\u043f", None))
        self.btm_nazad_6.setText(QCoreApplication.translate("Form_main", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.btm_nazad_7.setText(QCoreApplication.translate("Form_main", u"\u041f\u0430\u0443\u0437\u0430", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab), QCoreApplication.translate("Form_main", u"\u041c\u0443\u0437\u044b\u043a\u0430", None))
        self.btm_redact.setText(QCoreApplication.translate("Form_main", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_5), QCoreApplication.translate("Form_main", u"\u0421\u044e\u0436\u0435\u0442", None))
        self.btm_redact_2.setText(QCoreApplication.translate("Form_main", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.btm_add.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_del.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_6), QCoreApplication.translate("Form_main", u"\u041a\u0432\u0435\u0441\u0442\u044b", None))
        self.btm_del_2.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_2.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_7), QCoreApplication.translate("Form_main", u"\u0418\u0433\u0440\u043e\u043a\u0438", None))
        self.btm_del_3.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_3.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_8), QCoreApplication.translate("Form_main", u"\u041d\u041f\u0421", None))
        self.btm_del_4.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_4.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_save_predmet.setText(QCoreApplication.translate("Form_main", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_9), QCoreApplication.translate("Form_main", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b", None))
        self.btm_del_5.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_5.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_10), QCoreApplication.translate("Form_main", u"\u041b\u043e\u043a\u0430\u0446\u0438\u0438", None))
        self.btm_del_6.setText(QCoreApplication.translate("Form_main", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.btm_add_6.setText(QCoreApplication.translate("Form_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btm_del_7.setText(QCoreApplication.translate("Form_main", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget_predmets.setTabText(self.tabWidget_predmets.indexOf(self.tab_11), QCoreApplication.translate("Form_main", u"\u0417\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form_main", u"100", None))
        self.label_2.setText("")
        self.radioButton_14.setText(QCoreApplication.translate("Form_main", u"D12", None))
        self.radioButton_15.setText(QCoreApplication.translate("Form_main", u"D6", None))
#if QT_CONFIG(whatsthis)
        self.radioButton_11.setWhatsThis(QCoreApplication.translate("Form_main", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButton_11.setText(QCoreApplication.translate("Form_main", u"D100", None))
        self.radioButton_16.setText(QCoreApplication.translate("Form_main", u"D4", None))
        self.radioButton_13.setText(QCoreApplication.translate("Form_main", u"D20", None))
        self.radioButton_12.setText(QCoreApplication.translate("Form_main", u"D8", None))
        self.radioButton_17.setText(QCoreApplication.translate("Form_main", u"D10", None))
        self.radioButton_18.setText(QCoreApplication.translate("Form_main", u"D2", None))
    # retranslateUi

