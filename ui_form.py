# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGraphicsView,
    QGridLayout, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ImageLoading))
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(63, 54, 43);")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(980, 30, 911, 691))
        self.tabWidget.setStyleSheet(u"background-color: rgb(83, 76, 53);\n"
"border-color: rgb(44, 50, 28);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(15, 21, 881, 621))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graphicsView_2 = QGraphicsView(self.tab_2)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(20, 10, 881, 621))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graphicsView_3 = QGraphicsView(self.tab_3)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(10, 20, 881, 621))
        self.tabWidget.addTab(self.tab_3, "")
        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(1620, 840, 171, 151))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(980, 750, 401, 301))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(990, 760, 371, 271))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.formLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.formLayoutWidget)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.formLayoutWidget)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.radioButton_6)

        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(999, 769, 361, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_9 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout.addWidget(self.radioButton_9, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 3, 1, 1)

        self.radioButton_8 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 1, 4, 1, 1)

        self.radioButton_10 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.gridLayout.addWidget(self.radioButton_10, 2, 4, 1, 1)

        self.radioButton_7 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 1, 0, 1, 1)

        self.radioButton_11 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_11.setObjectName(u"radioButton_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.radioButton_11.sizePolicy().hasHeightForWidth())
        self.radioButton_11.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.radioButton_11, 0, 0, 1, 1)

        self.radioButton_12 = QRadioButton(self.gridLayoutWidget)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout.addWidget(self.radioButton_12, 0, 4, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u041a\u043d\u0438\u0433\u0430 \u043c\u0430\u0441\u0442\u0435\u0440\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u041a\u043d\u0438\u0433\u0430 \u0438\u0433\u0440\u043e\u043a\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0411\u0435\u0441\u0442\u0438\u0430\u0440\u0438\u0439", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_9.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_10.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_11.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_12.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi

