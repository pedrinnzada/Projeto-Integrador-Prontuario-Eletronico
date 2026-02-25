# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'esqueci_senha.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import imagens_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(903, 677)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(550, -350, 481, 1371))
        self.pushButton_4.setStyleSheet(u"image: url(:/img_login/img/fundo.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -50, 571, 731))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_4 = QWidget(self.widget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(50, 410, 361, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.campo_reg_red = QLineEdit(self.horizontalLayoutWidget_4)
        self.campo_reg_red.setObjectName(u"campo_reg_red")
        font = QFont()
        font.setFamilies([u"Franklin Gothic Heavy"])
        font.setPointSize(15)
        self.campo_reg_red.setFont(font)
        self.campo_reg_red.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: none;\n"
"border-bottom: 2px	 solid rgba(105,118, 132, 255);\n"
"color: black;\n"
"padding-bottom: 7px;\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.horizontalLayout_4.addWidget(self.campo_reg_red)

        self.horizontalLayoutWidget_5 = QWidget(self.widget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(50, 470, 361, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.campo_cpf_red = QLineEdit(self.horizontalLayoutWidget_5)
        self.campo_cpf_red.setObjectName(u"campo_cpf_red")
        self.campo_cpf_red.setFont(font)
        self.campo_cpf_red.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: none;\n"
"border-bottom: 2px	 solid rgba(105,118, 132, 255);\n"
"color: black;\n"
"padding-bottom: 7px;\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.campo_cpf_red.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.campo_cpf_red)

        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(40, 240, 351, 73))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(40)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(95, 166, 132);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayoutWidget_3 = QWidget(self.widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 590, 401, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.botao_voltar = QPushButton(self.horizontalLayoutWidget_3)
        self.botao_voltar.setObjectName(u"botao_voltar")
        self.botao_voltar.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(15)
        self.botao_voltar.setFont(font2)
        self.botao_voltar.setStyleSheet(u"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding-bottom: 3px;\n"
"border-radius: 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.botao_voltar)

        self.botao_redefinir = QPushButton(self.horizontalLayoutWidget_3)
        self.botao_redefinir.setObjectName(u"botao_redefinir")
        self.botao_redefinir.setMinimumSize(QSize(0, 40))
        self.botao_redefinir.setFont(font2)
        self.botao_redefinir.setStyleSheet(u"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding-bottom: 3px;\n"
"border-radius: 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.botao_redefinir)

        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 150, 171, 91))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(45)
        font3.setBold(False)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(95, 166, 132);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayoutWidget_6 = QWidget(self.widget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(40, 312, 241, 73))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(95, 166, 132);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalLayoutWidget_7 = QWidget(self.widget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(50, 520, 361, 51))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.campo_conf_cpf = QLineEdit(self.horizontalLayoutWidget_7)
        self.campo_conf_cpf.setObjectName(u"campo_conf_cpf")
        self.campo_conf_cpf.setFont(font)
        self.campo_conf_cpf.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: none;\n"
"border-bottom: 2px	 solid rgba(105,118, 132, 255);\n"
"color: black;\n"
"padding-bottom: 7px;\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.campo_conf_cpf.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.campo_conf_cpf)

        QWidget.setTabOrder(self.campo_reg_red, self.campo_cpf_red)
        QWidget.setTabOrder(self.campo_cpf_red, self.campo_conf_cpf)
        QWidget.setTabOrder(self.campo_conf_cpf, self.botao_voltar)
        QWidget.setTabOrder(self.botao_voltar, self.botao_redefinir)
        QWidget.setTabOrder(self.botao_redefinir, self.pushButton_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_4.setText("")
        self.campo_reg_red.setPlaceholderText(QCoreApplication.translate("Form", u" RA", None))
        self.campo_cpf_red.setPlaceholderText(QCoreApplication.translate("Form", u"CPF", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ESQUECEU A", None))
        self.botao_voltar.setText(QCoreApplication.translate("Form", u"VOLTAR", None))
        self.botao_redefinir.setText(QCoreApplication.translate("Form", u"REDEFINIR", None))
        self.label.setText(QCoreApplication.translate("Form", u"OL\u00c1,", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"SENHA ?", None))
        self.campo_conf_cpf.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmar CPF", None))
    # retranslateUi

