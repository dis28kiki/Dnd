# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_create3.ui'
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
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_Form3(object):
    def setupUi(self, Form3):
        if not Form3.objectName():
            Form3.setObjectName("Form3")
        Form3.resize(1920, 1080)
        self.label = QLabel(Form3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 0, 1920, 1080))
        self.label.setStyleSheet(
            'border-image: url("/home/dis/\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b/sharag/sh3_2/\u043c\u0434\u043a 02/kod/dnd/picture/forest5.jpg") 0 0 0 0 stretch stretch'
        )
        self.label_2 = QLabel(Form3)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(100, 100, 1720, 840))
        self.label_2.setStyleSheet(
            "/*background-color: rgba(241, 243, 181, 55);*/\n"
            "background-color: rgba(99, 113, 54, 75);\n"
            "border-radius: 145px;"
        )
        self.label_3 = QLabel(Form3)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(200, 170, 661, 701))
        self.label_3.setStyleSheet(
            "\n"
            "color: rgb(14, 4, 5);\n"
            'font: 500 italic 18pt "Z003 [urw]";\n'
            "background-color: rgba(193, 204, 178, 115);\n"
            "border-radius: 205px;\n"
            "opacity: 0.5;"
        )
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.ptm_del_kvest = QPushButton(Form3)
        self.ptm_del_kvest.setObjectName("ptm_del_kvest")
        self.ptm_del_kvest.setGeometry(QRect(1360, 830, 390, 40))
        self.ptm_del_kvest.setStyleSheet(
            "color: rgb(188, 197, 163);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(21, 22, 17,200);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.btm_add_kvest = QPushButton(Form3)
        self.btm_add_kvest.setObjectName("btm_add_kvest")
        self.btm_add_kvest.setGeometry(QRect(950, 830, 390, 40))
        self.btm_add_kvest.setStyleSheet(
            "color: rgb(188, 197, 163);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(21, 22, 17,200);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.list_kvest = QListWidget(Form3)
        self.list_kvest.setObjectName("list_kvest")
        self.list_kvest.setGeometry(QRect(950, 210, 800, 281))
        self.list_kvest.setStyleSheet(
            "color: rgb(14, 4, 5);\n"
            'font: 500 italic 16pt "Z003 [urw]";\n'
            "background-color: rgba(193, 204, 178, 195);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.list_kvest.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.btm_dalee = QPushButton(Form3)
        self.btm_dalee.setObjectName("btm_dalee")
        self.btm_dalee.setGeometry(QRect(1690, 970, 191, 40))
        self.btm_dalee.setStyleSheet(
            "color: rgb(14, 4, 5);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(193, 204, 178, 175);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.btm_nazad = QPushButton(Form3)
        self.btm_nazad.setObjectName("btm_nazad")
        self.btm_nazad.setGeometry(QRect(20, 30, 191, 40))
        self.btm_nazad.setStyleSheet(
            "color: rgb(14, 4, 5);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(193, 204, 178, 175);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.label_4 = QLabel(Form3)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(310, 200, 461, 641))
        self.label_4.setStyleSheet(
            '\ncolor: rgb(14, 4, 5);\nfont: 500 italic 18pt "Z003 [urw]";\n'
        )
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.list_kvest_2 = QListWidget(Form3)
        self.list_kvest_2.setObjectName("list_kvest_2")
        self.list_kvest_2.setGeometry(QRect(950, 610, 800, 201))
        self.list_kvest_2.setStyleSheet(
            "\n"
            "color: rgb(14, 4, 5);\n"
            'font: 500 italic 16pt "Z003 [urw]";\n'
            "background-color: rgba(193, 204, 178, 195);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.list_kvest_2.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOn
        )
        self.label_5 = QLabel(Form3)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(950, 180, 291, 31))
        self.label_5.setStyleSheet(
            '\ncolor: rgb(14, 4, 5);\nfont: 500 italic 18pt "Z003 [urw]";\n'
        )
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(Form3)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(980, 580, 291, 31))
        self.label_9.setStyleSheet(
            '\ncolor: rgb(14, 4, 5);\nfont: 500 italic 18pt "Z003 [urw]";\n'
        )
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btm_add_kvest_2 = QPushButton(Form3)
        self.btm_add_kvest_2.setObjectName("btm_add_kvest_2")
        self.btm_add_kvest_2.setGeometry(QRect(950, 510, 390, 40))
        self.btm_add_kvest_2.setStyleSheet(
            "color: rgb(188, 197, 163);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(21, 22, 17,200);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )
        self.ptm_del_kvest_2 = QPushButton(Form3)
        self.ptm_del_kvest_2.setObjectName("ptm_del_kvest_2")
        self.ptm_del_kvest_2.setGeometry(QRect(1360, 510, 390, 40))
        self.ptm_del_kvest_2.setStyleSheet(
            "color: rgb(188, 197, 163);\n"
            'font: 500 italic 20pt "Z003 [urw]";\n'
            "background-color: rgba(21, 22, 17,200);\n"
            "border-radius: 5px;\n"
            "opacity: 0.5;"
        )

        self.retranslateUi(Form3)

        QMetaObject.connectSlotsByName(Form3)

    # setupUi

    def retranslateUi(self, Form3):
        Form3.setWindowTitle(QCoreApplication.translate("Form3", "Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(
            QCoreApplication.translate(
                "Form3",
                '<html><head/><body><p align="justify"><br/></p></body></html>',
                None,
            )
        )
        self.ptm_del_kvest.setText(
            QCoreApplication.translate(
                "Form3", "\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None
            )
        )
        self.btm_add_kvest.setText(
            QCoreApplication.translate(
                "Form3", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.btm_dalee.setText(
            QCoreApplication.translate("Form3", "\u0414\u0430\u043b\u0435\u0435", None)
        )
        self.btm_nazad.setText(
            QCoreApplication.translate("Form3", "\u041d\u0430\u0437\u0430\u0434", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "Form3",
                '<html><head/><body><p align="center">\u041e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u0443\u0436\u0435 \u0441\u043e\u0432\u0441\u0435\u043c \u043d\u0435\u043c\u043d\u043e\u0433\u043e. \u0421\u0435\u0439\u0447\u0430\u0441 \u0442\u0432\u043e\u044f \u0446\u0435\u043b\u044c \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0430\u043d\u043a\u0435\u0442\u044b \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0435\u0439 \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u0432 \u0444\u043e\u0440\u043c\u0430\u0442\u0435 PDF. \u042d\u0442\u043e \u0432\u0430\u0436\u043d\u044b\u0439 \u044d\u0442\u0430\u043f \u043f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u043a\u0438, \u0432\u0435\u0434\u044c \u0438\u043c\u0435\u043d\u043d\u043e \u044d\u0442\u0438 \u043b\u0438\u0441\u0442\u044b \u0441\u0442\u0430\u043d\u0443\u0442 \u043e\u0441\u043d\u043e\u0432\u043e\u0439 \u0434\u043b\u044f \u0432\u0441\u0435\u0433\u043e \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0433\u043e \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435'
                "\u0439\u0441\u0442\u0432\u0438\u044f. \u041f\u043e\u043c\u0438\u043c\u043e \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0445 \u0430\u043d\u043a\u0435\u0442 \u0438\u0433\u0440\u043e\u043a\u043e\u0432, \u0442\u044b \u0442\u0430\u043a\u0436\u0435 \u043c\u043e\u0436\u0435\u0448\u044c \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u043d\u043a\u0435\u0442\u044b \u043d\u0435\u0438\u0433\u0440\u043e\u0432\u044b\u0445 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0435\u0439 \u0441\u044e\u0436\u0435\u0442\u0430 \u0442\u0435\u0445, \u043a\u0442\u043e \u0432\u0441\u0442\u0440\u0435\u0442\u0438\u0442\u0441\u044f \u043d\u0430 \u043f\u0443\u0442\u0438 \u0443 \u043f\u0440\u043e\u0442\u0430\u0433\u043e\u043d\u0438\u0441\u0442\u043e\u0432. \u042d\u0442\u043e \u043c\u043e\u0433\u0443\u0442 \u0431\u044b\u0442\u044c \u043a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043e\u044e\u0437\u043d\u0438\u043a\u0438, \u0437\u0430\u0433\u0430\u0434\u043e\u0447\u043d\u044b\u0435 \u0442\u043e\u0440\u0433"
                "\u043e\u0432\u0446\u044b, \u0433\u0440\u043e\u0437\u043d\u044b\u0435 \u0430\u043d\u0442\u0430\u0433\u043e\u043d\u0438\u0441\u0442\u044b \u0438\u043b\u0438 \u043f\u0440\u043e\u0441\u0442\u043e \u043a\u043e\u043b\u043e\u0440\u0438\u0442\u043d\u044b\u0435 \u0436\u0438\u0442\u0435\u043b\u0438 \u043c\u0438\u0440\u0430. \u0417\u0430\u0433\u0440\u0443\u0436\u0430\u044f \u0438\u0445 \u0437\u0430\u0440\u0430\u043d\u0435\u0435, \u0442\u044b \u0441\u043e\u0437\u0434\u0430\u0451\u0448\u044c \u043f\u043e\u043b\u043d\u043e\u0446\u0435\u043d\u043d\u0443\u044e \u0431\u0430\u0437\u0443 \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0445 \u043b\u0438\u0446, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u0431\u0443\u0434\u0435\u0442 \u0433\u043e\u0442\u043e\u0432\u0430 \u043a \u043b\u044e\u0431\u043e\u043c\u0443 \u043f\u043e\u0432\u043e\u0440\u043e\u0442\u0443 \u0441\u043e\u0431\u044b\u0442\u0438\u0439. \u041f\u043e\u0434\u0433\u043e\u0442\u043e\u0432\u044c \u0432\u0441\u0435 \u043b\u0438\u0441\u0442\u044b, \u0430 \u043f"
                "\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u043e\u043c\u043e\u0436\u0435\u0442 \u0442\u0435\u0431\u0435 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u0445 \u0438 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0438\u0433\u0440\u0443 \u0431\u043e\u043b\u0435\u0435 \u043f\u043b\u0430\u0432\u043d\u043e\u0439 \u0438 \u0437\u0430\u0445\u0432\u0430\u0442\u044b\u0432\u0430\u044e\u0449\u0435\u0439.</p></body></html>",
                None,
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "Form3",
                "\u0421\u043f\u0438\u0441\u043e\u043a \u0438\u0433\u0440\u043e\u043a\u043e\u0432",
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "Form3", "\u0421\u043f\u0438\u0441\u043e\u043a \u041d\u041f\u0421", None
            )
        )
        self.btm_add_kvest_2.setText(
            QCoreApplication.translate(
                "Form3", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None
            )
        )
        self.ptm_del_kvest_2.setText(
            QCoreApplication.translate(
                "Form3", "\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None
            )
        )

    # retranslateUi
