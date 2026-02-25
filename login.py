# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import files_rc
import imagens_rc

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import imagens_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(880, 672)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, -350, 471, 1371))
        self.pushButton_4.setStyleSheet(u"image: url(:/img_login/img/fundo.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, -50, 571, 731))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.botao_esquecisenha = QCommandLinkButton(self.widget)
        self.botao_esquecisenha.setObjectName(u"botao_esquecisenha")
        self.botao_esquecisenha.setGeometry(QRect(250, 640, 185, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.botao_esquecisenha.setFont(font)
        self.botao_esquecisenha.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #43A047;\n"
"    border: none;\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 6px 10px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(67, 160, 71, 0.12);\n"
"    color: #2E7D32;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(67, 160, 71, 0.25);\n"
"}\n"
"")
        self.horizontalLayoutWidget_4 = QWidget(self.widget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(50, 390, 361, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.campo_usuario = QLineEdit(self.horizontalLayoutWidget_4)
        self.campo_usuario.setObjectName(u"campo_usuario")
        font1 = QFont()
        font1.setFamilies([u"Franklin Gothic Heavy"])
        font1.setPointSize(15)
        self.campo_usuario.setFont(font1)
        self.campo_usuario.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: none;\n"
"border-bottom: 2px	 solid rgba(105,118, 132, 255);\n"
"color: black;\n"
"padding-bottom: 7px;\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.horizontalLayout_4.addWidget(self.campo_usuario)

        self.horizontalLayoutWidget_5 = QWidget(self.widget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(50, 470, 361, 80))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.campo_senha = QLineEdit(self.horizontalLayoutWidget_5)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setFont(font1)
        self.campo_senha.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: none;\n"
"border-bottom: 2px	 solid rgba(105,118, 132, 255);\n"
"color: black;\n"
"padding-bottom: 7px;\n"
"background-color: qlineargradient(spread:pad, x1:0.54, y1:1, x2:0.5, y2:0.04, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.campo_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.campo_senha)

        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(40, 240, 481, 83))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Black"])
        font2.setPointSize(40)
        font2.setBold(False)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(95, 166, 132);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalLayoutWidget_3 = QWidget(self.widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 560, 401, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.botao_login = QPushButton(self.horizontalLayoutWidget_3)
        self.botao_login.setObjectName(u"botao_login")
        self.botao_login.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(15)
        self.botao_login.setFont(font3)
        self.botao_login.setStyleSheet(u"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding-bottom: 3px;\n"
"border-radius: 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.botao_login)

        self.botao_cadastrar = QPushButton(self.horizontalLayoutWidget_3)
        self.botao_cadastrar.setObjectName(u"botao_cadastrar")
        self.botao_cadastrar.setMinimumSize(QSize(0, 40))
        self.botao_cadastrar.setFont(font3)
        self.botao_cadastrar.setStyleSheet(u"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding-bottom: 3px;\n"
"border-radius: 20px;\n"
"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.botao_cadastrar)

        self.horizontalLayoutWidget = QWidget(self.widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 150, 160, 91))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Black"])
        font4.setPointSize(45)
        font4.setBold(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(95, 166, 132);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 70, 121, 71))
        self.pushButton.setBaseSize(QSize(0, 0))
        self.pushButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(90, 90))
        QWidget.setTabOrder(self.campo_usuario, self.campo_senha)
        QWidget.setTabOrder(self.campo_senha, self.botao_login)
        QWidget.setTabOrder(self.botao_login, self.botao_cadastrar)
        QWidget.setTabOrder(self.botao_cadastrar, self.botao_esquecisenha)
        QWidget.setTabOrder(self.botao_esquecisenha, self.pushButton_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_4.setText("")
        self.botao_esquecisenha.setText(QCoreApplication.translate("Form", u"ESQUECI SENHA", None))
        self.campo_usuario.setPlaceholderText(QCoreApplication.translate("Form", u" Nome de Usu\u00e1rio", None))
        self.campo_senha.setPlaceholderText(QCoreApplication.translate("Form", u"CPF", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"SEJA BEM VINDO!", None))
        self.botao_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.botao_cadastrar.setText(QCoreApplication.translate("Form", u"CADASTRAR", None))
        self.label.setText(QCoreApplication.translate("Form", u"OL\u00c1,", None))
        self.pushButton.setText("")
    # retranslateUi

