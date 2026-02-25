# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1380, 921)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush8)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.LinkVisited, brush9)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush10)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush8)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Link, brush8)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.LinkVisited, brush9)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush10)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush11)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, brush8)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, brush9)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush10)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush10)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.gridLayout_209 = QGridLayout(self.centralwidget)
        self.gridLayout_209.setObjectName(u"gridLayout_209")
        self.gridLayout_209.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        self.btn_toggle_menu.setFont(font1)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.pushButton_2 = QPushButton(self.frame_label_top_btns)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(49, 45))

        self.horizontalLayout_10.addWidget(self.pushButton_2, 0, Qt.AlignLeft)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        self.label_title_bar_top.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_title_bar_top.setFont(font2)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)

        self.btn_tema = QPushButton(self.frame_label_top_btns)
        self.btn_tema.setObjectName(u"btn_tema")
        self.btn_tema.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding: 10px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/16x16/cil-moon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tema.setIcon(icon1)

        self.horizontalLayout_10.addWidget(self.btn_tema, 0, Qt.AlignRight)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_minimize.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_maximize_restore.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_close.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.label_top_info_1.setFont(font3)
        self.label_top_info_1.setStyleSheet(u"color: transparent; ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.gridLayout_418 = QGridLayout(self.page_home)
        self.gridLayout_418.setObjectName(u"gridLayout_418")
        self.scrollArea_4 = QScrollArea(self.page_home)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1260, 781))
        self.gridLayout_420 = QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_420.setObjectName(u"gridLayout_420")
        self.label_usuario = QLabel(self.scrollAreaWidgetContents_6)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setStyleSheet(u"QLabel{\n"
"font: 600 10pt \"Segoe UI\";\n"
"padding: 20px 10px;\n"
"background-color: transparent;\n"
"\n"
"}")

        self.gridLayout_420.addWidget(self.label_usuario, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setMinimumSize(QSize(40, 0))
        self.frame_8.setStyleSheet(u"QLineEdit{\n"
"background-color: transparent;\n"
"border: none;\n"
"color: black;\n"
"font-size: 15px;\n"
"font-family: Arial;\n"
"selection-color: white;\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"background-color: rgb(216, 216, 216);\n"
"font-style: italic;\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(230, 230, 230);\n"
"border-radius: 10px;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #cfcfcf;\n"
"border-radius: 10px;\n"
"border: none;\n"
"}\n"
"\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"padding: 5px 10px")

        self.horizontalLayout.addWidget(self.lineEdit_7)

        self.botao_buscar_paciente = QPushButton(self.frame_8)
        self.botao_buscar_paciente.setObjectName(u"botao_buscar_paciente")
        self.botao_buscar_paciente.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"icons/16x16/cil-magnifying-glass.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_buscar_paciente.setIcon(icon5)
        self.botao_buscar_paciente.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.botao_buscar_paciente)

        self.botao_limpar_dashboard = QPushButton(self.frame_8)
        self.botao_limpar_dashboard.setObjectName(u"botao_limpar_dashboard")
        icon6 = QIcon()
        icon6.addFile(u"icons/16x16/cil-remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.botao_limpar_dashboard.setIcon(icon6)
        self.botao_limpar_dashboard.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.botao_limpar_dashboard)


        self.gridLayout_420.addWidget(self.frame_8, 0, 4, 1, 2)

        self.label_nome_paciente = QLabel(self.scrollAreaWidgetContents_6)
        self.label_nome_paciente.setObjectName(u"label_nome_paciente")
        self.label_nome_paciente.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"font: 600 10pt \"Segoe UI\";\n"
"\n"
"}")

        self.gridLayout_420.addWidget(self.label_nome_paciente, 0, 3, 1, 1, Qt.AlignRight)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_422 = QGridLayout(self.frame_7)
        self.gridLayout_422.setObjectName(u"gridLayout_422")
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QCalendarWidget{\n"
"background-color: #2b335f;\n"
"color: white;\n"
"border: 1px solid #76b9c6;\n"
"border-radius: 5px;\n"
"	}\n"
"	\n"
"	QCalendarWidget QWidget{\n"
"		alternate-background-color: #2b335f;\n"
"	}\n"
"\n"
"QCalendarWidget QWidget{\n"
"background-color: #2b335f;\n"
"color: white;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"background-color: #2b335f;\n"
"color: white;\n"
"icon-size: 20px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox{\n"
"background-color: #2b335f;\n"
"color: white;\n"
"selection-background-color: #9147eb;\n"
"selection-color: white;\n"
"border: none;\n"
"border-radius: 0px;\n"
"padding: 3px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover{\n"
"background-color: #3a4380;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-button{\n"
"width: 0px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"background-color: #2b335f;\n"
"color: white;\n"
"border: 1px solid #76b9c6;\n"
"}\n"
"\n"
"QCalendarWidget QTableView{\n"
"background-color: #2b335f;\n"
"alternate-background-"
                        "color: #2b335f;\n"
"gridline-color: #76b9c6;\n"
"selection-background-color: #9147eb;\n"
"selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:selected{\n"
"background-color: transparent;\n"
"border: 2px solid #9147eb;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:hover{\n"
"background-color: #3a4380;\n"
"border-radius: 12px;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enable{\n"
"color:white;\n"
"selection-background-color: transparent;\n"
"selection-color: white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"color: #76b9c6;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_preymonth{\n"
"qproperty-icon: file:///C:/Users/Japa/Downloads/projeto_integrador_enfermagem-main/icons/16x16/cil-arrow-left.png;\n"
"\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth{\n"
"qproperty-icon:file:///C:/Users/Japa/Downloads/projeto_integrador_enfermagem-main/icons/16x16/cil-arrow-rig"
                        "ht.png;\n"
"\n"
"width: 20px;\n"
"height: 20px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_421 = QGridLayout(self.frame_9)
        self.gridLayout_421.setObjectName(u"gridLayout_421")
        self.calendar_registros = QCalendarWidget(self.frame_9)
        self.calendar_registros.setObjectName(u"calendar_registros")
        self.calendar_registros.setStyleSheet(u"")

        self.gridLayout_421.addWidget(self.calendar_registros, 0, 0, 1, 1)


        self.gridLayout_422.addWidget(self.frame_9, 1, 2, 1, 3)

        self.cardsLayout = QGridLayout()
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.card_paciente = QFrame(self.frame_7)
        self.card_paciente.setObjectName(u"card_paciente")
        self.card_paciente.setStyleSheet(u"QFrame { background:#111827; border-radius:10px; color:white;}")
        self._2 = QVBoxLayout(self.card_paciente)
        self._2.setObjectName(u"_2")
        self.label = QLabel(self.card_paciente)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.label.setFont(font4)

        self._2.addWidget(self.label)

        self.lbl_nome = QLabel(self.card_paciente)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self._2.addWidget(self.lbl_nome)

        self.lbl_leito = QLabel(self.card_paciente)
        self.lbl_leito.setObjectName(u"lbl_leito")

        self._2.addWidget(self.lbl_leito)


        self.cardsLayout.addWidget(self.card_paciente, 0, 0, 1, 1)

        self.card_sinais = QFrame(self.frame_7)
        self.card_sinais.setObjectName(u"card_sinais")
        self.card_sinais.setStyleSheet(u"QFrame { background:#111827; border-radius:10px; color:white;}")
        self._3 = QVBoxLayout(self.card_sinais)
        self._3.setObjectName(u"_3")
        self.label_6 = QLabel(self.card_sinais)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self._3.addWidget(self.label_6)

        self.lbl_pa = QLabel(self.card_sinais)
        self.lbl_pa.setObjectName(u"lbl_pa")

        self._3.addWidget(self.lbl_pa)

        self.lbl_fc = QLabel(self.card_sinais)
        self.lbl_fc.setObjectName(u"lbl_fc")

        self._3.addWidget(self.lbl_fc)

        self.lbl_spo2 = QLabel(self.card_sinais)
        self.lbl_spo2.setObjectName(u"lbl_spo2")

        self._3.addWidget(self.lbl_spo2)


        self.cardsLayout.addWidget(self.card_sinais, 0, 1, 1, 1)

        self.card_risco = QFrame(self.frame_7)
        self.card_risco.setObjectName(u"card_risco")
        self.card_risco.setStyleSheet(u"QFrame { background:#111827; border-radius:10px; color:white; }")
        self._4 = QVBoxLayout(self.card_risco)
        self._4.setObjectName(u"_4")
        self.label_304 = QLabel(self.card_risco)
        self.label_304.setObjectName(u"label_304")
        self.label_304.setFont(font4)

        self._4.addWidget(self.label_304)

        self.lbl_estado_geral = QLabel(self.card_risco)
        self.lbl_estado_geral.setObjectName(u"lbl_estado_geral")

        self._4.addWidget(self.lbl_estado_geral)

        self.lbl_ndc = QLabel(self.card_risco)
        self.lbl_ndc.setObjectName(u"lbl_ndc")

        self._4.addWidget(self.lbl_ndc)


        self.cardsLayout.addWidget(self.card_risco, 0, 2, 1, 1)

        self.card_internacao = QFrame(self.frame_7)
        self.card_internacao.setObjectName(u"card_internacao")
        self._5 = QVBoxLayout(self.card_internacao)
        self._5.setObjectName(u"_5")
        self.label_307 = QLabel(self.card_internacao)
        self.label_307.setObjectName(u"label_307")
        self.label_307.setFont(font4)

        self._5.addWidget(self.label_307)

        self.lbl_dias = QLabel(self.card_internacao)
        self.lbl_dias.setObjectName(u"lbl_dias")

        self._5.addWidget(self.lbl_dias)

        self.lbl_status = QLabel(self.card_internacao)
        self.lbl_status.setObjectName(u"lbl_status")

        self._5.addWidget(self.lbl_status)


        self.cardsLayout.addWidget(self.card_internacao, 0, 3, 1, 1)


        self.gridLayout_422.addLayout(self.cardsLayout, 0, 0, 1, 5)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_423 = QGridLayout(self.frame_11)
        self.gridLayout_423.setObjectName(u"gridLayout_423")
        self.table_registros = QTableWidget(self.frame_11)
        if (self.table_registros.columnCount() < 7):
            self.table_registros.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_registros.setObjectName(u"table_registros")
        self.table_registros.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_423.addWidget(self.table_registros, 0, 0, 1, 1)


        self.gridLayout_422.addWidget(self.frame_11, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_422.addItem(self.verticalSpacer, 3, 4, 1, 1)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_419 = QGridLayout(self.frame_10)
        self.gridLayout_419.setObjectName(u"gridLayout_419")
        self.frame_grafico = QFrame(self.frame_10)
        self.frame_grafico.setObjectName(u"frame_grafico")
        self.gridLayout_424 = QGridLayout(self.frame_grafico)
        self.gridLayout_424.setObjectName(u"gridLayout_424")
        self.label_310 = QLabel(self.frame_grafico)
        self.label_310.setObjectName(u"label_310")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_310.setFont(font5)
        self.label_310.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_310.setAlignment(Qt.AlignCenter)

        self.gridLayout_424.addWidget(self.label_310, 0, 0, 1, 1)

        self.grafico_placeholder = QWidget(self.frame_grafico)
        self.grafico_placeholder.setObjectName(u"grafico_placeholder")
        self.grafico_placeholder.setStyleSheet(u"background-color: rgb(17, 24, 39);")

        self.gridLayout_424.addWidget(self.grafico_placeholder, 1, 0, 1, 1)


        self.gridLayout_419.addWidget(self.frame_grafico, 0, 0, 1, 1)


        self.gridLayout_422.addWidget(self.frame_10, 2, 0, 2, 4)


        self.gridLayout_420.addWidget(self.frame_7, 1, 0, 1, 6)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_418.addWidget(self.scrollArea_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_home)
        self.info_paciente = QWidget()
        self.info_paciente.setObjectName(u"info_paciente")
        self.gridLayout = QGridLayout(self.info_paciente)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea_2 = QScrollArea(self.info_paciente)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"border: none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1218, 618))
        self.verticalLayout_143 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(1200, 600))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_286 = QGridLayout(self.frame_6)
        self.gridLayout_286.setObjectName(u"gridLayout_286")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_286.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.botao_proximo = QPushButton(self.frame_6)
        self.botao_proximo.setObjectName(u"botao_proximo")
        self.botao_proximo.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_286.addWidget(self.botao_proximo, 1, 6, 1, 1)

        self.botao_finalizar = QPushButton(self.frame_6)
        self.botao_finalizar.setObjectName(u"botao_finalizar")
        self.botao_finalizar.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"padding: 7px 15px;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_286.addWidget(self.botao_finalizar, 1, 3, 1, 1)

        self.botao_anterior = QPushButton(self.frame_6)
        self.botao_anterior.setObjectName(u"botao_anterior")
        self.botao_anterior.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_286.addWidget(self.botao_anterior, 1, 5, 1, 1)

        self.botao_limpar = QPushButton(self.frame_6)
        self.botao_limpar.setObjectName(u"botao_limpar")
        self.botao_limpar.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_286.addWidget(self.botao_limpar, 1, 4, 1, 1)

        self.tabWidget_2 = QTabWidget(self.frame_6)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"/* ===== TAB WIDGET GERAL ===== */\n"
"QTabWidget::pane {\n"
"    border: 1px solid rgb(60, 130, 95);\n"
"    border-radius: 10px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"/* ===== BARRA DAS ABAS ===== */\n"
"QTabBar::tab {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: white;\n"
"    padding: 10px 18px;\n"
"    margin-right: 6px;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    min-width: 120px;\n"
"}\n"
"\n"
"/* ===== ABA SELECIONADA ===== */\n"
"QTabBar::tab:selected {\n"
"     /* verde ativo */\n"
"	background-color: rgb(39, 104, 78);\n"
"    color: white;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* ===== HOVER (verde escuro elegante) ===== */\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(45, 120, 90);\n"
"}\n"
"\n"
"/* ===== ABA N\u00c3O SELECIONADA ===== */\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px;\n"
"    opacity: 0.95;\n"
"}")
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.gridLayout_3 = QGridLayout(self.tab1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupTecidos_3 = QGroupBox(self.tab1)
        self.groupTecidos_3.setObjectName(u"groupTecidos_3")
        self.groupTecidos_3.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"\n"
"QRad"
                        "ioButton{\n"
"font-size: 13px;\n"
"}\n"
"")
        self.nome_completo = QLineEdit(self.groupTecidos_3)
        self.nome_completo.setObjectName(u"nome_completo")
        self.nome_completo.setGeometry(QRect(160, 30, 121, 31))
        font6 = QFont()
        self.nome_completo.setFont(font6)
        self.nome_completo.setStyleSheet(u"")
        self.data_de_nascimento = QDateEdit(self.groupTecidos_3)
        self.data_de_nascimento.setObjectName(u"data_de_nascimento")
        self.data_de_nascimento.setGeometry(QRect(160, 65, 111, 21))
        font7 = QFont()
        font7.setPointSize(8)
        self.data_de_nascimento.setFont(font7)
        self.data_de_nascimento.setStyleSheet(u"")
        self.idade = QLineEdit(self.groupTecidos_3)
        self.idade.setObjectName(u"idade")
        self.idade.setGeometry(QRect(162, 89, 41, 31))
        self.idade.setFont(font6)
        self.idade.setStyleSheet(u"")
        self.estado_civil = QGroupBox(self.groupTecidos_3)
        self.estado_civil.setObjectName(u"estado_civil")
        self.estado_civil.setGeometry(QRect(160, 150, 381, 50))
        self.estado_civil.setStyleSheet(u"")
        self.estado_civil.setAlignment(Qt.AlignCenter)
        self.gridLayout_178 = QGridLayout(self.estado_civil)
        self.gridLayout_178.setObjectName(u"gridLayout_178")
        self.opcao_solteiro_5 = QRadioButton(self.estado_civil)
        self.opcao_solteiro_5.setObjectName(u"opcao_solteiro_5")
        self.opcao_solteiro_5.setFont(font6)

        self.gridLayout_178.addWidget(self.opcao_solteiro_5, 0, 0, 1, 1)

        self.opcao_casado_5 = QRadioButton(self.estado_civil)
        self.opcao_casado_5.setObjectName(u"opcao_casado_5")
        self.opcao_casado_5.setFont(font6)

        self.gridLayout_178.addWidget(self.opcao_casado_5, 0, 1, 1, 1)

        self.opcao_divorciado_5 = QRadioButton(self.estado_civil)
        self.opcao_divorciado_5.setObjectName(u"opcao_divorciado_5")
        self.opcao_divorciado_5.setFont(font6)

        self.gridLayout_178.addWidget(self.opcao_divorciado_5, 0, 2, 1, 1)

        self.opcao_viuvo_5 = QRadioButton(self.estado_civil)
        self.opcao_viuvo_5.setObjectName(u"opcao_viuvo_5")
        self.opcao_viuvo_5.setFont(font6)

        self.gridLayout_178.addWidget(self.opcao_viuvo_5, 0, 3, 1, 1)

        self.sexo = QGroupBox(self.groupTecidos_3)
        self.sexo.setObjectName(u"sexo")
        self.sexo.setGeometry(QRect(160, 110, 251, 50))
        self.sexo.setStyleSheet(u"")
        self.sexo.setAlignment(Qt.AlignCenter)
        self.gridLayout_125 = QGridLayout(self.sexo)
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.opcao_masculino_5 = QRadioButton(self.sexo)
        self.opcao_masculino_5.setObjectName(u"opcao_masculino_5")
        self.opcao_masculino_5.setFont(font6)

        self.gridLayout_125.addWidget(self.opcao_masculino_5, 0, 0, 1, 1)

        self.campo_feminino_5 = QRadioButton(self.sexo)
        self.campo_feminino_5.setObjectName(u"campo_feminino_5")
        self.campo_feminino_5.setFont(font6)

        self.gridLayout_125.addWidget(self.campo_feminino_5, 0, 1, 1, 1)

        self.opcao_outro_5 = QRadioButton(self.sexo)
        self.opcao_outro_5.setObjectName(u"opcao_outro_5")
        self.opcao_outro_5.setFont(font6)

        self.gridLayout_125.addWidget(self.opcao_outro_5, 0, 2, 1, 1)

        self.data_de_emissao_consulta = QDateEdit(self.groupTecidos_3)
        self.data_de_emissao_consulta.setObjectName(u"data_de_emissao_consulta")
        self.data_de_emissao_consulta.setGeometry(QRect(160, 408, 111, 20))
        self.data_de_emissao_consulta.setFont(font7)
        self.data_de_emissao_consulta.setStyleSheet(u"")
        self.nome_1 = QLabel(self.groupTecidos_3)
        self.nome_1.setObjectName(u"nome_1")
        self.nome_1.setGeometry(QRect(13, 30, 102, 29))
        self.nome_1.setFont(font6)
        self.nome_1.setStyleSheet(u"")
        self.data_nascimento_1 = QLabel(self.groupTecidos_3)
        self.data_nascimento_1.setObjectName(u"data_nascimento_1")
        self.data_nascimento_1.setGeometry(QRect(12, 63, 127, 21))
        self.data_nascimento_1.setFont(font6)
        self.data_nascimento_1.setStyleSheet(u"")
        self.idade_1 = QLabel(self.groupTecidos_3)
        self.idade_1.setObjectName(u"idade_1")
        self.idade_1.setGeometry(QRect(13, 90, 49, 29))
        self.idade_1.setFont(font6)
        self.idade_1.setStyleSheet(u"")
        self.sexo_1 = QLabel(self.groupTecidos_3)
        self.sexo_1.setObjectName(u"sexo_1")
        self.sexo_1.setGeometry(QRect(13, 130, 69, 21))
        self.sexo_1.setFont(font6)
        self.sexo_1.setStyleSheet(u"")
        self.profissao = QLineEdit(self.groupTecidos_3)
        self.profissao.setObjectName(u"profissao")
        self.profissao.setGeometry(QRect(161, 209, 121, 31))
        self.estado_civil_1 = QLabel(self.groupTecidos_3)
        self.estado_civil_1.setObjectName(u"estado_civil_1")
        self.estado_civil_1.setGeometry(QRect(10, 160, 81, 31))
        self.estado_civil_1.setFont(font6)
        self.estado_civil_1.setStyleSheet(u"")
        self.profissao_5 = QLabel(self.groupTecidos_3)
        self.profissao_5.setObjectName(u"profissao_5")
        self.profissao_5.setGeometry(QRect(10, 213, 59, 21))
        self.profissao_5.setFont(font6)
        self.profissao_5.setStyleSheet(u"")
        self.endereco_5 = QLabel(self.groupTecidos_3)
        self.endereco_5.setObjectName(u"endereco_5")
        self.endereco_5.setGeometry(QRect(10, 250, 63, 21))
        self.endereco_5.setFont(font6)
        self.endereco_5.setStyleSheet(u"")
        self.endereco = QLineEdit(self.groupTecidos_3)
        self.endereco.setObjectName(u"endereco")
        self.endereco.setGeometry(QRect(161, 247, 121, 31))
        self.telefone_5 = QLabel(self.groupTecidos_3)
        self.telefone_5.setObjectName(u"telefone_5")
        self.telefone_5.setGeometry(QRect(10, 290, 56, 29))
        self.telefone_5.setFont(font6)
        self.telefone_5.setStyleSheet(u"")
        self.responsavel_5 = QLabel(self.groupTecidos_3)
        self.responsavel_5.setObjectName(u"responsavel_5")
        self.responsavel_5.setGeometry(QRect(10, 330, 81, 21))
        self.responsavel_5.setFont(font6)
        self.responsavel_5.setStyleSheet(u"")
        self.telefone = QLineEdit(self.groupTecidos_3)
        self.telefone.setObjectName(u"telefone")
        self.telefone.setGeometry(QRect(160, 285, 121, 31))
        self.responsavel = QLineEdit(self.groupTecidos_3)
        self.responsavel.setObjectName(u"responsavel")
        self.responsavel.setGeometry(QRect(160, 325, 121, 31))
        self.numero_p_5 = QLabel(self.groupTecidos_3)
        self.numero_p_5.setObjectName(u"numero_p_5")
        self.numero_p_5.setGeometry(QRect(10, 360, 141, 29))
        self.numero_p_5.setFont(font6)
        self.numero_p_5.setStyleSheet(u"")
        self.numero_de_prontuario = QLineEdit(self.groupTecidos_3)
        self.numero_de_prontuario.setObjectName(u"numero_de_prontuario")
        self.numero_de_prontuario.setGeometry(QRect(161, 363, 121, 31))
        self.numero_de_prontuario.setFont(font6)
        self.numero_de_prontuario.setStyleSheet(u"color: black;\n"
"")
        self.data_co_5 = QLabel(self.groupTecidos_3)
        self.data_co_5.setObjectName(u"data_co_5")
        self.data_co_5.setGeometry(QRect(10, 408, 108, 19))
        self.data_co_5.setFont(font6)
        self.data_co_5.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.groupTecidos_3, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.gridLayout_148 = QGridLayout(self.tab2)
        self.gridLayout_148.setObjectName(u"gridLayout_148")
        self.groupLesoes_8 = QGroupBox(self.tab2)
        self.groupLesoes_8.setObjectName(u"groupLesoes_8")
        self.groupLesoes_8.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"      border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.label_199 = QLabel(self.groupLesoes_8)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(20, 50, 46, 17))
        self.label_199.setFont(font6)
        self.label_200 = QLabel(self.groupLesoes_8)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(18, 90, 222, 17))
        self.label_200.setFont(font6)
        self.label_201 = QLabel(self.groupLesoes_8)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(20, 130, 122, 17))
        self.label_201.setFont(font6)
        self.label_202 = QLabel(self.groupLesoes_8)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(20, 170, 34, 17))
        self.label_202.setFont(font6)
        self.label_203 = QLabel(self.groupLesoes_8)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(20, 202, 143, 17))
        self.label_203.setFont(font6)
        self.label_204 = QLabel(self.groupLesoes_8)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(20, 244, 73, 17))
        self.label_204.setFont(font6)
        self.label_205 = QLabel(self.groupLesoes_8)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(20, 286, 65, 17))
        self.label_205.setFont(font6)
        self.label_206 = QLabel(self.groupLesoes_8)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(20, 320, 131, 31))
        self.label_206.setFont(font6)
        self.label_207 = QLabel(self.groupLesoes_8)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setGeometry(QRect(20, 360, 151, 31))
        self.label_207.setFont(font6)
        self.label_208 = QLabel(self.groupLesoes_8)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setGeometry(QRect(20, 390, 131, 31))
        self.label_208.setFont(font6)
        self.avaliacao_de_dor = QComboBox(self.groupLesoes_8)
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.addItem("")
        self.avaliacao_de_dor.setObjectName(u"avaliacao_de_dor")
        self.avaliacao_de_dor.setGeometry(QRect(260, 400, 51, 21))
        self.label_209 = QLabel(self.groupLesoes_8)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setGeometry(QRect(20, 440, 75, 17))
        self.label_209.setFont(font6)
        self.tipo_de_dor = QGroupBox(self.groupLesoes_8)
        self.tipo_de_dor.setObjectName(u"tipo_de_dor")
        self.tipo_de_dor.setGeometry(QRect(256, 420, 453, 50))
        self.gridLayout_173 = QGridLayout(self.tipo_de_dor)
        self.gridLayout_173.setObjectName(u"gridLayout_173")
        self.radio_aguda_6 = QRadioButton(self.tipo_de_dor)
        self.radio_aguda_6.setObjectName(u"radio_aguda_6")
        self.radio_aguda_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_aguda_6, 0, 0, 1, 1)

        self.radio_cronica_6 = QRadioButton(self.tipo_de_dor)
        self.radio_cronica_6.setObjectName(u"radio_cronica_6")
        self.radio_cronica_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_cronica_6, 0, 1, 1, 1)

        self.radio_queimacao_6 = QRadioButton(self.tipo_de_dor)
        self.radio_queimacao_6.setObjectName(u"radio_queimacao_6")
        self.radio_queimacao_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_queimacao_6, 0, 2, 1, 1)

        self.radio_pontada_6 = QRadioButton(self.tipo_de_dor)
        self.radio_pontada_6.setObjectName(u"radio_pontada_6")
        self.radio_pontada_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_pontada_6, 0, 3, 1, 1)

        self.radio_pressao_6 = QRadioButton(self.tipo_de_dor)
        self.radio_pressao_6.setObjectName(u"radio_pressao_6")
        self.radio_pressao_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_pressao_6, 0, 4, 1, 1)

        self.radio_colica_6 = QRadioButton(self.tipo_de_dor)
        self.radio_colica_6.setObjectName(u"radio_colica_6")
        self.radio_colica_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_colica_6, 0, 5, 1, 1)

        self.radio_continua_6 = QRadioButton(self.tipo_de_dor)
        self.radio_continua_6.setObjectName(u"radio_continua_6")
        self.radio_continua_6.setFont(font6)

        self.gridLayout_173.addWidget(self.radio_continua_6, 0, 6, 1, 1)

        self.label_210 = QLabel(self.groupLesoes_8)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setGeometry(QRect(20, 480, 119, 31))
        self.label_210.setFont(font6)
        self.data = QDateEdit(self.groupLesoes_8)
        self.data.setObjectName(u"data")
        self.data.setGeometry(QRect(263, 160, 91, 31))
        self.inicio_dos_sintomas = QGroupBox(self.groupLesoes_8)
        self.inicio_dos_sintomas.setObjectName(u"inicio_dos_sintomas")
        self.inicio_dos_sintomas.setGeometry(QRect(260, 106, 152, 50))
        self.inicio_dos_sintomas.setStyleSheet(u"")
        self.gridLayout_152 = QGridLayout(self.inicio_dos_sintomas)
        self.gridLayout_152.setObjectName(u"gridLayout_152")
        self.radio_subito_6 = QRadioButton(self.inicio_dos_sintomas)
        self.radio_subito_6.setObjectName(u"radio_subito_6")
        self.radio_subito_6.setFont(font6)

        self.gridLayout_152.addWidget(self.radio_subito_6, 0, 0, 1, 1)

        self.radio_progressivo_6 = QRadioButton(self.inicio_dos_sintomas)
        self.radio_progressivo_6.setObjectName(u"radio_progressivo_6")
        self.radio_progressivo_6.setFont(font6)

        self.gridLayout_152.addWidget(self.radio_progressivo_6, 0, 1, 1, 1)

        self.motivo_da_internacao = QLineEdit(self.groupLesoes_8)
        self.motivo_da_internacao.setObjectName(u"motivo_da_internacao")
        self.motivo_da_internacao.setGeometry(QRect(262, 40, 121, 31))
        self.como_ele_chegou = QLineEdit(self.groupLesoes_8)
        self.como_ele_chegou.setObjectName(u"como_ele_chegou")
        self.como_ele_chegou.setGeometry(QRect(262, 80, 121, 31))
        self.duracao_dos_sintomas = QLineEdit(self.groupLesoes_8)
        self.duracao_dos_sintomas.setObjectName(u"duracao_dos_sintomas")
        self.duracao_dos_sintomas.setGeometry(QRect(260, 200, 121, 31))
        self.localizacao = QLineEdit(self.groupLesoes_8)
        self.localizacao.setObjectName(u"localizacao")
        self.localizacao.setGeometry(QRect(260, 240, 121, 31))
        self.irradiacao = QLineEdit(self.groupLesoes_8)
        self.irradiacao.setObjectName(u"irradiacao")
        self.irradiacao.setGeometry(QRect(260, 280, 121, 31))
        self.sintomas_associados = QLineEdit(self.groupLesoes_8)
        self.sintomas_associados.setObjectName(u"sintomas_associados")
        self.sintomas_associados.setGeometry(QRect(260, 320, 121, 31))
        self.tratamentos_ja_realizados = QLineEdit(self.groupLesoes_8)
        self.tratamentos_ja_realizados.setObjectName(u"tratamentos_ja_realizados")
        self.tratamentos_ja_realizados.setGeometry(QRect(260, 360, 121, 31))
        self.localizacao_da_dor = QLineEdit(self.groupLesoes_8)
        self.localizacao_da_dor.setObjectName(u"localizacao_da_dor")
        self.localizacao_da_dor.setGeometry(QRect(258, 480, 121, 31))

        self.gridLayout_148.addWidget(self.groupLesoes_8, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.gridLayout_62 = QGridLayout(self.tab3)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.groupLesoes_9 = QGroupBox(self.tab3)
        self.groupLesoes_9.setObjectName(u"groupLesoes_9")
        self.groupLesoes_9.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"         border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.mmhg_2 = QLabel(self.groupLesoes_9)
        self.mmhg_2.setObjectName(u"mmhg_2")
        self.mmhg_2.setGeometry(QRect(350, 40, 41, 17))
        self.mmhg_2.setFont(font6)
        self.bpm_2 = QLabel(self.groupLesoes_9)
        self.bpm_2.setObjectName(u"bpm_2")
        self.bpm_2.setGeometry(QRect(350, 80, 28, 17))
        self.bpm_2.setFont(font6)
        self.ritmo = QGroupBox(self.groupLesoes_9)
        self.ritmo.setObjectName(u"ritmo")
        self.ritmo.setGeometry(QRect(220, 270, 331, 71))
        font8 = QFont()
        font8.setBold(True)
        self.ritmo.setFont(font8)
        self.ritmo.setStyleSheet(u"")
        self.gridLayout_156 = QGridLayout(self.ritmo)
        self.gridLayout_156.setObjectName(u"gridLayout_156")
        self.arritmico_2 = QRadioButton(self.ritmo)
        self.arritmico_2.setObjectName(u"arritmico_2")
        self.arritmico_2.setFont(font6)

        self.gridLayout_156.addWidget(self.arritmico_2, 0, 0, 1, 1)

        self.filiforme_2 = QRadioButton(self.ritmo)
        self.filiforme_2.setObjectName(u"filiforme_2")
        self.filiforme_2.setFont(font6)

        self.gridLayout_156.addWidget(self.filiforme_2, 4, 0, 1, 1)

        self.eucardiaco_2 = QRadioButton(self.ritmo)
        self.eucardiaco_2.setObjectName(u"eucardiaco_2")
        self.eucardiaco_2.setFont(font6)

        self.gridLayout_156.addWidget(self.eucardiaco_2, 0, 2, 1, 1)

        self.taquicardico_2 = QRadioButton(self.ritmo)
        self.taquicardico_2.setObjectName(u"taquicardico_2")
        self.taquicardico_2.setFont(font6)

        self.gridLayout_156.addWidget(self.taquicardico_2, 4, 2, 1, 1)

        self.cheio_2 = QRadioButton(self.ritmo)
        self.cheio_2.setObjectName(u"cheio_2")
        self.cheio_2.setFont(font6)

        self.gridLayout_156.addWidget(self.cheio_2, 0, 3, 1, 1)

        self.bradicardio_2 = QRadioButton(self.ritmo)
        self.bradicardio_2.setObjectName(u"bradicardio_2")
        self.bradicardio_2.setFont(font6)

        self.gridLayout_156.addWidget(self.bradicardio_2, 4, 3, 1, 1)

        self.irpm_2 = QLabel(self.groupLesoes_9)
        self.irpm_2.setObjectName(u"irpm_2")
        self.irpm_2.setGeometry(QRect(350, 110, 27, 17))
        self.irpm_2.setFont(font6)
        self.tipo = QGroupBox(self.groupLesoes_9)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(220, 370, 313, 51))
        self.tipo.setStyleSheet(u"")
        self.gridLayout_157 = QGridLayout(self.tipo)
        self.gridLayout_157.setObjectName(u"gridLayout_157")
        self.dispnetico_2 = QRadioButton(self.tipo)
        self.dispnetico_2.setObjectName(u"dispnetico_2")
        self.dispnetico_2.setFont(font6)

        self.gridLayout_157.addWidget(self.dispnetico_2, 0, 1, 1, 1)

        self.eupnetico_2 = QRadioButton(self.tipo)
        self.eupnetico_2.setObjectName(u"eupnetico_2")
        self.eupnetico_2.setFont(font6)

        self.gridLayout_157.addWidget(self.eupnetico_2, 0, 0, 1, 1)

        self.taquipneico_2 = QRadioButton(self.tipo)
        self.taquipneico_2.setObjectName(u"taquipneico_2")
        self.taquipneico_2.setFont(font6)

        self.gridLayout_157.addWidget(self.taquipneico_2, 0, 2, 1, 1)

        self.classificacao_pressao = QGroupBox(self.groupLesoes_9)
        self.classificacao_pressao.setObjectName(u"classificacao_pressao")
        self.classificacao_pressao.setGeometry(QRect(220, 230, 171, 51))
        self.classificacao_pressao.setStyleSheet(u"")
        self.gridLayout_158 = QGridLayout(self.classificacao_pressao)
        self.gridLayout_158.setObjectName(u"gridLayout_158")
        self.hipotenso_2 = QRadioButton(self.classificacao_pressao)
        self.hipotenso_2.setObjectName(u"hipotenso_2")
        self.hipotenso_2.setFont(font6)

        self.gridLayout_158.addWidget(self.hipotenso_2, 0, 0, 1, 1)

        self.hipertenso_2 = QRadioButton(self.classificacao_pressao)
        self.hipertenso_2.setObjectName(u"hipertenso_2")
        self.hipertenso_2.setFont(font6)

        self.gridLayout_158.addWidget(self.hipertenso_2, 0, 1, 1, 1)

        self.celsius_2 = QLabel(self.groupLesoes_9)
        self.celsius_2.setObjectName(u"celsius_2")
        self.celsius_2.setGeometry(QRect(350, 150, 16, 17))
        self.celsius_2.setFont(font6)
        self.classificacao_temperatura = QGroupBox(self.groupLesoes_9)
        self.classificacao_temperatura.setObjectName(u"classificacao_temperatura")
        self.classificacao_temperatura.setGeometry(QRect(220, 330, 234, 51))
        self.classificacao_temperatura.setStyleSheet(u"")
        self.gridLayout_159 = QGridLayout(self.classificacao_temperatura)
        self.gridLayout_159.setObjectName(u"gridLayout_159")
        self.subfebril_2 = QRadioButton(self.classificacao_temperatura)
        self.subfebril_2.setObjectName(u"subfebril_2")
        self.subfebril_2.setFont(font6)

        self.gridLayout_159.addWidget(self.subfebril_2, 0, 1, 1, 1)

        self.febril_2 = QRadioButton(self.classificacao_temperatura)
        self.febril_2.setObjectName(u"febril_2")
        self.febril_2.setFont(font6)

        self.gridLayout_159.addWidget(self.febril_2, 0, 0, 1, 1)

        self.afebril_2 = QRadioButton(self.classificacao_temperatura)
        self.afebril_2.setObjectName(u"afebril_2")
        self.afebril_2.setFont(font6)

        self.gridLayout_159.addWidget(self.afebril_2, 0, 2, 1, 1)

        self.porcentagem_2 = QLabel(self.groupLesoes_9)
        self.porcentagem_2.setObjectName(u"porcentagem_2")
        self.porcentagem_2.setGeometry(QRect(350, 180, 16, 17))
        self.porcentagem_2.setFont(font6)
        self.escala_da_dor = QComboBox(self.groupLesoes_9)
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.addItem("")
        self.escala_da_dor.setObjectName(u"escala_da_dor")
        self.escala_da_dor.setGeometry(QRect(220, 213, 41, 21))
        font9 = QFont()
        font9.setPointSize(10)
        self.escala_da_dor.setFont(font9)
        self.escala_da_dor.setStyleSheet(u"")
        self.pressao_arterial = QLineEdit(self.groupLesoes_9)
        self.pressao_arterial.setObjectName(u"pressao_arterial")
        self.pressao_arterial.setGeometry(QRect(220, 35, 121, 31))
        self.frequencia_cardiaca_pulso = QLineEdit(self.groupLesoes_9)
        self.frequencia_cardiaca_pulso.setObjectName(u"frequencia_cardiaca_pulso")
        self.frequencia_cardiaca_pulso.setGeometry(QRect(220, 70, 121, 31))
        self.frequencia_respiratoria = QLineEdit(self.groupLesoes_9)
        self.frequencia_respiratoria.setObjectName(u"frequencia_respiratoria")
        self.frequencia_respiratoria.setGeometry(QRect(220, 104, 121, 31))
        self.pressao_art_2 = QLabel(self.groupLesoes_9)
        self.pressao_art_2.setObjectName(u"pressao_art_2")
        self.pressao_art_2.setGeometry(QRect(20, 36, 97, 29))
        self.pressao_art_2.setFont(font6)
        self.frequencia_cardiaca_2 = QLabel(self.groupLesoes_9)
        self.frequencia_cardiaca_2.setObjectName(u"frequencia_cardiaca_2")
        self.frequencia_cardiaca_2.setGeometry(QRect(20, 70, 129, 29))
        self.frequencia_cardiaca_2.setFont(font6)
        self.frequencia_respiratoria_2 = QLabel(self.groupLesoes_9)
        self.frequencia_respiratoria_2.setObjectName(u"frequencia_respiratoria_2")
        self.frequencia_respiratoria_2.setGeometry(QRect(19, 100, 149, 40))
        self.frequencia_respiratoria_2.setFont(font6)
        self.temperatura = QLineEdit(self.groupLesoes_9)
        self.temperatura.setObjectName(u"temperatura")
        self.temperatura.setGeometry(QRect(220, 138, 121, 31))
        self.temperatura_2 = QLabel(self.groupLesoes_9)
        self.temperatura_2.setObjectName(u"temperatura_2")
        self.temperatura_2.setGeometry(QRect(18, 140, 89, 29))
        self.temperatura_2.setFont(font6)
        self.saturacao_de_O2 = QLineEdit(self.groupLesoes_9)
        self.saturacao_de_O2.setObjectName(u"saturacao_de_O2")
        self.saturacao_de_O2.setGeometry(QRect(220, 174, 121, 31))
        self.saturacao_o2_2 = QLabel(self.groupLesoes_9)
        self.saturacao_o2_2.setObjectName(u"saturacao_o2_2")
        self.saturacao_o2_2.setGeometry(QRect(20, 170, 123, 29))
        self.saturacao_o2_2.setFont(font6)
        self.escala_dor_2 = QLabel(self.groupLesoes_9)
        self.escala_dor_2.setObjectName(u"escala_dor_2")
        self.escala_dor_2.setGeometry(QRect(20, 210, 102, 29))
        self.escala_dor_2.setFont(font6)
        self.classificacao_pressao_2 = QLabel(self.groupLesoes_9)
        self.classificacao_pressao_2.setObjectName(u"classificacao_pressao_2")
        self.classificacao_pressao_2.setGeometry(QRect(20, 240, 149, 39))
        self.classificacao_pressao_2.setFont(font6)
        self.ritmico_2 = QLabel(self.groupLesoes_9)
        self.ritmico_2.setObjectName(u"ritmico_2")
        self.ritmico_2.setGeometry(QRect(20, 300, 53, 21))
        self.ritmico_2.setFont(font6)
        self.clas_temperatura_2 = QLabel(self.groupLesoes_9)
        self.clas_temperatura_2.setObjectName(u"clas_temperatura_2")
        self.clas_temperatura_2.setGeometry(QRect(17, 340, 181, 39))
        self.clas_temperatura_2.setFont(font6)
        self.tipo_frequencia_r_2 = QLabel(self.groupLesoes_9)
        self.tipo_frequencia_r_2.setObjectName(u"tipo_frequencia_r_2")
        self.tipo_frequencia_r_2.setGeometry(QRect(20, 380, 199, 39))
        self.tipo_frequencia_r_2.setFont(font6)

        self.gridLayout_62.addWidget(self.groupLesoes_9, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_327 = QGridLayout(self.tab_2)
        self.gridLayout_327.setObjectName(u"gridLayout_327")
        self.groupLesoes_10 = QGroupBox(self.tab_2)
        self.groupLesoes_10.setObjectName(u"groupLesoes_10")
        self.groupLesoes_10.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"      border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.nivel_de_consciencia = QGroupBox(self.groupLesoes_10)
        self.nivel_de_consciencia.setObjectName(u"nivel_de_consciencia")
        self.nivel_de_consciencia.setGeometry(QRect(180, 25, 441, 51))
        self.nivel_de_consciencia.setStyleSheet(u"")
        self.gridLayout_225 = QGridLayout(self.nivel_de_consciencia)
        self.gridLayout_225.setObjectName(u"gridLayout_225")
        self.radio_alerta_2 = QRadioButton(self.nivel_de_consciencia)
        self.radio_alerta_2.setObjectName(u"radio_alerta_2")
        self.radio_alerta_2.setFont(font6)

        self.gridLayout_225.addWidget(self.radio_alerta_2, 0, 0, 1, 1)

        self.radio_semi_consciente_2 = QRadioButton(self.nivel_de_consciencia)
        self.radio_semi_consciente_2.setObjectName(u"radio_semi_consciente_2")
        self.radio_semi_consciente_2.setFont(font6)

        self.gridLayout_225.addWidget(self.radio_semi_consciente_2, 0, 1, 1, 1)

        self.radio_confuso_2 = QRadioButton(self.nivel_de_consciencia)
        self.radio_confuso_2.setObjectName(u"radio_confuso_2")
        self.radio_confuso_2.setFont(font6)

        self.gridLayout_225.addWidget(self.radio_confuso_2, 0, 2, 1, 1)

        self.radio_sonolento_2 = QRadioButton(self.nivel_de_consciencia)
        self.radio_sonolento_2.setObjectName(u"radio_sonolento_2")
        self.radio_sonolento_2.setFont(font6)

        self.gridLayout_225.addWidget(self.radio_sonolento_2, 0, 3, 1, 1)

        self.radio_inconsciente_2 = QRadioButton(self.nivel_de_consciencia)
        self.radio_inconsciente_2.setObjectName(u"radio_inconsciente_2")
        self.radio_inconsciente_2.setFont(font6)

        self.gridLayout_225.addWidget(self.radio_inconsciente_2, 0, 4, 1, 1)

        self.estado_geral = QGroupBox(self.groupLesoes_10)
        self.estado_geral.setObjectName(u"estado_geral")
        self.estado_geral.setGeometry(QRect(180, 70, 231, 51))
        self.estado_geral.setStyleSheet(u"")
        self.gridLayout_226 = QGridLayout(self.estado_geral)
        self.gridLayout_226.setObjectName(u"gridLayout_226")
        self.radio_bom_2 = QRadioButton(self.estado_geral)
        self.radio_bom_2.setObjectName(u"radio_bom_2")
        self.radio_bom_2.setFont(font6)

        self.gridLayout_226.addWidget(self.radio_bom_2, 0, 0, 1, 1)

        self.radio_regular_2 = QRadioButton(self.estado_geral)
        self.radio_regular_2.setObjectName(u"radio_regular_2")
        self.radio_regular_2.setFont(font6)

        self.gridLayout_226.addWidget(self.radio_regular_2, 0, 1, 1, 1)

        self.radio_ruim_2 = QRadioButton(self.estado_geral)
        self.radio_ruim_2.setObjectName(u"radio_ruim_2")
        self.radio_ruim_2.setFont(font6)

        self.gridLayout_226.addWidget(self.radio_ruim_2, 0, 2, 1, 1)

        self.hidratacao = QGroupBox(self.groupLesoes_10)
        self.hidratacao.setObjectName(u"hidratacao")
        self.hidratacao.setGeometry(QRect(180, 110, 281, 46))
        self.hidratacao.setStyleSheet(u"")
        self.gridLayout_227 = QGridLayout(self.hidratacao)
        self.gridLayout_227.setObjectName(u"gridLayout_227")
        self.radio_hidratado_2 = QRadioButton(self.hidratacao)
        self.radio_hidratado_2.setObjectName(u"radio_hidratado_2")
        self.radio_hidratado_2.setFont(font6)

        self.gridLayout_227.addWidget(self.radio_hidratado_2, 0, 0, 1, 1)

        self.radio_desidratado_2 = QRadioButton(self.hidratacao)
        self.radio_desidratado_2.setObjectName(u"radio_desidratado_2")
        self.radio_desidratado_2.setFont(font6)

        self.gridLayout_227.addWidget(self.radio_desidratado_2, 0, 2, 1, 1)

        self.nutricao = QGroupBox(self.groupLesoes_10)
        self.nutricao.setObjectName(u"nutricao")
        self.nutricao.setGeometry(QRect(180, 146, 281, 51))
        self.nutricao.setStyleSheet(u"")
        self.gridLayout_228 = QGridLayout(self.nutricao)
        self.gridLayout_228.setObjectName(u"gridLayout_228")
        self.radio_eutrofico_2 = QRadioButton(self.nutricao)
        self.radio_eutrofico_2.setObjectName(u"radio_eutrofico_2")
        self.radio_eutrofico_2.setFont(font6)

        self.gridLayout_228.addWidget(self.radio_eutrofico_2, 0, 0, 1, 1)

        self.radio_caquetico_2 = QRadioButton(self.nutricao)
        self.radio_caquetico_2.setObjectName(u"radio_caquetico_2")
        self.radio_caquetico_2.setFont(font6)

        self.gridLayout_228.addWidget(self.radio_caquetico_2, 0, 1, 1, 1)

        self.radio_obeso_2 = QRadioButton(self.nutricao)
        self.radio_obeso_2.setObjectName(u"radio_obeso_2")
        self.radio_obeso_2.setFont(font6)
        self.radio_obeso_2.setStyleSheet(u"border: none;")

        self.gridLayout_228.addWidget(self.radio_obeso_2, 0, 2, 1, 1)

        self.locomocao = QGroupBox(self.groupLesoes_10)
        self.locomocao.setObjectName(u"locomocao")
        self.locomocao.setGeometry(QRect(180, 187, 321, 51))
        self.locomocao.setStyleSheet(u"")
        self.gridLayout_229 = QGridLayout(self.locomocao)
        self.gridLayout_229.setObjectName(u"gridLayout_229")
        self.radio_independente_2 = QRadioButton(self.locomocao)
        self.radio_independente_2.setObjectName(u"radio_independente_2")
        self.radio_independente_2.setFont(font6)

        self.gridLayout_229.addWidget(self.radio_independente_2, 0, 0, 1, 1)

        self.radio_com_ajuda_2 = QRadioButton(self.locomocao)
        self.radio_com_ajuda_2.setObjectName(u"radio_com_ajuda_2")
        self.radio_com_ajuda_2.setFont(font6)

        self.gridLayout_229.addWidget(self.radio_com_ajuda_2, 0, 1, 1, 1)

        self.radio_restrito_2 = QRadioButton(self.locomocao)
        self.radio_restrito_2.setObjectName(u"radio_restrito_2")
        self.radio_restrito_2.setFont(font6)

        self.gridLayout_229.addWidget(self.radio_restrito_2, 0, 2, 1, 1)

        self.orientacao = QGroupBox(self.groupLesoes_10)
        self.orientacao.setObjectName(u"orientacao")
        self.orientacao.setGeometry(QRect(180, 230, 226, 51))
        self.orientacao.setStyleSheet(u"")
        self.gridLayout_230 = QGridLayout(self.orientacao)
        self.gridLayout_230.setObjectName(u"gridLayout_230")
        self.radio_desorientado_2 = QRadioButton(self.orientacao)
        self.radio_desorientado_2.setObjectName(u"radio_desorientado_2")
        self.radio_desorientado_2.setFont(font6)

        self.gridLayout_230.addWidget(self.radio_desorientado_2, 0, 2, 1, 1)

        self.radio_orientado_2 = QRadioButton(self.orientacao)
        self.radio_orientado_2.setObjectName(u"radio_orientado_2")
        self.radio_orientado_2.setFont(font6)

        self.gridLayout_230.addWidget(self.radio_orientado_2, 0, 1, 1, 1)

        self.quanto_ao = QGroupBox(self.groupLesoes_10)
        self.quanto_ao.setObjectName(u"quanto_ao")
        self.quanto_ao.setGeometry(QRect(180, 272, 242, 51))
        self.quanto_ao.setStyleSheet(u"")
        self.gridLayout_231 = QGridLayout(self.quanto_ao)
        self.gridLayout_231.setObjectName(u"gridLayout_231")
        self.radio_tempo_2 = QRadioButton(self.quanto_ao)
        self.radio_tempo_2.setObjectName(u"radio_tempo_2")
        self.radio_tempo_2.setFont(font6)

        self.gridLayout_231.addWidget(self.radio_tempo_2, 0, 0, 1, 1)

        self.radio_pessoa_2 = QRadioButton(self.quanto_ao)
        self.radio_pessoa_2.setObjectName(u"radio_pessoa_2")
        self.radio_pessoa_2.setFont(font6)
        self.radio_pessoa_2.setStyleSheet(u"")

        self.gridLayout_231.addWidget(self.radio_pessoa_2, 0, 1, 1, 1)

        self.radio_espaco_2 = QRadioButton(self.quanto_ao)
        self.radio_espaco_2.setObjectName(u"radio_espaco_2")
        self.radio_espaco_2.setFont(font6)

        self.gridLayout_231.addWidget(self.radio_espaco_2, 0, 2, 1, 1)

        self.comunicacao = QGroupBox(self.groupLesoes_10)
        self.comunicacao.setObjectName(u"comunicacao")
        self.comunicacao.setGeometry(QRect(180, 313, 671, 51))
        self.comunicacao.setStyleSheet(u"")
        self.gridLayout_232 = QGridLayout(self.comunicacao)
        self.gridLayout_232.setObjectName(u"gridLayout_232")
        self.radio_verbal_presente_2 = QRadioButton(self.comunicacao)
        self.radio_verbal_presente_2.setObjectName(u"radio_verbal_presente_2")
        self.radio_verbal_presente_2.setFont(font6)

        self.gridLayout_232.addWidget(self.radio_verbal_presente_2, 0, 2, 1, 1)

        self.radio_comunicativo_2 = QRadioButton(self.comunicacao)
        self.radio_comunicativo_2.setObjectName(u"radio_comunicativo_2")
        self.radio_comunicativo_2.setFont(font6)

        self.gridLayout_232.addWidget(self.radio_comunicativo_2, 0, 0, 1, 1)

        self.radio_verbal_prejudicada_2 = QRadioButton(self.comunicacao)
        self.radio_verbal_prejudicada_2.setObjectName(u"radio_verbal_prejudicada_2")
        self.radio_verbal_prejudicada_2.setFont(font6)

        self.gridLayout_232.addWidget(self.radio_verbal_prejudicada_2, 0, 3, 1, 1)

        self.radio_nao_comunicativo_2 = QRadioButton(self.comunicacao)
        self.radio_nao_comunicativo_2.setObjectName(u"radio_nao_comunicativo_2")
        self.radio_nao_comunicativo_2.setFont(font6)

        self.gridLayout_232.addWidget(self.radio_nao_comunicativo_2, 0, 1, 1, 1)

        self.postura = QGroupBox(self.groupLesoes_10)
        self.postura.setObjectName(u"postura")
        self.postura.setGeometry(QRect(180, 396, 142, 46))
        self.postura.setStyleSheet(u"")
        self.gridLayout_233 = QGridLayout(self.postura)
        self.gridLayout_233.setObjectName(u"gridLayout_233")
        self.radio_sofrivel_2 = QRadioButton(self.postura)
        self.radio_sofrivel_2.setObjectName(u"radio_sofrivel_2")
        self.radio_sofrivel_2.setFont(font6)

        self.gridLayout_233.addWidget(self.radio_sofrivel_2, 0, 2, 1, 1)

        self.radio_boa_2 = QRadioButton(self.postura)
        self.radio_boa_2.setObjectName(u"radio_boa_2")
        self.radio_boa_2.setFont(font6)

        self.gridLayout_233.addWidget(self.radio_boa_2, 0, 0, 1, 1)

        self.atencao = QGroupBox(self.groupLesoes_10)
        self.atencao.setObjectName(u"atencao")
        self.atencao.setGeometry(QRect(180, 432, 212, 51))
        self.atencao.setStyleSheet(u"")
        self.gridLayout_234 = QGridLayout(self.atencao)
        self.gridLayout_234.setObjectName(u"gridLayout_234")
        self.radio_vigilancia_2 = QRadioButton(self.atencao)
        self.radio_vigilancia_2.setObjectName(u"radio_vigilancia_2")
        self.radio_vigilancia_2.setFont(font6)

        self.gridLayout_234.addWidget(self.radio_vigilancia_2, 0, 0, 1, 1)

        self.radio_tenacidade_2 = QRadioButton(self.atencao)
        self.radio_tenacidade_2.setObjectName(u"radio_tenacidade_2")
        self.radio_tenacidade_2.setFont(font6)

        self.gridLayout_234.addWidget(self.radio_tenacidade_2, 0, 1, 1, 1)

        self.memoria = QGroupBox(self.groupLesoes_10)
        self.memoria.setObjectName(u"memoria")
        self.memoria.setGeometry(QRect(920, 20, 351, 51))
        self.memoria.setStyleSheet(u"")
        self.gridLayout_235 = QGridLayout(self.memoria)
        self.gridLayout_235.setObjectName(u"gridLayout_235")
        self.radio_integra_2 = QRadioButton(self.memoria)
        self.radio_integra_2.setObjectName(u"radio_integra_2")
        self.radio_integra_2.setFont(font6)

        self.gridLayout_235.addWidget(self.radio_integra_2, 0, 0, 1, 1)

        self.radio_deficiente_2 = QRadioButton(self.memoria)
        self.radio_deficiente_2.setObjectName(u"radio_deficiente_2")
        self.radio_deficiente_2.setFont(font6)

        self.gridLayout_235.addWidget(self.radio_deficiente_2, 0, 1, 1, 1)

        self.radio_recente_2 = QRadioButton(self.memoria)
        self.radio_recente_2.setObjectName(u"radio_recente_2")
        self.radio_recente_2.setFont(font6)

        self.gridLayout_235.addWidget(self.radio_recente_2, 0, 2, 1, 1)

        self.radio_passada_2 = QRadioButton(self.memoria)
        self.radio_passada_2.setObjectName(u"radio_passada_2")
        self.radio_passada_2.setFont(font6)

        self.gridLayout_235.addWidget(self.radio_passada_2, 0, 3, 1, 1)

        self.atitude = QGroupBox(self.groupLesoes_10)
        self.atitude.setObjectName(u"atitude")
        self.atitude.setGeometry(QRect(920, 60, 237, 46))
        self.atitude.setStyleSheet(u"")
        self.gridLayout_236 = QGridLayout(self.atitude)
        self.gridLayout_236.setObjectName(u"gridLayout_236")
        self.radio_ativa_2 = QRadioButton(self.atitude)
        self.radio_ativa_2.setObjectName(u"radio_ativa_2")
        self.radio_ativa_2.setFont(font6)

        self.gridLayout_236.addWidget(self.radio_ativa_2, 0, 0, 1, 1)

        self.radio_passiva_2 = QRadioButton(self.atitude)
        self.radio_passiva_2.setObjectName(u"radio_passiva_2")
        self.radio_passiva_2.setFont(font6)

        self.gridLayout_236.addWidget(self.radio_passiva_2, 0, 1, 1, 1)

        self.radio_forcada_2 = QRadioButton(self.atitude)
        self.radio_forcada_2.setObjectName(u"radio_forcada_2")
        self.radio_forcada_2.setFont(font6)

        self.gridLayout_236.addWidget(self.radio_forcada_2, 0, 2, 1, 1)

        self.movimentacao = QGroupBox(self.groupLesoes_10)
        self.movimentacao.setObjectName(u"movimentacao")
        self.movimentacao.setGeometry(QRect(180, 513, 642, 50))
        self.movimentacao.setStyleSheet(u"")
        self.gridLayout_237 = QGridLayout(self.movimentacao)
        self.gridLayout_237.setObjectName(u"gridLayout_237")
        self.radio_semi_acamado_2 = QRadioButton(self.movimentacao)
        self.radio_semi_acamado_2.setObjectName(u"radio_semi_acamado_2")
        self.radio_semi_acamado_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_semi_acamado_2, 0, 4, 1, 1)

        self.radio_deambula_2 = QRadioButton(self.movimentacao)
        self.radio_deambula_2.setObjectName(u"radio_deambula_2")
        self.radio_deambula_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_deambula_2, 0, 0, 1, 1)

        self.radio_acamado_2 = QRadioButton(self.movimentacao)
        self.radio_acamado_2.setObjectName(u"radio_acamado_2")
        self.radio_acamado_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_acamado_2, 0, 1, 1, 1)

        self.radio_restrito_leito_2 = QRadioButton(self.movimentacao)
        self.radio_restrito_leito_2.setObjectName(u"radio_restrito_leito_2")
        self.radio_restrito_leito_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_restrito_leito_2, 0, 2, 1, 1)

        self.radio_sem_movimentacao_2 = QRadioButton(self.movimentacao)
        self.radio_sem_movimentacao_2.setObjectName(u"radio_sem_movimentacao_2")
        self.radio_sem_movimentacao_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_sem_movimentacao_2, 0, 3, 1, 1)

        self.radio_deambula_ajuda_2 = QRadioButton(self.movimentacao)
        self.radio_deambula_ajuda_2.setObjectName(u"radio_deambula_ajuda_2")
        self.radio_deambula_ajuda_2.setFont(font6)

        self.gridLayout_237.addWidget(self.radio_deambula_ajuda_2, 0, 5, 1, 1)

        self.movimenta_se_com_ajuda = QGroupBox(self.groupLesoes_10)
        self.movimenta_se_com_ajuda.setObjectName(u"movimenta_se_com_ajuda")
        self.movimenta_se_com_ajuda.setGeometry(QRect(920, 96, 108, 51))
        self.movimenta_se_com_ajuda.setStyleSheet(u"")
        self.gridLayout_238 = QGridLayout(self.movimenta_se_com_ajuda)
        self.gridLayout_238.setObjectName(u"gridLayout_238")
        self.radio_sim_2 = QRadioButton(self.movimenta_se_com_ajuda)
        self.radio_sim_2.setObjectName(u"radio_sim_2")
        self.radio_sim_2.setFont(font6)
        self.radio_sim_2.setStyleSheet(u"border: none;")

        self.gridLayout_238.addWidget(self.radio_sim_2, 0, 0, 1, 1)

        self.radio_nao_2 = QRadioButton(self.movimenta_se_com_ajuda)
        self.radio_nao_2.setObjectName(u"radio_nao_2")
        self.radio_nao_2.setFont(font6)
        self.radio_nao_2.setStyleSheet(u"border: none;")

        self.gridLayout_238.addWidget(self.radio_nao_2, 0, 1, 1, 1)

        self.expressao_facial = QGroupBox(self.groupLesoes_10)
        self.expressao_facial.setObjectName(u"expressao_facial")
        self.expressao_facial.setGeometry(QRect(180, 473, 559, 50))
        self.expressao_facial.setStyleSheet(u"")
        self.gridLayout_239 = QGridLayout(self.expressao_facial)
        self.gridLayout_239.setObjectName(u"gridLayout_239")
        self.radio_inexpressivo_2 = QRadioButton(self.expressao_facial)
        self.radio_inexpressivo_2.setObjectName(u"radio_inexpressivo_2")
        self.radio_inexpressivo_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_inexpressivo_2, 0, 3, 1, 1)

        self.radio_apatico_2 = QRadioButton(self.expressao_facial)
        self.radio_apatico_2.setObjectName(u"radio_apatico_2")
        self.radio_apatico_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_apatico_2, 0, 0, 1, 1)

        self.radio_desapontado_2 = QRadioButton(self.expressao_facial)
        self.radio_desapontado_2.setObjectName(u"radio_desapontado_2")
        self.radio_desapontado_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_desapontado_2, 0, 4, 1, 1)

        self.radio_desconfiado_2 = QRadioButton(self.expressao_facial)
        self.radio_desconfiado_2.setObjectName(u"radio_desconfiado_2")
        self.radio_desconfiado_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_desconfiado_2, 0, 6, 1, 1)

        self.radio_colerico_2 = QRadioButton(self.expressao_facial)
        self.radio_colerico_2.setObjectName(u"radio_colerico_2")
        self.radio_colerico_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_colerico_2, 0, 1, 1, 1)

        self.radio_tenso_2 = QRadioButton(self.expressao_facial)
        self.radio_tenso_2.setObjectName(u"radio_tenso_2")
        self.radio_tenso_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_tenso_2, 0, 2, 1, 1)

        self.radio_triste_2 = QRadioButton(self.expressao_facial)
        self.radio_triste_2.setObjectName(u"radio_triste_2")
        self.radio_triste_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_triste_2, 0, 5, 1, 1)

        self.radio_alegre_2 = QRadioButton(self.expressao_facial)
        self.radio_alegre_2.setObjectName(u"radio_alegre_2")
        self.radio_alegre_2.setFont(font6)

        self.gridLayout_239.addWidget(self.radio_alegre_2, 0, 7, 1, 1)

        self.causa = QLineEdit(self.groupLesoes_10)
        self.causa.setObjectName(u"causa")
        self.causa.setGeometry(QRect(180, 370, 121, 31))
        self.de = QLineEdit(self.groupLesoes_10)
        self.de.setObjectName(u"de")
        self.de.setGeometry(QRect(920, 150, 121, 31))
        self.label_115 = QLabel(self.groupLesoes_10)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(20, 40, 131, 18))
        self.label_115.setFont(font6)
        self.label_108 = QLabel(self.groupLesoes_10)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(20, 90, 96, 18))
        self.label_108.setFont(font6)
        self.label_112 = QLabel(self.groupLesoes_10)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(20, 130, 81, 18))
        self.label_112.setFont(font6)
        self.label_121 = QLabel(self.groupLesoes_10)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(20, 160, 62, 29))
        self.label_121.setFont(font6)
        self.label_114 = QLabel(self.groupLesoes_10)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(20, 210, 87, 18))
        self.label_114.setFont(font6)
        self.label_136 = QLabel(self.groupLesoes_10)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(20, 250, 81, 18))
        self.label_136.setFont(font6)
        self.label_117 = QLabel(self.groupLesoes_10)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(20, 290, 76, 18))
        self.label_117.setFont(font6)
        self.label_122 = QLabel(self.groupLesoes_10)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(20, 330, 101, 18))
        self.label_122.setFont(font6)
        self.label_111 = QLabel(self.groupLesoes_10)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(20, 380, 50, 18))
        self.label_111.setFont(font6)
        self.label_113 = QLabel(self.groupLesoes_10)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(20, 410, 58, 29))
        self.label_113.setFont(font6)
        self.label_116 = QLabel(self.groupLesoes_10)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(20, 456, 62, 18))
        self.label_116.setFont(font6)
        self.label_118 = QLabel(self.groupLesoes_10)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(20, 494, 126, 18))
        self.label_118.setFont(font6)
        self.label_120 = QLabel(self.groupLesoes_10)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(20, 534, 99, 18))
        self.label_120.setFont(font6)
        self.label_110 = QLabel(self.groupLesoes_10)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(730, 40, 66, 18))
        self.label_110.setFont(font6)
        self.label_119 = QLabel(self.groupLesoes_10)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(730, 80, 53, 18))
        self.label_119.setFont(font6)
        self.label_135 = QLabel(self.groupLesoes_10)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(730, 120, 169, 18))
        self.label_135.setFont(font6)
        self.label_109 = QLabel(self.groupLesoes_10)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(730, 150, 25, 29))
        self.label_109.setFont(font6)

        self.gridLayout_327.addWidget(self.groupLesoes_10, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_330 = QGridLayout(self.tab_3)
        self.gridLayout_330.setObjectName(u"gridLayout_330")
        self.groupLesoes_11 = QGroupBox(self.tab_3)
        self.groupLesoes_11.setObjectName(u"groupLesoes_11")
        self.groupLesoes_11.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.pupilas = QGroupBox(self.groupLesoes_11)
        self.pupilas.setObjectName(u"pupilas")
        self.pupilas.setGeometry(QRect(220, 30, 191, 46))
        self.pupilas.setStyleSheet(u"")
        self.gridLayout_253 = QGridLayout(self.pupilas)
        self.gridLayout_253.setObjectName(u"gridLayout_253")
        self.radio_isocoricas = QRadioButton(self.pupilas)
        self.radio_isocoricas.setObjectName(u"radio_isocoricas")
        self.radio_isocoricas.setFont(font6)

        self.gridLayout_253.addWidget(self.radio_isocoricas, 0, 0, 1, 1)

        self.radio_anisoricas = QRadioButton(self.pupilas)
        self.radio_anisoricas.setObjectName(u"radio_anisoricas")
        self.radio_anisoricas.setFont(font6)

        self.gridLayout_253.addWidget(self.radio_anisoricas, 0, 1, 1, 1)

        self.reagentes_a_luz = QGroupBox(self.groupLesoes_11)
        self.reagentes_a_luz.setObjectName(u"reagentes_a_luz")
        self.reagentes_a_luz.setGeometry(QRect(220, 66, 101, 46))
        self.reagentes_a_luz.setStyleSheet(u"")
        self.gridLayout_260 = QGridLayout(self.reagentes_a_luz)
        self.gridLayout_260.setObjectName(u"gridLayout_260")
        self.radio_sim_3 = QRadioButton(self.reagentes_a_luz)
        self.radio_sim_3.setObjectName(u"radio_sim_3")
        self.radio_sim_3.setFont(font6)

        self.gridLayout_260.addWidget(self.radio_sim_3, 0, 0, 1, 1)

        self.radio_nao_3 = QRadioButton(self.reagentes_a_luz)
        self.radio_nao_3.setObjectName(u"radio_nao_3")
        self.radio_nao_3.setFont(font6)

        self.gridLayout_260.addWidget(self.radio_nao_3, 0, 1, 1, 1)

        self.forca_muscular = QGroupBox(self.groupLesoes_11)
        self.forca_muscular.setObjectName(u"forca_muscular")
        self.forca_muscular.setGeometry(QRect(220, 102, 191, 46))
        self.forca_muscular.setStyleSheet(u"")
        self.gridLayout_241 = QGridLayout(self.forca_muscular)
        self.gridLayout_241.setObjectName(u"gridLayout_241")
        self.radio_preservada = QRadioButton(self.forca_muscular)
        self.radio_preservada.setObjectName(u"radio_preservada")
        self.radio_preservada.setFont(font6)
        self.radio_preservada.setStyleSheet(u"border: none;")

        self.gridLayout_241.addWidget(self.radio_preservada, 0, 0, 1, 1)

        self.radio_reduzida = QRadioButton(self.forca_muscular)
        self.radio_reduzida.setObjectName(u"radio_reduzida")
        self.radio_reduzida.setFont(font6)

        self.gridLayout_241.addWidget(self.radio_reduzida, 0, 1, 1, 1)

        self.reflexos = QGroupBox(self.groupLesoes_11)
        self.reflexos.setObjectName(u"reflexos")
        self.reflexos.setGeometry(QRect(220, 138, 191, 46))
        self.reflexos.setStyleSheet(u"")
        self.gridLayout_257 = QGridLayout(self.reflexos)
        self.gridLayout_257.setObjectName(u"gridLayout_257")
        self.radio_preservados = QRadioButton(self.reflexos)
        self.radio_preservados.setObjectName(u"radio_preservados")
        self.radio_preservados.setFont(font6)

        self.gridLayout_257.addWidget(self.radio_preservados, 0, 0, 1, 1)

        self.radio_alterados = QRadioButton(self.reflexos)
        self.radio_alterados.setObjectName(u"radio_alterados")
        self.radio_alterados.setFont(font6)

        self.gridLayout_257.addWidget(self.radio_alterados, 0, 1, 1, 1)

        self.sensibilidade = QGroupBox(self.groupLesoes_11)
        self.sensibilidade.setObjectName(u"sensibilidade")
        self.sensibilidade.setGeometry(QRect(220, 174, 191, 46))
        self.sensibilidade.setStyleSheet(u"")
        self.gridLayout_246 = QGridLayout(self.sensibilidade)
        self.gridLayout_246.setObjectName(u"gridLayout_246")
        self.radio_normal = QRadioButton(self.sensibilidade)
        self.radio_normal.setObjectName(u"radio_normal")
        self.radio_normal.setFont(font6)

        self.gridLayout_246.addWidget(self.radio_normal, 0, 0, 1, 1)

        self.radio_reduzida_sensibilidade = QRadioButton(self.sensibilidade)
        self.radio_reduzida_sensibilidade.setObjectName(u"radio_reduzida_sensibilidade")
        self.radio_reduzida_sensibilidade.setFont(font6)

        self.gridLayout_246.addWidget(self.radio_reduzida_sensibilidade, 0, 1, 1, 1)

        self.escala_de_coma_de_Glasgow = QGroupBox(self.groupLesoes_11)
        self.escala_de_coma_de_Glasgow.setObjectName(u"escala_de_coma_de_Glasgow")
        self.escala_de_coma_de_Glasgow.setGeometry(QRect(220, 210, 101, 46))
        self.escala_de_coma_de_Glasgow.setStyleSheet(u"")
        self.gridLayout_243 = QGridLayout(self.escala_de_coma_de_Glasgow)
        self.gridLayout_243.setObjectName(u"gridLayout_243")
        self.radio_sim_coma = QRadioButton(self.escala_de_coma_de_Glasgow)
        self.radio_sim_coma.setObjectName(u"radio_sim_coma")
        self.radio_sim_coma.setFont(font6)

        self.gridLayout_243.addWidget(self.radio_sim_coma, 0, 0, 1, 1)

        self.radio_nao_coma = QRadioButton(self.escala_de_coma_de_Glasgow)
        self.radio_nao_coma.setObjectName(u"radio_nao_coma")
        self.radio_nao_coma.setFont(font6)

        self.gridLayout_243.addWidget(self.radio_nao_coma, 0, 1, 1, 1)

        self.abertura_ocular = QComboBox(self.groupLesoes_11)
        self.abertura_ocular.addItem("")
        self.abertura_ocular.addItem("")
        self.abertura_ocular.addItem("")
        self.abertura_ocular.addItem("")
        self.abertura_ocular.setObjectName(u"abertura_ocular")
        self.abertura_ocular.setGeometry(QRect(220, 260, 54, 31))
        self.resposta_verbal = QComboBox(self.groupLesoes_11)
        self.resposta_verbal.addItem("")
        self.resposta_verbal.addItem("")
        self.resposta_verbal.addItem("")
        self.resposta_verbal.addItem("")
        self.resposta_verbal.addItem("")
        self.resposta_verbal.setObjectName(u"resposta_verbal")
        self.resposta_verbal.setGeometry(QRect(220, 300, 54, 31))
        self.resposta_motora = QComboBox(self.groupLesoes_11)
        self.resposta_motora.addItem("")
        self.resposta_motora.addItem("")
        self.resposta_motora.addItem("")
        self.resposta_motora.addItem("")
        self.resposta_motora.addItem("")
        self.resposta_motora.addItem("")
        self.resposta_motora.setObjectName(u"resposta_motora")
        self.resposta_motora.setGeometry(QRect(220, 340, 54, 30))
        self.resposta_pupilar = QComboBox(self.groupLesoes_11)
        self.resposta_pupilar.addItem("")
        self.resposta_pupilar.addItem("")
        self.resposta_pupilar.addItem("")
        self.resposta_pupilar.setObjectName(u"resposta_pupilar")
        self.resposta_pupilar.setGeometry(QRect(220, 380, 54, 30))
        self.label_140 = QLabel(self.groupLesoes_11)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(30, 50, 56, 18))
        self.label_140.setFont(font6)
        self.label_141 = QLabel(self.groupLesoes_11)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(30, 80, 121, 18))
        self.label_141.setFont(font6)
        self.label_145 = QLabel(self.groupLesoes_11)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(30, 120, 111, 18))
        self.label_145.setFont(font6)
        self.label_138 = QLabel(self.groupLesoes_11)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(30, 160, 64, 18))
        self.label_138.setFont(font6)
        self.label_146 = QLabel(self.groupLesoes_11)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(30, 200, 100, 18))
        self.label_146.setFont(font6)
        self.label_142 = QLabel(self.groupLesoes_11)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(30, 230, 171, 18))
        self.label_142.setFont(font6)
        self.label_139 = QLabel(self.groupLesoes_11)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(30, 260, 101, 29))
        self.label_139.setFont(font6)
        self.label_137 = QLabel(self.groupLesoes_11)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(30, 300, 101, 29))
        self.label_137.setFont(font6)
        self.label_143 = QLabel(self.groupLesoes_11)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(30, 340, 111, 29))
        self.label_143.setFont(font6)
        self.label_144 = QLabel(self.groupLesoes_11)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(30, 380, 111, 29))
        self.label_144.setFont(font6)

        self.gridLayout_330.addWidget(self.groupLesoes_11, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_332 = QGridLayout(self.tab_4)
        self.gridLayout_332.setObjectName(u"gridLayout_332")
        self.groupLesoes_12 = QGroupBox(self.tab_4)
        self.groupLesoes_12.setObjectName(u"groupLesoes_12")
        self.groupLesoes_12.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top:12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}"
                        "\n"
"\n"
"")
        self.mobilidade = QGroupBox(self.groupLesoes_12)
        self.mobilidade.setObjectName(u"mobilidade")
        self.mobilidade.setGeometry(QRect(170, 467, 162, 51))
        self.mobilidade.setStyleSheet(u"")
        self.gridLayout_245 = QGridLayout(self.mobilidade)
        self.gridLayout_245.setObjectName(u"gridLayout_245")
        self.radio_mobilidade_presente = QRadioButton(self.mobilidade)
        self.radio_mobilidade_presente.setObjectName(u"radio_mobilidade_presente")
        self.radio_mobilidade_presente.setFont(font6)

        self.gridLayout_245.addWidget(self.radio_mobilidade_presente, 0, 0, 1, 1)

        self.radio_mobilidade_ausente = QRadioButton(self.mobilidade)
        self.radio_mobilidade_ausente.setObjectName(u"radio_mobilidade_ausente")
        self.radio_mobilidade_ausente.setFont(font6)

        self.gridLayout_245.addWidget(self.radio_mobilidade_ausente, 0, 1, 1, 1)

        self.elasticidade = QGroupBox(self.groupLesoes_12)
        self.elasticidade.setObjectName(u"elasticidade")
        self.elasticidade.setGeometry(QRect(170, 260, 183, 51))
        self.gridLayout_249 = QGridLayout(self.elasticidade)
        self.gridLayout_249.setObjectName(u"gridLayout_249")
        self.radio_elasticidade_preservada = QRadioButton(self.elasticidade)
        self.radio_elasticidade_preservada.setObjectName(u"radio_elasticidade_preservada")
        self.radio_elasticidade_preservada.setFont(font6)

        self.gridLayout_249.addWidget(self.radio_elasticidade_preservada, 0, 0, 1, 1)

        self.radio_elasticidade_diminuida = QRadioButton(self.elasticidade)
        self.radio_elasticidade_diminuida.setObjectName(u"radio_elasticidade_diminuida")
        self.radio_elasticidade_diminuida.setFont(font6)

        self.gridLayout_249.addWidget(self.radio_elasticidade_diminuida, 0, 1, 1, 1)

        self.espessura = QGroupBox(self.groupLesoes_12)
        self.espessura.setObjectName(u"espessura")
        self.espessura.setGeometry(QRect(170, 425, 311, 51))
        self.gridLayout_262 = QGridLayout(self.espessura)
        self.gridLayout_262.setObjectName(u"gridLayout_262")
        self.radio_eufrofica_espessura = QRadioButton(self.espessura)
        self.radio_eufrofica_espessura.setObjectName(u"radio_eufrofica_espessura")
        self.radio_eufrofica_espessura.setFont(font6)

        self.gridLayout_262.addWidget(self.radio_eufrofica_espessura, 0, 0, 1, 1)

        self.radio_atrofica = QRadioButton(self.espessura)
        self.radio_atrofica.setObjectName(u"radio_atrofica")
        self.radio_atrofica.setFont(font6)

        self.gridLayout_262.addWidget(self.radio_atrofica, 0, 1, 1, 1)

        self.radio_hipertrofica = QRadioButton(self.espessura)
        self.radio_hipertrofica.setObjectName(u"radio_hipertrofica")
        self.radio_hipertrofica.setFont(font6)

        self.gridLayout_262.addWidget(self.radio_hipertrofica, 0, 2, 1, 1)

        self.radio_espessa = QRadioButton(self.espessura)
        self.radio_espessa.setObjectName(u"radio_espessa")
        self.radio_espessa.setFont(font6)

        self.gridLayout_262.addWidget(self.radio_espessa, 0, 3, 1, 1)

        self.textura = QGroupBox(self.groupLesoes_12)
        self.textura.setObjectName(u"textura")
        self.textura.setGeometry(QRect(170, 383, 321, 51))
        self.gridLayout_66 = QGridLayout(self.textura)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.radio_eufrofica = QRadioButton(self.textura)
        self.radio_eufrofica.setObjectName(u"radio_eufrofica")
        self.radio_eufrofica.setFont(font6)

        self.gridLayout_66.addWidget(self.radio_eufrofica, 0, 0, 1, 1)

        self.radio_seca = QRadioButton(self.textura)
        self.radio_seca.setObjectName(u"radio_seca")
        self.radio_seca.setFont(font6)

        self.gridLayout_66.addWidget(self.radio_seca, 0, 1, 1, 1)

        self.radio_lisa = QRadioButton(self.textura)
        self.radio_lisa.setObjectName(u"radio_lisa")
        self.radio_lisa.setFont(font6)

        self.gridLayout_66.addWidget(self.radio_lisa, 0, 2, 1, 1)

        self.radio_aspera = QRadioButton(self.textura)
        self.radio_aspera.setObjectName(u"radio_aspera")
        self.radio_aspera.setFont(font6)

        self.gridLayout_66.addWidget(self.radio_aspera, 0, 3, 1, 1)

        self.radio_enrugada = QRadioButton(self.textura)
        self.radio_enrugada.setObjectName(u"radio_enrugada")
        self.radio_enrugada.setFont(font6)

        self.gridLayout_66.addWidget(self.radio_enrugada, 0, 4, 1, 1)

        self.presenca_de_sudorese = QGroupBox(self.groupLesoes_12)
        self.presenca_de_sudorese.setObjectName(u"presenca_de_sudorese")
        self.presenca_de_sudorese.setGeometry(QRect(170, 302, 331, 51))
        self.gridLayout_123 = QGridLayout(self.presenca_de_sudorese)
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.radio_presenca_sim = QRadioButton(self.presenca_de_sudorese)
        self.radio_presenca_sim.setObjectName(u"radio_presenca_sim")
        self.radio_presenca_sim.setFont(font6)

        self.gridLayout_123.addWidget(self.radio_presenca_sim, 0, 0, 1, 1)

        self.radio_presenca_nao = QRadioButton(self.presenca_de_sudorese)
        self.radio_presenca_nao.setObjectName(u"radio_presenca_nao")
        self.radio_presenca_nao.setFont(font6)

        self.gridLayout_123.addWidget(self.radio_presenca_nao, 0, 1, 1, 1)

        self.radio_diaforese = QRadioButton(self.presenca_de_sudorese)
        self.radio_diaforese.setObjectName(u"radio_diaforese")
        self.radio_diaforese.setFont(font6)

        self.gridLayout_123.addWidget(self.radio_diaforese, 0, 2, 1, 1)

        self.radio_hiperidrose = QRadioButton(self.presenca_de_sudorese)
        self.radio_hiperidrose.setObjectName(u"radio_hiperidrose")
        self.radio_hiperidrose.setFont(font6)

        self.gridLayout_123.addWidget(self.radio_hiperidrose, 0, 3, 1, 1)

        self.radio_xerodermia = QRadioButton(self.presenca_de_sudorese)
        self.radio_xerodermia.setObjectName(u"radio_xerodermia")
        self.radio_xerodermia.setFont(font6)

        self.gridLayout_123.addWidget(self.radio_xerodermia, 0, 4, 1, 1)

        self.coloracao_da_pele = QGroupBox(self.groupLesoes_12)
        self.coloracao_da_pele.setObjectName(u"coloracao_da_pele")
        self.coloracao_da_pele.setGeometry(QRect(170, 184, 337, 51))
        self.gridLayout_265 = QGridLayout(self.coloracao_da_pele)
        self.gridLayout_265.setObjectName(u"gridLayout_265")
        self.radio_hipocorada = QRadioButton(self.coloracao_da_pele)
        self.radio_hipocorada.setObjectName(u"radio_hipocorada")
        self.radio_hipocorada.setFont(font6)

        self.gridLayout_265.addWidget(self.radio_hipocorada, 0, 1, 1, 1)

        self.radio_palidez = QRadioButton(self.coloracao_da_pele)
        self.radio_palidez.setObjectName(u"radio_palidez")
        self.radio_palidez.setFont(font6)

        self.gridLayout_265.addWidget(self.radio_palidez, 0, 2, 1, 1)

        self.radio_normocorada = QRadioButton(self.coloracao_da_pele)
        self.radio_normocorada.setObjectName(u"radio_normocorada")
        self.radio_normocorada.setFont(font6)

        self.gridLayout_265.addWidget(self.radio_normocorada, 0, 0, 1, 1)

        self.radio_hiperemiade = QRadioButton(self.coloracao_da_pele)
        self.radio_hiperemiade.setObjectName(u"radio_hiperemiade")
        self.radio_hiperemiade.setFont(font6)

        self.gridLayout_265.addWidget(self.radio_hiperemiade, 0, 3, 1, 1)

        self.cianose = QGroupBox(self.groupLesoes_12)
        self.cianose.setObjectName(u"cianose")
        self.cianose.setGeometry(QRect(170, 110, 171, 50))
        self.gridLayout_65 = QGridLayout(self.cianose)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.radio_acianotico = QRadioButton(self.cianose)
        self.radio_acianotico.setObjectName(u"radio_acianotico")
        self.radio_acianotico.setFont(font6)

        self.gridLayout_65.addWidget(self.radio_acianotico, 0, 0, 1, 1)

        self.radio_cianotico = QRadioButton(self.cianose)
        self.radio_cianotico.setObjectName(u"radio_cianotico")
        self.radio_cianotico.setFont(font6)

        self.gridLayout_65.addWidget(self.radio_cianotico, 0, 1, 1, 1)

        self.icterica = QGroupBox(self.groupLesoes_12)
        self.icterica.setObjectName(u"icterica")
        self.icterica.setGeometry(QRect(170, 70, 171, 50))
        self.gridLayout_64 = QGridLayout(self.icterica)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.radio_anicterico = QRadioButton(self.icterica)
        self.radio_anicterico.setObjectName(u"radio_anicterico")
        self.radio_anicterico.setFont(font6)

        self.gridLayout_64.addWidget(self.radio_anicterico, 0, 0, 1, 1)

        self.radio_icterico = QRadioButton(self.icterica)
        self.radio_icterico.setObjectName(u"radio_icterico")
        self.radio_icterico.setFont(font6)

        self.gridLayout_64.addWidget(self.radio_icterico, 0, 1, 1, 1)

        self.turgor_cutaneo = QGroupBox(self.groupLesoes_12)
        self.turgor_cutaneo.setObjectName(u"turgor_cutaneo")
        self.turgor_cutaneo.setGeometry(QRect(170, 30, 171, 50))
        self.turgor_cutaneo.setStyleSheet(u"")
        self.gridLayout_63 = QGridLayout(self.turgor_cutaneo)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.radio_preservado = QRadioButton(self.turgor_cutaneo)
        self.radio_preservado.setObjectName(u"radio_preservado")
        self.radio_preservado.setFont(font6)

        self.gridLayout_63.addWidget(self.radio_preservado, 0, 0, 1, 1)

        self.radio_Diminuido = QRadioButton(self.turgor_cutaneo)
        self.radio_Diminuido.setObjectName(u"radio_Diminuido")
        self.radio_Diminuido.setFont(font6)

        self.gridLayout_63.addWidget(self.radio_Diminuido, 0, 1, 1, 1)

        self.label_155 = QLabel(self.groupLesoes_12)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setGeometry(QRect(20, 50, 109, 19))
        self.label_155.setFont(font6)
        self.label_147 = QLabel(self.groupLesoes_12)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setGeometry(QRect(20, 90, 61, 19))
        self.label_147.setFont(font6)
        self.label_148 = QLabel(self.groupLesoes_12)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(20, 130, 69, 19))
        self.label_148.setFont(font6)
        self.label_159 = QLabel(self.groupLesoes_12)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setGeometry(QRect(20, 170, 49, 19))
        self.label_159.setFont(font6)
        self.label_149 = QLabel(self.groupLesoes_12)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(20, 200, 119, 29))
        self.label_149.setFont(font6)
        self.label_157 = QLabel(self.groupLesoes_12)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setGeometry(QRect(20, 240, 49, 19))
        self.label_157.setFont(font6)
        self.label_158 = QLabel(self.groupLesoes_12)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setGeometry(QRect(20, 280, 91, 19))
        self.label_158.setFont(font6)
        self.label_154 = QLabel(self.groupLesoes_12)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(20, 320, 139, 19))
        self.label_154.setFont(font6)
        self.label_153 = QLabel(self.groupLesoes_12)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(20, 361, 49, 29))
        self.label_153.setFont(font6)
        self.label_152 = QLabel(self.groupLesoes_12)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(20, 410, 59, 19))
        self.label_152.setFont(font6)
        self.label_156 = QLabel(self.groupLesoes_12)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setGeometry(QRect(20, 450, 69, 19))
        self.label_156.setFont(font6)
        self.label_151 = QLabel(self.groupLesoes_12)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setGeometry(QRect(20, 488, 71, 19))
        self.label_151.setFont(font6)
        self.cianose_local = QLineEdit(self.groupLesoes_12)
        self.cianose_local.setObjectName(u"cianose_local")
        self.cianose_local.setGeometry(QRect(170, 162, 121, 31))
        self.outras_coloracao_da_pele = QLineEdit(self.groupLesoes_12)
        self.outras_coloracao_da_pele.setObjectName(u"outras_coloracao_da_pele")
        self.outras_coloracao_da_pele.setGeometry(QRect(170, 239, 121, 31))
        self.ps_local = QLineEdit(self.groupLesoes_12)
        self.ps_local.setObjectName(u"ps_local")
        self.ps_local.setGeometry(QRect(170, 359, 121, 31))

        self.gridLayout_332.addWidget(self.groupLesoes_12, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_410 = QGridLayout(self.tab_5)
        self.gridLayout_410.setObjectName(u"gridLayout_410")
        self.groupLesoes_13 = QGroupBox(self.tab_5)
        self.groupLesoes_13.setObjectName(u"groupLesoes_13")
        self.groupLesoes_13.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.m_distribuicao = QGroupBox(self.groupLesoes_13)
        self.m_distribuicao.setObjectName(u"m_distribuicao")
        self.m_distribuicao.setGeometry(QRect(170, 290, 193, 50))
        self.gridLayout_143 = QGridLayout(self.m_distribuicao)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.btn_linear = QRadioButton(self.m_distribuicao)
        self.btn_linear.setObjectName(u"btn_linear")

        self.gridLayout_143.addWidget(self.btn_linear, 0, 0, 1, 1)

        self.btn_circular = QRadioButton(self.m_distribuicao)
        self.btn_circular.setObjectName(u"btn_circular")

        self.gridLayout_143.addWidget(self.btn_circular, 0, 1, 1, 1)

        self.btn_arco = QRadioButton(self.m_distribuicao)
        self.btn_arco.setObjectName(u"btn_arco")

        self.gridLayout_143.addWidget(self.btn_arco, 0, 2, 1, 1)

        self.label_226 = QLabel(self.groupLesoes_13)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setGeometry(QRect(770, 80, 71, 16))
        self.lesoes_hemorragicas = QGroupBox(self.groupLesoes_13)
        self.lesoes_hemorragicas.setObjectName(u"lesoes_hemorragicas")
        self.lesoes_hemorragicas.setGeometry(QRect(170, 330, 94, 50))
        self.gridLayout_142 = QGridLayout(self.lesoes_hemorragicas)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.btn_sim_3 = QRadioButton(self.lesoes_hemorragicas)
        self.btn_sim_3.setObjectName(u"btn_sim_3")

        self.gridLayout_142.addWidget(self.btn_sim_3, 0, 0, 1, 1)

        self.btn_nao_3 = QRadioButton(self.lesoes_hemorragicas)
        self.btn_nao_3.setObjectName(u"btn_nao_3")

        self.gridLayout_142.addWidget(self.btn_nao_3, 0, 1, 1, 1)

        self.lh_tipo = QGroupBox(self.groupLesoes_13)
        self.lh_tipo.setObjectName(u"lh_tipo")
        self.lh_tipo.setGeometry(QRect(170, 370, 251, 50))
        self.gridLayout_144 = QGridLayout(self.lh_tipo)
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.btn_esquimose = QRadioButton(self.lh_tipo)
        self.btn_esquimose.setObjectName(u"btn_esquimose")

        self.gridLayout_144.addWidget(self.btn_esquimose, 0, 1, 1, 1)

        self.btn_petequias = QRadioButton(self.lh_tipo)
        self.btn_petequias.setObjectName(u"btn_petequias")

        self.gridLayout_144.addWidget(self.btn_petequias, 0, 0, 1, 1)

        self.btn_hematoma = QRadioButton(self.lh_tipo)
        self.btn_hematoma.setObjectName(u"btn_hematoma")

        self.gridLayout_144.addWidget(self.btn_hematoma, 0, 2, 1, 1)

        self.label_227 = QLabel(self.groupLesoes_13)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setGeometry(QRect(20, 320, 81, 16))
        self.label_228 = QLabel(self.groupLesoes_13)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setGeometry(QRect(20, 200, 71, 16))
        self.m_quantidade = QSpinBox(self.groupLesoes_13)
        self.m_quantidade.setObjectName(u"m_quantidade")
        self.m_quantidade.setGeometry(QRect(170, 236, 42, 22))
        self.lv_distribuicao = QGroupBox(self.groupLesoes_13)
        self.lv_distribuicao.setObjectName(u"lv_distribuicao")
        self.lv_distribuicao.setGeometry(QRect(940, 180, 221, 51))
        self.gridLayout_130 = QGridLayout(self.lv_distribuicao)
        self.gridLayout_130.setObjectName(u"gridLayout_130")
        self.btn_circular_2 = QRadioButton(self.lv_distribuicao)
        self.btn_circular_2.setObjectName(u"btn_circular_2")

        self.gridLayout_130.addWidget(self.btn_circular_2, 0, 1, 1, 1)

        self.btn_arco_2 = QRadioButton(self.lv_distribuicao)
        self.btn_arco_2.setObjectName(u"btn_arco_2")

        self.gridLayout_130.addWidget(self.btn_arco_2, 0, 2, 1, 1)

        self.btn_linear_2 = QRadioButton(self.lv_distribuicao)
        self.btn_linear_2.setObjectName(u"btn_linear_2")

        self.gridLayout_130.addWidget(self.btn_linear_2, 0, 0, 1, 1)

        self.lv_local = QLineEdit(self.groupLesoes_13)
        self.lv_local.setObjectName(u"lv_local")
        self.lv_local.setGeometry(QRect(940, 37, 121, 31))
        self.label_229 = QLabel(self.groupLesoes_13)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setGeometry(QRect(20, 241, 91, 16))
        self.label_230 = QLabel(self.groupLesoes_13)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setGeometry(QRect(20, 350, 141, 21))
        self.label_231 = QLabel(self.groupLesoes_13)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setGeometry(QRect(770, 200, 81, 16))
        self.label_232 = QLabel(self.groupLesoes_13)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setGeometry(QRect(20, 280, 61, 16))
        self.label_233 = QLabel(self.groupLesoes_13)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setGeometry(QRect(20, 30, 91, 31))
        self.label_234 = QLabel(self.groupLesoes_13)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setGeometry(QRect(20, 110, 47, 13))
        self.label_235 = QLabel(self.groupLesoes_13)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setGeometry(QRect(20, 530, 91, 16))
        self.lh_local = QLineEdit(self.groupLesoes_13)
        self.lh_local.setObjectName(u"lh_local")
        self.lh_local.setGeometry(QRect(170, 430, 121, 31))
        self.label_236 = QLabel(self.groupLesoes_13)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setGeometry(QRect(20, 620, 47, 21))
        self.lh_quantidade = QSpinBox(self.groupLesoes_13)
        self.lh_quantidade.setObjectName(u"lh_quantidade")
        self.lh_quantidade.setGeometry(QRect(170, 530, 42, 22))
        self.label_237 = QLabel(self.groupLesoes_13)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setGeometry(QRect(20, 390, 47, 21))
        self.label_238 = QLabel(self.groupLesoes_13)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setGeometry(QRect(770, 245, 161, 21))
        self.label_239 = QLabel(self.groupLesoes_13)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setGeometry(QRect(20, 160, 47, 13))
        self.label_240 = QLabel(self.groupLesoes_13)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setGeometry(QRect(770, 320, 47, 13))
        self.lv_tamanho = QGroupBox(self.groupLesoes_13)
        self.lv_tamanho.setObjectName(u"lv_tamanho")
        self.lv_tamanho.setGeometry(QRect(940, 60, 92, 50))
        self.gridLayout_134 = QGridLayout(self.lv_tamanho)
        self.gridLayout_134.setObjectName(u"gridLayout_134")
        self.btn_p_3 = QRadioButton(self.lv_tamanho)
        self.btn_p_3.setObjectName(u"btn_p_3")

        self.gridLayout_134.addWidget(self.btn_p_3, 0, 0, 1, 1)

        self.btn_m_3 = QRadioButton(self.lv_tamanho)
        self.btn_m_3.setObjectName(u"btn_m_3")

        self.gridLayout_134.addWidget(self.btn_m_3, 0, 1, 1, 1)

        self.btn_g_3 = QRadioButton(self.lv_tamanho)
        self.btn_g_3.setObjectName(u"btn_g_3")

        self.gridLayout_134.addWidget(self.btn_g_3, 0, 2, 1, 1)

        self.lh_tamanho = QGroupBox(self.groupLesoes_13)
        self.lh_tamanho.setObjectName(u"lh_tamanho")
        self.lh_tamanho.setGeometry(QRect(170, 460, 92, 50))
        self.gridLayout_137 = QGridLayout(self.lh_tamanho)
        self.gridLayout_137.setObjectName(u"gridLayout_137")
        self.btn_p_2 = QRadioButton(self.lh_tamanho)
        self.btn_p_2.setObjectName(u"btn_p_2")

        self.gridLayout_137.addWidget(self.btn_p_2, 0, 0, 1, 1)

        self.btn_m_2 = QRadioButton(self.lh_tamanho)
        self.btn_m_2.setObjectName(u"btn_m_2")

        self.gridLayout_137.addWidget(self.btn_m_2, 0, 1, 1, 1)

        self.btn_g_2 = QRadioButton(self.lh_tamanho)
        self.btn_g_2.setObjectName(u"btn_g_2")

        self.gridLayout_137.addWidget(self.btn_g_2, 0, 2, 1, 1)

        self.sc_tipo = QGroupBox(self.groupLesoes_13)
        self.sc_tipo.setObjectName(u"sc_tipo")
        self.sc_tipo.setGeometry(QRect(940, 260, 271, 50))
        self.gridLayout_128 = QGridLayout(self.sc_tipo)
        self.gridLayout_128.setObjectName(u"gridLayout_128")
        self.btn_escoriacoes = QRadioButton(self.sc_tipo)
        self.btn_escoriacoes.setObjectName(u"btn_escoriacoes")

        self.gridLayout_128.addWidget(self.btn_escoriacoes, 0, 0, 1, 1)

        self.btn_fissura = QRadioButton(self.sc_tipo)
        self.btn_fissura.setObjectName(u"btn_fissura")

        self.gridLayout_128.addWidget(self.btn_fissura, 0, 2, 1, 1)

        self.btn_fistula = QRadioButton(self.sc_tipo)
        self.btn_fistula.setObjectName(u"btn_fistula")

        self.gridLayout_128.addWidget(self.btn_fistula, 0, 3, 1, 1)

        self.btn_ulceras = QRadioButton(self.sc_tipo)
        self.btn_ulceras.setObjectName(u"btn_ulceras")

        self.gridLayout_128.addWidget(self.btn_ulceras, 0, 1, 1, 1)

        self.label_241 = QLabel(self.groupLesoes_13)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setGeometry(QRect(770, 160, 61, 16))
        self.label_242 = QLabel(self.groupLesoes_13)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setGeometry(QRect(770, 40, 47, 13))
        self.m_formato = QGroupBox(self.groupLesoes_13)
        self.m_formato.setObjectName(u"m_formato")
        self.m_formato.setGeometry(QRect(170, 250, 144, 50))
        self.gridLayout_133 = QGridLayout(self.m_formato)
        self.gridLayout_133.setObjectName(u"gridLayout_133")
        self.btn_regular = QRadioButton(self.m_formato)
        self.btn_regular.setObjectName(u"btn_regular")

        self.gridLayout_133.addWidget(self.btn_regular, 0, 0, 1, 1)

        self.btn_irregular = QRadioButton(self.m_formato)
        self.btn_irregular.setObjectName(u"btn_irregular")

        self.gridLayout_133.addWidget(self.btn_irregular, 0, 1, 1, 1)

        self.label_243 = QLabel(self.groupLesoes_13)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setGeometry(QRect(20, 70, 61, 16))
        self.label_244 = QLabel(self.groupLesoes_13)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setGeometry(QRect(20, 570, 121, 16))
        self.lesoes_vasculares = QGroupBox(self.groupLesoes_13)
        self.lesoes_vasculares.setObjectName(u"lesoes_vasculares")
        self.lesoes_vasculares.setGeometry(QRect(170, 550, 94, 50))
        self.gridLayout_136 = QGridLayout(self.lesoes_vasculares)
        self.gridLayout_136.setObjectName(u"gridLayout_136")
        self.btn_sim_4 = QRadioButton(self.lesoes_vasculares)
        self.btn_sim_4.setObjectName(u"btn_sim_4")

        self.gridLayout_136.addWidget(self.btn_sim_4, 0, 0, 1, 1)

        self.btn_nao_4 = QRadioButton(self.lesoes_vasculares)
        self.btn_nao_4.setObjectName(u"btn_nao_4")

        self.gridLayout_136.addWidget(self.btn_nao_4, 0, 1, 1, 1)

        self.label_264 = QLabel(self.groupLesoes_13)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setGeometry(QRect(20, 480, 71, 16))
        self.lv_quantidade = QSpinBox(self.groupLesoes_13)
        self.lv_quantidade.setObjectName(u"lv_quantidade")
        self.lv_quantidade.setGeometry(QRect(940, 120, 42, 22))
        self.m_tamanho = QGroupBox(self.groupLesoes_13)
        self.m_tamanho.setObjectName(u"m_tamanho")
        self.m_tamanho.setGeometry(QRect(170, 180, 92, 50))
        self.gridLayout_132 = QGridLayout(self.m_tamanho)
        self.gridLayout_132.setObjectName(u"gridLayout_132")
        self.btn_p = QRadioButton(self.m_tamanho)
        self.btn_p.setObjectName(u"btn_p")

        self.gridLayout_132.addWidget(self.btn_p, 0, 0, 1, 1)

        self.btn_m = QRadioButton(self.m_tamanho)
        self.btn_m.setObjectName(u"btn_m")

        self.gridLayout_132.addWidget(self.btn_m, 0, 1, 1, 1)

        self.btn_g = QRadioButton(self.m_tamanho)
        self.btn_g.setObjectName(u"btn_g")

        self.gridLayout_132.addWidget(self.btn_g, 0, 2, 1, 1)

        self.tipo_das_manchas = QGroupBox(self.groupLesoes_13)
        self.tipo_das_manchas.setObjectName(u"tipo_das_manchas")
        self.tipo_das_manchas.setGeometry(QRect(170, 100, 194, 50))
        self.gridLayout_127 = QGridLayout(self.tipo_das_manchas)
        self.gridLayout_127.setObjectName(u"gridLayout_127")
        self.btn_hipo = QRadioButton(self.tipo_das_manchas)
        self.btn_hipo.setObjectName(u"btn_hipo")

        self.gridLayout_127.addWidget(self.btn_hipo, 0, 0, 1, 1)

        self.btn_hiper = QRadioButton(self.tipo_das_manchas)
        self.btn_hiper.setObjectName(u"btn_hiper")

        self.gridLayout_127.addWidget(self.btn_hiper, 0, 1, 1, 1)

        self.manchas = QGroupBox(self.groupLesoes_13)
        self.manchas.setObjectName(u"manchas")
        self.manchas.setGeometry(QRect(170, 60, 111, 46))
        self.manchas.setStyleSheet(u"")
        self.gridLayout_126 = QGridLayout(self.manchas)
        self.gridLayout_126.setObjectName(u"gridLayout_126")
        self.btn_sim_2 = QRadioButton(self.manchas)
        self.btn_sim_2.setObjectName(u"btn_sim_2")

        self.gridLayout_126.addWidget(self.btn_sim_2, 0, 0, 1, 1)

        self.btn_nao_2 = QRadioButton(self.manchas)
        self.btn_nao_2.setObjectName(u"btn_nao_2")

        self.gridLayout_126.addWidget(self.btn_nao_2, 0, 1, 1, 1)

        self.solucoes_de_continuidade = QGroupBox(self.groupLesoes_13)
        self.solucoes_de_continuidade.setObjectName(u"solucoes_de_continuidade")
        self.solucoes_de_continuidade.setGeometry(QRect(940, 220, 158, 50))
        self.gridLayout_129 = QGridLayout(self.solucoes_de_continuidade)
        self.gridLayout_129.setObjectName(u"gridLayout_129")
        self.btn_presentes = QRadioButton(self.solucoes_de_continuidade)
        self.btn_presentes.setObjectName(u"btn_presentes")

        self.gridLayout_129.addWidget(self.btn_presentes, 0, 0, 1, 1)

        self.btn_ausentes = QRadioButton(self.solucoes_de_continuidade)
        self.btn_ausentes.setObjectName(u"btn_ausentes")

        self.gridLayout_129.addWidget(self.btn_ausentes, 0, 1, 1, 1)

        self.sc_local = QLineEdit(self.groupLesoes_13)
        self.sc_local.setObjectName(u"sc_local")
        self.sc_local.setGeometry(QRect(940, 316, 121, 31))
        self.local_das_manchas = QLineEdit(self.groupLesoes_13)
        self.local_das_manchas.setObjectName(u"local_das_manchas")
        self.local_das_manchas.setGeometry(QRect(170, 156, 121, 31))
        self.lesoes_planas = QGroupBox(self.groupLesoes_13)
        self.lesoes_planas.setObjectName(u"lesoes_planas")
        self.lesoes_planas.setGeometry(QRect(170, 10, 106, 51))
        self.lesoes_planas.setStyleSheet(u"")
        self.gridLayout_288 = QGridLayout(self.lesoes_planas)
        self.gridLayout_288.setObjectName(u"gridLayout_288")
        self.btn_sim = QRadioButton(self.lesoes_planas)
        self.btn_sim.setObjectName(u"btn_sim")

        self.gridLayout_288.addWidget(self.btn_sim, 0, 0, 1, 1)

        self.btn_nao = QRadioButton(self.lesoes_planas)
        self.btn_nao.setObjectName(u"btn_nao")

        self.gridLayout_288.addWidget(self.btn_nao, 0, 1, 1, 1)

        self.lv_formato = QGroupBox(self.groupLesoes_13)
        self.lv_formato.setObjectName(u"lv_formato")
        self.lv_formato.setGeometry(QRect(940, 140, 144, 50))
        self.gridLayout_131 = QGridLayout(self.lv_formato)
        self.gridLayout_131.setObjectName(u"gridLayout_131")
        self.btn_regular_3 = QRadioButton(self.lv_formato)
        self.btn_regular_3.setObjectName(u"btn_regular_3")

        self.gridLayout_131.addWidget(self.btn_regular_3, 0, 0, 1, 1)

        self.btn_irregular_2 = QRadioButton(self.lv_formato)
        self.btn_irregular_2.setObjectName(u"btn_irregular_2")

        self.gridLayout_131.addWidget(self.btn_irregular_2, 0, 1, 1, 1)

        self.label_265 = QLabel(self.groupLesoes_13)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setGeometry(QRect(770, 280, 31, 16))
        self.label_266 = QLabel(self.groupLesoes_13)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setGeometry(QRect(770, 120, 81, 16))
        self.label_267 = QLabel(self.groupLesoes_13)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setGeometry(QRect(20, 440, 47, 13))
        self.lv_tipo = QGroupBox(self.groupLesoes_13)
        self.lv_tipo.setObjectName(u"lv_tipo")
        self.lv_tipo.setGeometry(QRect(170, 600, 190, 50))
        self.gridLayout_135 = QGridLayout(self.lv_tipo)
        self.gridLayout_135.setObjectName(u"gridLayout_135")
        self.btn_telangectasia = QRadioButton(self.lv_tipo)
        self.btn_telangectasia.setObjectName(u"btn_telangectasia")

        self.gridLayout_135.addWidget(self.btn_telangectasia, 0, 0, 1, 1)

        self.btn_eritmatosa = QRadioButton(self.lv_tipo)
        self.btn_eritmatosa.setObjectName(u"btn_eritmatosa")

        self.gridLayout_135.addWidget(self.btn_eritmatosa, 0, 1, 1, 1)

        self.label_270 = QLabel(self.groupLesoes_13)
        self.label_270.setObjectName(u"label_270")
        self.label_270.setGeometry(QRect(770, 360, 71, 16))
        self.sc_tamanho = QGroupBox(self.groupLesoes_13)
        self.sc_tamanho.setObjectName(u"sc_tamanho")
        self.sc_tamanho.setGeometry(QRect(940, 340, 92, 50))
        self.gridLayout_150 = QGridLayout(self.sc_tamanho)
        self.gridLayout_150.setObjectName(u"gridLayout_150")
        self.btn_p_4 = QRadioButton(self.sc_tamanho)
        self.btn_p_4.setObjectName(u"btn_p_4")

        self.gridLayout_150.addWidget(self.btn_p_4, 0, 0, 1, 1)

        self.btn_m_4 = QRadioButton(self.sc_tamanho)
        self.btn_m_4.setObjectName(u"btn_m_4")

        self.gridLayout_150.addWidget(self.btn_m_4, 0, 1, 1, 1)

        self.btn_g_4 = QRadioButton(self.sc_tamanho)
        self.btn_g_4.setObjectName(u"btn_g_4")

        self.gridLayout_150.addWidget(self.btn_g_4, 0, 2, 1, 1)

        self.label_273 = QLabel(self.groupLesoes_13)
        self.label_273.setObjectName(u"label_273")
        self.label_273.setGeometry(QRect(770, 510, 47, 21))
        self.sc_contorno = QLineEdit(self.groupLesoes_13)
        self.sc_contorno.setObjectName(u"sc_contorno")
        self.sc_contorno.setGeometry(QRect(940, 437, 121, 31))
        self.label_277 = QLabel(self.groupLesoes_13)
        self.label_277.setObjectName(u"label_277")
        self.label_277.setGeometry(QRect(771, 480, 61, 21))
        self.sc_odor = QGroupBox(self.groupLesoes_13)
        self.sc_odor.setObjectName(u"sc_odor")
        self.sc_odor.setGeometry(QRect(940, 380, 94, 50))
        self.gridLayout_151 = QGridLayout(self.sc_odor)
        self.gridLayout_151.setObjectName(u"gridLayout_151")
        self.btn_nao_5 = QRadioButton(self.sc_odor)
        self.btn_nao_5.setObjectName(u"btn_nao_5")

        self.gridLayout_151.addWidget(self.btn_nao_5, 0, 1, 1, 1)

        self.btn_sim_5 = QRadioButton(self.sc_odor)
        self.btn_sim_5.setObjectName(u"btn_sim_5")

        self.gridLayout_151.addWidget(self.btn_sim_5, 0, 0, 1, 1)

        self.label_279 = QLabel(self.groupLesoes_13)
        self.label_279.setObjectName(u"label_279")
        self.label_279.setGeometry(QRect(770, 400, 47, 13))
        self.label_281 = QLabel(self.groupLesoes_13)
        self.label_281.setObjectName(u"label_281")
        self.label_281.setGeometry(QRect(770, 440, 121, 16))
        self.sc_secrecao_tipo = QLineEdit(self.groupLesoes_13)
        self.sc_secrecao_tipo.setObjectName(u"sc_secrecao_tipo")
        self.sc_secrecao_tipo.setGeometry(QRect(940, 520, 121, 31))
        self.sc_secrecao = QGroupBox(self.groupLesoes_13)
        self.sc_secrecao.setObjectName(u"sc_secrecao")
        self.sc_secrecao.setGeometry(QRect(940, 460, 94, 51))
        self.gridLayout_153 = QGridLayout(self.sc_secrecao)
        self.gridLayout_153.setObjectName(u"gridLayout_153")
        self.btn_sim_25 = QRadioButton(self.sc_secrecao)
        self.btn_sim_25.setObjectName(u"btn_sim_25")

        self.gridLayout_153.addWidget(self.btn_sim_25, 0, 0, 1, 1)

        self.btn_nao_25 = QRadioButton(self.sc_secrecao)
        self.btn_nao_25.setObjectName(u"btn_nao_25")

        self.gridLayout_153.addWidget(self.btn_nao_25, 0, 1, 1, 1)


        self.gridLayout_410.addWidget(self.groupLesoes_13, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_141 = QGridLayout(self.tab)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.groupLesoes_30 = QGroupBox(self.tab)
        self.groupLesoes_30.setObjectName(u"groupLesoes_30")
        self.groupLesoes_30.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"         border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.le_tipo = QGroupBox(self.groupLesoes_30)
        self.le_tipo.setObjectName(u"le_tipo")
        self.le_tipo.setGeometry(QRect(163, 54, 131, 51))
        self.gridLayout_154 = QGridLayout(self.le_tipo)
        self.gridLayout_154.setObjectName(u"gridLayout_154")
        self.btn_escama = QRadioButton(self.le_tipo)
        self.btn_escama.setObjectName(u"btn_escama")

        self.gridLayout_154.addWidget(self.btn_escama, 0, 0, 1, 1)

        self.btn_crosta = QRadioButton(self.le_tipo)
        self.btn_crosta.setObjectName(u"btn_crosta")

        self.gridLayout_154.addWidget(self.btn_crosta, 0, 1, 1, 1)

        self.label_125 = QLabel(self.groupLesoes_30)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(30, 251, 71, 16))
        self.label_126 = QLabel(self.groupLesoes_30)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(30, 289, 47, 13))
        self.le_prurido = QGroupBox(self.groupLesoes_30)
        self.le_prurido.setObjectName(u"le_prurido")
        self.le_prurido.setGeometry(QRect(160, 152, 94, 50))
        self.gridLayout_149 = QGridLayout(self.le_prurido)
        self.gridLayout_149.setObjectName(u"gridLayout_149")
        self.btn_sim_13 = QRadioButton(self.le_prurido)
        self.btn_sim_13.setObjectName(u"btn_sim_13")

        self.gridLayout_149.addWidget(self.btn_sim_13, 0, 0, 1, 1)

        self.btn_nao_13 = QRadioButton(self.le_prurido)
        self.btn_nao_13.setObjectName(u"btn_nao_13")

        self.gridLayout_149.addWidget(self.btn_nao_13, 0, 1, 1, 1)

        self.lesoes_escamativas = QGroupBox(self.groupLesoes_30)
        self.lesoes_escamativas.setObjectName(u"lesoes_escamativas")
        self.lesoes_escamativas.setGeometry(QRect(163, 15, 158, 50))
        self.gridLayout_147 = QGridLayout(self.lesoes_escamativas)
        self.gridLayout_147.setObjectName(u"gridLayout_147")
        self.btn_presentes_2 = QRadioButton(self.lesoes_escamativas)
        self.btn_presentes_2.setObjectName(u"btn_presentes_2")

        self.gridLayout_147.addWidget(self.btn_presentes_2, 0, 0, 1, 1)

        self.btn_ausentes_2 = QRadioButton(self.lesoes_escamativas)
        self.btn_ausentes_2.setObjectName(u"btn_ausentes_2")

        self.gridLayout_147.addWidget(self.btn_ausentes_2, 0, 1, 1, 1)

        self.label_127 = QLabel(self.groupLesoes_30)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(30, 177, 47, 13))
        self.le_cicatriz = QGroupBox(self.groupLesoes_30)
        self.le_cicatriz.setObjectName(u"le_cicatriz")
        self.le_cicatriz.setGeometry(QRect(160, 265, 281, 50))
        self.gridLayout_145 = QGridLayout(self.le_cicatriz)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.btn_sim_14 = QRadioButton(self.le_cicatriz)
        self.btn_sim_14.setObjectName(u"btn_sim_14")

        self.gridLayout_145.addWidget(self.btn_sim_14, 0, 0, 1, 1)

        self.btn_nao_14 = QRadioButton(self.le_cicatriz)
        self.btn_nao_14.setObjectName(u"btn_nao_14")

        self.gridLayout_145.addWidget(self.btn_nao_14, 0, 1, 1, 1)

        self.btn_remanescente = QRadioButton(self.le_cicatriz)
        self.btn_remanescente.setObjectName(u"btn_remanescente")

        self.gridLayout_145.addWidget(self.btn_remanescente, 0, 2, 1, 1)

        self.btn_recentes = QRadioButton(self.le_cicatriz)
        self.btn_recentes.setObjectName(u"btn_recentes")

        self.gridLayout_145.addWidget(self.btn_recentes, 0, 3, 1, 1)

        self.le_c_outras = QLineEdit(self.groupLesoes_30)
        self.le_c_outras.setObjectName(u"le_c_outras")
        self.le_c_outras.setGeometry(QRect(160, 350, 121, 31))
        self.le_quantidade = QSpinBox(self.groupLesoes_30)
        self.le_quantidade.setObjectName(u"le_quantidade")
        self.le_quantidade.setGeometry(QRect(165, 140, 42, 22))
        self.le_atrofia = QGroupBox(self.groupLesoes_30)
        self.le_atrofia.setObjectName(u"le_atrofia")
        self.le_atrofia.setGeometry(QRect(160, 192, 101, 50))
        self.gridLayout_146 = QGridLayout(self.le_atrofia)
        self.gridLayout_146.setObjectName(u"gridLayout_146")
        self.btn_sim_15 = QRadioButton(self.le_atrofia)
        self.btn_sim_15.setObjectName(u"btn_sim_15")

        self.gridLayout_146.addWidget(self.btn_sim_15, 0, 0, 1, 1)

        self.btn_nao_15 = QRadioButton(self.le_atrofia)
        self.btn_nao_15.setObjectName(u"btn_nao_15")

        self.gridLayout_146.addWidget(self.btn_nao_15, 0, 1, 1, 1)

        self.label_128 = QLabel(self.groupLesoes_30)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(30, 145, 81, 16))
        self.label_129 = QLabel(self.groupLesoes_30)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(30, 77, 47, 13))
        self.le_c_local = QLineEdit(self.groupLesoes_30)
        self.le_c_local.setObjectName(u"le_c_local")
        self.le_c_local.setGeometry(QRect(160, 317, 121, 31))
        self.label_130 = QLabel(self.groupLesoes_30)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(30, 215, 47, 13))
        self.label_131 = QLabel(self.groupLesoes_30)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(30, 325, 47, 13))
        self.label_132 = QLabel(self.groupLesoes_30)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(30, 112, 47, 13))
        self.label_133 = QLabel(self.groupLesoes_30)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(30, 40, 131, 16))
        self.label_134 = QLabel(self.groupLesoes_30)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(30, 358, 47, 13))
        self.le_especificar = QLineEdit(self.groupLesoes_30)
        self.le_especificar.setObjectName(u"le_especificar")
        self.le_especificar.setGeometry(QRect(160, 244, 121, 31))
        self.ls_contorno = QGroupBox(self.groupLesoes_30)
        self.ls_contorno.setObjectName(u"ls_contorno")
        self.ls_contorno.setGeometry(QRect(814, 10, 200, 50))
        self.gridLayout_163 = QGridLayout(self.ls_contorno)
        self.gridLayout_163.setObjectName(u"gridLayout_163")
        self.btn_plano = QRadioButton(self.ls_contorno)
        self.btn_plano.setObjectName(u"btn_plano")

        self.gridLayout_163.addWidget(self.btn_plano, 0, 0, 1, 1)

        self.btn_elevado = QRadioButton(self.ls_contorno)
        self.btn_elevado.setObjectName(u"btn_elevado")

        self.gridLayout_163.addWidget(self.btn_elevado, 0, 1, 1, 1)

        self.btn_deprimido = QRadioButton(self.ls_contorno)
        self.btn_deprimido.setObjectName(u"btn_deprimido")

        self.gridLayout_163.addWidget(self.btn_deprimido, 0, 2, 1, 1)

        self.label_187 = QLabel(self.groupLesoes_30)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(680, 120, 47, 13))
        self.ls_tipos = QGroupBox(self.groupLesoes_30)
        self.ls_tipos.setObjectName(u"ls_tipos")
        self.ls_tipos.setGeometry(QRect(160, 410, 365, 50))
        self.gridLayout_160 = QGridLayout(self.ls_tipos)
        self.gridLayout_160.setObjectName(u"gridLayout_160")
        self.btn_papula = QRadioButton(self.ls_tipos)
        self.btn_papula.setObjectName(u"btn_papula")

        self.gridLayout_160.addWidget(self.btn_papula, 0, 0, 1, 1)

        self.btn_nodulo = QRadioButton(self.ls_tipos)
        self.btn_nodulo.setObjectName(u"btn_nodulo")

        self.gridLayout_160.addWidget(self.btn_nodulo, 0, 1, 1, 1)

        self.btn_urticaria = QRadioButton(self.ls_tipos)
        self.btn_urticaria.setObjectName(u"btn_urticaria")

        self.gridLayout_160.addWidget(self.btn_urticaria, 0, 2, 1, 1)

        self.btn_espessamento = QRadioButton(self.ls_tipos)
        self.btn_espessamento.setObjectName(u"btn_espessamento")

        self.gridLayout_160.addWidget(self.btn_espessamento, 0, 3, 1, 1)

        self.btn_tuberculo = QRadioButton(self.ls_tipos)
        self.btn_tuberculo.setObjectName(u"btn_tuberculo")

        self.gridLayout_160.addWidget(self.btn_tuberculo, 0, 4, 1, 1)

        self.ls_distribuicao = QGroupBox(self.groupLesoes_30)
        self.ls_distribuicao.setObjectName(u"ls_distribuicao")
        self.ls_distribuicao.setGeometry(QRect(816, 50, 193, 50))
        self.gridLayout_164 = QGridLayout(self.ls_distribuicao)
        self.gridLayout_164.setObjectName(u"gridLayout_164")
        self.btn_linear_3 = QRadioButton(self.ls_distribuicao)
        self.btn_linear_3.setObjectName(u"btn_linear_3")

        self.gridLayout_164.addWidget(self.btn_linear_3, 0, 0, 1, 1)

        self.btn_circular_3 = QRadioButton(self.ls_distribuicao)
        self.btn_circular_3.setObjectName(u"btn_circular_3")

        self.gridLayout_164.addWidget(self.btn_circular_3, 0, 1, 1, 1)

        self.btn_arco_3 = QRadioButton(self.ls_distribuicao)
        self.btn_arco_3.setObjectName(u"btn_arco_3")

        self.gridLayout_164.addWidget(self.btn_arco_3, 0, 2, 1, 1)

        self.label_188 = QLabel(self.groupLesoes_30)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(680, 396, 81, 16))
        self.label_189 = QLabel(self.groupLesoes_30)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(680, 70, 81, 16))
        self.lcl_secrecao = QGroupBox(self.groupLesoes_30)
        self.lcl_secrecao.setObjectName(u"lcl_secrecao")
        self.lcl_secrecao.setGeometry(QRect(828, 457, 94, 50))
        self.gridLayout_172 = QGridLayout(self.lcl_secrecao)
        self.gridLayout_172.setObjectName(u"gridLayout_172")
        self.btn_sim_16 = QRadioButton(self.lcl_secrecao)
        self.btn_sim_16.setObjectName(u"btn_sim_16")

        self.gridLayout_172.addWidget(self.btn_sim_16, 0, 0, 1, 1)

        self.btn_nao_16 = QRadioButton(self.lcl_secrecao)
        self.btn_nao_16.setObjectName(u"btn_nao_16")

        self.gridLayout_172.addWidget(self.btn_nao_16, 0, 1, 1, 1)

        self.lcl_local = QLineEdit(self.groupLesoes_30)
        self.lcl_local.setObjectName(u"lcl_local")
        self.lcl_local.setGeometry(QRect(823, 225, 121, 31))
        self.label_190 = QLabel(self.groupLesoes_30)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(680, 325, 61, 16))
        self.label_191 = QLabel(self.groupLesoes_30)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(680, 30, 71, 20))
        self.lcl_formato = QGroupBox(self.groupLesoes_30)
        self.lcl_formato.setObjectName(u"lcl_formato")
        self.lcl_formato.setGeometry(QRect(823, 303, 144, 50))
        self.gridLayout_169 = QGridLayout(self.lcl_formato)
        self.gridLayout_169.setObjectName(u"gridLayout_169")
        self.btn_regular_4 = QRadioButton(self.lcl_formato)
        self.btn_regular_4.setObjectName(u"btn_regular_4")

        self.gridLayout_169.addWidget(self.btn_regular_4, 0, 0, 1, 1)

        self.btn_irregular_4 = QRadioButton(self.lcl_formato)
        self.btn_irregular_4.setObjectName(u"btn_irregular_4")

        self.gridLayout_169.addWidget(self.btn_irregular_4, 0, 1, 1, 1)

        self.label_192 = QLabel(self.groupLesoes_30)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(680, 476, 61, 16))
        self.lesoes_com_conteudo_liquido = QGroupBox(self.groupLesoes_30)
        self.lesoes_com_conteudo_liquido.setObjectName(u"lesoes_com_conteudo_liquido")
        self.lesoes_com_conteudo_liquido.setGeometry(QRect(818, 130, 94, 50))
        self.gridLayout_166 = QGridLayout(self.lesoes_com_conteudo_liquido)
        self.gridLayout_166.setObjectName(u"gridLayout_166")
        self.btn_sim_17 = QRadioButton(self.lesoes_com_conteudo_liquido)
        self.btn_sim_17.setObjectName(u"btn_sim_17")

        self.gridLayout_166.addWidget(self.btn_sim_17, 0, 0, 1, 1)

        self.btn_nao_17 = QRadioButton(self.lesoes_com_conteudo_liquido)
        self.btn_nao_17.setObjectName(u"btn_nao_17")

        self.gridLayout_166.addWidget(self.btn_nao_17, 0, 1, 1, 1)

        self.label_193 = QLabel(self.groupLesoes_30)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(30, 394, 91, 16))
        self.label_194 = QLabel(self.groupLesoes_30)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(680, 190, 47, 21))
        self.label_195 = QLabel(self.groupLesoes_30)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(30, 470, 47, 13))
        self.ls_local = QLineEdit(self.groupLesoes_30)
        self.ls_local.setObjectName(u"ls_local")
        self.ls_local.setGeometry(QRect(160, 462, 121, 31))
        self.lcl_tamanho = QGroupBox(self.groupLesoes_30)
        self.lcl_tamanho.setObjectName(u"lcl_tamanho")
        self.lcl_tamanho.setGeometry(QRect(820, 250, 92, 51))
        self.gridLayout_168 = QGridLayout(self.lcl_tamanho)
        self.gridLayout_168.setObjectName(u"gridLayout_168")
        self.btn_p_6 = QRadioButton(self.lcl_tamanho)
        self.btn_p_6.setObjectName(u"btn_p_6")

        self.gridLayout_168.addWidget(self.btn_p_6, 0, 0, 1, 1)

        self.btn_m_6 = QRadioButton(self.lcl_tamanho)
        self.btn_m_6.setObjectName(u"btn_m_6")

        self.gridLayout_168.addWidget(self.btn_m_6, 0, 1, 1, 1)

        self.btn_g_6 = QRadioButton(self.lcl_tamanho)
        self.btn_g_6.setObjectName(u"btn_g_6")

        self.gridLayout_168.addWidget(self.btn_g_6, 0, 2, 1, 1)

        self.lcl_secrecao_tipo = QLineEdit(self.groupLesoes_30)
        self.lcl_secrecao_tipo.setObjectName(u"lcl_secrecao_tipo")
        self.lcl_secrecao_tipo.setGeometry(QRect(830, 510, 121, 31))
        self.label_196 = QLabel(self.groupLesoes_30)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(680, 235, 47, 13))
        self.label_197 = QLabel(self.groupLesoes_30)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(31, 575, 61, 16))
        self.label_198 = QLabel(self.groupLesoes_30)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(680, 360, 71, 16))
        self.label_245 = QLabel(self.groupLesoes_30)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setGeometry(QRect(680, 150, 131, 16))
        self.label_246 = QLabel(self.groupLesoes_30)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setGeometry(QRect(680, 510, 47, 21))
        self.lesoes_solidas = QGroupBox(self.groupLesoes_30)
        self.lesoes_solidas.setObjectName(u"lesoes_solidas")
        self.lesoes_solidas.setGeometry(QRect(160, 371, 94, 50))
        self.gridLayout_155 = QGridLayout(self.lesoes_solidas)
        self.gridLayout_155.setObjectName(u"gridLayout_155")
        self.btn_sim_18 = QRadioButton(self.lesoes_solidas)
        self.btn_sim_18.setObjectName(u"btn_sim_18")

        self.gridLayout_155.addWidget(self.btn_sim_18, 0, 0, 1, 1)

        self.btn_nao_18 = QRadioButton(self.lesoes_solidas)
        self.btn_nao_18.setObjectName(u"btn_nao_18")

        self.gridLayout_155.addWidget(self.btn_nao_18, 0, 1, 1, 1)

        self.ls_quantidade = QSpinBox(self.groupLesoes_30)
        self.ls_quantidade.setObjectName(u"ls_quantidade")
        self.ls_quantidade.setGeometry(QRect(164, 540, 42, 22))
        self.label_247 = QLabel(self.groupLesoes_30)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setGeometry(QRect(30, 428, 47, 21))
        self.lcl_distribuicao = QGroupBox(self.groupLesoes_30)
        self.lcl_distribuicao.setObjectName(u"lcl_distribuicao")
        self.lcl_distribuicao.setGeometry(QRect(826, 376, 193, 50))
        self.gridLayout_170 = QGridLayout(self.lcl_distribuicao)
        self.gridLayout_170.setObjectName(u"gridLayout_170")
        self.btn_linear_4 = QRadioButton(self.lcl_distribuicao)
        self.btn_linear_4.setObjectName(u"btn_linear_4")

        self.gridLayout_170.addWidget(self.btn_linear_4, 0, 0, 1, 1)

        self.btn_circular_4 = QRadioButton(self.lcl_distribuicao)
        self.btn_circular_4.setObjectName(u"btn_circular_4")

        self.gridLayout_170.addWidget(self.btn_circular_4, 0, 1, 1, 1)

        self.btn_arco_4 = QRadioButton(self.lcl_distribuicao)
        self.btn_arco_4.setObjectName(u"btn_arco_4")

        self.gridLayout_170.addWidget(self.btn_arco_4, 0, 2, 1, 1)

        self.label_248 = QLabel(self.groupLesoes_30)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setGeometry(QRect(30, 541, 81, 16))
        self.lcl_quantidade = QSpinBox(self.groupLesoes_30)
        self.lcl_quantidade.setObjectName(u"lcl_quantidade")
        self.lcl_quantidade.setGeometry(QRect(827, 360, 42, 22))
        self.ls_tamanho = QGroupBox(self.groupLesoes_30)
        self.ls_tamanho.setObjectName(u"ls_tamanho")
        self.ls_tamanho.setGeometry(QRect(160, 483, 92, 51))
        self.gridLayout_161 = QGridLayout(self.ls_tamanho)
        self.gridLayout_161.setObjectName(u"gridLayout_161")
        self.btn_p_5 = QRadioButton(self.ls_tamanho)
        self.btn_p_5.setObjectName(u"btn_p_5")

        self.gridLayout_161.addWidget(self.btn_p_5, 0, 0, 1, 1)

        self.btn_m_5 = QRadioButton(self.ls_tamanho)
        self.btn_m_5.setObjectName(u"btn_m_5")

        self.gridLayout_161.addWidget(self.btn_m_5, 0, 1, 1, 1)

        self.btn_g_5 = QRadioButton(self.ls_tamanho)
        self.btn_g_5.setObjectName(u"btn_g_5")

        self.gridLayout_161.addWidget(self.btn_g_5, 0, 2, 1, 1)

        self.label_249 = QLabel(self.groupLesoes_30)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setGeometry(QRect(680, 440, 47, 13))
        self.lcl_odor = QGroupBox(self.groupLesoes_30)
        self.lcl_odor.setObjectName(u"lcl_odor")
        self.lcl_odor.setGeometry(QRect(827, 417, 94, 50))
        self.gridLayout_171 = QGridLayout(self.lcl_odor)
        self.gridLayout_171.setObjectName(u"gridLayout_171")
        self.btn_sim_19 = QRadioButton(self.lcl_odor)
        self.btn_sim_19.setObjectName(u"btn_sim_19")

        self.gridLayout_171.addWidget(self.btn_sim_19, 0, 0, 1, 1)

        self.btn_nao_19 = QRadioButton(self.lcl_odor)
        self.btn_nao_19.setObjectName(u"btn_nao_19")

        self.gridLayout_171.addWidget(self.btn_nao_19, 0, 1, 1, 1)

        self.label_250 = QLabel(self.groupLesoes_30)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setGeometry(QRect(680, 280, 61, 16))
        self.ls_odor = QGroupBox(self.groupLesoes_30)
        self.ls_odor.setObjectName(u"ls_odor")
        self.ls_odor.setGeometry(QRect(817, 90, 94, 50))
        self.gridLayout_165 = QGridLayout(self.ls_odor)
        self.gridLayout_165.setObjectName(u"gridLayout_165")
        self.btn_sim_20 = QRadioButton(self.ls_odor)
        self.btn_sim_20.setObjectName(u"btn_sim_20")

        self.gridLayout_165.addWidget(self.btn_sim_20, 0, 0, 1, 1)

        self.btn_nao_20 = QRadioButton(self.ls_odor)
        self.btn_nao_20.setObjectName(u"btn_nao_20")

        self.gridLayout_165.addWidget(self.btn_nao_20, 0, 1, 1, 1)

        self.ls_formato = QGroupBox(self.groupLesoes_30)
        self.ls_formato.setObjectName(u"ls_formato")
        self.ls_formato.setGeometry(QRect(160, 552, 144, 50))
        self.gridLayout_162 = QGridLayout(self.ls_formato)
        self.gridLayout_162.setObjectName(u"gridLayout_162")
        self.btn_regular_5 = QRadioButton(self.ls_formato)
        self.btn_regular_5.setObjectName(u"btn_regular_5")

        self.gridLayout_162.addWidget(self.btn_regular_5, 0, 0, 1, 1)

        self.btn_irregular_3 = QRadioButton(self.ls_formato)
        self.btn_irregular_3.setObjectName(u"btn_irregular_3")

        self.gridLayout_162.addWidget(self.btn_irregular_3, 0, 1, 1, 1)

        self.lcl_tipo = QGroupBox(self.groupLesoes_30)
        self.lcl_tipo.setObjectName(u"lcl_tipo")
        self.lcl_tipo.setGeometry(QRect(820, 170, 250, 51))
        self.gridLayout_167 = QGridLayout(self.lcl_tipo)
        self.gridLayout_167.setObjectName(u"gridLayout_167")
        self.btn_vesicula = QRadioButton(self.lcl_tipo)
        self.btn_vesicula.setObjectName(u"btn_vesicula")

        self.gridLayout_167.addWidget(self.btn_vesicula, 0, 0, 1, 1)

        self.btn_bolha = QRadioButton(self.lcl_tipo)
        self.btn_bolha.setObjectName(u"btn_bolha")

        self.gridLayout_167.addWidget(self.btn_bolha, 0, 1, 1, 1)

        self.btn_pustula = QRadioButton(self.lcl_tipo)
        self.btn_pustula.setObjectName(u"btn_pustula")

        self.gridLayout_167.addWidget(self.btn_pustula, 0, 2, 1, 1)

        self.btn_abcesso = QRadioButton(self.lcl_tipo)
        self.btn_abcesso.setObjectName(u"btn_abcesso")

        self.gridLayout_167.addWidget(self.btn_abcesso, 0, 3, 1, 1)

        self.label_251 = QLabel(self.groupLesoes_30)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setGeometry(QRect(30, 505, 71, 16))
        self.le_local = QLineEdit(self.groupLesoes_30)
        self.le_local.setObjectName(u"le_local")
        self.le_local.setGeometry(QRect(163, 107, 121, 31))

        self.gridLayout_141.addWidget(self.groupLesoes_30, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_191 = QGridLayout(self.tab_22)
        self.gridLayout_191.setObjectName(u"gridLayout_191")
        self.groupLesoes_31 = QGroupBox(self.tab_22)
        self.groupLesoes_31.setObjectName(u"groupLesoes_31")
        self.groupLesoes_31.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.limitacoes_im = QGroupBox(self.groupLesoes_31)
        self.limitacoes_im.setObjectName(u"limitacoes_im")
        self.limitacoes_im.setGeometry(QRect(240, 390, 129, 51))
        self.gridLayout_192 = QGridLayout(self.limitacoes_im)
        self.gridLayout_192.setObjectName(u"gridLayout_192")
        self.radioButton_182 = QRadioButton(self.limitacoes_im)
        self.radioButton_182.setObjectName(u"radioButton_182")
        self.radioButton_182.setFont(font6)

        self.gridLayout_192.addWidget(self.radioButton_182, 0, 2, 1, 1)

        self.radioButton_183 = QRadioButton(self.limitacoes_im)
        self.radioButton_183.setObjectName(u"radioButton_183")
        self.radioButton_183.setFont(font6)

        self.gridLayout_192.addWidget(self.radioButton_183, 0, 1, 1, 1)

        self.mobilidade_im = QGroupBox(self.groupLesoes_31)
        self.mobilidade_im.setObjectName(u"mobilidade_im")
        self.mobilidade_im.setGeometry(QRect(240, 150, 153, 51))
        self.mobilidade_im.setStyleSheet(u"")
        self.gridLayout_193 = QGridLayout(self.mobilidade_im)
        self.gridLayout_193.setObjectName(u"gridLayout_193")
        self.radioButton_184 = QRadioButton(self.mobilidade_im)
        self.radioButton_184.setObjectName(u"radioButton_184")
        self.radioButton_184.setFont(font6)

        self.gridLayout_193.addWidget(self.radioButton_184, 0, 0, 1, 1)

        self.radioButton_185 = QRadioButton(self.mobilidade_im)
        self.radioButton_185.setObjectName(u"radioButton_185")
        self.radioButton_185.setFont(font6)

        self.gridLayout_193.addWidget(self.radioButton_185, 0, 1, 1, 1)

        self.label_303 = QLabel(self.groupLesoes_31)
        self.label_303.setObjectName(u"label_303")
        self.label_303.setGeometry(QRect(600, 90, 201, 18))
        self.label_303.setFont(font6)
        self.label_305 = QLabel(self.groupLesoes_31)
        self.label_305.setObjectName(u"label_305")
        self.label_305.setGeometry(QRect(40, 450, 161, 18))
        self.label_305.setFont(font6)
        self.label_306 = QLabel(self.groupLesoes_31)
        self.label_306.setObjectName(u"label_306")
        self.label_306.setGeometry(QRect(40, 490, 56, 18))
        self.label_306.setFont(font6)
        self.musculatura_im = QGroupBox(self.groupLesoes_31)
        self.musculatura_im.setObjectName(u"musculatura_im")
        self.musculatura_im.setGeometry(QRect(240, 65, 279, 51))
        self.musculatura_im.setStyleSheet(u"")
        self.gridLayout_194 = QGridLayout(self.musculatura_im)
        self.gridLayout_194.setObjectName(u"gridLayout_194")
        self.radioButton_186 = QRadioButton(self.musculatura_im)
        self.radioButton_186.setObjectName(u"radioButton_186")
        self.radioButton_186.setFont(font6)

        self.gridLayout_194.addWidget(self.radioButton_186, 0, 0, 1, 1)

        self.radioButton_187 = QRadioButton(self.musculatura_im)
        self.radioButton_187.setObjectName(u"radioButton_187")
        self.radioButton_187.setFont(font6)
        self.radioButton_187.setStyleSheet(u"Border: none;")

        self.gridLayout_194.addWidget(self.radioButton_187, 0, 1, 1, 1)

        self.radioButton_188 = QRadioButton(self.musculatura_im)
        self.radioButton_188.setObjectName(u"radioButton_188")
        self.radioButton_188.setFont(font6)

        self.gridLayout_194.addWidget(self.radioButton_188, 0, 2, 1, 1)

        self.label_308 = QLabel(self.groupLesoes_31)
        self.label_308.setObjectName(u"label_308")
        self.label_308.setGeometry(QRect(40, 370, 121, 18))
        self.label_308.setFont(font6)
        self.label_14 = QLabel(self.groupLesoes_31)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 250, 101, 18))
        self.label_14.setFont(font6)
        self.groupBox = QGroupBox(self.groupLesoes_31)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(193, 20, 119, 36))
        self.groupBox.setStyleSheet(u"border: none;")
        self.deformidades_im = QGroupBox(self.groupLesoes_31)
        self.deformidades_im.setObjectName(u"deformidades_im")
        self.deformidades_im.setGeometry(QRect(240, 310, 119, 51))
        self.deformidades_im.setStyleSheet(u"")
        self.gridLayout_195 = QGridLayout(self.deformidades_im)
        self.gridLayout_195.setObjectName(u"gridLayout_195")
        self.radioButton_189 = QRadioButton(self.deformidades_im)
        self.radioButton_189.setObjectName(u"radioButton_189")
        self.radioButton_189.setFont(font6)

        self.gridLayout_195.addWidget(self.radioButton_189, 0, 0, 1, 1)

        self.radioButton_190 = QRadioButton(self.deformidades_im)
        self.radioButton_190.setObjectName(u"radioButton_190")
        self.radioButton_190.setFont(font6)

        self.gridLayout_195.addWidget(self.radioButton_190, 0, 1, 1, 1)

        self.label_309 = QLabel(self.groupLesoes_31)
        self.label_309.setObjectName(u"label_309")
        self.label_309.setGeometry(QRect(600, 40, 131, 18))
        self.label_309.setFont(font6)
        self.coordenacao_im = QGroupBox(self.groupLesoes_31)
        self.coordenacao_im.setObjectName(u"coordenacao_im")
        self.coordenacao_im.setGeometry(QRect(240, 190, 210, 51))
        self.coordenacao_im.setStyleSheet(u"")
        self.gridLayout_196 = QGridLayout(self.coordenacao_im)
        self.gridLayout_196.setObjectName(u"gridLayout_196")
        self.radioButton_191 = QRadioButton(self.coordenacao_im)
        self.radioButton_191.setObjectName(u"radioButton_191")
        self.radioButton_191.setFont(font6)

        self.gridLayout_196.addWidget(self.radioButton_191, 0, 0, 1, 1)

        self.radioButton_192 = QRadioButton(self.coordenacao_im)
        self.radioButton_192.setObjectName(u"radioButton_192")
        self.radioButton_192.setFont(font6)

        self.gridLayout_196.addWidget(self.radioButton_192, 0, 1, 1, 1)

        self.perfusao_im = QGroupBox(self.groupLesoes_31)
        self.perfusao_im.setObjectName(u"perfusao_im")
        self.perfusao_im.setGeometry(QRect(770, 20, 311, 51))
        self.gridLayout_197 = QGridLayout(self.perfusao_im)
        self.gridLayout_197.setObjectName(u"gridLayout_197")
        self.radioButton_193 = QRadioButton(self.perfusao_im)
        self.radioButton_193.setObjectName(u"radioButton_193")
        self.radioButton_193.setFont(font6)

        self.gridLayout_197.addWidget(self.radioButton_193, 0, 0, 1, 1)

        self.radioButton_194 = QRadioButton(self.perfusao_im)
        self.radioButton_194.setObjectName(u"radioButton_194")
        self.radioButton_194.setFont(font6)

        self.gridLayout_197.addWidget(self.radioButton_194, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupLesoes_31)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 130, 42, 18))
        self.label_7.setFont(font6)
        self.label_316 = QLabel(self.groupLesoes_31)
        self.label_316.setObjectName(u"label_316")
        self.label_316.setGeometry(QRect(40, 210, 161, 18))
        self.label_316.setFont(font6)
        self.label_317 = QLabel(self.groupLesoes_31)
        self.label_317.setObjectName(u"label_317")
        self.label_317.setGeometry(QRect(40, 290, 92, 18))
        self.label_317.setFont(font6)
        self.rigidez_im = QGroupBox(self.groupLesoes_31)
        self.rigidez_im.setObjectName(u"rigidez_im")
        self.rigidez_im.setGeometry(QRect(240, 350, 311, 51))
        self.rigidez_im.setStyleSheet(u"")
        self.gridLayout_198 = QGridLayout(self.rigidez_im)
        self.gridLayout_198.setObjectName(u"gridLayout_198")
        self.radioButton_195 = QRadioButton(self.rigidez_im)
        self.radioButton_195.setObjectName(u"radioButton_195")
        self.radioButton_195.setFont(font6)
        self.radioButton_195.setStyleSheet(u"border: none;")

        self.gridLayout_198.addWidget(self.radioButton_195, 0, 0, 1, 1)

        self.radioButton_196 = QRadioButton(self.rigidez_im)
        self.radioButton_196.setObjectName(u"radioButton_196")
        self.radioButton_196.setFont(font6)

        self.gridLayout_198.addWidget(self.radioButton_196, 0, 1, 1, 1)

        self.label_319 = QLabel(self.groupLesoes_31)
        self.label_319.setObjectName(u"label_319")
        self.label_319.setGeometry(QRect(40, 40, 100, 18))
        self.label_319.setFont(font6)
        self.sensibilidade_im = QGroupBox(self.groupLesoes_31)
        self.sensibilidade_im.setObjectName(u"sensibilidade_im")
        self.sensibilidade_im.setGeometry(QRect(240, 230, 191, 51))
        self.sensibilidade_im.setStyleSheet(u"")
        self.gridLayout_199 = QGridLayout(self.sensibilidade_im)
        self.gridLayout_199.setObjectName(u"gridLayout_199")
        self.radioButton_197 = QRadioButton(self.sensibilidade_im)
        self.radioButton_197.setObjectName(u"radioButton_197")
        self.radioButton_197.setFont(font6)

        self.gridLayout_199.addWidget(self.radioButton_197, 0, 0, 1, 1)

        self.radioButton_198 = QRadioButton(self.sensibilidade_im)
        self.radioButton_198.setObjectName(u"radioButton_198")
        self.radioButton_198.setFont(font6)

        self.gridLayout_199.addWidget(self.radioButton_198, 0, 1, 1, 1)

        self.simetria_im = QGroupBox(self.groupLesoes_31)
        self.simetria_im.setObjectName(u"simetria_im")
        self.simetria_im.setGeometry(QRect(240, 20, 251, 51))
        self.gridLayout_200 = QGridLayout(self.simetria_im)
        self.gridLayout_200.setObjectName(u"gridLayout_200")
        self.radio_sim_seni_3 = QRadioButton(self.simetria_im)
        self.radio_sim_seni_3.setObjectName(u"radio_sim_seni_3")
        self.radio_sim_seni_3.setFont(font6)

        self.gridLayout_200.addWidget(self.radio_sim_seni_3, 0, 0, 1, 1)

        self.radioButton_199 = QRadioButton(self.simetria_im)
        self.radioButton_199.setObjectName(u"radioButton_199")
        self.radioButton_199.setFont(font6)

        self.gridLayout_200.addWidget(self.radioButton_199, 0, 1, 1, 1)

        self.label_320 = QLabel(self.groupLesoes_31)
        self.label_320.setObjectName(u"label_320")
        self.label_320.setGeometry(QRect(40, 330, 111, 18))
        self.label_320.setFont(font6)
        self.label_321 = QLabel(self.groupLesoes_31)
        self.label_321.setObjectName(u"label_321")
        self.label_321.setGeometry(QRect(40, 170, 131, 18))
        self.label_321.setFont(font6)
        self.quaL_im = QLineEdit(self.groupLesoes_31)
        self.quaL_im.setObjectName(u"quaL_im")
        self.quaL_im.setGeometry(QRect(240, 490, 133, 31))
        self.condicoes_im = QLineEdit(self.groupLesoes_31)
        self.condicoes_im.setObjectName(u"condicoes_im")
        self.condicoes_im.setGeometry(QRect(810, 80, 133, 31))
        self.local_im = QLineEdit(self.groupLesoes_31)
        self.local_im.setObjectName(u"local_im")
        self.local_im.setGeometry(QRect(243, 121, 133, 31))
        self.label_322 = QLabel(self.groupLesoes_31)
        self.label_322.setObjectName(u"label_322")
        self.label_322.setGeometry(QRect(40, 85, 98, 18))
        self.label_322.setFont(font6)
        self.alteracoes_im = QGroupBox(self.groupLesoes_31)
        self.alteracoes_im.setObjectName(u"alteracoes_im")
        self.alteracoes_im.setGeometry(QRect(240, 430, 129, 51))
        self.gridLayout_201 = QGridLayout(self.alteracoes_im)
        self.gridLayout_201.setObjectName(u"gridLayout_201")
        self.radioButton_200 = QRadioButton(self.alteracoes_im)
        self.radioButton_200.setObjectName(u"radioButton_200")
        self.radioButton_200.setFont(font6)

        self.gridLayout_201.addWidget(self.radioButton_200, 0, 0, 1, 1)

        self.radioButton_201 = QRadioButton(self.alteracoes_im)
        self.radioButton_201.setObjectName(u"radioButton_201")
        self.radioButton_201.setFont(font6)

        self.gridLayout_201.addWidget(self.radioButton_201, 0, 1, 1, 1)

        self.label_323 = QLabel(self.groupLesoes_31)
        self.label_323.setObjectName(u"label_323")
        self.label_323.setGeometry(QRect(40, 410, 191, 18))
        self.label_323.setFont(font6)
        self.forca_im = QGroupBox(self.groupLesoes_31)
        self.forca_im.setObjectName(u"forca_im")
        self.forca_im.setGeometry(QRect(240, 270, 281, 51))
        self.forca_im.setStyleSheet(u"")
        self.gridLayout_202 = QGridLayout(self.forca_im)
        self.gridLayout_202.setObjectName(u"gridLayout_202")
        self.radioButton_202 = QRadioButton(self.forca_im)
        self.radioButton_202.setObjectName(u"radioButton_202")
        self.radioButton_202.setFont(font6)

        self.gridLayout_202.addWidget(self.radioButton_202, 0, 0, 1, 1)

        self.radioButton_203 = QRadioButton(self.forca_im)
        self.radioButton_203.setObjectName(u"radioButton_203")
        self.radioButton_203.setFont(font6)

        self.gridLayout_202.addWidget(self.radioButton_203, 0, 1, 1, 1)

        self.radioButton_204 = QRadioButton(self.forca_im)
        self.radioButton_204.setObjectName(u"radioButton_204")
        self.radioButton_204.setFont(font6)

        self.gridLayout_202.addWidget(self.radioButton_204, 0, 2, 1, 1)

        self.formas_im = QLineEdit(self.groupLesoes_31)
        self.formas_im.setObjectName(u"formas_im")
        self.formas_im.setGeometry(QRect(770, 150, 133, 31))
        self.label_324 = QLabel(self.groupLesoes_31)
        self.label_324.setObjectName(u"label_324")
        self.label_324.setGeometry(QRect(600, 160, 151, 18))
        self.label_324.setFont(font6)
        self.label_325 = QLabel(self.groupLesoes_31)
        self.label_325.setObjectName(u"label_325")
        self.label_325.setGeometry(QRect(600, 210, 81, 18))
        self.label_325.setFont(font6)
        self.outras_im = QLineEdit(self.groupLesoes_31)
        self.outras_im.setObjectName(u"outras_im")
        self.outras_im.setGeometry(QRect(770, 199, 133, 31))

        self.gridLayout_191.addWidget(self.groupLesoes_31, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_22, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_411 = QGridLayout(self.tab_6)
        self.gridLayout_411.setObjectName(u"gridLayout_411")
        self.groupLesoes_14 = QGroupBox(self.tab_6)
        self.groupLesoes_14.setObjectName(u"groupLesoes_14")
        self.groupLesoes_14.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"         border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.sensibilidade_ms = QGroupBox(self.groupLesoes_14)
        self.sensibilidade_ms.setObjectName(u"sensibilidade_ms")
        self.sensibilidade_ms.setGeometry(QRect(210, 24, 94, 50))
        self.sensibilidade_ms.setStyleSheet(u"")
        self.gridLayout_326 = QGridLayout(self.sensibilidade_ms)
        self.gridLayout_326.setObjectName(u"gridLayout_326")
        self.radio_sim_seni = QRadioButton(self.sensibilidade_ms)
        self.radio_sim_seni.setObjectName(u"radio_sim_seni")
        self.radio_sim_seni.setFont(font6)

        self.gridLayout_326.addWidget(self.radio_sim_seni, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.sensibilidade_ms)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font6)

        self.gridLayout_326.addWidget(self.radioButton_2, 0, 1, 1, 1)

        self.forca_motora_ms = QGroupBox(self.groupLesoes_14)
        self.forca_motora_ms.setObjectName(u"forca_motora_ms")
        self.forca_motora_ms.setGeometry(QRect(210, 65, 247, 46))
        self.forca_motora_ms.setStyleSheet(u"")
        self.gridLayout_287 = QGridLayout(self.forca_motora_ms)
        self.gridLayout_287.setObjectName(u"gridLayout_287")
        self.radioButton_3 = QRadioButton(self.forca_motora_ms)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font6)

        self.gridLayout_287.addWidget(self.radioButton_3, 0, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.forca_motora_ms)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font6)
        self.radioButton_4.setStyleSheet(u"Border: none;")

        self.gridLayout_287.addWidget(self.radioButton_4, 0, 1, 1, 1)

        self.radioButton_5 = QRadioButton(self.forca_motora_ms)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setFont(font6)

        self.gridLayout_287.addWidget(self.radioButton_5, 0, 2, 1, 1)

        self.edema_ms = QGroupBox(self.groupLesoes_14)
        self.edema_ms.setObjectName(u"edema_ms")
        self.edema_ms.setGeometry(QRect(210, 100, 94, 50))
        self.edema_ms.setStyleSheet(u"")
        self.gridLayout_331 = QGridLayout(self.edema_ms)
        self.gridLayout_331.setObjectName(u"gridLayout_331")
        self.radioButton_6 = QRadioButton(self.edema_ms)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setFont(font6)

        self.gridLayout_331.addWidget(self.radioButton_6, 0, 0, 1, 1)

        self.radioButton_7 = QRadioButton(self.edema_ms)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setFont(font6)

        self.gridLayout_331.addWidget(self.radioButton_7, 0, 1, 1, 1)

        self.pulsos_perifericos_ms = QGroupBox(self.groupLesoes_14)
        self.pulsos_perifericos_ms.setObjectName(u"pulsos_perifericos_ms")
        self.pulsos_perifericos_ms.setGeometry(QRect(210, 140, 94, 50))
        self.pulsos_perifericos_ms.setStyleSheet(u"")
        self.gridLayout_290 = QGridLayout(self.pulsos_perifericos_ms)
        self.gridLayout_290.setObjectName(u"gridLayout_290")
        self.radioButton_8 = QRadioButton(self.pulsos_perifericos_ms)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setFont(font6)

        self.gridLayout_290.addWidget(self.radioButton_8, 0, 0, 1, 1)

        self.radioButton_9 = QRadioButton(self.pulsos_perifericos_ms)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setFont(font6)

        self.gridLayout_290.addWidget(self.radioButton_9, 0, 1, 1, 1)

        self.paresia_ms = QGroupBox(self.groupLesoes_14)
        self.paresia_ms.setObjectName(u"paresia_ms")
        self.paresia_ms.setGeometry(QRect(210, 180, 94, 50))
        self.paresia_ms.setStyleSheet(u"")
        self.gridLayout_325 = QGridLayout(self.paresia_ms)
        self.gridLayout_325.setObjectName(u"gridLayout_325")
        self.radioButton_11 = QRadioButton(self.paresia_ms)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setFont(font6)

        self.gridLayout_325.addWidget(self.radioButton_11, 0, 0, 1, 1)

        self.radioButton_10 = QRadioButton(self.paresia_ms)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setFont(font6)

        self.gridLayout_325.addWidget(self.radioButton_10, 0, 1, 1, 1)

        self.plegia_ms = QGroupBox(self.groupLesoes_14)
        self.plegia_ms.setObjectName(u"plegia_ms")
        self.plegia_ms.setGeometry(QRect(210, 220, 94, 50))
        self.plegia_ms.setStyleSheet(u"")
        self.gridLayout_333 = QGridLayout(self.plegia_ms)
        self.gridLayout_333.setObjectName(u"gridLayout_333")
        self.radioButton_12 = QRadioButton(self.plegia_ms)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setFont(font6)

        self.gridLayout_333.addWidget(self.radioButton_12, 0, 0, 1, 1)

        self.radioButton_13 = QRadioButton(self.plegia_ms)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setFont(font6)

        self.gridLayout_333.addWidget(self.radioButton_13, 0, 1, 1, 1)

        self.label_168 = QLabel(self.groupLesoes_14)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(80, 45, 100, 18))
        self.label_168.setFont(font6)
        self.label_169 = QLabel(self.groupLesoes_14)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(80, 85, 91, 18))
        self.label_169.setFont(font6)
        self.label_162 = QLabel(self.groupLesoes_14)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(80, 120, 63, 18))
        self.label_162.setFont(font6)
        self.label_150 = QLabel(self.groupLesoes_14)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setGeometry(QRect(80, 160, 111, 18))
        self.label_150.setFont(font6)
        self.label_160 = QLabel(self.groupLesoes_14)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(80, 200, 51, 18))
        self.label_160.setFont(font6)
        self.label_171 = QLabel(self.groupLesoes_14)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(80, 240, 49, 19))
        self.label_171.setFont(font6)
        self.label_164 = QLabel(self.groupLesoes_14)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(80, 280, 92, 18))
        self.label_164.setFont(font6)
        self.amputacoes_ms = QGroupBox(self.groupLesoes_14)
        self.amputacoes_ms.setObjectName(u"amputacoes_ms")
        self.amputacoes_ms.setGeometry(QRect(210, 260, 95, 50))
        self.amputacoes_ms.setStyleSheet(u"")
        self.gridLayout_335 = QGridLayout(self.amputacoes_ms)
        self.gridLayout_335.setObjectName(u"gridLayout_335")
        self.radioButton_18 = QRadioButton(self.amputacoes_ms)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setFont(font6)

        self.gridLayout_335.addWidget(self.radioButton_18, 0, 0, 1, 1)

        self.radioButton_19 = QRadioButton(self.amputacoes_ms)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setFont(font6)

        self.gridLayout_335.addWidget(self.radioButton_19, 0, 1, 1, 1)

        self.label_165 = QLabel(self.groupLesoes_14)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(80, 320, 50, 18))
        self.label_165.setFont(font6)
        self.gesso_ms = QGroupBox(self.groupLesoes_14)
        self.gesso_ms.setObjectName(u"gesso_ms")
        self.gesso_ms.setGeometry(QRect(210, 300, 94, 50))
        self.gesso_ms.setStyleSheet(u"")
        self.gridLayout_319 = QGridLayout(self.gesso_ms)
        self.gridLayout_319.setObjectName(u"gridLayout_319")
        self.radioButton_14 = QRadioButton(self.gesso_ms)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setFont(font6)

        self.gridLayout_319.addWidget(self.radioButton_14, 0, 0, 1, 1)

        self.radioButton_15 = QRadioButton(self.gesso_ms)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setFont(font6)

        self.gridLayout_319.addWidget(self.radioButton_15, 0, 1, 1, 1)

        self.tala_gessado_ms = QGroupBox(self.groupLesoes_14)
        self.tala_gessado_ms.setObjectName(u"tala_gessado_ms")
        self.tala_gessado_ms.setGeometry(QRect(210, 340, 94, 50))
        self.tala_gessado_ms.setStyleSheet(u"")
        self.gridLayout_323 = QGridLayout(self.tala_gessado_ms)
        self.gridLayout_323.setObjectName(u"gridLayout_323")
        self.radioButton_16 = QRadioButton(self.tala_gessado_ms)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setFont(font6)
        self.radioButton_16.setStyleSheet(u"border: none;")

        self.gridLayout_323.addWidget(self.radioButton_16, 0, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.tala_gessado_ms)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setFont(font6)

        self.gridLayout_323.addWidget(self.radioButton_17, 0, 1, 1, 1)

        self.label_163 = QLabel(self.groupLesoes_14)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(80, 362, 100, 18))
        self.label_163.setFont(font6)
        self.label_170 = QLabel(self.groupLesoes_14)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(80, 403, 121, 18))
        self.label_170.setFont(font6)
        self.dispositivo_venoso_ms = QGroupBox(self.groupLesoes_14)
        self.dispositivo_venoso_ms.setObjectName(u"dispositivo_venoso_ms")
        self.dispositivo_venoso_ms.setGeometry(QRect(210, 380, 94, 50))
        self.gridLayout_316 = QGridLayout(self.dispositivo_venoso_ms)
        self.gridLayout_316.setObjectName(u"gridLayout_316")
        self.radioButton_21 = QRadioButton(self.dispositivo_venoso_ms)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setFont(font6)

        self.gridLayout_316.addWidget(self.radioButton_21, 0, 1, 1, 1)

        self.radioButton_20 = QRadioButton(self.dispositivo_venoso_ms)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setFont(font6)

        self.gridLayout_316.addWidget(self.radioButton_20, 0, 0, 1, 1)

        self.lesos_ms = QGroupBox(self.groupLesoes_14)
        self.lesos_ms.setObjectName(u"lesos_ms")
        self.lesos_ms.setGeometry(QRect(210, 420, 94, 50))
        self.gridLayout_297 = QGridLayout(self.lesos_ms)
        self.gridLayout_297.setObjectName(u"gridLayout_297")
        self.radioButton_22 = QRadioButton(self.lesos_ms)
        self.radioButton_22.setObjectName(u"radioButton_22")
        self.radioButton_22.setFont(font6)

        self.gridLayout_297.addWidget(self.radioButton_22, 0, 0, 1, 1)

        self.radioButton_23 = QRadioButton(self.lesos_ms)
        self.radioButton_23.setObjectName(u"radioButton_23")
        self.radioButton_23.setFont(font6)

        self.gridLayout_297.addWidget(self.radioButton_23, 0, 1, 1, 1)

        self.label_167 = QLabel(self.groupLesoes_14)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(80, 440, 56, 18))
        self.label_167.setFont(font6)
        self.local_amputacoes_ms = QLineEdit(self.groupLesoes_14)
        self.local_amputacoes_ms.setObjectName(u"local_amputacoes_ms")
        self.local_amputacoes_ms.setGeometry(QRect(370, 275, 121, 31))
        self.label_172 = QLabel(self.groupLesoes_14)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(320, 280, 41, 17))
        self.label_172.setFont(font6)
        self.local_dispositivo_venoso_ms = QLineEdit(self.groupLesoes_14)
        self.local_dispositivo_venoso_ms.setObjectName(u"local_dispositivo_venoso_ms")
        self.local_dispositivo_venoso_ms.setGeometry(QRect(370, 396, 121, 31))
        self.label_166 = QLabel(self.groupLesoes_14)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(320, 407, 41, 17))
        self.label_166.setFont(font6)
        self.local_lesoes_ms = QLineEdit(self.groupLesoes_14)
        self.local_lesoes_ms.setObjectName(u"local_lesoes_ms")
        self.local_lesoes_ms.setGeometry(QRect(370, 435, 121, 31))
        self.label_161 = QLabel(self.groupLesoes_14)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(320, 443, 41, 17))
        self.label_161.setFont(font6)

        self.gridLayout_411.addWidget(self.groupLesoes_14, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_412 = QGridLayout(self.tab_7)
        self.gridLayout_412.setObjectName(u"gridLayout_412")
        self.groupLesoes_15 = QGroupBox(self.tab_7)
        self.groupLesoes_15.setObjectName(u"groupLesoes_15")
        self.groupLesoes_15.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.sensibilidade_mi = QGroupBox(self.groupLesoes_15)
        self.sensibilidade_mi.setObjectName(u"sensibilidade_mi")
        self.sensibilidade_mi.setGeometry(QRect(250, 40, 202, 51))
        self.sensibilidade_mi.setStyleSheet(u"")
        self.gridLayout_356 = QGridLayout(self.sensibilidade_mi)
        self.gridLayout_356.setObjectName(u"gridLayout_356")
        self.radio_preservada_2 = QRadioButton(self.sensibilidade_mi)
        self.radio_preservada_2.setObjectName(u"radio_preservada_2")
        self.radio_preservada_2.setFont(font6)
        self.radio_preservada_2.setStyleSheet(u"border: none;\n"
"")

        self.gridLayout_356.addWidget(self.radio_preservada_2, 0, 0, 1, 1)

        self.radio_alterada = QRadioButton(self.sensibilidade_mi)
        self.radio_alterada.setObjectName(u"radio_alterada")
        self.radio_alterada.setFont(font6)

        self.gridLayout_356.addWidget(self.radio_alterada, 0, 1, 1, 1)

        self.label_173 = QLabel(self.groupLesoes_15)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(100, 60, 81, 18))
        self.label_173.setFont(font6)
        self.label_182 = QLabel(self.groupLesoes_15)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setGeometry(QRect(100, 100, 91, 18))
        self.label_182.setFont(font6)
        self.forca_motora_mi = QGroupBox(self.groupLesoes_15)
        self.forca_motora_mi.setObjectName(u"forca_motora_mi")
        self.forca_motora_mi.setGeometry(QRect(250, 81, 261, 51))
        self.forca_motora_mi.setStyleSheet(u"")
        self.gridLayout_339 = QGridLayout(self.forca_motora_mi)
        self.gridLayout_339.setObjectName(u"gridLayout_339")
        self.radio_preservada_forca = QRadioButton(self.forca_motora_mi)
        self.radio_preservada_forca.setObjectName(u"radio_preservada_forca")
        self.radio_preservada_forca.setFont(font6)

        self.gridLayout_339.addWidget(self.radio_preservada_forca, 0, 0, 1, 1)

        self.radio_diminuida_forca = QRadioButton(self.forca_motora_mi)
        self.radio_diminuida_forca.setObjectName(u"radio_diminuida_forca")
        self.radio_diminuida_forca.setFont(font6)

        self.gridLayout_339.addWidget(self.radio_diminuida_forca, 0, 1, 1, 1)

        self.radio_ausente_forca = QRadioButton(self.forca_motora_mi)
        self.radio_ausente_forca.setObjectName(u"radio_ausente_forca")
        self.radio_ausente_forca.setFont(font6)

        self.gridLayout_339.addWidget(self.radio_ausente_forca, 0, 2, 1, 1)

        self.edema_mi = QGroupBox(self.groupLesoes_15)
        self.edema_mi.setObjectName(u"edema_mi")
        self.edema_mi.setGeometry(QRect(250, 122, 101, 51))
        self.edema_mi.setStyleSheet(u"")
        self.gridLayout_345 = QGridLayout(self.edema_mi)
        self.gridLayout_345.setObjectName(u"gridLayout_345")
        self.radio_sim_edemas = QRadioButton(self.edema_mi)
        self.radio_sim_edemas.setObjectName(u"radio_sim_edemas")
        self.radio_sim_edemas.setFont(font6)

        self.gridLayout_345.addWidget(self.radio_sim_edemas, 0, 0, 1, 1)

        self.radio_nao_edemas = QRadioButton(self.edema_mi)
        self.radio_nao_edemas.setObjectName(u"radio_nao_edemas")
        self.radio_nao_edemas.setFont(font6)

        self.gridLayout_345.addWidget(self.radio_nao_edemas, 0, 1, 1, 1)

        self.pulsos_perifericos_mi = QGroupBox(self.groupLesoes_15)
        self.pulsos_perifericos_mi.setObjectName(u"pulsos_perifericos_mi")
        self.pulsos_perifericos_mi.setGeometry(QRect(250, 163, 201, 51))
        self.pulsos_perifericos_mi.setStyleSheet(u"")
        self.gridLayout_337 = QGridLayout(self.pulsos_perifericos_mi)
        self.gridLayout_337.setObjectName(u"gridLayout_337")
        self.radio_palpaveis = QRadioButton(self.pulsos_perifericos_mi)
        self.radio_palpaveis.setObjectName(u"radio_palpaveis")
        self.radio_palpaveis.setFont(font6)

        self.gridLayout_337.addWidget(self.radio_palpaveis, 0, 0, 1, 1)

        self.radio_nao_palpaveis = QRadioButton(self.pulsos_perifericos_mi)
        self.radio_nao_palpaveis.setObjectName(u"radio_nao_palpaveis")
        self.radio_nao_palpaveis.setFont(font6)

        self.gridLayout_337.addWidget(self.radio_nao_palpaveis, 0, 1, 1, 1)

        self.paresia_mi = QGroupBox(self.groupLesoes_15)
        self.paresia_mi.setObjectName(u"paresia_mi")
        self.paresia_mi.setGeometry(QRect(250, 204, 94, 50))
        self.paresia_mi.setStyleSheet(u"")
        self.gridLayout_354 = QGridLayout(self.paresia_mi)
        self.gridLayout_354.setObjectName(u"gridLayout_354")
        self.radio_sim_paresia = QRadioButton(self.paresia_mi)
        self.radio_sim_paresia.setObjectName(u"radio_sim_paresia")
        self.radio_sim_paresia.setFont(font6)

        self.gridLayout_354.addWidget(self.radio_sim_paresia, 0, 0, 1, 1)

        self.radio_nao_paresia = QRadioButton(self.paresia_mi)
        self.radio_nao_paresia.setObjectName(u"radio_nao_paresia")
        self.radio_nao_paresia.setFont(font6)

        self.gridLayout_354.addWidget(self.radio_nao_paresia, 0, 1, 1, 1)

        self.plegia_mi = QGroupBox(self.groupLesoes_15)
        self.plegia_mi.setObjectName(u"plegia_mi")
        self.plegia_mi.setGeometry(QRect(250, 245, 94, 50))
        self.plegia_mi.setStyleSheet(u"")
        self.gridLayout_351 = QGridLayout(self.plegia_mi)
        self.gridLayout_351.setObjectName(u"gridLayout_351")
        self.radio_sim_plegia = QRadioButton(self.plegia_mi)
        self.radio_sim_plegia.setObjectName(u"radio_sim_plegia")
        self.radio_sim_plegia.setFont(font6)

        self.gridLayout_351.addWidget(self.radio_sim_plegia, 0, 0, 1, 1)

        self.radio_nao_plegia = QRadioButton(self.plegia_mi)
        self.radio_nao_plegia.setObjectName(u"radio_nao_plegia")
        self.radio_nao_plegia.setFont(font6)

        self.gridLayout_351.addWidget(self.radio_nao_plegia, 0, 1, 1, 1)

        self.amputacoes_mi = QGroupBox(self.groupLesoes_15)
        self.amputacoes_mi.setObjectName(u"amputacoes_mi")
        self.amputacoes_mi.setGeometry(QRect(250, 281, 94, 50))
        self.amputacoes_mi.setStyleSheet(u"")
        self.gridLayout_362 = QGridLayout(self.amputacoes_mi)
        self.gridLayout_362.setObjectName(u"gridLayout_362")
        self.radio_sim_amputacoes = QRadioButton(self.amputacoes_mi)
        self.radio_sim_amputacoes.setObjectName(u"radio_sim_amputacoes")
        self.radio_sim_amputacoes.setFont(font6)

        self.gridLayout_362.addWidget(self.radio_sim_amputacoes, 0, 0, 1, 1)

        self.radio_nao_amputacoes = QRadioButton(self.amputacoes_mi)
        self.radio_nao_amputacoes.setObjectName(u"radio_nao_amputacoes")
        self.radio_nao_amputacoes.setFont(font6)

        self.gridLayout_362.addWidget(self.radio_nao_amputacoes, 0, 1, 1, 1)

        self.gesso_mi = QGroupBox(self.groupLesoes_15)
        self.gesso_mi.setObjectName(u"gesso_mi")
        self.gesso_mi.setGeometry(QRect(250, 322, 94, 50))
        self.gesso_mi.setStyleSheet(u"")
        self.gridLayout_342 = QGridLayout(self.gesso_mi)
        self.gridLayout_342.setObjectName(u"gridLayout_342")
        self.radio_sim_gesso = QRadioButton(self.gesso_mi)
        self.radio_sim_gesso.setObjectName(u"radio_sim_gesso")
        self.radio_sim_gesso.setFont(font6)
        self.radio_sim_gesso.setStyleSheet(u"border: none;\n"
"")

        self.gridLayout_342.addWidget(self.radio_sim_gesso, 0, 0, 1, 1)

        self.radio_nao_gesso = QRadioButton(self.gesso_mi)
        self.radio_nao_gesso.setObjectName(u"radio_nao_gesso")
        self.radio_nao_gesso.setFont(font6)

        self.gridLayout_342.addWidget(self.radio_nao_gesso, 0, 1, 1, 1)

        self.tala_gessado_mi = QGroupBox(self.groupLesoes_15)
        self.tala_gessado_mi.setObjectName(u"tala_gessado_mi")
        self.tala_gessado_mi.setGeometry(QRect(250, 363, 94, 50))
        self.tala_gessado_mi.setStyleSheet(u"")
        self.gridLayout_358 = QGridLayout(self.tala_gessado_mi)
        self.gridLayout_358.setObjectName(u"gridLayout_358")
        self.radio_sim_tala = QRadioButton(self.tala_gessado_mi)
        self.radio_sim_tala.setObjectName(u"radio_sim_tala")
        self.radio_sim_tala.setFont(font6)
        self.radio_sim_tala.setStyleSheet(u"border: none;\n"
"")

        self.gridLayout_358.addWidget(self.radio_sim_tala, 0, 0, 1, 1)

        self.radio_nao_tala = QRadioButton(self.tala_gessado_mi)
        self.radio_nao_tala.setObjectName(u"radio_nao_tala")
        self.radio_nao_tala.setFont(font6)

        self.gridLayout_358.addWidget(self.radio_nao_tala, 0, 1, 1, 1)

        self.dispositivo_venoso_mi = QGroupBox(self.groupLesoes_15)
        self.dispositivo_venoso_mi.setObjectName(u"dispositivo_venoso_mi")
        self.dispositivo_venoso_mi.setGeometry(QRect(250, 404, 94, 50))
        self.dispositivo_venoso_mi.setStyleSheet(u"")
        self.gridLayout_140 = QGridLayout(self.dispositivo_venoso_mi)
        self.gridLayout_140.setObjectName(u"gridLayout_140")
        self.radio_sim_venoso = QRadioButton(self.dispositivo_venoso_mi)
        self.radio_sim_venoso.setObjectName(u"radio_sim_venoso")
        self.radio_sim_venoso.setFont(font6)

        self.gridLayout_140.addWidget(self.radio_sim_venoso, 0, 0, 1, 1)

        self.radio_nao_venoso = QRadioButton(self.dispositivo_venoso_mi)
        self.radio_nao_venoso.setObjectName(u"radio_nao_venoso")
        self.radio_nao_venoso.setFont(font6)

        self.gridLayout_140.addWidget(self.radio_nao_venoso, 0, 1, 1, 1)

        self.lesos_mi = QGroupBox(self.groupLesoes_15)
        self.lesos_mi.setObjectName(u"lesos_mi")
        self.lesos_mi.setGeometry(QRect(250, 445, 94, 50))
        self.gridLayout_366 = QGridLayout(self.lesos_mi)
        self.gridLayout_366.setObjectName(u"gridLayout_366")
        self.radio_nao_lesoes = QRadioButton(self.lesos_mi)
        self.radio_nao_lesoes.setObjectName(u"radio_nao_lesoes")
        self.radio_nao_lesoes.setFont(font6)

        self.gridLayout_366.addWidget(self.radio_nao_lesoes, 0, 1, 1, 1)

        self.radio_sim_lesoes = QRadioButton(self.lesos_mi)
        self.radio_sim_lesoes.setObjectName(u"radio_sim_lesoes")
        self.radio_sim_lesoes.setFont(font6)

        self.gridLayout_366.addWidget(self.radio_sim_lesoes, 0, 0, 1, 1)

        self.label_179 = QLabel(self.groupLesoes_15)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(100, 140, 61, 18))
        self.label_179.setFont(font6)
        self.label_186 = QLabel(self.groupLesoes_15)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setGeometry(QRect(100, 190, 111, 18))
        self.label_186.setFont(font6)
        self.label_174 = QLabel(self.groupLesoes_15)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(100, 228, 59, 18))
        self.label_174.setFont(font6)
        self.label_175 = QLabel(self.groupLesoes_15)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(100, 267, 49, 18))
        self.label_175.setFont(font6)
        self.label_177 = QLabel(self.groupLesoes_15)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(100, 305, 92, 18))
        self.label_177.setFont(font6)
        self.label_180 = QLabel(self.groupLesoes_15)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setGeometry(QRect(100, 347, 41, 18))
        self.label_180.setFont(font6)
        self.label_178 = QLabel(self.groupLesoes_15)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(100, 387, 91, 18))
        self.label_178.setFont(font6)
        self.label_185 = QLabel(self.groupLesoes_15)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setGeometry(QRect(100, 428, 121, 18))
        self.label_185.setFont(font6)
        self.label_183 = QLabel(self.groupLesoes_15)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setGeometry(QRect(100, 471, 51, 18))
        self.label_183.setFont(font6)
        self.local_amputacoes_mi = QLineEdit(self.groupLesoes_15)
        self.local_amputacoes_mi.setObjectName(u"local_amputacoes_mi")
        self.local_amputacoes_mi.setGeometry(QRect(410, 300, 121, 31))
        self.label_181 = QLabel(self.groupLesoes_15)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setGeometry(QRect(360, 307, 41, 17))
        self.label_181.setFont(font6)
        self.local_dispositivo_venoso_mi = QLineEdit(self.groupLesoes_15)
        self.local_dispositivo_venoso_mi.setObjectName(u"local_dispositivo_venoso_mi")
        self.local_dispositivo_venoso_mi.setGeometry(QRect(410, 420, 121, 31))
        self.local_dispositivo_venoso_mi.setStyleSheet(u"")
        self.label_176 = QLabel(self.groupLesoes_15)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(360, 430, 41, 17))
        self.label_176.setFont(font6)
        self.local_lesoes_mi = QLineEdit(self.groupLesoes_15)
        self.local_lesoes_mi.setObjectName(u"local_lesoes_mi")
        self.local_lesoes_mi.setGeometry(QRect(410, 460, 121, 31))
        self.label_184 = QLabel(self.groupLesoes_15)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setGeometry(QRect(360, 470, 41, 17))
        self.label_184.setFont(font6)

        self.gridLayout_412.addWidget(self.groupLesoes_15, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_413 = QGridLayout(self.tab_8)
        self.gridLayout_413.setObjectName(u"gridLayout_413")
        self.groupLesoes_16 = QGroupBox(self.tab_8)
        self.groupLesoes_16.setObjectName(u"groupLesoes_16")
        self.groupLesoes_16.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"       border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.layoutWidget_152 = QWidget(self.groupLesoes_16)
        self.layoutWidget_152.setObjectName(u"layoutWidget_152")
        self.layoutWidget_152.setGeometry(QRect(140, 380, 2, 2))
        self.gridLayout_389 = QGridLayout(self.layoutWidget_152)
        self.gridLayout_389.setObjectName(u"gridLayout_389")
        self.gridLayout_389.setContentsMargins(0, 0, 0, 0)
        self.unha = QGroupBox(self.groupLesoes_16)
        self.unha.setObjectName(u"unha")
        self.unha.setGeometry(QRect(140, 40, 182, 51))
        self.unha.setStyleSheet(u"")
        self.gridLayout_385 = QGridLayout(self.unha)
        self.gridLayout_385.setObjectName(u"gridLayout_385")
        self.radio_regular_3 = QRadioButton(self.unha)
        self.radio_regular_3.setObjectName(u"radio_regular_3")
        self.radio_regular_3.setFont(font6)

        self.gridLayout_385.addWidget(self.radio_regular_3, 0, 0, 1, 1)

        self.radio_irregular = QRadioButton(self.unha)
        self.radio_irregular.setObjectName(u"radio_irregular")
        self.radio_irregular.setFont(font6)

        self.gridLayout_385.addWidget(self.radio_irregular, 0, 1, 1, 1)

        self.label_216 = QLabel(self.groupLesoes_16)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setGeometry(QRect(30, 60, 51, 31))
        self.label_216.setFont(font6)
        self.implantacao = QGroupBox(self.groupLesoes_16)
        self.implantacao.setObjectName(u"implantacao")
        self.implantacao.setGeometry(QRect(140, 85, 311, 51))
        self.implantacao.setStyleSheet(u"")
        self.gridLayout_374 = QGridLayout(self.implantacao)
        self.gridLayout_374.setObjectName(u"gridLayout_374")
        self.radio_angulo_reto = QRadioButton(self.implantacao)
        self.radio_angulo_reto.setObjectName(u"radio_angulo_reto")
        self.radio_angulo_reto.setFont(font6)

        self.gridLayout_374.addWidget(self.radio_angulo_reto, 0, 0, 1, 1)

        self.radio_menor = QRadioButton(self.implantacao)
        self.radio_menor.setObjectName(u"radio_menor")
        self.radio_menor.setFont(font6)

        self.gridLayout_374.addWidget(self.radio_menor, 0, 1, 1, 1)

        self.radio_maior = QRadioButton(self.implantacao)
        self.radio_maior.setObjectName(u"radio_maior")
        self.radio_maior.setFont(font6)

        self.gridLayout_374.addWidget(self.radio_maior, 0, 2, 1, 1)

        self.label_212 = QLabel(self.groupLesoes_16)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setGeometry(QRect(30, 100, 89, 39))
        self.label_212.setFont(font6)
        self.label_218 = QLabel(self.groupLesoes_16)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setGeometry(QRect(30, 250, 59, 39))
        self.label_218.setFont(font6)
        self.label_217 = QLabel(self.groupLesoes_16)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setGeometry(QRect(30, 290, 79, 39))
        self.label_217.setFont(font6)
        self.superficie = QGroupBox(self.groupLesoes_16)
        self.superficie.setObjectName(u"superficie")
        self.superficie.setGeometry(QRect(140, 280, 311, 51))
        self.superficie.setStyleSheet(u"")
        self.gridLayout_376 = QGridLayout(self.superficie)
        self.gridLayout_376.setObjectName(u"gridLayout_376")
        self.radio_lisa_2 = QRadioButton(self.superficie)
        self.radio_lisa_2.setObjectName(u"radio_lisa_2")
        self.radio_lisa_2.setFont(font6)

        self.gridLayout_376.addWidget(self.radio_lisa_2, 0, 1, 1, 1)

        self.radio_distrofica = QRadioButton(self.superficie)
        self.radio_distrofica.setObjectName(u"radio_distrofica")
        self.radio_distrofica.setFont(font6)

        self.gridLayout_376.addWidget(self.radio_distrofica, 0, 0, 1, 1)

        self.espessura_olhos = QGroupBox(self.groupLesoes_16)
        self.espessura_olhos.setObjectName(u"espessura_olhos")
        self.espessura_olhos.setGeometry(QRect(140, 206, 331, 46))
        self.espessura_olhos.setStyleSheet(u"")
        self.gridLayout_388 = QGridLayout(self.espessura_olhos)
        self.gridLayout_388.setObjectName(u"gridLayout_388")
        self.radio_preservada_3 = QRadioButton(self.espessura_olhos)
        self.radio_preservada_3.setObjectName(u"radio_preservada_3")
        self.radio_preservada_3.setFont(font6)

        self.gridLayout_388.addWidget(self.radio_preservada_3, 0, 0, 1, 1)

        self.radio_fina = QRadioButton(self.espessura_olhos)
        self.radio_fina.setObjectName(u"radio_fina")
        self.radio_fina.setFont(font6)

        self.gridLayout_388.addWidget(self.radio_fina, 0, 1, 1, 1)

        self.radio_grossa = QRadioButton(self.espessura_olhos)
        self.radio_grossa.setObjectName(u"radio_grossa")
        self.radio_grossa.setFont(font6)

        self.gridLayout_388.addWidget(self.radio_grossa, 0, 2, 1, 1)

        self.coloracao = QGroupBox(self.groupLesoes_16)
        self.coloracao.setObjectName(u"coloracao")
        self.coloracao.setGeometry(QRect(140, 130, 301, 46))
        self.coloracao.setStyleSheet(u"")
        self.gridLayout_372 = QGridLayout(self.coloracao)
        self.gridLayout_372.setObjectName(u"gridLayout_372")
        self.radio_rosada = QRadioButton(self.coloracao)
        self.radio_rosada.setObjectName(u"radio_rosada")
        self.radio_rosada.setFont(font6)

        self.gridLayout_372.addWidget(self.radio_rosada, 0, 0, 1, 1)

        self.radio_cianotica = QRadioButton(self.coloracao)
        self.radio_cianotica.setObjectName(u"radio_cianotica")
        self.radio_cianotica.setFont(font6)

        self.gridLayout_372.addWidget(self.radio_cianotica, 0, 1, 1, 1)

        self.radio_palida = QRadioButton(self.coloracao)
        self.radio_palida.setObjectName(u"radio_palida")
        self.radio_palida.setFont(font6)

        self.gridLayout_372.addWidget(self.radio_palida, 0, 2, 1, 1)

        self.radio_descorada = QRadioButton(self.coloracao)
        self.radio_descorada.setObjectName(u"radio_descorada")
        self.radio_descorada.setFont(font6)

        self.gridLayout_372.addWidget(self.radio_descorada, 0, 3, 1, 1)

        self.u_outra = QLineEdit(self.groupLesoes_16)
        self.u_outra.setObjectName(u"u_outra")
        self.u_outra.setGeometry(QRect(140, 180, 121, 31))
        self.e_outra = QLineEdit(self.groupLesoes_16)
        self.e_outra.setObjectName(u"e_outra")
        self.e_outra.setGeometry(QRect(140, 257, 121, 31))
        self.s_outra = QLineEdit(self.groupLesoes_16)
        self.s_outra.setObjectName(u"s_outra")
        self.s_outra.setGeometry(QRect(140, 336, 121, 31))
        self.label_215 = QLabel(self.groupLesoes_16)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setGeometry(QRect(30, 140, 89, 39))
        self.label_215.setFont(font6)
        self.label_211 = QLabel(self.groupLesoes_16)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setGeometry(QRect(30, 180, 59, 39))
        self.label_211.setFont(font6)
        self.label_213 = QLabel(self.groupLesoes_16)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setGeometry(QRect(30, 220, 71, 31))
        self.label_213.setFont(font6)
        self.label_214 = QLabel(self.groupLesoes_16)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setGeometry(QRect(30, 330, 59, 39))
        self.label_214.setFont(font6)
        self.label_223 = QLabel(self.groupLesoes_16)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setGeometry(QRect(700, 50, 49, 39))
        self.label_223.setFont(font6)
        self.brilho = QGroupBox(self.groupLesoes_16)
        self.brilho.setObjectName(u"brilho")
        self.brilho.setGeometry(QRect(850, 40, 151, 46))
        self.brilho.setStyleSheet(u"")
        self.gridLayout_409 = QGridLayout(self.brilho)
        self.gridLayout_409.setObjectName(u"gridLayout_409")
        self.radio_presente = QRadioButton(self.brilho)
        self.radio_presente.setObjectName(u"radio_presente")
        self.radio_presente.setFont(font6)

        self.gridLayout_409.addWidget(self.radio_presente, 0, 0, 1, 1)

        self.radio_opaco = QRadioButton(self.brilho)
        self.radio_opaco.setObjectName(u"radio_opaco")
        self.radio_opaco.setFont(font6)

        self.gridLayout_409.addWidget(self.radio_opaco, 0, 1, 1, 1)

        self.label_224 = QLabel(self.groupLesoes_16)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setGeometry(QRect(700, 90, 99, 39))
        self.label_224.setFont(font6)
        self.consistencia = QGroupBox(self.groupLesoes_16)
        self.consistencia.setObjectName(u"consistencia")
        self.consistencia.setGeometry(QRect(850, 77, 141, 51))
        self.consistencia.setStyleSheet(u"")
        self.gridLayout_395 = QGridLayout(self.consistencia)
        self.gridLayout_395.setObjectName(u"gridLayout_395")
        self.radio_fragil = QRadioButton(self.consistencia)
        self.radio_fragil.setObjectName(u"radio_fragil")
        self.radio_fragil.setFont(font6)

        self.gridLayout_395.addWidget(self.radio_fragil, 0, 0, 1, 1)

        self.radio_forte = QRadioButton(self.consistencia)
        self.radio_forte.setObjectName(u"radio_forte")
        self.radio_forte.setFont(font6)

        self.gridLayout_395.addWidget(self.radio_forte, 0, 1, 1, 1)

        self.label_220 = QLabel(self.groupLesoes_16)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setGeometry(QRect(700, 130, 99, 39))
        self.label_220.setFont(font6)
        self.leuconiquia = QGroupBox(self.groupLesoes_16)
        self.leuconiquia.setObjectName(u"leuconiquia")
        self.leuconiquia.setGeometry(QRect(850, 120, 101, 51))
        self.leuconiquia.setStyleSheet(u"")
        self.gridLayout_407 = QGridLayout(self.leuconiquia)
        self.gridLayout_407.setObjectName(u"gridLayout_407")
        self.radio_leuconiquia_sim = QRadioButton(self.leuconiquia)
        self.radio_leuconiquia_sim.setObjectName(u"radio_leuconiquia_sim")
        self.radio_leuconiquia_sim.setFont(font6)

        self.gridLayout_407.addWidget(self.radio_leuconiquia_sim, 0, 0, 1, 1)

        self.radio_leuconiquia_nao = QRadioButton(self.leuconiquia)
        self.radio_leuconiquia_nao.setObjectName(u"radio_leuconiquia_nao")
        self.radio_leuconiquia_nao.setFont(font6)

        self.gridLayout_407.addWidget(self.radio_leuconiquia_nao, 0, 1, 1, 1)

        self.label_221 = QLabel(self.groupLesoes_16)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setGeometry(QRect(700, 170, 49, 39))
        self.label_221.setFont(font6)
        self.l_qual = QLineEdit(self.groupLesoes_16)
        self.l_qual.setObjectName(u"l_qual")
        self.l_qual.setGeometry(QRect(850, 180, 121, 31))
        self.label_225 = QLabel(self.groupLesoes_16)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setGeometry(QRect(700, 210, 80, 39))
        self.label_225.setFont(font6)
        self.onicofagia = QGroupBox(self.groupLesoes_16)
        self.onicofagia.setObjectName(u"onicofagia")
        self.onicofagia.setGeometry(QRect(850, 205, 101, 46))
        self.onicofagia.setStyleSheet(u"")
        self.gridLayout_399 = QGridLayout(self.onicofagia)
        self.gridLayout_399.setObjectName(u"gridLayout_399")
        self.radio_onicofagia_sim = QRadioButton(self.onicofagia)
        self.radio_onicofagia_sim.setObjectName(u"radio_onicofagia_sim")
        self.radio_onicofagia_sim.setFont(font6)

        self.gridLayout_399.addWidget(self.radio_onicofagia_sim, 0, 0, 1, 1)

        self.radio_onicofagia_nao = QRadioButton(self.onicofagia)
        self.radio_onicofagia_nao.setObjectName(u"radio_onicofagia_nao")
        self.radio_onicofagia_nao.setFont(font6)
        self.radio_onicofagia_nao.setStyleSheet(u"border: none;")

        self.gridLayout_399.addWidget(self.radio_onicofagia_nao, 0, 1, 1, 1)

        self.label_222 = QLabel(self.groupLesoes_16)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setGeometry(QRect(700, 250, 131, 39))
        self.label_222.setFont(font6)
        self.condicoes_de_higiene = QGroupBox(self.groupLesoes_16)
        self.condicoes_de_higiene.setObjectName(u"condicoes_de_higiene")
        self.condicoes_de_higiene.setGeometry(QRect(850, 243, 241, 51))
        self.condicoes_de_higiene.setStyleSheet(u"")
        self.gridLayout_402 = QGridLayout(self.condicoes_de_higiene)
        self.gridLayout_402.setObjectName(u"gridLayout_402")
        self.radio_precaria = QRadioButton(self.condicoes_de_higiene)
        self.radio_precaria.setObjectName(u"radio_precaria")
        self.radio_precaria.setFont(font6)

        self.gridLayout_402.addWidget(self.radio_precaria, 0, 2, 1, 1)

        self.radio_satisfatoria = QRadioButton(self.condicoes_de_higiene)
        self.radio_satisfatoria.setObjectName(u"radio_satisfatoria")
        self.radio_satisfatoria.setFont(font6)

        self.gridLayout_402.addWidget(self.radio_satisfatoria, 0, 0, 1, 1)

        self.radio_regular_4 = QRadioButton(self.condicoes_de_higiene)
        self.radio_regular_4.setObjectName(u"radio_regular_4")
        self.radio_regular_4.setFont(font6)

        self.gridLayout_402.addWidget(self.radio_regular_4, 0, 1, 1, 1)

        self.label_219 = QLabel(self.groupLesoes_16)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setGeometry(QRect(700, 290, 59, 39))
        self.label_219.setFont(font6)
        self.c_outra = QLineEdit(self.groupLesoes_16)
        self.c_outra.setObjectName(u"c_outra")
        self.c_outra.setGeometry(QRect(850, 300, 121, 31))

        self.gridLayout_413.addWidget(self.groupLesoes_16, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_414 = QGridLayout(self.tab_9)
        self.gridLayout_414.setObjectName(u"gridLayout_414")
        self.groupLesoes_17 = QGroupBox(self.tab_9)
        self.groupLesoes_17.setObjectName(u"groupLesoes_17")
        self.groupLesoes_17.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.outro_cranio = QLineEdit(self.groupLesoes_17)
        self.outro_cranio.setObjectName(u"outro_cranio")
        self.outro_cranio.setGeometry(QRect(150, 66, 121, 31))
        self.label_88 = QLabel(self.groupLesoes_17)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(20, 70, 51, 16))
        self.label_89 = QLabel(self.groupLesoes_17)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(20, 270, 71, 16))
        self.label_90 = QLabel(self.groupLesoes_17)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(20, 460, 81, 16))
        self.massas = QGroupBox(self.groupLesoes_17)
        self.massas.setObjectName(u"massas")
        self.massas.setGeometry(QRect(150, 130, 101, 51))
        self.gridLayout_101 = QGridLayout(self.massas)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.btn_sim_7 = QRadioButton(self.massas)
        self.btn_sim_7.setObjectName(u"btn_sim_7")

        self.gridLayout_101.addWidget(self.btn_sim_7, 0, 0, 1, 1)

        self.btn_nao_7 = QRadioButton(self.massas)
        self.btn_nao_7.setObjectName(u"btn_nao_7")

        self.gridLayout_101.addWidget(self.btn_nao_7, 0, 1, 1, 1)

        self.label_91 = QLabel(self.groupLesoes_17)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(20, 310, 61, 16))
        self.label_92 = QLabel(self.groupLesoes_17)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(20, 420, 121, 16))
        self.simetria_cranio = QGroupBox(self.groupLesoes_17)
        self.simetria_cranio.setObjectName(u"simetria_cranio")
        self.simetria_cranio.setGeometry(QRect(150, 90, 171, 51))
        self.gridLayout_102 = QGridLayout(self.simetria_cranio)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.btn_simetrico = QRadioButton(self.simetria_cranio)
        self.btn_simetrico.setObjectName(u"btn_simetrico")

        self.gridLayout_102.addWidget(self.btn_simetrico, 0, 0, 1, 1)

        self.btn_assimetrico = QRadioButton(self.simetria_cranio)
        self.btn_assimetrico.setObjectName(u"btn_assimetrico")

        self.gridLayout_102.addWidget(self.btn_assimetrico, 0, 1, 1, 1)

        self.label_93 = QLabel(self.groupLesoes_17)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(20, 380, 41, 16))
        self.forma_cranio = QGroupBox(self.groupLesoes_17)
        self.forma_cranio.setObjectName(u"forma_cranio")
        self.forma_cranio.setGeometry(QRect(150, 10, 151, 51))
        self.gridLayout_103 = QGridLayout(self.forma_cranio)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.btn_arredondado = QRadioButton(self.forma_cranio)
        self.btn_arredondado.setObjectName(u"btn_arredondado")

        self.gridLayout_103.addWidget(self.btn_arredondado, 0, 0, 1, 1)

        self.btn_oval = QRadioButton(self.forma_cranio)
        self.btn_oval.setObjectName(u"btn_oval")

        self.gridLayout_103.addWidget(self.btn_oval, 0, 1, 1, 1)

        self.escamas = QGroupBox(self.groupLesoes_17)
        self.escamas.setObjectName(u"escamas")
        self.escamas.setGeometry(QRect(150, 244, 101, 51))
        self.gridLayout_104 = QGridLayout(self.escamas)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.btn_sim_8 = QRadioButton(self.escamas)
        self.btn_sim_8.setObjectName(u"btn_sim_8")

        self.gridLayout_104.addWidget(self.btn_sim_8, 0, 0, 1, 1)

        self.btn_nao_8 = QRadioButton(self.escamas)
        self.btn_nao_8.setObjectName(u"btn_nao_8")

        self.gridLayout_104.addWidget(self.btn_nao_8, 0, 1, 1, 1)

        self.label_94 = QLabel(self.groupLesoes_17)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(20, 150, 61, 16))
        self.abaulamento = QGroupBox(self.groupLesoes_17)
        self.abaulamento.setObjectName(u"abaulamento")
        self.abaulamento.setGeometry(QRect(150, 170, 101, 51))
        self.gridLayout_105 = QGridLayout(self.abaulamento)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.btn_sim_9 = QRadioButton(self.abaulamento)
        self.btn_sim_9.setObjectName(u"btn_sim_9")

        self.gridLayout_105.addWidget(self.btn_sim_9, 0, 0, 1, 1)

        self.btn_nao_9 = QRadioButton(self.abaulamento)
        self.btn_nao_9.setObjectName(u"btn_nao_9")

        self.gridLayout_105.addWidget(self.btn_nao_9, 0, 1, 1, 1)

        self.cc_tipo = QLineEdit(self.groupLesoes_17)
        self.cc_tipo.setObjectName(u"cc_tipo")
        self.cc_tipo.setGeometry(QRect(150, 340, 121, 31))
        self.label_95 = QLabel(self.groupLesoes_17)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(20, 110, 61, 16))
        self.label_96 = QLabel(self.groupLesoes_17)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(20, 230, 71, 16))
        self.cabelos_cor = QGroupBox(self.groupLesoes_17)
        self.cabelos_cor.setObjectName(u"cabelos_cor")
        self.cabelos_cor.setGeometry(QRect(149, 394, 221, 51))
        self.gridLayout_106 = QGridLayout(self.cabelos_cor)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.btn_artificial = QRadioButton(self.cabelos_cor)
        self.btn_artificial.setObjectName(u"btn_artificial")

        self.gridLayout_106.addWidget(self.btn_artificial, 0, 1, 1, 1)

        self.btn_natural = QRadioButton(self.cabelos_cor)
        self.btn_natural.setObjectName(u"btn_natural")

        self.gridLayout_106.addWidget(self.btn_natural, 0, 0, 1, 1)

        self.btn_distribuicao = QRadioButton(self.cabelos_cor)
        self.btn_distribuicao.setObjectName(u"btn_distribuicao")

        self.gridLayout_106.addWidget(self.btn_distribuicao, 0, 2, 1, 1)

        self.label_97 = QLabel(self.groupLesoes_17)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(20, 190, 91, 16))
        self.lesoes = QGroupBox(self.groupLesoes_17)
        self.lesoes.setObjectName(u"lesoes")
        self.lesoes.setGeometry(QRect(150, 286, 101, 51))
        self.gridLayout_107 = QGridLayout(self.lesoes)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.btn_sim_10 = QRadioButton(self.lesoes)
        self.btn_sim_10.setObjectName(u"btn_sim_10")

        self.gridLayout_107.addWidget(self.btn_sim_10, 0, 0, 1, 1)

        self.btn_nao_10 = QRadioButton(self.lesoes)
        self.btn_nao_10.setObjectName(u"btn_nao_10")

        self.gridLayout_107.addWidget(self.btn_nao_10, 0, 1, 1, 1)

        self.label_98 = QLabel(self.groupLesoes_17)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(20, 30, 51, 16))
        self.cc_local = QLineEdit(self.groupLesoes_17)
        self.cc_local.setObjectName(u"cc_local")
        self.cc_local.setGeometry(QRect(150, 373, 121, 31))
        self.label_99 = QLabel(self.groupLesoes_17)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(20, 340, 41, 16))
        self.quantidade = QGroupBox(self.groupLesoes_17)
        self.quantidade.setObjectName(u"quantidade")
        self.quantidade.setGeometry(QRect(150, 435, 221, 51))
        self.gridLayout_108 = QGridLayout(self.quantidade)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.btn_preservada = QRadioButton(self.quantidade)
        self.btn_preservada.setObjectName(u"btn_preservada")

        self.gridLayout_108.addWidget(self.btn_preservada, 0, 0, 1, 1)

        self.btn_com_alteracao = QRadioButton(self.quantidade)
        self.btn_com_alteracao.setObjectName(u"btn_com_alteracao")

        self.gridLayout_108.addWidget(self.btn_com_alteracao, 0, 1, 1, 1)

        self.contorno = QLineEdit(self.groupLesoes_17)
        self.contorno.setObjectName(u"contorno")
        self.contorno.setGeometry(QRect(150, 223, 121, 31))
        self.label_100 = QLabel(self.groupLesoes_17)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(450, 70, 191, 31))
        self.label_101 = QLabel(self.groupLesoes_17)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(450, 190, 61, 16))
        self.prurido = QGroupBox(self.groupLesoes_17)
        self.prurido.setObjectName(u"prurido")
        self.prurido.setGeometry(QRect(660, 127, 101, 51))
        self.gridLayout_109 = QGridLayout(self.prurido)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.btn_sim_11 = QRadioButton(self.prurido)
        self.btn_sim_11.setObjectName(u"btn_sim_11")

        self.gridLayout_109.addWidget(self.btn_sim_11, 0, 0, 1, 1)

        self.btn_nao_11 = QRadioButton(self.prurido)
        self.btn_nao_11.setObjectName(u"btn_nao_11")

        self.gridLayout_109.addWidget(self.btn_nao_11, 0, 1, 1, 1)

        self.localizacao_das_anormalidades = QGroupBox(self.groupLesoes_17)
        self.localizacao_das_anormalidades.setObjectName(u"localizacao_das_anormalidades")
        self.localizacao_das_anormalidades.setGeometry(QRect(660, 50, 211, 51))
        self.gridLayout_110 = QGridLayout(self.localizacao_das_anormalidades)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.btn_anterior = QRadioButton(self.localizacao_das_anormalidades)
        self.btn_anterior.setObjectName(u"btn_anterior")

        self.gridLayout_110.addWidget(self.btn_anterior, 0, 0, 1, 1)

        self.btn_central = QRadioButton(self.localizacao_das_anormalidades)
        self.btn_central.setObjectName(u"btn_central")

        self.gridLayout_110.addWidget(self.btn_central, 0, 1, 1, 1)

        self.btn_posterior = QRadioButton(self.localizacao_das_anormalidades)
        self.btn_posterior.setObjectName(u"btn_posterior")

        self.gridLayout_110.addWidget(self.btn_posterior, 0, 2, 1, 1)

        self.label_102 = QLabel(self.groupLesoes_17)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(450, 270, 81, 16))
        self.tipo_alteracao_cabelo = QGroupBox(self.groupLesoes_17)
        self.tipo_alteracao_cabelo.setObjectName(u"tipo_alteracao_cabelo")
        self.tipo_alteracao_cabelo.setGeometry(QRect(660, 10, 441, 51))
        self.gridLayout_111 = QGridLayout(self.tipo_alteracao_cabelo)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.btn_queda = QRadioButton(self.tipo_alteracao_cabelo)
        self.btn_queda.setObjectName(u"btn_queda")

        self.gridLayout_111.addWidget(self.btn_queda, 0, 1, 1, 1)

        self.btn_alopecia = QRadioButton(self.tipo_alteracao_cabelo)
        self.btn_alopecia.setObjectName(u"btn_alopecia")

        self.gridLayout_111.addWidget(self.btn_alopecia, 0, 2, 1, 1)

        self.bt_hirutismo = QRadioButton(self.tipo_alteracao_cabelo)
        self.bt_hirutismo.setObjectName(u"bt_hirutismo")

        self.gridLayout_111.addWidget(self.bt_hirutismo, 0, 3, 1, 1)

        self.btn_calvicie = QRadioButton(self.tipo_alteracao_cabelo)
        self.btn_calvicie.setObjectName(u"btn_calvicie")

        self.gridLayout_111.addWidget(self.btn_calvicie, 0, 0, 1, 1)

        self.btn_hipertricose = QRadioButton(self.tipo_alteracao_cabelo)
        self.btn_hipertricose.setObjectName(u"btn_hipertricose")

        self.gridLayout_111.addWidget(self.btn_hipertricose, 0, 4, 1, 1)

        self.btn_madarose = QRadioButton(self.tipo_alteracao_cabelo)
        self.btn_madarose.setObjectName(u"btn_madarose")

        self.gridLayout_111.addWidget(self.btn_madarose, 0, 5, 1, 1)

        self.chs_outra = QLineEdit(self.groupLesoes_17)
        self.chs_outra.setObjectName(u"chs_outra")
        self.chs_outra.setGeometry(QRect(663, 262, 121, 31))
        self.label_103 = QLabel(self.groupLesoes_17)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(450, 230, 211, 21))
        self.condicoes_de_higiene_cranio = QGroupBox(self.groupLesoes_17)
        self.condicoes_de_higiene_cranio.setObjectName(u"condicoes_de_higiene_cranio")
        self.condicoes_de_higiene_cranio.setGeometry(QRect(660, 210, 141, 50))
        self.gridLayout_112 = QGridLayout(self.condicoes_de_higiene_cranio)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.btn_regular_2 = QRadioButton(self.condicoes_de_higiene_cranio)
        self.btn_regular_2.setObjectName(u"btn_regular_2")
        self.btn_regular_2.setStyleSheet(u"")

        self.gridLayout_112.addWidget(self.btn_regular_2, 0, 0, 1, 1)

        self.btn_precaria = QRadioButton(self.condicoes_de_higiene_cranio)
        self.btn_precaria.setObjectName(u"btn_precaria")

        self.gridLayout_112.addWidget(self.btn_precaria, 0, 1, 1, 1)

        self.label_104 = QLabel(self.groupLesoes_17)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(450, 144, 61, 16))
        self.label_105 = QLabel(self.groupLesoes_17)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(450, 110, 51, 16))
        self.label_106 = QLabel(self.groupLesoes_17)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(450, 43, 41, 16))
        self.parasitas = QGroupBox(self.groupLesoes_17)
        self.parasitas.setObjectName(u"parasitas")
        self.parasitas.setGeometry(QRect(660, 170, 101, 49))
        self.gridLayout_113 = QGridLayout(self.parasitas)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.btn_sim_12 = QRadioButton(self.parasitas)
        self.btn_sim_12.setObjectName(u"btn_sim_12")

        self.gridLayout_113.addWidget(self.btn_sim_12, 0, 0, 1, 1)

        self.btn_nao_12 = QRadioButton(self.parasitas)
        self.btn_nao_12.setObjectName(u"btn_nao_12")

        self.gridLayout_113.addWidget(self.btn_nao_12, 0, 1, 1, 1)

        self.la_outra = QLineEdit(self.groupLesoes_17)
        self.la_outra.setObjectName(u"la_outra")
        self.la_outra.setGeometry(QRect(660, 105, 121, 31))

        self.gridLayout_414.addWidget(self.groupLesoes_17, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_415 = QGridLayout(self.tab_10)
        self.gridLayout_415.setObjectName(u"gridLayout_415")
        self.groupLesoes_18 = QGroupBox(self.tab_10)
        self.groupLesoes_18.setObjectName(u"groupLesoes_18")
        self.groupLesoes_18.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.label_23 = QLabel(self.groupLesoes_18)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(40, 353, 69, 19))
        self.simetria_face = QGroupBox(self.groupLesoes_18)
        self.simetria_face.setObjectName(u"simetria_face")
        self.simetria_face.setGeometry(QRect(280, 130, 170, 50))
        self.gridLayout_46 = QGridLayout(self.simetria_face)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.btn_simetrica = QRadioButton(self.simetria_face)
        self.btn_simetrica.setObjectName(u"btn_simetrica")

        self.gridLayout_46.addWidget(self.btn_simetrica, 0, 0, 1, 1)

        self.btn_assimetrica = QRadioButton(self.simetria_face)
        self.btn_assimetrica.setObjectName(u"btn_assimetrica")

        self.gridLayout_46.addWidget(self.btn_assimetrica, 0, 1, 1, 1)

        self.dor_seios_frontais = QGroupBox(self.groupLesoes_18)
        self.dor_seios_frontais.setObjectName(u"dor_seios_frontais")
        self.dor_seios_frontais.setGeometry(QRect(280, 210, 94, 50))
        self.gridLayout_49 = QGridLayout(self.dor_seios_frontais)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.btn_sim_21 = QRadioButton(self.dor_seios_frontais)
        self.btn_sim_21.setObjectName(u"btn_sim_21")

        self.gridLayout_49.addWidget(self.btn_sim_21, 0, 0, 1, 1)

        self.btn_nao_21 = QRadioButton(self.dor_seios_frontais)
        self.btn_nao_21.setObjectName(u"btn_nao_21")

        self.gridLayout_49.addWidget(self.btn_nao_21, 0, 1, 1, 1)

        self.label_24 = QLabel(self.groupLesoes_18)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(40, 310, 221, 19))
        self.label_25 = QLabel(self.groupLesoes_18)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(40, 150, 69, 19))
        self.label_26 = QLabel(self.groupLesoes_18)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(40, 70, 79, 19))
        self.dor_seios_paranasais = QGroupBox(self.groupLesoes_18)
        self.dor_seios_paranasais.setObjectName(u"dor_seios_paranasais")
        self.dor_seios_paranasais.setGeometry(QRect(280, 250, 94, 50))
        self.gridLayout_48 = QGridLayout(self.dor_seios_paranasais)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.btn_sim_22 = QRadioButton(self.dor_seios_paranasais)
        self.btn_sim_22.setObjectName(u"btn_sim_22")

        self.gridLayout_48.addWidget(self.btn_sim_22, 0, 0, 1, 1)

        self.btn_nao_22 = QRadioButton(self.dor_seios_paranasais)
        self.btn_nao_22.setObjectName(u"btn_nao_22")

        self.gridLayout_48.addWidget(self.btn_nao_22, 0, 1, 1, 1)

        self.outras = QLineEdit(self.groupLesoes_18)
        self.outras.setObjectName(u"outras")
        self.outras.setGeometry(QRect(280, 350, 121, 31))
        self.formato = QGroupBox(self.groupLesoes_18)
        self.formato.setObjectName(u"formato")
        self.formato.setGeometry(QRect(280, 50, 183, 50))
        self.gridLayout_45 = QGridLayout(self.formato)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.btn_arredondar = QRadioButton(self.formato)
        self.btn_arredondar.setObjectName(u"btn_arredondar")

        self.gridLayout_45.addWidget(self.btn_arredondar, 0, 0, 1, 1)

        self.btn_triangular = QRadioButton(self.formato)
        self.btn_triangular.setObjectName(u"btn_triangular")

        self.gridLayout_45.addWidget(self.btn_triangular, 0, 1, 1, 1)

        self.label_27 = QLabel(self.groupLesoes_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 110, 59, 19))
        self.f_outro = QLineEdit(self.groupLesoes_18)
        self.f_outro.setObjectName(u"f_outro")
        self.f_outro.setGeometry(QRect(280, 106, 121, 31))
        self.dor_seios_maxilares = QGroupBox(self.groupLesoes_18)
        self.dor_seios_maxilares.setObjectName(u"dor_seios_maxilares")
        self.dor_seios_maxilares.setGeometry(QRect(280, 290, 101, 50))
        self.gridLayout_47 = QGridLayout(self.dor_seios_maxilares)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.btn_nao_23 = QRadioButton(self.dor_seios_maxilares)
        self.btn_nao_23.setObjectName(u"btn_nao_23")

        self.gridLayout_47.addWidget(self.btn_nao_23, 0, 1, 1, 1)

        self.btn_sim_23 = QRadioButton(self.dor_seios_maxilares)
        self.btn_sim_23.setObjectName(u"btn_sim_23")

        self.gridLayout_47.addWidget(self.btn_sim_23, 0, 0, 1, 1)

        self.label_28 = QLabel(self.groupLesoes_18)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 270, 231, 19))
        self.edema_palpebral = QGroupBox(self.groupLesoes_18)
        self.edema_palpebral.setObjectName(u"edema_palpebral")
        self.edema_palpebral.setGeometry(QRect(280, 170, 94, 50))
        self.gridLayout_50 = QGridLayout(self.edema_palpebral)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.btn_sim_24 = QRadioButton(self.edema_palpebral)
        self.btn_sim_24.setObjectName(u"btn_sim_24")

        self.gridLayout_50.addWidget(self.btn_sim_24, 0, 0, 1, 1)

        self.btn_nao_24 = QRadioButton(self.edema_palpebral)
        self.btn_nao_24.setObjectName(u"btn_nao_24")

        self.gridLayout_50.addWidget(self.btn_nao_24, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupLesoes_18)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(40, 190, 111, 19))
        self.label_30 = QLabel(self.groupLesoes_18)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(40, 230, 211, 19))

        self.gridLayout_415.addWidget(self.groupLesoes_18, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_416 = QGridLayout(self.tab_11)
        self.gridLayout_416.setObjectName(u"gridLayout_416")
        self.groupLesoes_19 = QGroupBox(self.tab_11)
        self.groupLesoes_19.setObjectName(u"groupLesoes_19")
        self.groupLesoes_19.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"      border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.acuidade_visual = QGroupBox(self.groupLesoes_19)
        self.acuidade_visual.setObjectName(u"acuidade_visual")
        self.acuidade_visual.setGeometry(QRect(200, 100, 194, 51))
        self.acuidade_visual.setStyleSheet(u"")
        self.acuidade_visual.setAlignment(Qt.AlignCenter)
        self.gridLayout_16 = QGridLayout(self.acuidade_visual)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.radioButton_49 = QRadioButton(self.acuidade_visual)
        self.radioButton_49.setObjectName(u"radioButton_49")
        self.radioButton_49.setFont(font6)

        self.gridLayout_16.addWidget(self.radioButton_49, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_50 = QRadioButton(self.acuidade_visual)
        self.radioButton_50.setObjectName(u"radioButton_50")
        self.radioButton_50.setFont(font6)

        self.gridLayout_16.addWidget(self.radioButton_50, 0, 1, 1, 1)

        self.fotorreativas = QGroupBox(self.groupLesoes_19)
        self.fotorreativas.setObjectName(u"fotorreativas")
        self.fotorreativas.setGeometry(QRect(200, 220, 117, 51))
        self.fotorreativas.setStyleSheet(u"")
        self.fotorreativas.setAlignment(Qt.AlignCenter)
        self.gridLayout_17 = QGridLayout(self.fotorreativas)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.radioButton_51 = QRadioButton(self.fotorreativas)
        self.radioButton_51.setObjectName(u"radioButton_51")
        self.radioButton_51.setFont(font6)

        self.gridLayout_17.addWidget(self.radioButton_51, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_52 = QRadioButton(self.fotorreativas)
        self.radioButton_52.setObjectName(u"radioButton_52")
        self.radioButton_52.setFont(font6)

        self.gridLayout_17.addWidget(self.radioButton_52, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupLesoes_19)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 118, 19))
        self.label_3.setFont(font6)
        self.halo_senil = QGroupBox(self.groupLesoes_19)
        self.halo_senil.setObjectName(u"halo_senil")
        self.halo_senil.setGeometry(QRect(200, 260, 179, 51))
        self.halo_senil.setStyleSheet(u"")
        self.halo_senil.setAlignment(Qt.AlignCenter)
        self.gridLayout_18 = QGridLayout(self.halo_senil)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.radioButton_53 = QRadioButton(self.halo_senil)
        self.radioButton_53.setObjectName(u"radioButton_53")
        self.radioButton_53.setFont(font6)

        self.gridLayout_18.addWidget(self.radioButton_53, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_54 = QRadioButton(self.halo_senil)
        self.radioButton_54.setObjectName(u"radioButton_54")
        self.radioButton_54.setFont(font6)

        self.gridLayout_18.addWidget(self.radioButton_54, 0, 1, 1, 1)

        self.distancia = QGroupBox(self.groupLesoes_19)
        self.distancia.setObjectName(u"distancia")
        self.distancia.setGeometry(QRect(200, 60, 220, 51))
        self.distancia.setStyleSheet(u"")
        self.distancia.setAlignment(Qt.AlignCenter)
        self.gridLayout_19 = QGridLayout(self.distancia)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.radioButton_55 = QRadioButton(self.distancia)
        self.radioButton_55.setObjectName(u"radioButton_55")
        self.radioButton_55.setFont(font6)

        self.gridLayout_19.addWidget(self.radioButton_55, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_56 = QRadioButton(self.distancia)
        self.radioButton_56.setObjectName(u"radioButton_56")
        self.radioButton_56.setFont(font6)

        self.gridLayout_19.addWidget(self.radioButton_56, 0, 1, 1, 1)

        self.label_269 = QLabel(self.groupLesoes_19)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setGeometry(QRect(30, 40, 79, 19))
        self.label_269.setFont(font6)
        self.label_299 = QLabel(self.groupLesoes_19)
        self.label_299.setObjectName(u"label_299")
        self.label_299.setGeometry(QRect(30, 460, 151, 19))
        self.label_299.setFont(font6)
        self.label_299.setStyleSheet(u"font-size: 16px;")
        self.coloracao_olhos = QLineEdit(self.groupLesoes_19)
        self.coloracao_olhos.setObjectName(u"coloracao_olhos")
        self.coloracao_olhos.setGeometry(QRect(200, 423, 121, 31))
        self.label_263 = QLabel(self.groupLesoes_19)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setGeometry(QRect(30, 320, 73, 19))
        self.label_263.setFont(font6)
        self.esclerotica = QLabel(self.groupLesoes_19)
        self.esclerotica.setObjectName(u"esclerotica")
        self.esclerotica.setGeometry(QRect(30, 400, 161, 19))
        self.esclerotica.setFont(font6)
        self.esclerotica.setStyleSheet(u"font-size: 16px;")
        self.presenca_de_secrecoes = QGroupBox(self.groupLesoes_19)
        self.presenca_de_secrecoes.setObjectName(u"presenca_de_secrecoes")
        self.presenca_de_secrecoes.setGeometry(QRect(200, 342, 101, 51))
        self.presenca_de_secrecoes.setStyleSheet(u"")
        self.presenca_de_secrecoes.setAlignment(Qt.AlignCenter)
        self.gridLayout_20 = QGridLayout(self.presenca_de_secrecoes)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.radioButton_57 = QRadioButton(self.presenca_de_secrecoes)
        self.radioButton_57.setObjectName(u"radioButton_57")
        self.radioButton_57.setFont(font6)

        self.gridLayout_20.addWidget(self.radioButton_57, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_58 = QRadioButton(self.presenca_de_secrecoes)
        self.radioButton_58.setObjectName(u"radioButton_58")
        self.radioButton_58.setFont(font6)

        self.gridLayout_20.addWidget(self.radioButton_58, 0, 1, 1, 1)

        self.tamanho = QGroupBox(self.groupLesoes_19)
        self.tamanho.setObjectName(u"tamanho")
        self.tamanho.setGeometry(QRect(200, 180, 212, 50))
        self.tamanho.setStyleSheet(u"")
        self.tamanho.setAlignment(Qt.AlignCenter)
        self.gridLayout_21 = QGridLayout(self.tamanho)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.radioButton_60 = QRadioButton(self.tamanho)
        self.radioButton_60.setObjectName(u"radioButton_60")
        self.radioButton_60.setFont(font6)

        self.gridLayout_21.addWidget(self.radioButton_60, 0, 0, 1, 1)

        self.radioButton_61 = QRadioButton(self.tamanho)
        self.radioButton_61.setObjectName(u"radioButton_61")
        self.radioButton_61.setFont(font6)

        self.gridLayout_21.addWidget(self.radioButton_61, 0, 1, 1, 1)

        self.radioButton_59 = QRadioButton(self.tamanho)
        self.radioButton_59.setObjectName(u"radioButton_59")
        self.radioButton_59.setFont(font6)

        self.gridLayout_21.addWidget(self.radioButton_59, 0, 2, 1, 1)

        self.label_259 = QLabel(self.groupLesoes_19)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setGeometry(QRect(30, 240, 97, 19))
        self.label_259.setFont(font6)
        self.label_271 = QLabel(self.groupLesoes_19)
        self.label_271.setObjectName(u"label_271")
        self.label_271.setGeometry(QRect(30, 80, 69, 19))
        self.label_271.setFont(font6)
        self.label_272 = QLabel(self.groupLesoes_19)
        self.label_272.setObjectName(u"label_272")
        self.label_272.setGeometry(QRect(30, 490, 83, 19))
        self.label_272.setFont(font6)
        self.label_268 = QLabel(self.groupLesoes_19)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setGeometry(QRect(30, 427, 76, 19))
        self.label_268.setFont(font6)
        self.label_260 = QLabel(self.groupLesoes_19)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setGeometry(QRect(30, 200, 73, 19))
        self.label_260.setFont(font6)
        self.label_261 = QLabel(self.groupLesoes_19)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setGeometry(QRect(30, 280, 77, 19))
        self.label_261.setFont(font6)
        self.label_262 = QLabel(self.groupLesoes_19)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setGeometry(QRect(30, 360, 164, 19))
        self.label_262.setFont(font6)
        self.conjuntiva = QGroupBox(self.groupLesoes_19)
        self.conjuntiva.setObjectName(u"conjuntiva")
        self.conjuntiva.setGeometry(QRect(200, 300, 570, 51))
        self.conjuntiva.setStyleSheet(u"")
        self.conjuntiva.setAlignment(Qt.AlignCenter)
        self.gridLayout_22 = QGridLayout(self.conjuntiva)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.radioButton_62 = QRadioButton(self.conjuntiva)
        self.radioButton_62.setObjectName(u"radioButton_62")
        self.radioButton_62.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_62, 1, 3, 1, 1)

        self.radioButton_63 = QRadioButton(self.conjuntiva)
        self.radioButton_63.setObjectName(u"radioButton_63")
        self.radioButton_63.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_63, 1, 1, 1, 1)

        self.radioButton_64 = QRadioButton(self.conjuntiva)
        self.radioButton_64.setObjectName(u"radioButton_64")
        self.radioButton_64.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_64, 1, 4, 1, 1)

        self.radioButton_65 = QRadioButton(self.conjuntiva)
        self.radioButton_65.setObjectName(u"radioButton_65")
        self.radioButton_65.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_65, 1, 0, 1, 1, Qt.AlignTop)

        self.radioButton_66 = QRadioButton(self.conjuntiva)
        self.radioButton_66.setObjectName(u"radioButton_66")
        self.radioButton_66.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_66, 1, 2, 1, 1)

        self.radioButton_67 = QRadioButton(self.conjuntiva)
        self.radioButton_67.setObjectName(u"radioButton_67")
        self.radioButton_67.setFont(font6)

        self.gridLayout_22.addWidget(self.radioButton_67, 1, 5, 1, 1)

        self.simetricos = QGroupBox(self.groupLesoes_19)
        self.simetricos.setObjectName(u"simetricos")
        self.simetricos.setGeometry(QRect(200, 20, 101, 51))
        self.simetricos.setStyleSheet(u"")
        self.simetricos.setAlignment(Qt.AlignCenter)
        self.gridLayout_23 = QGridLayout(self.simetricos)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.radioButton_68 = QRadioButton(self.simetricos)
        self.radioButton_68.setObjectName(u"radioButton_68")
        self.radioButton_68.setFont(font6)

        self.gridLayout_23.addWidget(self.radioButton_68, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_69 = QRadioButton(self.simetricos)
        self.radioButton_69.setObjectName(u"radioButton_69")
        self.radioButton_69.setFont(font6)

        self.gridLayout_23.addWidget(self.radioButton_69, 0, 1, 1, 1)

        self.integridade_2 = QLabel(self.groupLesoes_19)
        self.integridade_2.setObjectName(u"integridade_2")
        self.integridade_2.setGeometry(QRect(30, 160, 71, 19))
        self.integridade_2.setFont(font6)
        self.integridade_2.setStyleSheet(u"font-size: 16px;")
        self.preservada = QGroupBox(self.groupLesoes_19)
        self.preservada.setObjectName(u"preservada")
        self.preservada.setGeometry(QRect(200, 460, 101, 51))
        self.preservada.setStyleSheet(u"")
        self.preservada.setAlignment(Qt.AlignCenter)
        self.gridLayout_24 = QGridLayout(self.preservada)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.radioButton_70 = QRadioButton(self.preservada)
        self.radioButton_70.setObjectName(u"radioButton_70")
        self.radioButton_70.setFont(font6)

        self.gridLayout_24.addWidget(self.radioButton_70, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_71 = QRadioButton(self.preservada)
        self.radioButton_71.setObjectName(u"radioButton_71")
        self.radioButton_71.setFont(font6)

        self.gridLayout_24.addWidget(self.radioButton_71, 0, 1, 1, 1)

        self.descricao_forumen = QLineEdit(self.groupLesoes_19)
        self.descricao_forumen.setObjectName(u"descricao_forumen")
        self.descricao_forumen.setGeometry(QRect(870, 127, 121, 31))
        self.integro = QLabel(self.groupLesoes_19)
        self.integro.setObjectName(u"integro")
        self.integro.setGeometry(QRect(610, 130, 101, 19))
        self.integro.setFont(font6)
        self.label_274 = QLabel(self.groupLesoes_19)
        self.label_274.setObjectName(u"label_274")
        self.label_274.setGeometry(QRect(610, 60, 157, 19))
        self.label_274.setFont(font6)
        self.label_275 = QLabel(self.groupLesoes_19)
        self.label_275.setObjectName(u"label_275")
        self.label_275.setGeometry(QRect(610, 100, 171, 19))
        self.label_275.setFont(font6)
        self.label_275.setStyleSheet(u"font-size: 16px;")
        self.descricao_movimento_ocular = QLineEdit(self.groupLesoes_19)
        self.descricao_movimento_ocular.setObjectName(u"descricao_movimento_ocular")
        self.descricao_movimento_ocular.setGeometry(QRect(960, 58, 121, 30))
        self.label_256 = QLabel(self.groupLesoes_19)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setGeometry(QRect(610, 173, 53, 19))
        self.label_256.setFont(font6)
        self.forumen_lacrimal = QGroupBox(self.groupLesoes_19)
        self.forumen_lacrimal.setObjectName(u"forumen_lacrimal")
        self.forumen_lacrimal.setGeometry(QRect(760, 110, 101, 51))
        self.forumen_lacrimal.setStyleSheet(u"")
        self.forumen_lacrimal.setAlignment(Qt.AlignCenter)
        self.gridLayout_25 = QGridLayout(self.forumen_lacrimal)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.radioButton_72 = QRadioButton(self.forumen_lacrimal)
        self.radioButton_72.setObjectName(u"radioButton_72")
        self.radioButton_72.setFont(font6)

        self.gridLayout_25.addWidget(self.radioButton_72, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_73 = QRadioButton(self.forumen_lacrimal)
        self.radioButton_73.setObjectName(u"radioButton_73")
        self.radioButton_73.setFont(font6)

        self.gridLayout_25.addWidget(self.radioButton_73, 0, 1, 1, 1)

        self.outras_obs_olhos = QLineEdit(self.groupLesoes_19)
        self.outras_obs_olhos.setObjectName(u"outras_obs_olhos")
        self.outras_obs_olhos.setGeometry(QRect(760, 170, 121, 31))
        self.movimentos_oculares = QGroupBox(self.groupLesoes_19)
        self.movimentos_oculares.setObjectName(u"movimentos_oculares")
        self.movimentos_oculares.setGeometry(QRect(760, 40, 191, 51))
        self.movimentos_oculares.setStyleSheet(u"")
        self.movimentos_oculares.setAlignment(Qt.AlignCenter)
        self.gridLayout_26 = QGridLayout(self.movimentos_oculares)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.radioButton_74 = QRadioButton(self.movimentos_oculares)
        self.radioButton_74.setObjectName(u"radioButton_74")
        self.radioButton_74.setFont(font6)

        self.gridLayout_26.addWidget(self.radioButton_74, 0, 0, 1, 1, Qt.AlignTop)

        self.radioButton_75 = QRadioButton(self.movimentos_oculares)
        self.radioButton_75.setObjectName(u"radioButton_75")
        self.radioButton_75.setFont(font6)

        self.gridLayout_26.addWidget(self.radioButton_75, 0, 1, 1, 1)

        self.acuidade_visual.raise_()
        self.fotorreativas.raise_()
        self.label_3.raise_()
        self.halo_senil.raise_()
        self.distancia.raise_()
        self.label_269.raise_()
        self.label_299.raise_()
        self.coloracao_olhos.raise_()
        self.label_263.raise_()
        self.esclerotica.raise_()
        self.presenca_de_secrecoes.raise_()
        self.tamanho.raise_()
        self.label_259.raise_()
        self.label_271.raise_()
        self.label_272.raise_()
        self.label_268.raise_()
        self.label_260.raise_()
        self.label_261.raise_()
        self.label_262.raise_()
        self.conjuntiva.raise_()
        self.simetricos.raise_()
        self.integridade_2.raise_()
        self.preservada.raise_()
        self.descricao_forumen.raise_()
        self.integro.raise_()
        self.label_274.raise_()
        self.label_275.raise_()
        self.descricao_movimento_ocular.raise_()
        self.forumen_lacrimal.raise_()
        self.outras_obs_olhos.raise_()
        self.movimentos_oculares.raise_()
        self.label_256.raise_()

        self.gridLayout_416.addWidget(self.groupLesoes_19, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_417 = QGridLayout(self.tab_12)
        self.gridLayout_417.setObjectName(u"gridLayout_417")
        self.groupLesoes_20 = QGroupBox(self.tab_12)
        self.groupLesoes_20.setObjectName(u"groupLesoes_20")
        self.groupLesoes_20.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"    border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.label_11 = QLabel(self.groupLesoes_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 310, 167, 18))
        self.label_11.setFont(font6)
        self.simetria_narinas = QGroupBox(self.groupLesoes_20)
        self.simetria_narinas.setObjectName(u"simetria_narinas")
        self.simetria_narinas.setGeometry(QRect(210, 40, 191, 51))
        self.simetria_narinas.setStyleSheet(u"")
        self.gridLayout_33 = QGridLayout(self.simetria_narinas)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.radio_simetricas_3 = QRadioButton(self.simetria_narinas)
        self.radio_simetricas_3.setObjectName(u"radio_simetricas_3")
        self.radio_simetricas_3.setFont(font6)

        self.gridLayout_33.addWidget(self.radio_simetricas_3, 0, 1, 1, 1)

        self.radio_simetricas_4 = QRadioButton(self.simetria_narinas)
        self.radio_simetricas_4.setObjectName(u"radio_simetricas_4")
        self.radio_simetricas_4.setFont(font6)

        self.gridLayout_33.addWidget(self.radio_simetricas_4, 0, 0, 1, 1)

        self.coloracao_externa = QLineEdit(self.groupLesoes_20)
        self.coloracao_externa.setObjectName(u"coloracao_externa")
        self.coloracao_externa.setGeometry(QRect(210, 220, 121, 31))
        self.coloracao_interna = QGroupBox(self.groupLesoes_20)
        self.coloracao_interna.setObjectName(u"coloracao_interna")
        self.coloracao_interna.setGeometry(QRect(210, 330, 101, 51))
        self.gridLayout_34 = QGridLayout(self.coloracao_interna)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.radioButton_90 = QRadioButton(self.coloracao_interna)
        self.radioButton_90.setObjectName(u"radioButton_90")
        self.radioButton_90.setFont(font6)

        self.gridLayout_34.addWidget(self.radioButton_90, 0, 2, 1, 1)

        self.radioButton_91 = QRadioButton(self.coloracao_interna)
        self.radioButton_91.setObjectName(u"radioButton_91")
        self.radioButton_91.setFont(font6)

        self.gridLayout_34.addWidget(self.radioButton_91, 0, 1, 1, 1)

        self.secrecoes = QGroupBox(self.groupLesoes_20)
        self.secrecoes.setObjectName(u"secrecoes")
        self.secrecoes.setGeometry(QRect(210, 370, 101, 51))
        self.gridLayout_36 = QGridLayout(self.secrecoes)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.radioButton_92 = QRadioButton(self.secrecoes)
        self.radioButton_92.setObjectName(u"radioButton_92")
        self.radioButton_92.setFont(font6)

        self.gridLayout_36.addWidget(self.radioButton_92, 0, 0, 1, 1)

        self.radioButton_93 = QRadioButton(self.secrecoes)
        self.radioButton_93.setObjectName(u"radioButton_93")
        self.radioButton_93.setFont(font6)

        self.gridLayout_36.addWidget(self.radioButton_93, 0, 1, 1, 1)

        self.lesoes_narinas = QGroupBox(self.groupLesoes_20)
        self.lesoes_narinas.setObjectName(u"lesoes_narinas")
        self.lesoes_narinas.setGeometry(QRect(210, 120, 101, 51))
        self.gridLayout_38 = QGridLayout(self.lesoes_narinas)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.radioButton_94 = QRadioButton(self.lesoes_narinas)
        self.radioButton_94.setObjectName(u"radioButton_94")
        self.radioButton_94.setFont(font6)

        self.gridLayout_38.addWidget(self.radioButton_94, 0, 2, 1, 1)

        self.radioButton_95 = QRadioButton(self.lesoes_narinas)
        self.radioButton_95.setObjectName(u"radioButton_95")
        self.radioButton_95.setFont(font6)

        self.gridLayout_38.addWidget(self.radioButton_95, 0, 1, 1, 1)

        self.integridade_preserva = QLineEdit(self.groupLesoes_20)
        self.integridade_preserva.setObjectName(u"integridade_preserva")
        self.integridade_preserva.setGeometry(QRect(210, 306, 121, 31))
        self.label_15 = QLabel(self.groupLesoes_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 180, 63, 18))
        self.label_15.setFont(font6)
        self.label_8 = QLabel(self.groupLesoes_20)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 60, 63, 18))
        self.label_8.setFont(font6)
        self.integridade_preservada_narinas = QGroupBox(self.groupLesoes_20)
        self.integridade_preservada_narinas.setObjectName(u"integridade_preservada_narinas")
        self.integridade_preservada_narinas.setGeometry(QRect(210, 80, 101, 51))
        self.gridLayout_39 = QGridLayout(self.integridade_preservada_narinas)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.radio_sim_4 = QRadioButton(self.integridade_preservada_narinas)
        self.radio_sim_4.setObjectName(u"radio_sim_4")
        self.radio_sim_4.setFont(font6)

        self.gridLayout_39.addWidget(self.radio_sim_4, 0, 0, 1, 1)

        self.radioButton_96 = QRadioButton(self.integridade_preservada_narinas)
        self.radioButton_96.setObjectName(u"radioButton_96")
        self.radioButton_96.setFont(font6)

        self.gridLayout_39.addWidget(self.radioButton_96, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupLesoes_20)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 140, 56, 18))
        self.label_9.setFont(font6)
        self.label_16 = QLabel(self.groupLesoes_20)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 350, 77, 18))
        self.label_16.setFont(font6)
        self.label_18 = QLabel(self.groupLesoes_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(40, 436, 34, 18))
        self.label_18.setFont(font6)
        self.label_17 = QLabel(self.groupLesoes_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(40, 220, 77, 18))
        self.label_17.setFont(font6)
        self.label_19 = QLabel(self.groupLesoes_20)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 100, 167, 18))
        self.label_19.setFont(font6)
        self.label_20 = QLabel(self.groupLesoes_20)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(40, 270, 116, 18))
        self.label_20.setFont(font6)
        self.edemas_simetria = QGroupBox(self.groupLesoes_20)
        self.edemas_simetria.setObjectName(u"edemas_simetria")
        self.edemas_simetria.setGeometry(QRect(210, 160, 101, 51))
        self.gridLayout_40 = QGridLayout(self.edemas_simetria)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.radioButton_97 = QRadioButton(self.edemas_simetria)
        self.radioButton_97.setObjectName(u"radioButton_97")
        self.radioButton_97.setFont(font6)

        self.gridLayout_40.addWidget(self.radioButton_97, 0, 1, 1, 1)

        self.radioButton_98 = QRadioButton(self.edemas_simetria)
        self.radioButton_98.setObjectName(u"radioButton_98")
        self.radioButton_98.setFont(font6)

        self.gridLayout_40.addWidget(self.radioButton_98, 0, 0, 1, 1)

        self.label_21 = QLabel(self.groupLesoes_20)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(40, 395, 80, 18))
        self.label_21.setFont(font6)
        self.cavidade_nasal = QGroupBox(self.groupLesoes_20)
        self.cavidade_nasal.setObjectName(u"cavidade_nasal")
        self.cavidade_nasal.setGeometry(QRect(210, 248, 101, 51))
        self.gridLayout_41 = QGridLayout(self.cavidade_nasal)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.radioButton_99 = QRadioButton(self.cavidade_nasal)
        self.radioButton_99.setObjectName(u"radioButton_99")
        self.radioButton_99.setFont(font6)

        self.gridLayout_41.addWidget(self.radioButton_99, 0, 1, 1, 1)

        self.radioButton_100 = QRadioButton(self.cavidade_nasal)
        self.radioButton_100.setObjectName(u"radioButton_100")
        self.radioButton_100.setFont(font6)

        self.gridLayout_41.addWidget(self.radioButton_100, 0, 0, 1, 1)

        self.tipo_secrecao_nasal = QGroupBox(self.groupLesoes_20)
        self.tipo_secrecao_nasal.setObjectName(u"tipo_secrecao_nasal")
        self.tipo_secrecao_nasal.setGeometry(QRect(208, 412, 186, 51))
        self.gridLayout_174 = QGridLayout(self.tipo_secrecao_nasal)
        self.gridLayout_174.setObjectName(u"gridLayout_174")
        self.radioButton_102 = QRadioButton(self.tipo_secrecao_nasal)
        self.radioButton_102.setObjectName(u"radioButton_102")
        self.radioButton_102.setFont(font6)

        self.gridLayout_174.addWidget(self.radioButton_102, 0, 0, 1, 1)

        self.radioButton_103 = QRadioButton(self.tipo_secrecao_nasal)
        self.radioButton_103.setObjectName(u"radioButton_103")
        self.radioButton_103.setFont(font6)

        self.gridLayout_174.addWidget(self.radioButton_103, 0, 1, 1, 1)

        self.outras_narinas = QLineEdit(self.groupLesoes_20)
        self.outras_narinas.setObjectName(u"outras_narinas")
        self.outras_narinas.setGeometry(QRect(204, 598, 133, 31))
        self.label_312 = QLabel(self.groupLesoes_20)
        self.label_312.setObjectName(u"label_312")
        self.label_312.setGeometry(QRect(38, 482, 67, 18))
        self.label_312.setFont(font6)
        self.label_313 = QLabel(self.groupLesoes_20)
        self.label_313.setObjectName(u"label_313")
        self.label_313.setGeometry(QRect(37, 600, 51, 20))
        self.label_313.setFont(font6)
        self.tamanho_narinas = QGroupBox(self.groupLesoes_20)
        self.tamanho_narinas.setObjectName(u"tamanho_narinas")
        self.tamanho_narinas.setGeometry(QRect(207, 454, 137, 51))
        self.gridLayout_175 = QGridLayout(self.tamanho_narinas)
        self.gridLayout_175.setObjectName(u"gridLayout_175")
        self.radioButton_148 = QRadioButton(self.tamanho_narinas)
        self.radioButton_148.setObjectName(u"radioButton_148")
        self.radioButton_148.setFont(font6)

        self.gridLayout_175.addWidget(self.radioButton_148, 0, 0, 1, 1)

        self.radioButton_152 = QRadioButton(self.tamanho_narinas)
        self.radioButton_152.setObjectName(u"radioButton_152")
        self.radioButton_152.setFont(font6)

        self.gridLayout_175.addWidget(self.radioButton_152, 0, 1, 1, 1)

        self.radioButton_153 = QRadioButton(self.tamanho_narinas)
        self.radioButton_153.setObjectName(u"radioButton_153")
        self.radioButton_153.setFont(font6)

        self.gridLayout_175.addWidget(self.radioButton_153, 0, 2, 1, 1)

        self.label_314 = QLabel(self.groupLesoes_20)
        self.label_314.setObjectName(u"label_314")
        self.label_314.setGeometry(QRect(37, 523, 121, 18))
        self.label_314.setFont(font6)
        self.desvio_de_septo = QGroupBox(self.groupLesoes_20)
        self.desvio_de_septo.setObjectName(u"desvio_de_septo")
        self.desvio_de_septo.setGeometry(QRect(206, 496, 141, 51))
        self.gridLayout_176 = QGridLayout(self.desvio_de_septo)
        self.gridLayout_176.setObjectName(u"gridLayout_176")
        self.radioButton_154 = QRadioButton(self.desvio_de_septo)
        self.radioButton_154.setObjectName(u"radioButton_154")
        self.radioButton_154.setFont(font6)

        self.gridLayout_176.addWidget(self.radioButton_154, 0, 0, 1, 1)

        self.radioButton_155 = QRadioButton(self.desvio_de_septo)
        self.radioButton_155.setObjectName(u"radioButton_155")
        self.radioButton_155.setFont(font6)

        self.gridLayout_176.addWidget(self.radioButton_155, 0, 1, 1, 1)

        self.olfato = QGroupBox(self.groupLesoes_20)
        self.olfato.setObjectName(u"olfato")
        self.olfato.setGeometry(QRect(204, 538, 310, 51))
        self.gridLayout_177 = QGridLayout(self.olfato)
        self.gridLayout_177.setObjectName(u"gridLayout_177")
        self.radioButton_156 = QRadioButton(self.olfato)
        self.radioButton_156.setObjectName(u"radioButton_156")
        self.radioButton_156.setFont(font6)

        self.gridLayout_177.addWidget(self.radioButton_156, 0, 0, 1, 1)

        self.radioButton_157 = QRadioButton(self.olfato)
        self.radioButton_157.setObjectName(u"radioButton_157")
        self.radioButton_157.setFont(font6)

        self.gridLayout_177.addWidget(self.radioButton_157, 0, 1, 1, 1)

        self.radioButton_158 = QRadioButton(self.olfato)
        self.radioButton_158.setObjectName(u"radioButton_158")
        self.radioButton_158.setFont(font6)

        self.gridLayout_177.addWidget(self.radioButton_158, 0, 2, 1, 1)

        self.label_315 = QLabel(self.groupLesoes_20)
        self.label_315.setObjectName(u"label_315")
        self.label_315.setGeometry(QRect(38, 565, 45, 18))
        self.label_315.setFont(font6)

        self.gridLayout_417.addWidget(self.groupLesoes_20, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_115 = QGridLayout(self.tab_14)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.groupLesoes_22 = QGroupBox(self.tab_14)
        self.groupLesoes_22.setObjectName(u"groupLesoes_22")
        self.groupLesoes_22.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"      border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.groupBox_150 = QGroupBox(self.groupLesoes_22)
        self.groupBox_150.setObjectName(u"groupBox_150")
        self.groupBox_150.setGeometry(QRect(120, 30, 224, 46))
        self.groupBox_150.setStyleSheet(u"border: none;\n"
"")
        self.gridLayout_299 = QGridLayout(self.groupBox_150)
        self.gridLayout_299.setObjectName(u"gridLayout_299")
        self.groupBox_151 = QGroupBox(self.groupLesoes_22)
        self.groupBox_151.setObjectName(u"groupBox_151")
        self.groupBox_151.setGeometry(QRect(180, 70, 119, 46))
        self.groupBox_151.setStyleSheet(u"border: none;")
        self.gridLayout_300 = QGridLayout(self.groupBox_151)
        self.gridLayout_300.setObjectName(u"gridLayout_300")
        self.groupBox_152 = QGroupBox(self.groupLesoes_22)
        self.groupBox_152.setObjectName(u"groupBox_152")
        self.groupBox_152.setGeometry(QRect(180, 115, 209, 41))
        self.groupBox_152.setStyleSheet(u"border: none;")
        self.gridLayout_301 = QGridLayout(self.groupBox_152)
        self.gridLayout_301.setObjectName(u"gridLayout_301")
        self.groupBox_154 = QGroupBox(self.groupLesoes_22)
        self.groupBox_154.setObjectName(u"groupBox_154")
        self.groupBox_154.setGeometry(QRect(160, 190, 178, 46))
        self.groupBox_154.setStyleSheet(u"border: none;")
        self.gridLayout_303 = QGridLayout(self.groupBox_154)
        self.gridLayout_303.setObjectName(u"gridLayout_303")
        self.groupBox_155 = QGroupBox(self.groupLesoes_22)
        self.groupBox_155.setObjectName(u"groupBox_155")
        self.groupBox_155.setGeometry(QRect(270, 230, 119, 46))
        self.groupBox_155.setStyleSheet(u"border: none;")
        self.gridLayout_305 = QGridLayout(self.groupBox_155)
        self.gridLayout_305.setObjectName(u"gridLayout_305")
        self.integridade_preservada_pa = QGroupBox(self.groupLesoes_22)
        self.integridade_preservada_pa.setObjectName(u"integridade_preservada_pa")
        self.integridade_preservada_pa.setGeometry(QRect(200, 16, 101, 51))
        self.integridade_preservada_pa.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.integridade_preservada_pa)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.opcao_sim_ip = QRadioButton(self.integridade_preservada_pa)
        self.opcao_sim_ip.setObjectName(u"opcao_sim_ip")
        self.opcao_sim_ip.setFont(font6)
        self.opcao_sim_ip.setStyleSheet(u"border-radius:none;")

        self.gridLayout_2.addWidget(self.opcao_sim_ip, 0, 0, 1, 1)

        self.opcao_nao_ip = QRadioButton(self.integridade_preservada_pa)
        self.opcao_nao_ip.setObjectName(u"opcao_nao_ip")
        self.opcao_nao_ip.setFont(font6)

        self.gridLayout_2.addWidget(self.opcao_nao_ip, 0, 1, 1, 1)

        self.label_276 = QLabel(self.groupLesoes_22)
        self.label_276.setObjectName(u"label_276")
        self.label_276.setGeometry(QRect(20, 80, 159, 19))
        self.label_276.setFont(font6)
        self.label_280 = QLabel(self.groupLesoes_22)
        self.label_280.setObjectName(u"label_280")
        self.label_280.setGeometry(QRect(20, 160, 118, 19))
        self.label_280.setFont(font6)
        self.acuidade_auditiva_pa = QGroupBox(self.groupLesoes_22)
        self.acuidade_auditiva_pa.setObjectName(u"acuidade_auditiva_pa")
        self.acuidade_auditiva_pa.setGeometry(QRect(200, 257, 211, 51))
        self.acuidade_auditiva_pa.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.acuidade_auditiva_pa)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.opcao_diminuida_aa = QRadioButton(self.acuidade_auditiva_pa)
        self.opcao_diminuida_aa.setObjectName(u"opcao_diminuida_aa")
        self.opcao_diminuida_aa.setFont(font6)

        self.gridLayout_7.addWidget(self.opcao_diminuida_aa, 0, 2, 1, 1)

        self.opcao_preservada_aa = QRadioButton(self.acuidade_auditiva_pa)
        self.opcao_preservada_aa.setObjectName(u"opcao_preservada_aa")
        self.opcao_preservada_aa.setFont(font6)

        self.gridLayout_7.addWidget(self.opcao_preservada_aa, 0, 1, 1, 1)

        self.label_283 = QLabel(self.groupLesoes_22)
        self.label_283.setObjectName(u"label_283")
        self.label_283.setGeometry(QRect(20, 240, 145, 19))
        self.label_283.setFont(font6)
        self.condicoes_de_higiene_pa = QGroupBox(self.groupLesoes_22)
        self.condicoes_de_higiene_pa.setObjectName(u"condicoes_de_higiene_pa")
        self.condicoes_de_higiene_pa.setGeometry(QRect(200, 97, 161, 51))
        self.condicoes_de_higiene_pa.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.condicoes_de_higiene_pa)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.opcao_satisfatoria_ch = QRadioButton(self.condicoes_de_higiene_pa)
        self.opcao_satisfatoria_ch.setObjectName(u"opcao_satisfatoria_ch")
        self.opcao_satisfatoria_ch.setFont(font6)

        self.gridLayout_5.addWidget(self.opcao_satisfatoria_ch, 0, 0, 1, 1)

        self.opcao_precaria_ch = QRadioButton(self.condicoes_de_higiene_pa)
        self.opcao_precaria_ch.setObjectName(u"opcao_precaria_ch")
        self.opcao_precaria_ch.setFont(font6)

        self.gridLayout_5.addWidget(self.opcao_precaria_ch, 0, 1, 1, 1)

        self.ssxzxzx = QLabel(self.groupLesoes_22)
        self.ssxzxzx.setObjectName(u"ssxzxzx")
        self.ssxzxzx.setGeometry(QRect(20, 40, 169, 19))
        self.ssxzxzx.setFont(font6)
        self.queixa_de_zumbido = QGroupBox(self.groupLesoes_22)
        self.queixa_de_zumbido.setObjectName(u"queixa_de_zumbido")
        self.queixa_de_zumbido.setGeometry(QRect(200, 217, 117, 51))
        self.queixa_de_zumbido.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.queixa_de_zumbido)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.opcao_sim_qz = QRadioButton(self.queixa_de_zumbido)
        self.opcao_sim_qz.setObjectName(u"opcao_sim_qz")
        self.opcao_sim_qz.setFont(font6)

        self.gridLayout_8.addWidget(self.opcao_sim_qz, 0, 0, 1, 1)

        self.opcao_nao_qz = QRadioButton(self.queixa_de_zumbido)
        self.opcao_nao_qz.setObjectName(u"opcao_nao_qz")
        self.opcao_nao_qz.setFont(font6)

        self.gridLayout_8.addWidget(self.opcao_nao_qz, 0, 1, 1, 1)

        self.label_278 = QLabel(self.groupLesoes_22)
        self.label_278.setObjectName(u"label_278")
        self.label_278.setGeometry(QRect(20, 120, 158, 19))
        self.label_278.setFont(font6)
        self.label_284 = QLabel(self.groupLesoes_22)
        self.label_284.setObjectName(u"label_284")
        self.label_284.setGeometry(QRect(20, 280, 134, 19))
        self.label_284.setFont(font6)
        self.queixa_de_odor = QGroupBox(self.groupLesoes_22)
        self.queixa_de_odor.setObjectName(u"queixa_de_odor")
        self.queixa_de_odor.setGeometry(QRect(200, 137, 101, 51))
        self.queixa_de_odor.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.queixa_de_odor)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.opcao_sim_qo = QRadioButton(self.queixa_de_odor)
        self.opcao_sim_qo.setObjectName(u"opcao_sim_qo")
        self.opcao_sim_qo.setFont(font6)

        self.gridLayout_9.addWidget(self.opcao_sim_qo, 0, 0, 1, 1)

        self.opcao_nao_qo = QRadioButton(self.queixa_de_odor)
        self.opcao_nao_qo.setObjectName(u"opcao_nao_qo")
        self.opcao_nao_qo.setFont(font6)

        self.gridLayout_9.addWidget(self.opcao_nao_qo, 0, 1, 1, 1)

        self.presenca_de_cerumen = QGroupBox(self.groupLesoes_22)
        self.presenca_de_cerumen.setObjectName(u"presenca_de_cerumen")
        self.presenca_de_cerumen.setGeometry(QRect(200, 56, 101, 51))
        self.presenca_de_cerumen.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.presenca_de_cerumen)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.opcao_sim_pc = QRadioButton(self.presenca_de_cerumen)
        self.opcao_sim_pc.setObjectName(u"opcao_sim_pc")
        self.opcao_sim_pc.setFont(font6)
        self.opcao_sim_pc.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.opcao_sim_pc, 0, 0, 1, 1)

        self.opcao_nao_pc = QRadioButton(self.presenca_de_cerumen)
        self.opcao_nao_pc.setObjectName(u"opcao_nao_pc")
        self.opcao_nao_pc.setFont(font6)

        self.gridLayout_10.addWidget(self.opcao_nao_pc, 0, 1, 1, 1)

        self.label_282 = QLabel(self.groupLesoes_22)
        self.label_282.setObjectName(u"label_282")
        self.label_282.setGeometry(QRect(20, 200, 164, 19))
        self.label_282.setFont(font6)
        self.presenca_de_secrecoes_pa = QGroupBox(self.groupLesoes_22)
        self.presenca_de_secrecoes_pa.setObjectName(u"presenca_de_secrecoes_pa")
        self.presenca_de_secrecoes_pa.setGeometry(QRect(200, 177, 117, 51))
        self.presenca_de_secrecoes_pa.setStyleSheet(u"")
        self.gridLayout_11 = QGridLayout(self.presenca_de_secrecoes_pa)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.opcao_sim_ps = QRadioButton(self.presenca_de_secrecoes_pa)
        self.opcao_sim_ps.setObjectName(u"opcao_sim_ps")
        self.opcao_sim_ps.setFont(font6)

        self.gridLayout_11.addWidget(self.opcao_sim_ps, 0, 0, 1, 1)

        self.opcao_nao_ps = QRadioButton(self.presenca_de_secrecoes_pa)
        self.opcao_nao_ps.setObjectName(u"opcao_nao_ps")
        self.opcao_nao_ps.setFont(font6)

        self.gridLayout_11.addWidget(self.opcao_nao_ps, 0, 1, 1, 1)

        self.label_257 = QLabel(self.groupLesoes_22)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setGeometry(QRect(540, 115, 53, 19))
        self.label_257.setFont(font6)
        self.uso_de_aparelho_auditivo = QGroupBox(self.groupLesoes_22)
        self.uso_de_aparelho_auditivo.setObjectName(u"uso_de_aparelho_auditivo")
        self.uso_de_aparelho_auditivo.setGeometry(QRect(760, 20, 117, 51))
        self.uso_de_aparelho_auditivo.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.uso_de_aparelho_auditivo)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.opcao_sim_upa = QRadioButton(self.uso_de_aparelho_auditivo)
        self.opcao_sim_upa.setObjectName(u"opcao_sim_upa")
        self.opcao_sim_upa.setFont(font6)

        self.gridLayout_12.addWidget(self.opcao_sim_upa, 0, 0, 1, 1)

        self.opcao_nao_upa = QRadioButton(self.uso_de_aparelho_auditivo)
        self.opcao_nao_upa.setObjectName(u"opcao_nao_upa")
        self.opcao_nao_upa.setFont(font6)

        self.gridLayout_12.addWidget(self.opcao_nao_upa, 0, 1, 1, 1)

        self.label_286 = QLabel(self.groupLesoes_22)
        self.label_286.setObjectName(u"label_286")
        self.label_286.setGeometry(QRect(540, 78, 115, 19))
        self.label_286.setFont(font6)
        self.label_285 = QLabel(self.groupLesoes_22)
        self.label_285.setObjectName(u"label_285")
        self.label_285.setGeometry(QRect(540, 40, 182, 19))
        self.label_285.setFont(font6)
        self.implantacao_pa = QLineEdit(self.groupLesoes_22)
        self.implantacao_pa.setObjectName(u"implantacao_pa")
        self.implantacao_pa.setGeometry(QRect(760, 73, 121, 31))
        self.outra_implantacao_pa = QLineEdit(self.groupLesoes_22)
        self.outra_implantacao_pa.setObjectName(u"outra_implantacao_pa")
        self.outra_implantacao_pa.setGeometry(QRect(760, 111, 121, 31))

        self.gridLayout_115.addWidget(self.groupLesoes_22, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_116 = QGridLayout(self.tab_15)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.groupLesoes_23 = QGroupBox(self.tab_15)
        self.groupLesoes_23.setObjectName(u"groupLesoes_23")
        self.groupLesoes_23.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"       border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.groupBox_156 = QGroupBox(self.groupLesoes_23)
        self.groupBox_156.setObjectName(u"groupBox_156")
        self.groupBox_156.setGeometry(QRect(120, 30, 224, 46))
        self.groupBox_156.setStyleSheet(u"border: none;\n"
"")
        self.gridLayout_306 = QGridLayout(self.groupBox_156)
        self.gridLayout_306.setObjectName(u"gridLayout_306")
        self.groupBox_157 = QGroupBox(self.groupLesoes_23)
        self.groupBox_157.setObjectName(u"groupBox_157")
        self.groupBox_157.setGeometry(QRect(180, 70, 119, 46))
        self.groupBox_157.setStyleSheet(u"border: none;")
        self.gridLayout_307 = QGridLayout(self.groupBox_157)
        self.gridLayout_307.setObjectName(u"gridLayout_307")
        self.groupBox_160 = QGroupBox(self.groupLesoes_23)
        self.groupBox_160.setObjectName(u"groupBox_160")
        self.groupBox_160.setGeometry(QRect(160, 190, 178, 46))
        self.groupBox_160.setStyleSheet(u"border: none;")
        self.gridLayout_312 = QGridLayout(self.groupBox_160)
        self.gridLayout_312.setObjectName(u"gridLayout_312")
        self.groupBox_161 = QGroupBox(self.groupLesoes_23)
        self.groupBox_161.setObjectName(u"groupBox_161")
        self.groupBox_161.setGeometry(QRect(270, 230, 119, 46))
        self.groupBox_161.setStyleSheet(u"border: none;")
        self.gridLayout_313 = QGridLayout(self.groupBox_161)
        self.gridLayout_313.setObjectName(u"gridLayout_313")
        self.label_289 = QLabel(self.groupLesoes_23)
        self.label_289.setObjectName(u"label_289")
        self.label_289.setGeometry(QRect(30, 405, 86, 19))
        self.label_289.setFont(font6)
        self.label_293 = QLabel(self.groupLesoes_23)
        self.label_293.setObjectName(u"label_293")
        self.label_293.setGeometry(QRect(30, 200, 42, 19))
        self.label_293.setFont(font6)
        self.central_rc = QGroupBox(self.groupLesoes_23)
        self.central_rc.setObjectName(u"central_rc")
        self.central_rc.setGeometry(QRect(190, 60, 101, 51))
        self.gridLayout_13 = QGridLayout(self.central_rc)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.opcao_sim_central = QRadioButton(self.central_rc)
        self.opcao_sim_central.setObjectName(u"opcao_sim_central")
        self.opcao_sim_central.setFont(font6)

        self.gridLayout_13.addWidget(self.opcao_sim_central, 0, 0, 1, 1)

        self.opcao_nao_central = QRadioButton(self.central_rc)
        self.opcao_nao_central.setObjectName(u"opcao_nao_central")
        self.opcao_nao_central.setFont(font6)

        self.gridLayout_13.addWidget(self.opcao_nao_central, 0, 1, 1, 1)

        self.label_254 = QLabel(self.groupLesoes_23)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setGeometry(QRect(30, 240, 107, 19))
        self.label_254.setFont(font6)
        self.pulso_carotideo_rc = QGroupBox(self.groupLesoes_23)
        self.pulso_carotideo_rc.setObjectName(u"pulso_carotideo_rc")
        self.pulso_carotideo_rc.setGeometry(QRect(190, 300, 151, 51))
        self.gridLayout_14 = QGridLayout(self.pulso_carotideo_rc)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.opcao_ausente_pc = QRadioButton(self.pulso_carotideo_rc)
        self.opcao_ausente_pc.setObjectName(u"opcao_ausente_pc")
        self.opcao_ausente_pc.setFont(font6)

        self.gridLayout_14.addWidget(self.opcao_ausente_pc, 0, 0, 1, 1)

        self.opcao_presente_pc = QRadioButton(self.pulso_carotideo_rc)
        self.opcao_presente_pc.setObjectName(u"opcao_presente_pc")
        self.opcao_presente_pc.setFont(font6)

        self.gridLayout_14.addWidget(self.opcao_presente_pc, 0, 1, 1, 1)

        self.presenca_de_massas_rc = QGroupBox(self.groupLesoes_23)
        self.presenca_de_massas_rc.setObjectName(u"presenca_de_massas_rc")
        self.presenca_de_massas_rc.setGeometry(QRect(190, 100, 101, 51))
        self.gridLayout_15 = QGridLayout(self.presenca_de_massas_rc)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.opcao_sim_pm = QRadioButton(self.presenca_de_massas_rc)
        self.opcao_sim_pm.setObjectName(u"opcao_sim_pm")
        self.opcao_sim_pm.setFont(font6)

        self.gridLayout_15.addWidget(self.opcao_sim_pm, 0, 0, 1, 1)

        self.opcao_nao_pm = QRadioButton(self.presenca_de_massas_rc)
        self.opcao_nao_pm.setObjectName(u"opcao_nao_pm")
        self.opcao_nao_pm.setFont(font6)

        self.gridLayout_15.addWidget(self.opcao_nao_pm, 0, 1, 1, 1)

        self.movimentacao_rc = QGroupBox(self.groupLesoes_23)
        self.movimentacao_rc.setObjectName(u"movimentacao_rc")
        self.movimentacao_rc.setGeometry(QRect(190, 220, 161, 51))
        self.gridLayout_27 = QGridLayout(self.movimentacao_rc)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.opcao_preservada_m = QRadioButton(self.movimentacao_rc)
        self.opcao_preservada_m.setObjectName(u"opcao_preservada_m")
        self.opcao_preservada_m.setFont(font6)

        self.gridLayout_27.addWidget(self.opcao_preservada_m, 0, 0, 1, 1)

        self.opcao_alterada_m = QRadioButton(self.movimentacao_rc)
        self.opcao_alterada_m.setObjectName(u"opcao_alterada_m")
        self.opcao_alterada_m.setFont(font6)

        self.gridLayout_27.addWidget(self.opcao_alterada_m, 0, 1, 1, 1)

        self.fremio_tatil = QLineEdit(self.groupLesoes_23)
        self.fremio_tatil.setObjectName(u"fremio_tatil")
        self.fremio_tatil.setGeometry(QRect(190, 397, 121, 31))
        self.label_291 = QLabel(self.groupLesoes_23)
        self.label_291.setObjectName(u"label_291")
        self.label_291.setGeometry(QRect(30, 320, 117, 19))
        self.label_291.setFont(font6)
        self.local_rc = QLineEdit(self.groupLesoes_23)
        self.local_rc.setObjectName(u"local_rc")
        self.local_rc.setGeometry(QRect(190, 196, 121, 31))
        self.label_294 = QLabel(self.groupLesoes_23)
        self.label_294.setObjectName(u"label_294")
        self.label_294.setGeometry(QRect(30, 160, 72, 19))
        self.label_294.setFont(font6)
        self.rigidez_de_nuca = QGroupBox(self.groupLesoes_23)
        self.rigidez_de_nuca.setObjectName(u"rigidez_de_nuca")
        self.rigidez_de_nuca.setGeometry(QRect(190, 260, 101, 51))
        self.gridLayout_28 = QGridLayout(self.rigidez_de_nuca)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.opcao_sim_rn = QRadioButton(self.rigidez_de_nuca)
        self.opcao_sim_rn.setObjectName(u"opcao_sim_rn")
        self.opcao_sim_rn.setFont(font6)

        self.gridLayout_28.addWidget(self.opcao_sim_rn, 0, 0, 1, 1)

        self.opcao_nao_rn = QRadioButton(self.rigidez_de_nuca)
        self.opcao_nao_rn.setObjectName(u"opcao_nao_rn")
        self.opcao_nao_rn.setFont(font6)

        self.gridLayout_28.addWidget(self.opcao_nao_rn, 0, 1, 1, 1)

        self.label_296 = QLabel(self.groupLesoes_23)
        self.label_296.setObjectName(u"label_296")
        self.label_296.setGeometry(QRect(30, 80, 56, 19))
        self.label_296.setFont(font6)
        self.label_295 = QLabel(self.groupLesoes_23)
        self.label_295.setObjectName(u"label_295")
        self.label_295.setGeometry(QRect(30, 120, 146, 19))
        self.label_295.setFont(font6)
        self.ingurgimento_jugular_rc = QGroupBox(self.groupLesoes_23)
        self.ingurgimento_jugular_rc.setObjectName(u"ingurgimento_jugular_rc")
        self.ingurgimento_jugular_rc.setGeometry(QRect(190, 340, 151, 51))
        self.gridLayout_29 = QGridLayout(self.ingurgimento_jugular_rc)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.opcao_ausente_ij = QRadioButton(self.ingurgimento_jugular_rc)
        self.opcao_ausente_ij.setObjectName(u"opcao_ausente_ij")
        self.opcao_ausente_ij.setFont(font6)

        self.gridLayout_29.addWidget(self.opcao_ausente_ij, 0, 0, 1, 1)

        self.opcao_presente_ij = QRadioButton(self.ingurgimento_jugular_rc)
        self.opcao_presente_ij.setObjectName(u"opcao_presente_ij")
        self.opcao_presente_ij.setFont(font6)

        self.gridLayout_29.addWidget(self.opcao_presente_ij, 0, 1, 1, 1)

        self.simetrica_rc = QGroupBox(self.groupLesoes_23)
        self.simetrica_rc.setObjectName(u"simetrica_rc")
        self.simetrica_rc.setGeometry(QRect(190, 20, 101, 51))
        self.gridLayout_30 = QGridLayout(self.simetrica_rc)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.opcao_sim_simetrica = QRadioButton(self.simetrica_rc)
        self.opcao_sim_simetrica.setObjectName(u"opcao_sim_simetrica")
        self.opcao_sim_simetrica.setFont(font6)

        self.gridLayout_30.addWidget(self.opcao_sim_simetrica, 0, 0, 1, 1)

        self.opcao_nao_simetrica = QRadioButton(self.simetrica_rc)
        self.opcao_nao_simetrica.setObjectName(u"opcao_nao_simetrica")
        self.opcao_nao_simetrica.setFont(font6)

        self.gridLayout_30.addWidget(self.opcao_nao_simetrica, 0, 1, 1, 1)

        self.cicratizes = QGroupBox(self.groupLesoes_23)
        self.cicratizes.setObjectName(u"cicratizes")
        self.cicratizes.setGeometry(QRect(190, 140, 101, 51))
        self.gridLayout_31 = QGridLayout(self.cicratizes)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.opcao_sim_cicatrizes = QRadioButton(self.cicratizes)
        self.opcao_sim_cicatrizes.setObjectName(u"opcao_sim_cicatrizes")
        self.opcao_sim_cicatrizes.setFont(font6)

        self.gridLayout_31.addWidget(self.opcao_sim_cicatrizes, 0, 1, 1, 1)

        self.opcao_nao_cicatrizes = QRadioButton(self.cicratizes)
        self.opcao_nao_cicatrizes.setObjectName(u"opcao_nao_cicatrizes")
        self.opcao_nao_cicatrizes.setFont(font6)

        self.gridLayout_31.addWidget(self.opcao_nao_cicatrizes, 0, 2, 1, 1)

        self.label_290 = QLabel(self.groupLesoes_23)
        self.label_290.setObjectName(u"label_290")
        self.label_290.setGeometry(QRect(30, 360, 160, 19))
        self.label_290.setFont(font6)
        self.label_297 = QLabel(self.groupLesoes_23)
        self.label_297.setObjectName(u"label_297")
        self.label_297.setGeometry(QRect(30, 40, 71, 19))
        self.label_297.setFont(font6)
        self.label_292 = QLabel(self.groupLesoes_23)
        self.label_292.setObjectName(u"label_292")
        self.label_292.setGeometry(QRect(30, 280, 119, 19))
        self.label_292.setFont(font6)
        self.label_258 = QLabel(self.groupLesoes_23)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setGeometry(QRect(520, 124, 53, 19))
        self.label_258.setFont(font6)
        self.linfonodos = QGroupBox(self.groupLesoes_23)
        self.linfonodos.setObjectName(u"linfonodos")
        self.linfonodos.setGeometry(QRect(620, 22, 321, 51))
        self.gridLayout_32 = QGridLayout(self.linfonodos)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.opcao_dolores_lin = QRadioButton(self.linfonodos)
        self.opcao_dolores_lin.setObjectName(u"opcao_dolores_lin")
        self.opcao_dolores_lin.setFont(font6)

        self.gridLayout_32.addWidget(self.opcao_dolores_lin, 0, 3, 1, 1)

        self.opcao_palpaveis_lin = QRadioButton(self.linfonodos)
        self.opcao_palpaveis_lin.setObjectName(u"opcao_palpaveis_lin")
        self.opcao_palpaveis_lin.setFont(font6)

        self.gridLayout_32.addWidget(self.opcao_palpaveis_lin, 0, 0, 1, 1)

        self.opcao_indolores_lin = QRadioButton(self.linfonodos)
        self.opcao_indolores_lin.setObjectName(u"opcao_indolores_lin")
        self.opcao_indolores_lin.setFont(font6)

        self.gridLayout_32.addWidget(self.opcao_indolores_lin, 0, 2, 1, 1)

        self.opcao_nao_p_lin = QRadioButton(self.linfonodos)
        self.opcao_nao_p_lin.setObjectName(u"opcao_nao_p_lin")
        self.opcao_nao_p_lin.setFont(font6)

        self.gridLayout_32.addWidget(self.opcao_nao_p_lin, 0, 1, 1, 1)

        self.outras_rc = QLineEdit(self.groupLesoes_23)
        self.outras_rc.setObjectName(u"outras_rc")
        self.outras_rc.setGeometry(QRect(620, 120, 121, 31))
        self.label_287 = QLabel(self.groupLesoes_23)
        self.label_287.setObjectName(u"label_287")
        self.label_287.setGeometry(QRect(520, 85, 64, 19))
        self.label_287.setFont(font6)
        self.tireoide_rc = QGroupBox(self.groupLesoes_23)
        self.tireoide_rc.setObjectName(u"tireoide_rc")
        self.tireoide_rc.setGeometry(QRect(620, 64, 181, 51))
        self.gridLayout_35 = QGridLayout(self.tireoide_rc)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.opcao_preservada_tir = QRadioButton(self.tireoide_rc)
        self.opcao_preservada_tir.setObjectName(u"opcao_preservada_tir")
        self.opcao_preservada_tir.setFont(font6)

        self.gridLayout_35.addWidget(self.opcao_preservada_tir, 0, 0, 1, 1)

        self.opcao_aumentada_tir = QRadioButton(self.tireoide_rc)
        self.opcao_aumentada_tir.setObjectName(u"opcao_aumentada_tir")
        self.opcao_aumentada_tir.setFont(font6)

        self.gridLayout_35.addWidget(self.opcao_aumentada_tir, 0, 1, 1, 1)

        self.label_288 = QLabel(self.groupLesoes_23)
        self.label_288.setObjectName(u"label_288")
        self.label_288.setGeometry(QRect(520, 40, 89, 19))
        self.label_288.setFont(font6)

        self.gridLayout_116.addWidget(self.groupLesoes_23, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_117 = QGridLayout(self.tab_16)
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.groupLesoes_24 = QGroupBox(self.tab_16)
        self.groupLesoes_24.setObjectName(u"groupLesoes_24")
        self.groupLesoes_24.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.groupBox_162 = QGroupBox(self.groupLesoes_24)
        self.groupBox_162.setObjectName(u"groupBox_162")
        self.groupBox_162.setGeometry(QRect(120, 30, 224, 46))
        self.groupBox_162.setStyleSheet(u"border: none;\n"
"")
        self.gridLayout_314 = QGridLayout(self.groupBox_162)
        self.gridLayout_314.setObjectName(u"gridLayout_314")
        self.groupBox_163 = QGroupBox(self.groupLesoes_24)
        self.groupBox_163.setObjectName(u"groupBox_163")
        self.groupBox_163.setGeometry(QRect(180, 70, 119, 46))
        self.groupBox_163.setStyleSheet(u"border: none;")
        self.gridLayout_425 = QGridLayout(self.groupBox_163)
        self.gridLayout_425.setObjectName(u"gridLayout_425")
        self.groupBox_164 = QGroupBox(self.groupLesoes_24)
        self.groupBox_164.setObjectName(u"groupBox_164")
        self.groupBox_164.setGeometry(QRect(180, 110, 209, 46))
        self.groupBox_164.setStyleSheet(u"border: none;")
        self.gridLayout_426 = QGridLayout(self.groupBox_164)
        self.gridLayout_426.setObjectName(u"gridLayout_426")
        self.groupBox_165 = QGroupBox(self.groupLesoes_24)
        self.groupBox_165.setObjectName(u"groupBox_165")
        self.groupBox_165.setGeometry(QRect(140, 150, 218, 46))
        self.groupBox_165.setStyleSheet(u"border: none;\n"
"")
        self.gridLayout_427 = QGridLayout(self.groupBox_165)
        self.gridLayout_427.setObjectName(u"gridLayout_427")
        self.groupBox_166 = QGroupBox(self.groupLesoes_24)
        self.groupBox_166.setObjectName(u"groupBox_166")
        self.groupBox_166.setGeometry(QRect(160, 190, 178, 46))
        self.groupBox_166.setStyleSheet(u"border: none;")
        self.gridLayout_428 = QGridLayout(self.groupBox_166)
        self.gridLayout_428.setObjectName(u"gridLayout_428")
        self.groupBox_167 = QGroupBox(self.groupLesoes_24)
        self.groupBox_167.setObjectName(u"groupBox_167")
        self.groupBox_167.setGeometry(QRect(270, 230, 119, 46))
        self.groupBox_167.setStyleSheet(u"border: none;")
        self.gridLayout_448 = QGridLayout(self.groupBox_167)
        self.gridLayout_448.setObjectName(u"gridLayout_448")
        self.oxigenacao = QGroupBox(self.groupLesoes_24)
        self.oxigenacao.setObjectName(u"oxigenacao")
        self.oxigenacao.setGeometry(QRect(280, 527, 741, 51))
        self.gridLayout_67 = QGridLayout(self.oxigenacao)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.radioButton_48 = QRadioButton(self.oxigenacao)
        self.radioButton_48.setObjectName(u"radioButton_48")

        self.gridLayout_67.addWidget(self.radioButton_48, 0, 1, 1, 1)

        self.radioButton_76 = QRadioButton(self.oxigenacao)
        self.radioButton_76.setObjectName(u"radioButton_76")

        self.gridLayout_67.addWidget(self.radioButton_76, 0, 0, 1, 1)

        self.radioButton_77 = QRadioButton(self.oxigenacao)
        self.radioButton_77.setObjectName(u"radioButton_77")

        self.gridLayout_67.addWidget(self.radioButton_77, 0, 2, 1, 1)

        self.radioButton_78 = QRadioButton(self.oxigenacao)
        self.radioButton_78.setObjectName(u"radioButton_78")

        self.gridLayout_67.addWidget(self.radioButton_78, 0, 3, 1, 1)

        self.radioButton_79 = QRadioButton(self.oxigenacao)
        self.radioButton_79.setObjectName(u"radioButton_79")

        self.gridLayout_67.addWidget(self.radioButton_79, 0, 4, 1, 1)

        self.radioButton_80 = QRadioButton(self.oxigenacao)
        self.radioButton_80.setObjectName(u"radioButton_80")

        self.gridLayout_67.addWidget(self.radioButton_80, 0, 5, 1, 1)

        self.label_67 = QLabel(self.groupLesoes_24)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(111, 201, 121, 18))
        self.label_67.setFont(font6)
        self.bulhas_dois_tempos = QGroupBox(self.groupLesoes_24)
        self.bulhas_dois_tempos.setObjectName(u"bulhas_dois_tempos")
        self.bulhas_dois_tempos.setGeometry(QRect(280, 410, 111, 51))
        self.gridLayout_68 = QGridLayout(self.bulhas_dois_tempos)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.radioButton_82 = QRadioButton(self.bulhas_dois_tempos)
        self.radioButton_82.setObjectName(u"radioButton_82")

        self.gridLayout_68.addWidget(self.radioButton_82, 0, 0, 1, 1)

        self.radioButton_81 = QRadioButton(self.bulhas_dois_tempos)
        self.radioButton_81.setObjectName(u"radioButton_81")

        self.gridLayout_68.addWidget(self.radioButton_81, 0, 1, 1, 1)

        self.bulhas_cardiacas = QGroupBox(self.groupLesoes_24)
        self.bulhas_cardiacas.setObjectName(u"bulhas_cardiacas")
        self.bulhas_cardiacas.setGeometry(QRect(280, 370, 181, 51))
        self.gridLayout_77 = QGridLayout(self.bulhas_cardiacas)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.radioButton_83 = QRadioButton(self.bulhas_cardiacas)
        self.radioButton_83.setObjectName(u"radioButton_83")

        self.gridLayout_77.addWidget(self.radioButton_83, 0, 0, 1, 1)

        self.radioButton_84 = QRadioButton(self.bulhas_cardiacas)
        self.radioButton_84.setObjectName(u"radioButton_84")

        self.gridLayout_77.addWidget(self.radioButton_84, 0, 1, 1, 1)

        self.label_68 = QLabel(self.groupLesoes_24)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(111, 121, 82, 18))
        self.label_68.setFont(font6)
        self.especificar = QLineEdit(self.groupLesoes_24)
        self.especificar.setObjectName(u"especificar")
        self.especificar.setGeometry(QRect(280, 505, 121, 31))
        self.integridade_cutanea = QGroupBox(self.groupLesoes_24)
        self.integridade_cutanea.setObjectName(u"integridade_cutanea")
        self.integridade_cutanea.setGeometry(QRect(280, 136, 181, 51))
        self.gridLayout_81 = QGridLayout(self.integridade_cutanea)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.radioButton_85 = QRadioButton(self.integridade_cutanea)
        self.radioButton_85.setObjectName(u"radioButton_85")

        self.gridLayout_81.addWidget(self.radioButton_85, 0, 0, 1, 1)

        self.radioButton_86 = QRadioButton(self.integridade_cutanea)
        self.radioButton_86.setObjectName(u"radioButton_86")

        self.gridLayout_81.addWidget(self.radioButton_86, 0, 1, 1, 1)

        self.label_69 = QLabel(self.groupLesoes_24)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(111, 81, 104, 18))
        self.label_69.setFont(font6)
        self.forma_torax = QGroupBox(self.groupLesoes_24)
        self.forma_torax.setObjectName(u"forma_torax")
        self.forma_torax.setGeometry(QRect(280, 16, 351, 51))
        self.gridLayout_82 = QGridLayout(self.forma_torax)
        self.gridLayout_82.setObjectName(u"gridLayout_82")
        self.radioButton_87 = QRadioButton(self.forma_torax)
        self.radioButton_87.setObjectName(u"radioButton_87")

        self.gridLayout_82.addWidget(self.radioButton_87, 0, 2, 1, 1)

        self.radioButton_88 = QRadioButton(self.forma_torax)
        self.radioButton_88.setObjectName(u"radioButton_88")

        self.gridLayout_82.addWidget(self.radioButton_88, 0, 1, 1, 1)

        self.radioButton_89 = QRadioButton(self.forma_torax)
        self.radioButton_89.setObjectName(u"radioButton_89")

        self.gridLayout_82.addWidget(self.radioButton_89, 0, 0, 1, 1)

        self.radioButton_101 = QRadioButton(self.forma_torax)
        self.radioButton_101.setObjectName(u"radioButton_101")

        self.gridLayout_82.addWidget(self.radioButton_101, 0, 3, 1, 1)

        self.label_70 = QLabel(self.groupLesoes_24)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(110, 470, 57, 18))
        self.label_70.setFont(font6)
        self.tipo_deformidades = QGroupBox(self.groupLesoes_24)
        self.tipo_deformidades.setObjectName(u"tipo_deformidades")
        self.tipo_deformidades.setGeometry(QRect(280, 96, 211, 51))
        self.gridLayout_83 = QGridLayout(self.tipo_deformidades)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.radioButton_119 = QRadioButton(self.tipo_deformidades)
        self.radioButton_119.setObjectName(u"radioButton_119")

        self.gridLayout_83.addWidget(self.radioButton_119, 0, 0, 1, 1)

        self.radioButton_120 = QRadioButton(self.tipo_deformidades)
        self.radioButton_120.setObjectName(u"radioButton_120")

        self.gridLayout_83.addWidget(self.radioButton_120, 0, 2, 1, 1)

        self.radioButton_121 = QRadioButton(self.tipo_deformidades)
        self.radioButton_121.setObjectName(u"radioButton_121")

        self.gridLayout_83.addWidget(self.radioButton_121, 0, 1, 1, 1)

        self.fonese = QGroupBox(self.groupLesoes_24)
        self.fonese.setObjectName(u"fonese")
        self.fonese.setGeometry(QRect(280, 450, 181, 51))
        self.gridLayout_84 = QGridLayout(self.fonese)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.radioButton_122 = QRadioButton(self.fonese)
        self.radioButton_122.setObjectName(u"radioButton_122")

        self.gridLayout_84.addWidget(self.radioButton_122, 0, 1, 1, 1)

        self.radioButton_123 = QRadioButton(self.fonese)
        self.radioButton_123.setObjectName(u"radioButton_123")

        self.gridLayout_84.addWidget(self.radioButton_123, 0, 0, 1, 1)

        self.label_71 = QLabel(self.groupLesoes_24)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(110, 360, 42, 18))
        self.label_71.setFont(font6)
        self.tipo_de_alteracao = QGroupBox(self.groupLesoes_24)
        self.tipo_de_alteracao.setObjectName(u"tipo_de_alteracao")
        self.tipo_de_alteracao.setGeometry(QRect(280, 296, 301, 51))
        self.gridLayout_85 = QGridLayout(self.tipo_de_alteracao)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.radioButton_124 = QRadioButton(self.tipo_de_alteracao)
        self.radioButton_124.setObjectName(u"radioButton_124")

        self.gridLayout_85.addWidget(self.radioButton_124, 0, 0, 1, 1)

        self.radioButton_125 = QRadioButton(self.tipo_de_alteracao)
        self.radioButton_125.setObjectName(u"radioButton_125")

        self.gridLayout_85.addWidget(self.radioButton_125, 0, 1, 1, 1)

        self.radioButton_126 = QRadioButton(self.tipo_de_alteracao)
        self.radioButton_126.setObjectName(u"radioButton_126")

        self.gridLayout_85.addWidget(self.radioButton_126, 0, 2, 1, 1)

        self.expansibilidade = QGroupBox(self.groupLesoes_24)
        self.expansibilidade.setObjectName(u"expansibilidade")
        self.expansibilidade.setGeometry(QRect(280, 176, 181, 51))
        self.gridLayout_86 = QGridLayout(self.expansibilidade)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.radioButton_127 = QRadioButton(self.expansibilidade)
        self.radioButton_127.setObjectName(u"radioButton_127")

        self.gridLayout_86.addWidget(self.radioButton_127, 0, 0, 1, 1)

        self.radioButton_128 = QRadioButton(self.expansibilidade)
        self.radioButton_128.setObjectName(u"radioButton_128")

        self.gridLayout_86.addWidget(self.radioButton_128, 0, 1, 1, 1)

        self.label_72 = QLabel(self.groupLesoes_24)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(111, 41, 50, 18))
        self.label_72.setFont(font6)
        self.local_torax = QLineEdit(self.groupLesoes_24)
        self.local_torax.setObjectName(u"local_torax")
        self.local_torax.setGeometry(QRect(280, 350, 121, 31))
        self.label_73 = QLabel(self.groupLesoes_24)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(110, 240, 121, 18))
        self.label_73.setFont(font6)
        self.label_74 = QLabel(self.groupLesoes_24)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(111, 161, 151, 18))
        self.label_74.setFont(font6)
        self.label_75 = QLabel(self.groupLesoes_24)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(110, 280, 91, 18))
        self.label_75.setFont(font6)
        self.deformidades = QGroupBox(self.groupLesoes_24)
        self.deformidades.setObjectName(u"deformidades")
        self.deformidades.setGeometry(QRect(280, 56, 111, 51))
        self.gridLayout_87 = QGridLayout(self.deformidades)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.radioButton_129 = QRadioButton(self.deformidades)
        self.radioButton_129.setObjectName(u"radioButton_129")

        self.gridLayout_87.addWidget(self.radioButton_129, 0, 1, 1, 1)

        self.radioButton_130 = QRadioButton(self.deformidades)
        self.radioButton_130.setObjectName(u"radioButton_130")

        self.gridLayout_87.addWidget(self.radioButton_130, 0, 0, 1, 1)

        self.label_76 = QLabel(self.groupLesoes_24)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(110, 510, 140, 18))
        self.label_76.setFont(font6)
        self.alteracoes = QGroupBox(self.groupLesoes_24)
        self.alteracoes.setObjectName(u"alteracoes")
        self.alteracoes.setGeometry(QRect(280, 216, 111, 51))
        self.gridLayout_88 = QGridLayout(self.alteracoes)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.radioButton_131 = QRadioButton(self.alteracoes)
        self.radioButton_131.setObjectName(u"radioButton_131")

        self.gridLayout_88.addWidget(self.radioButton_131, 0, 1, 1, 1)

        self.radioButton_132 = QRadioButton(self.alteracoes)
        self.radioButton_132.setObjectName(u"radioButton_132")

        self.gridLayout_88.addWidget(self.radioButton_132, 0, 0, 1, 1)

        self.label_77 = QLabel(self.groupLesoes_24)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(110, 310, 41, 29))
        self.label_77.setFont(font6)
        self.respiracao_torax = QGroupBox(self.groupLesoes_24)
        self.respiracao_torax.setObjectName(u"respiracao_torax")
        self.respiracao_torax.setGeometry(QRect(280, 256, 181, 51))
        self.gridLayout_89 = QGridLayout(self.respiracao_torax)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.radioButton_133 = QRadioButton(self.respiracao_torax)
        self.radioButton_133.setObjectName(u"radioButton_133")

        self.gridLayout_89.addWidget(self.radioButton_133, 0, 0, 1, 1)

        self.radioButton_134 = QRadioButton(self.respiracao_torax)
        self.radioButton_134.setObjectName(u"radioButton_134")

        self.gridLayout_89.addWidget(self.radioButton_134, 0, 1, 1, 1)

        self.label_78 = QLabel(self.groupLesoes_24)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(110, 390, 128, 18))
        self.label_78.setFont(font6)
        self.label_79 = QLabel(self.groupLesoes_24)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(110, 550, 88, 18))
        self.label_79.setFont(font6)
        self.label_80 = QLabel(self.groupLesoes_24)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(110, 430, 161, 18))
        self.label_80.setFont(font6)

        self.gridLayout_117.addWidget(self.groupLesoes_24, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_16, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_114 = QGridLayout(self.tab_13)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.groupLesoes_21 = QGroupBox(self.tab_13)
        self.groupLesoes_21.setObjectName(u"groupLesoes_21")
        self.groupLesoes_21.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"            border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.groupBox_146 = QGroupBox(self.groupLesoes_21)
        self.groupBox_146.setObjectName(u"groupBox_146")
        self.groupBox_146.setGeometry(QRect(180, 70, 119, 46))
        self.groupBox_146.setStyleSheet(u"border: none;")
        self.gridLayout_291 = QGridLayout(self.groupBox_146)
        self.gridLayout_291.setObjectName(u"gridLayout_291")
        self.groupBox_37 = QGroupBox(self.groupLesoes_21)
        self.groupBox_37.setObjectName(u"groupBox_37")
        self.groupBox_37.setGeometry(QRect(180, 110, 209, 46))
        self.groupBox_37.setStyleSheet(u"border: none;")
        self.gridLayout_292 = QGridLayout(self.groupBox_37)
        self.gridLayout_292.setObjectName(u"gridLayout_292")
        self.groupBox_147 = QGroupBox(self.groupLesoes_21)
        self.groupBox_147.setObjectName(u"groupBox_147")
        self.groupBox_147.setGeometry(QRect(140, 150, 218, 46))
        self.groupBox_147.setStyleSheet(u"border: none;\n"
"")
        self.gridLayout_293 = QGridLayout(self.groupBox_147)
        self.gridLayout_293.setObjectName(u"gridLayout_293")
        self.groupBox_149 = QGroupBox(self.groupLesoes_21)
        self.groupBox_149.setObjectName(u"groupBox_149")
        self.groupBox_149.setGeometry(QRect(270, 230, 119, 46))
        self.groupBox_149.setStyleSheet(u"border: none;")
        self.gridLayout_296 = QGridLayout(self.groupBox_149)
        self.gridLayout_296.setObjectName(u"gridLayout_296")
        self.label_31 = QLabel(self.groupLesoes_21)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(20, 320, 98, 18))
        self.label_31.setFont(font6)
        self.ml_rima_labial = QGroupBox(self.groupLesoes_21)
        self.ml_rima_labial.setObjectName(u"ml_rima_labial")
        self.ml_rima_labial.setGeometry(QRect(200, 130, 171, 50))
        self.gridLayout_51 = QGridLayout(self.ml_rima_labial)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.radioButton_24 = QRadioButton(self.ml_rima_labial)
        self.radioButton_24.setObjectName(u"radioButton_24")

        self.gridLayout_51.addWidget(self.radioButton_24, 0, 0, 1, 1)

        self.radioButton_25 = QRadioButton(self.ml_rima_labial)
        self.radioButton_25.setObjectName(u"radioButton_25")

        self.gridLayout_51.addWidget(self.radioButton_25, 0, 1, 1, 1)

        self.ml_edema_bf = QGroupBox(self.groupLesoes_21)
        self.ml_edema_bf.setObjectName(u"ml_edema_bf")
        self.ml_edema_bf.setGeometry(QRect(200, 90, 101, 50))
        self.gridLayout_52 = QGridLayout(self.ml_edema_bf)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.radioButton_26 = QRadioButton(self.ml_edema_bf)
        self.radioButton_26.setObjectName(u"radioButton_26")

        self.gridLayout_52.addWidget(self.radioButton_26, 0, 0, 1, 1)

        self.radioButton_27 = QRadioButton(self.ml_edema_bf)
        self.radioButton_27.setObjectName(u"radioButton_27")

        self.gridLayout_52.addWidget(self.radioButton_27, 0, 1, 1, 1)

        self.label_32 = QLabel(self.groupLesoes_21)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 70, 167, 18))
        self.label_32.setFont(font6)
        self.ml_especificar_bf = QLineEdit(self.groupLesoes_21)
        self.ml_especificar_bf.setObjectName(u"ml_especificar_bf")
        self.ml_especificar_bf.setGeometry(QRect(200, 190, 121, 31))
        self.label_33 = QLabel(self.groupLesoes_21)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(20, 150, 82, 18))
        self.label_33.setFont(font6)
        self.label_34 = QLabel(self.groupLesoes_21)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(20, 110, 55, 18))
        self.label_34.setFont(font6)
        self.g_especificar_bf = QLineEdit(self.groupLesoes_21)
        self.g_especificar_bf.setObjectName(u"g_especificar_bf")
        self.g_especificar_bf.setGeometry(QRect(200, 440, 121, 31))
        self.ml_integridade_preservada_bf = QGroupBox(self.groupLesoes_21)
        self.ml_integridade_preservada_bf.setObjectName(u"ml_integridade_preservada_bf")
        self.ml_integridade_preservada_bf.setGeometry(QRect(200, 50, 101, 50))
        self.gridLayout_53 = QGridLayout(self.ml_integridade_preservada_bf)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.radioButton = QRadioButton(self.ml_integridade_preservada_bf)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_53.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_28 = QRadioButton(self.ml_integridade_preservada_bf)
        self.radioButton_28.setObjectName(u"radioButton_28")

        self.gridLayout_53.addWidget(self.radioButton_28, 0, 1, 1, 1)

        self.label_35 = QLabel(self.groupLesoes_21)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(20, 440, 139, 18))
        self.label_35.setFont(font6)
        self.label_36 = QLabel(self.groupLesoes_21)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 240, 111, 21))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"font-size: 16px;")
        self.label_37 = QLabel(self.groupLesoes_21)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(20, 198, 131, 18))
        self.label_37.setFont(font6)
        self.g_sangramento_bf = QGroupBox(self.groupLesoes_21)
        self.g_sangramento_bf.setObjectName(u"g_sangramento_bf")
        self.g_sangramento_bf.setGeometry(QRect(200, 300, 101, 50))
        self.gridLayout_54 = QGridLayout(self.g_sangramento_bf)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.radioButton_29 = QRadioButton(self.g_sangramento_bf)
        self.radioButton_29.setObjectName(u"radioButton_29")

        self.gridLayout_54.addWidget(self.radioButton_29, 0, 0, 1, 1)

        self.radioButton_30 = QRadioButton(self.g_sangramento_bf)
        self.radioButton_30.setObjectName(u"radioButton_30")

        self.gridLayout_54.addWidget(self.radioButton_30, 0, 1, 1, 1)

        self.label_38 = QLabel(self.groupLesoes_21)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(20, 40, 151, 18))
        self.label_38.setFont(font6)
        self.label_38.setStyleSheet(u"font-size: 16px;")
        self.label_39 = QLabel(self.groupLesoes_21)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 400, 132, 18))
        self.label_39.setFont(font6)
        self.label_40 = QLabel(self.groupLesoes_21)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(20, 280, 167, 18))
        self.label_40.setFont(font6)
        self.g_integridade_reservada_bf = QGroupBox(self.groupLesoes_21)
        self.g_integridade_reservada_bf.setObjectName(u"g_integridade_reservada_bf")
        self.g_integridade_reservada_bf.setGeometry(QRect(200, 260, 101, 50))
        self.gridLayout_55 = QGridLayout(self.g_integridade_reservada_bf)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.radioButton_31 = QRadioButton(self.g_integridade_reservada_bf)
        self.radioButton_31.setObjectName(u"radioButton_31")

        self.gridLayout_55.addWidget(self.radioButton_31, 0, 0, 1, 1)

        self.radioButton_32 = QRadioButton(self.g_integridade_reservada_bf)
        self.radioButton_32.setObjectName(u"radioButton_32")

        self.gridLayout_55.addWidget(self.radioButton_32, 0, 1, 1, 1)

        self.g_edema_bf = QGroupBox(self.groupLesoes_21)
        self.g_edema_bf.setObjectName(u"g_edema_bf")
        self.g_edema_bf.setGeometry(QRect(200, 340, 101, 50))
        self.gridLayout_56 = QGridLayout(self.g_edema_bf)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.radioButton_33 = QRadioButton(self.g_edema_bf)
        self.radioButton_33.setObjectName(u"radioButton_33")

        self.gridLayout_56.addWidget(self.radioButton_33, 0, 1, 1, 1)

        self.radioButton_34 = QRadioButton(self.g_edema_bf)
        self.radioButton_34.setObjectName(u"radioButton_34")

        self.gridLayout_56.addWidget(self.radioButton_34, 0, 0, 1, 1)

        self.label_41 = QLabel(self.groupLesoes_21)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 360, 132, 18))
        self.label_41.setFont(font6)
        self.g_lesoes_bf = QGroupBox(self.groupLesoes_21)
        self.g_lesoes_bf.setObjectName(u"g_lesoes_bf")
        self.g_lesoes_bf.setGeometry(QRect(200, 380, 101, 50))
        self.gridLayout_57 = QGridLayout(self.g_lesoes_bf)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.radioButton_35 = QRadioButton(self.g_lesoes_bf)
        self.radioButton_35.setObjectName(u"radioButton_35")

        self.gridLayout_57.addWidget(self.radioButton_35, 0, 1, 1, 1)

        self.radioButton_36 = QRadioButton(self.g_lesoes_bf)
        self.radioButton_36.setObjectName(u"radioButton_36")

        self.gridLayout_57.addWidget(self.radioButton_36, 0, 0, 1, 1)

        self.label_42 = QLabel(self.groupLesoes_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(440, 70, 120, 18))
        self.label_42.setFont(font6)
        self.label_43 = QLabel(self.groupLesoes_21)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(440, 121, 113, 18))
        self.label_43.setFont(font6)
        self.uso_de_protese = QGroupBox(self.groupLesoes_21)
        self.uso_de_protese.setObjectName(u"uso_de_protese")
        self.uso_de_protese.setGeometry(QRect(570, 90, 161, 71))
        self.gridLayout_58 = QGridLayout(self.uso_de_protese)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.radioButton_37 = QRadioButton(self.uso_de_protese)
        self.radioButton_37.setObjectName(u"radioButton_37")

        self.gridLayout_58.addWidget(self.radioButton_37, 1, 0, 1, 1)

        self.radioButton_38 = QRadioButton(self.uso_de_protese)
        self.radioButton_38.setObjectName(u"radioButton_38")

        self.gridLayout_58.addWidget(self.radioButton_38, 1, 1, 1, 1)

        self.radioButton_39 = QRadioButton(self.uso_de_protese)
        self.radioButton_39.setObjectName(u"radioButton_39")

        self.gridLayout_58.addWidget(self.radioButton_39, 0, 1, 1, 1)

        self.radioButton_40 = QRadioButton(self.uso_de_protese)
        self.radioButton_40.setObjectName(u"radioButton_40")

        self.gridLayout_58.addWidget(self.radioButton_40, 0, 0, 1, 1)

        self.label_44 = QLabel(self.groupLesoes_21)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(440, 177, 97, 18))
        self.label_44.setFont(font6)
        self.label_45 = QLabel(self.groupLesoes_21)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(440, 40, 71, 18))
        self.label_45.setFont(font6)
        self.label_45.setStyleSheet(u"font-size: 16px;")
        self.denticao_natural = QGroupBox(self.groupLesoes_21)
        self.denticao_natural.setObjectName(u"denticao_natural")
        self.denticao_natural.setGeometry(QRect(570, 50, 101, 50))
        self.gridLayout_59 = QGridLayout(self.denticao_natural)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.radioButton_41 = QRadioButton(self.denticao_natural)
        self.radioButton_41.setObjectName(u"radioButton_41")

        self.gridLayout_59.addWidget(self.radioButton_41, 0, 0, 1, 1)

        self.radioButton_42 = QRadioButton(self.denticao_natural)
        self.radioButton_42.setObjectName(u"radioButton_42")

        self.gridLayout_59.addWidget(self.radioButton_42, 0, 1, 1, 1)

        self.d_conservacao_bf = QGroupBox(self.groupLesoes_21)
        self.d_conservacao_bf.setObjectName(u"d_conservacao_bf")
        self.d_conservacao_bf.setGeometry(QRect(570, 151, 231, 61))
        self.gridLayout_60 = QGridLayout(self.d_conservacao_bf)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.radioButton_43 = QRadioButton(self.d_conservacao_bf)
        self.radioButton_43.setObjectName(u"radioButton_43")

        self.gridLayout_60.addWidget(self.radioButton_43, 0, 1, 1, 1)

        self.radioButton_44 = QRadioButton(self.d_conservacao_bf)
        self.radioButton_44.setObjectName(u"radioButton_44")

        self.gridLayout_60.addWidget(self.radioButton_44, 0, 0, 1, 1)

        self.radioButton_45 = QRadioButton(self.d_conservacao_bf)
        self.radioButton_45.setObjectName(u"radioButton_45")

        self.gridLayout_60.addWidget(self.radioButton_45, 0, 2, 1, 1)

        self.p_coloracao_bf = QLineEdit(self.groupLesoes_21)
        self.p_coloracao_bf.setObjectName(u"p_coloracao_bf")
        self.p_coloracao_bf.setGeometry(QRect(580, 275, 121, 31))
        self.label_46 = QLabel(self.groupLesoes_21)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(440, 310, 129, 18))
        self.label_46.setFont(font6)
        self.label_47 = QLabel(self.groupLesoes_21)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(440, 280, 131, 18))
        self.label_47.setFont(font6)
        self.label_48 = QLabel(self.groupLesoes_21)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(440, 240, 61, 31))
        self.label_48.setFont(font6)
        self.label_48.setStyleSheet(u"font-size: 16px;")
        self.p_lesoes_palato = QGroupBox(self.groupLesoes_21)
        self.p_lesoes_palato.setObjectName(u"p_lesoes_palato")
        self.p_lesoes_palato.setGeometry(QRect(570, 300, 101, 50))
        self.gridLayout_61 = QGridLayout(self.p_lesoes_palato)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.radioButton_46 = QRadioButton(self.p_lesoes_palato)
        self.radioButton_46.setObjectName(u"radioButton_46")

        self.gridLayout_61.addWidget(self.radioButton_46, 0, 0, 1, 1)

        self.radioButton_47 = QRadioButton(self.p_lesoes_palato)
        self.radioButton_47.setObjectName(u"radioButton_47")

        self.gridLayout_61.addWidget(self.radioButton_47, 0, 1, 1, 1)

        self.label_49 = QLabel(self.groupLesoes_21)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(440, 480, 83, 18))
        self.label_49.setFont(font6)
        self.l_lesoes_lingua = QGroupBox(self.groupLesoes_21)
        self.l_lesoes_lingua.setObjectName(u"l_lesoes_lingua")
        self.l_lesoes_lingua.setGeometry(QRect(570, 420, 101, 50))
        self.gridLayout_70 = QGridLayout(self.l_lesoes_lingua)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.radioButton_104 = QRadioButton(self.l_lesoes_lingua)
        self.radioButton_104.setObjectName(u"radioButton_104")

        self.gridLayout_70.addWidget(self.radioButton_104, 0, 0, 1, 1)

        self.radioButton_105 = QRadioButton(self.l_lesoes_lingua)
        self.radioButton_105.setObjectName(u"radioButton_105")

        self.gridLayout_70.addWidget(self.radioButton_105, 0, 1, 1, 1)

        self.l_coloracao_bf = QLineEdit(self.groupLesoes_21)
        self.l_coloracao_bf.setObjectName(u"l_coloracao_bf")
        self.l_coloracao_bf.setGeometry(QRect(580, 394, 121, 31))
        self.label_50 = QLabel(self.groupLesoes_21)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(440, 440, 121, 18))
        self.label_50.setFont(font6)
        self.label_51 = QLabel(self.groupLesoes_21)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(440, 400, 131, 18))
        self.label_51.setFont(font6)
        self.l_ulceracoes_bf = QGroupBox(self.groupLesoes_21)
        self.l_ulceracoes_bf.setObjectName(u"l_ulceracoes_bf")
        self.l_ulceracoes_bf.setGeometry(QRect(570, 460, 101, 50))
        self.gridLayout_71 = QGridLayout(self.l_ulceracoes_bf)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.radioButton_106 = QRadioButton(self.l_ulceracoes_bf)
        self.radioButton_106.setObjectName(u"radioButton_106")

        self.gridLayout_71.addWidget(self.radioButton_106, 0, 0, 1, 1)

        self.radioButton_107 = QRadioButton(self.l_ulceracoes_bf)
        self.radioButton_107.setObjectName(u"radioButton_107")

        self.gridLayout_71.addWidget(self.radioButton_107, 0, 1, 1, 1)

        self.label_52 = QLabel(self.groupLesoes_21)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(440, 360, 91, 21))
        self.label_52.setFont(font6)
        self.label_52.setStyleSheet(u"font-size: 16px;")
        self.label_53 = QLabel(self.groupLesoes_21)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(840, 110, 58, 18))
        self.label_53.setFont(font6)
        self.n_faringe_bf = QGroupBox(self.groupLesoes_21)
        self.n_faringe_bf.setObjectName(u"n_faringe_bf")
        self.n_faringe_bf.setGeometry(QRect(980, 90, 191, 51))
        self.gridLayout_72 = QGridLayout(self.n_faringe_bf)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.radioButton_108 = QRadioButton(self.n_faringe_bf)
        self.radioButton_108.setObjectName(u"radioButton_108")

        self.gridLayout_72.addWidget(self.radioButton_108, 0, 1, 1, 1)

        self.radioButton_109 = QRadioButton(self.n_faringe_bf)
        self.radioButton_109.setObjectName(u"radioButton_109")

        self.gridLayout_72.addWidget(self.radioButton_109, 0, 0, 1, 1)

        self.label_54 = QLabel(self.groupLesoes_21)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(840, 230, 131, 21))
        self.label_54.setFont(font6)
        self.label_54.setStyleSheet(u"font-size: 16px;")
        self.label_55 = QLabel(self.groupLesoes_21)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(840, 150, 141, 18))
        self.label_55.setFont(font6)
        self.n_edema_faringe = QGroupBox(self.groupLesoes_21)
        self.n_edema_faringe.setObjectName(u"n_edema_faringe")
        self.n_edema_faringe.setGeometry(QRect(980, 170, 101, 50))
        self.gridLayout_73 = QGridLayout(self.n_edema_faringe)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.radioButton_110 = QRadioButton(self.n_edema_faringe)
        self.radioButton_110.setObjectName(u"radioButton_110")

        self.gridLayout_73.addWidget(self.radioButton_110, 0, 1, 1, 1)

        self.radioButton_111 = QRadioButton(self.n_edema_faringe)
        self.radioButton_111.setObjectName(u"radioButton_111")

        self.gridLayout_73.addWidget(self.radioButton_111, 0, 0, 1, 1)

        self.label_56 = QLabel(self.groupLesoes_21)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(840, 70, 70, 18))
        self.label_56.setFont(font6)
        self.label_57 = QLabel(self.groupLesoes_21)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(840, 260, 82, 18))
        self.label_57.setFont(font6)
        self.label_58 = QLabel(self.groupLesoes_21)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(840, 190, 71, 18))
        self.label_58.setFont(font6)
        self.n_coloracao_faringe = QGroupBox(self.groupLesoes_21)
        self.n_coloracao_faringe.setObjectName(u"n_coloracao_faringe")
        self.n_coloracao_faringe.setGeometry(QRect(980, 130, 101, 50))
        self.gridLayout_74 = QGridLayout(self.n_coloracao_faringe)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.radioButton_112 = QRadioButton(self.n_coloracao_faringe)
        self.radioButton_112.setObjectName(u"radioButton_112")

        self.gridLayout_74.addWidget(self.radioButton_112, 0, 0, 1, 1)

        self.radioButton_113 = QRadioButton(self.n_coloracao_faringe)
        self.radioButton_113.setObjectName(u"radioButton_113")

        self.gridLayout_74.addWidget(self.radioButton_113, 0, 1, 1, 1)

        self.label_59 = QLabel(self.groupLesoes_21)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(840, 40, 91, 18))
        self.label_59.setFont(font6)
        self.label_59.setStyleSheet(u"font-size: 16px;")
        self.n_acpectos_bf = QGroupBox(self.groupLesoes_21)
        self.n_acpectos_bf.setObjectName(u"n_acpectos_bf")
        self.n_acpectos_bf.setGeometry(QRect(980, 40, 191, 61))
        self.gridLayout_75 = QGridLayout(self.n_acpectos_bf)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.radioButton_114 = QRadioButton(self.n_acpectos_bf)
        self.radioButton_114.setObjectName(u"radioButton_114")

        self.gridLayout_75.addWidget(self.radioButton_114, 1, 1, 1, 1)

        self.radioButton_115 = QRadioButton(self.n_acpectos_bf)
        self.radioButton_115.setObjectName(u"radioButton_115")

        self.gridLayout_75.addWidget(self.radioButton_115, 1, 0, 1, 1)

        self.radioButton_116 = QRadioButton(self.n_acpectos_bf)
        self.radioButton_116.setObjectName(u"radioButton_116")

        self.gridLayout_75.addWidget(self.radioButton_116, 0, 1, 1, 1)

        self.radioButton_117 = QRadioButton(self.n_acpectos_bf)
        self.radioButton_117.setObjectName(u"radioButton_117")

        self.gridLayout_75.addWidget(self.radioButton_117, 0, 0, 1, 1)

        self.label_60 = QLabel(self.groupLesoes_21)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(840, 294, 82, 18))
        self.label_60.setFont(font6)
        self.label_252 = QLabel(self.groupLesoes_21)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setGeometry(QRect(840, 330, 82, 18))
        self.label_252.setFont(font6)
        self.a_integra_bf = QGroupBox(self.groupLesoes_21)
        self.a_integra_bf.setObjectName(u"a_integra_bf")
        self.a_integra_bf.setGeometry(QRect(980, 240, 101, 50))
        self.gridLayout_138 = QGridLayout(self.a_integra_bf)
        self.gridLayout_138.setObjectName(u"gridLayout_138")
        self.radioButton_146 = QRadioButton(self.a_integra_bf)
        self.radioButton_146.setObjectName(u"radioButton_146")

        self.gridLayout_138.addWidget(self.radioButton_146, 0, 1, 1, 1)

        self.radioButton_147 = QRadioButton(self.a_integra_bf)
        self.radioButton_147.setObjectName(u"radioButton_147")

        self.gridLayout_138.addWidget(self.radioButton_147, 0, 0, 1, 1)

        self.a_alteracoes_bf = QLineEdit(self.groupLesoes_21)
        self.a_alteracoes_bf.setObjectName(u"a_alteracoes_bf")
        self.a_alteracoes_bf.setGeometry(QRect(980, 292, 121, 31))
        self.a_uvula_bf = QGroupBox(self.groupLesoes_21)
        self.a_uvula_bf.setObjectName(u"a_uvula_bf")
        self.a_uvula_bf.setGeometry(QRect(941, 314, 331, 51))
        self.gridLayout_139 = QGridLayout(self.a_uvula_bf)
        self.gridLayout_139.setObjectName(u"gridLayout_139")
        self.radioButton_151 = QRadioButton(self.a_uvula_bf)
        self.radioButton_151.setObjectName(u"radioButton_151")

        self.gridLayout_139.addWidget(self.radioButton_151, 0, 0, 1, 1)

        self.radioButton_150 = QRadioButton(self.a_uvula_bf)
        self.radioButton_150.setObjectName(u"radioButton_150")

        self.gridLayout_139.addWidget(self.radioButton_150, 0, 1, 1, 1)

        self.radioButton_149 = QRadioButton(self.a_uvula_bf)
        self.radioButton_149.setObjectName(u"radioButton_149")

        self.gridLayout_139.addWidget(self.radioButton_149, 0, 2, 1, 1)

        self.label_253 = QLabel(self.groupLesoes_21)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setGeometry(QRect(840, 370, 82, 18))
        self.label_253.setFont(font6)
        self.a_outras_bf = QLineEdit(self.groupLesoes_21)
        self.a_outras_bf.setObjectName(u"a_outras_bf")
        self.a_outras_bf.setGeometry(QRect(980, 370, 121, 31))

        self.gridLayout_114.addWidget(self.groupLesoes_21, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.gridLayout_118 = QGridLayout(self.tab_17)
        self.gridLayout_118.setObjectName(u"gridLayout_118")
        self.groupLesoes_25 = QGroupBox(self.tab_17)
        self.groupLesoes_25.setObjectName(u"groupLesoes_25")
        self.groupLesoes_25.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
" border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.mastectomia = QLabel(self.groupLesoes_25)
        self.mastectomia.setObjectName(u"mastectomia")
        self.mastectomia.setGeometry(QRect(30, 120, 93, 19))
        self.mastectomia.setFont(font6)
        self.label_300 = QLabel(self.groupLesoes_25)
        self.label_300.setObjectName(u"label_300")
        self.label_300.setGeometry(QRect(30, 380, 98, 19))
        self.label_300.setFont(font6)
        self.expressao_mamilar_2 = QLabel(self.groupLesoes_25)
        self.expressao_mamilar_2.setObjectName(u"expressao_mamilar_2")
        self.expressao_mamilar_2.setGeometry(QRect(30, 461, 162, 19))
        self.expressao_mamilar_2.setFont(font6)
        self.sensibilidade_mamas = QLineEdit(self.groupLesoes_25)
        self.sensibilidade_mamas.setObjectName(u"sensibilidade_mamas")
        self.sensibilidade_mamas.setGeometry(QRect(180, 375, 121, 31))
        self.label_255 = QLabel(self.groupLesoes_25)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setGeometry(QRect(30, 270, 93, 19))
        self.label_255.setFont(font6)
        self.tamanho_mamas = QLineEdit(self.groupLesoes_25)
        self.tamanho_mamas.setObjectName(u"tamanho_mamas")
        self.tamanho_mamas.setGeometry(QRect(180, 340, 121, 31))
        self.campo_presenca_secrecoes = QLineEdit(self.groupLesoes_25)
        self.campo_presenca_secrecoes.setObjectName(u"campo_presenca_secrecoes")
        self.campo_presenca_secrecoes.setGeometry(QRect(320, 455, 121, 35))
        self.localizacao_mamas = QLineEdit(self.groupLesoes_25)
        self.localizacao_mamas.setObjectName(u"localizacao_mamas")
        self.localizacao_mamas.setGeometry(QRect(180, 235, 121, 31))
        self.forma_mamas = QGroupBox(self.groupLesoes_25)
        self.forma_mamas.setObjectName(u"forma_mamas")
        self.forma_mamas.setGeometry(QRect(180, 60, 219, 50))
        self.forma_mamas.setStyleSheet(u"")
        self.gridLayout_93 = QGridLayout(self.forma_mamas)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.opcao_globosa_f = QRadioButton(self.forma_mamas)
        self.opcao_globosa_f.setObjectName(u"opcao_globosa_f")
        self.opcao_globosa_f.setFont(font6)

        self.gridLayout_93.addWidget(self.opcao_globosa_f, 0, 0, 1, 1)

        self.opcao_pendular_f = QRadioButton(self.forma_mamas)
        self.opcao_pendular_f.setObjectName(u"opcao_pendular_f")
        self.opcao_pendular_f.setFont(font6)

        self.gridLayout_93.addWidget(self.opcao_pendular_f, 0, 1, 1, 1)

        self.opcao_ingurtidas_f = QRadioButton(self.forma_mamas)
        self.opcao_ingurtidas_f.setObjectName(u"opcao_ingurtidas_f")
        self.opcao_ingurtidas_f.setFont(font6)

        self.gridLayout_93.addWidget(self.opcao_ingurtidas_f, 0, 2, 1, 1)

        self.planicie_dos_mamilos = QGroupBox(self.groupLesoes_25)
        self.planicie_dos_mamilos.setObjectName(u"planicie_dos_mamilos")
        self.planicie_dos_mamilos.setGeometry(QRect(180, 140, 292, 50))
        self.planicie_dos_mamilos.setStyleSheet(u"")
        self.gridLayout_91 = QGridLayout(self.planicie_dos_mamilos)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.opcao_plano_pm = QRadioButton(self.planicie_dos_mamilos)
        self.opcao_plano_pm.setObjectName(u"opcao_plano_pm")
        self.opcao_plano_pm.setFont(font6)

        self.gridLayout_91.addWidget(self.opcao_plano_pm, 0, 0, 1, 1)

        self.opcao_semiplanos_pm = QRadioButton(self.planicie_dos_mamilos)
        self.opcao_semiplanos_pm.setObjectName(u"opcao_semiplanos_pm")
        self.opcao_semiplanos_pm.setFont(font6)

        self.gridLayout_91.addWidget(self.opcao_semiplanos_pm, 0, 1, 1, 1)

        self.opcao_invertidos_pm = QRadioButton(self.planicie_dos_mamilos)
        self.opcao_invertidos_pm.setObjectName(u"opcao_invertidos_pm")
        self.opcao_invertidos_pm.setFont(font6)

        self.gridLayout_91.addWidget(self.opcao_invertidos_pm, 0, 3, 1, 1)

        self.opcao_protusos_pm = QRadioButton(self.planicie_dos_mamilos)
        self.opcao_protusos_pm.setObjectName(u"opcao_protusos_pm")
        self.opcao_protusos_pm.setFont(font6)

        self.gridLayout_91.addWidget(self.opcao_protusos_pm, 0, 2, 1, 1)

        self.label_311 = QLabel(self.groupLesoes_25)
        self.label_311.setObjectName(u"label_311")
        self.label_311.setGeometry(QRect(30, 420, 191, 19))
        self.label_311.setFont(font6)
        self.label_311.setStyleSheet(u"font-size: 16px;")
        self.consistencia_mamas = QLineEdit(self.groupLesoes_25)
        self.consistencia_mamas.setObjectName(u"consistencia_mamas")
        self.consistencia_mamas.setGeometry(QRect(180, 270, 121, 31))
        self.tamanho_2 = QLabel(self.groupLesoes_25)
        self.tamanho_2.setObjectName(u"tamanho_2")
        self.tamanho_2.setGeometry(QRect(30, 340, 73, 19))
        self.tamanho_2.setFont(font6)
        self.planice_mamilos = QLabel(self.groupLesoes_25)
        self.planice_mamilos.setObjectName(u"planice_mamilos")
        self.planice_mamilos.setGeometry(QRect(30, 160, 121, 19))
        self.planice_mamilos.setFont(font6)
        self.label_12 = QLabel(self.groupLesoes_25)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 240, 85, 19))
        self.label_12.setFont(font6)
        self.palpacao_de_massas = QGroupBox(self.groupLesoes_25)
        self.palpacao_de_massas.setObjectName(u"palpacao_de_massas")
        self.palpacao_de_massas.setGeometry(QRect(180, 180, 101, 51))
        self.palpacao_de_massas.setStyleSheet(u"")
        self.gridLayout_92 = QGridLayout(self.palpacao_de_massas)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.opcao_sim_pm_2 = QRadioButton(self.palpacao_de_massas)
        self.opcao_sim_pm_2.setObjectName(u"opcao_sim_pm_2")
        self.opcao_sim_pm_2.setFont(font6)

        self.gridLayout_92.addWidget(self.opcao_sim_pm_2, 0, 0, 1, 1)

        self.opcao_nao_pm_2 = QRadioButton(self.palpacao_de_massas)
        self.opcao_nao_pm_2.setObjectName(u"opcao_nao_pm_2")
        self.opcao_nao_pm_2.setFont(font6)

        self.gridLayout_92.addWidget(self.opcao_nao_pm_2, 0, 1, 1, 1)

        self.palpacao_massas = QLabel(self.groupLesoes_25)
        self.palpacao_massas.setObjectName(u"palpacao_massas")
        self.palpacao_massas.setGeometry(QRect(30, 200, 131, 19))
        self.palpacao_massas.setFont(font6)
        self.forma = QLabel(self.groupLesoes_25)
        self.forma.setObjectName(u"forma")
        self.forma.setGeometry(QRect(30, 80, 51, 19))
        self.forma.setFont(font6)
        self.expressao_mamilar_mamas = QGroupBox(self.groupLesoes_25)
        self.expressao_mamilar_mamas.setObjectName(u"expressao_mamilar_mamas")
        self.expressao_mamilar_mamas.setGeometry(QRect(180, 440, 121, 50))
        self.expressao_mamilar_mamas.setStyleSheet(u"")
        self.gridLayout_95 = QGridLayout(self.expressao_mamilar_mamas)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.opcao_sim_ps_2 = QRadioButton(self.expressao_mamilar_mamas)
        self.opcao_sim_ps_2.setObjectName(u"opcao_sim_ps_2")
        self.opcao_sim_ps_2.setFont(font6)

        self.gridLayout_95.addWidget(self.opcao_sim_ps_2, 0, 0, 1, 1)

        self.opcao_nao_ps_2 = QRadioButton(self.expressao_mamilar_mamas)
        self.opcao_nao_ps_2.setObjectName(u"opcao_nao_ps_2")
        self.opcao_nao_ps_2.setFont(font6)

        self.gridLayout_95.addWidget(self.opcao_nao_ps_2, 0, 1, 1, 1)

        self.label_301 = QLabel(self.groupLesoes_25)
        self.label_301.setObjectName(u"label_301")
        self.label_301.setGeometry(QRect(30, 310, 82, 19))
        self.label_301.setFont(font6)
        self.label_298 = QLabel(self.groupLesoes_25)
        self.label_298.setObjectName(u"label_298")
        self.label_298.setGeometry(QRect(30, 40, 64, 19))
        self.label_298.setFont(font6)
        self.mastectomia_mamas = QGroupBox(self.groupLesoes_25)
        self.mastectomia_mamas.setObjectName(u"mastectomia_mamas")
        self.mastectomia_mamas.setGeometry(QRect(180, 100, 238, 50))
        self.mastectomia_mamas.setStyleSheet(u"")
        self.gridLayout_94 = QGridLayout(self.mastectomia_mamas)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.opcao_direita_m = QRadioButton(self.mastectomia_mamas)
        self.opcao_direita_m.setObjectName(u"opcao_direita_m")
        self.opcao_direita_m.setFont(font6)

        self.gridLayout_94.addWidget(self.opcao_direita_m, 0, 0, 1, 1)

        self.opcao_esquerda_m = QRadioButton(self.mastectomia_mamas)
        self.opcao_esquerda_m.setObjectName(u"opcao_esquerda_m")
        self.opcao_esquerda_m.setFont(font6)

        self.gridLayout_94.addWidget(self.opcao_esquerda_m, 0, 1, 1, 1)

        self.opcao_nr_m = QRadioButton(self.mastectomia_mamas)
        self.opcao_nr_m.setObjectName(u"opcao_nr_m")
        self.opcao_nr_m.setFont(font6)

        self.gridLayout_94.addWidget(self.opcao_nr_m, 0, 2, 1, 1)

        self.mobilidade_mamas = QLineEdit(self.groupLesoes_25)
        self.mobilidade_mamas.setObjectName(u"mobilidade_mamas")
        self.mobilidade_mamas.setGeometry(QRect(180, 305, 121, 31))
        self.simetria_mamas = QGroupBox(self.groupLesoes_25)
        self.simetria_mamas.setObjectName(u"simetria_mamas")
        self.simetria_mamas.setGeometry(QRect(180, 20, 94, 50))
        self.simetria_mamas.setStyleSheet(u"")
        self.gridLayout_90 = QGridLayout(self.simetria_mamas)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.opcao_sim_simetria = QRadioButton(self.simetria_mamas)
        self.opcao_sim_simetria.setObjectName(u"opcao_sim_simetria")
        self.opcao_sim_simetria.setFont(font6)

        self.gridLayout_90.addWidget(self.opcao_sim_simetria, 0, 0, 1, 1)

        self.opcao_nao_simetria = QRadioButton(self.simetria_mamas)
        self.opcao_nao_simetria.setObjectName(u"opcao_nao_simetria")
        self.opcao_nao_simetria.setFont(font6)

        self.gridLayout_90.addWidget(self.opcao_nao_simetria, 0, 1, 1, 1)


        self.gridLayout_118.addWidget(self.groupLesoes_25, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_119 = QGridLayout(self.tab_18)
        self.gridLayout_119.setObjectName(u"gridLayout_119")
        self.groupLesoes_26 = QGroupBox(self.tab_18)
        self.groupLesoes_26.setObjectName(u"groupLesoes_26")
        self.groupLesoes_26.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"         border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.groupBox_175 = QGroupBox(self.groupLesoes_26)
        self.groupBox_175.setObjectName(u"groupBox_175")
        self.groupBox_175.setGeometry(QRect(180, 70, 119, 46))
        self.groupBox_175.setStyleSheet(u"border: none;")
        self.gridLayout_456 = QGridLayout(self.groupBox_175)
        self.gridLayout_456.setObjectName(u"gridLayout_456")
        self.label_22 = QLabel(self.groupLesoes_26)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 160, 101, 39))
        self.label_22.setFont(font6)
        self.label_2 = QLabel(self.groupLesoes_26)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 162, 39))
        self.label_2.setFont(font6)
        self.expectoracao = QGroupBox(self.groupLesoes_26)
        self.expectoracao.setObjectName(u"expectoracao")
        self.expectoracao.setGeometry(QRect(290, 150, 101, 51))
        self.expectoracao.setStyleSheet(u"")
        self.gridLayout_37 = QGridLayout(self.expectoracao)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.radio_expectoracao_sim = QRadioButton(self.expectoracao)
        self.radio_expectoracao_sim.setObjectName(u"radio_expectoracao_sim")
        self.radio_expectoracao_sim.setFont(font6)

        self.gridLayout_37.addWidget(self.radio_expectoracao_sim, 0, 0, 1, 1)

        self.radio_expectoracao_nao = QRadioButton(self.expectoracao)
        self.radio_expectoracao_nao.setObjectName(u"radio_expectoracao_nao")
        self.radio_expectoracao_nao.setFont(font6)

        self.gridLayout_37.addWidget(self.radio_expectoracao_nao, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupLesoes_26)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 295, 39))
        self.label_4.setFont(font6)
        self.tosse = QGroupBox(self.groupLesoes_26)
        self.tosse.setObjectName(u"tosse")
        self.tosse.setGeometry(QRect(290, 110, 171, 51))
        self.tosse.setStyleSheet(u"")
        self.gridLayout_42 = QGridLayout(self.tosse)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.radio_presente_2 = QRadioButton(self.tosse)
        self.radio_presente_2.setObjectName(u"radio_presente_2")
        self.radio_presente_2.setFont(font6)

        self.gridLayout_42.addWidget(self.radio_presente_2, 0, 2, 1, 1)

        self.radio_ausente = QRadioButton(self.tosse)
        self.radio_ausente.setObjectName(u"radio_ausente")
        self.radio_ausente.setFont(font6)

        self.gridLayout_42.addWidget(self.radio_ausente, 0, 3, 1, 1)

        self.murmurios_vesiculares = QGroupBox(self.groupLesoes_26)
        self.murmurios_vesiculares.setObjectName(u"murmurios_vesiculares")
        self.murmurios_vesiculares.setGeometry(QRect(290, 30, 404, 50))
        self.gridLayout_44 = QGridLayout(self.murmurios_vesiculares)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.radio_Fisiologicos = QRadioButton(self.murmurios_vesiculares)
        self.radio_Fisiologicos.setObjectName(u"radio_Fisiologicos")
        self.radio_Fisiologicos.setFont(font6)

        self.gridLayout_44.addWidget(self.radio_Fisiologicos, 0, 0, 1, 1)

        self.radio_sem_ruidos = QRadioButton(self.murmurios_vesiculares)
        self.radio_sem_ruidos.setObjectName(u"radio_sem_ruidos")
        self.radio_sem_ruidos.setFont(font6)

        self.gridLayout_44.addWidget(self.radio_sem_ruidos, 0, 1, 1, 1)

        self.radio_com_ruidos = QRadioButton(self.murmurios_vesiculares)
        self.radio_com_ruidos.setObjectName(u"radio_com_ruidos")
        self.radio_com_ruidos.setFont(font6)

        self.gridLayout_44.addWidget(self.radio_com_ruidos, 0, 2, 1, 1)

        self.tipos_de_ruidos = QGroupBox(self.groupLesoes_26)
        self.tipos_de_ruidos.setObjectName(u"tipos_de_ruidos")
        self.tipos_de_ruidos.setGeometry(QRect(290, 70, 621, 50))
        self.tipos_de_ruidos.setStyleSheet(u"")
        self.gridLayout_43 = QGridLayout(self.tipos_de_ruidos)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.radio_estertores_subcrepitantes = QRadioButton(self.tipos_de_ruidos)
        self.radio_estertores_subcrepitantes.setObjectName(u"radio_estertores_subcrepitantes")
        self.radio_estertores_subcrepitantes.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_estertores_subcrepitantes, 0, 1, 1, 1)

        self.radio_sibilos = QRadioButton(self.tipos_de_ruidos)
        self.radio_sibilos.setObjectName(u"radio_sibilos")
        self.radio_sibilos.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_sibilos, 0, 2, 1, 1)

        self.radio_roncos = QRadioButton(self.tipos_de_ruidos)
        self.radio_roncos.setObjectName(u"radio_roncos")
        self.radio_roncos.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_roncos, 0, 3, 1, 1)

        self.radio_atrito_pleural = QRadioButton(self.tipos_de_ruidos)
        self.radio_atrito_pleural.setObjectName(u"radio_atrito_pleural")
        self.radio_atrito_pleural.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_atrito_pleural, 0, 4, 1, 1)

        self.radio_estertores_crepitantes = QRadioButton(self.tipos_de_ruidos)
        self.radio_estertores_crepitantes.setObjectName(u"radio_estertores_crepitantes")
        self.radio_estertores_crepitantes.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_estertores_crepitantes, 0, 0, 1, 1)

        self.radio_nao_presente = QRadioButton(self.tipos_de_ruidos)
        self.radio_nao_presente.setObjectName(u"radio_nao_presente")
        self.radio_nao_presente.setFont(font6)

        self.gridLayout_43.addWidget(self.radio_nao_presente, 0, 5, 1, 1)

        self.label_5 = QLabel(self.groupLesoes_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 120, 89, 39))
        self.label_5.setFont(font6)

        self.gridLayout_119.addWidget(self.groupLesoes_26, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_120 = QGridLayout(self.tab_19)
        self.gridLayout_120.setObjectName(u"gridLayout_120")
        self.groupLesoes_27 = QGroupBox(self.tab_19)
        self.groupLesoes_27.setObjectName(u"groupLesoes_27")
        self.groupLesoes_27.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.sensibilidade_palpacao = QGroupBox(self.groupLesoes_27)
        self.sensibilidade_palpacao.setObjectName(u"sensibilidade_palpacao")
        self.sensibilidade_palpacao.setGeometry(QRect(211, 83, 451, 50))
        self.sensibilidade_palpacao.setStyleSheet(u"")
        self.gridLayout_124 = QGridLayout(self.sensibilidade_palpacao)
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.radio_flacido = QRadioButton(self.sensibilidade_palpacao)
        self.radio_flacido.setObjectName(u"radio_flacido")
        self.radio_flacido.setFont(font6)

        self.gridLayout_124.addWidget(self.radio_flacido, 0, 2, 1, 1)

        self.radio_indolor = QRadioButton(self.sensibilidade_palpacao)
        self.radio_indolor.setObjectName(u"radio_indolor")
        self.radio_indolor.setFont(font6)

        self.gridLayout_124.addWidget(self.radio_indolor, 0, 0, 1, 1)

        self.radio_dor = QRadioButton(self.sensibilidade_palpacao)
        self.radio_dor.setObjectName(u"radio_dor")
        self.radio_dor.setFont(font6)

        self.gridLayout_124.addWidget(self.radio_dor, 0, 1, 1, 1)

        self.radio_resistente = QRadioButton(self.sensibilidade_palpacao)
        self.radio_resistente.setObjectName(u"radio_resistente")
        self.radio_resistente.setFont(font6)

        self.gridLayout_124.addWidget(self.radio_resistente, 0, 3, 1, 1)

        self.ausculta_abdominal = QGroupBox(self.groupLesoes_27)
        self.ausculta_abdominal.setObjectName(u"ausculta_abdominal")
        self.ausculta_abdominal.setGeometry(QRect(210, 124, 441, 50))
        self.ausculta_abdominal.setStyleSheet(u"")
        self.gridLayout_100 = QGridLayout(self.ausculta_abdominal)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.radio_presenca = QRadioButton(self.ausculta_abdominal)
        self.radio_presenca.setObjectName(u"radio_presenca")
        self.radio_presenca.setFont(font6)

        self.gridLayout_100.addWidget(self.radio_presenca, 0, 0, 1, 1)

        self.radio_ausencia = QRadioButton(self.ausculta_abdominal)
        self.radio_ausencia.setObjectName(u"radio_ausencia")
        self.radio_ausencia.setFont(font6)

        self.gridLayout_100.addWidget(self.radio_ausencia, 0, 1, 1, 1)

        self.simetria = QGroupBox(self.groupLesoes_27)
        self.simetria.setObjectName(u"simetria")
        self.simetria.setGeometry(QRect(210, 164, 171, 51))
        self.simetria.setStyleSheet(u"")
        self.gridLayout_76 = QGridLayout(self.simetria)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.radio_simetrico = QRadioButton(self.simetria)
        self.radio_simetrico.setObjectName(u"radio_simetrico")
        self.radio_simetrico.setFont(font6)

        self.gridLayout_76.addWidget(self.radio_simetrico, 0, 0, 1, 1)

        self.radio_assimetrico = QRadioButton(self.simetria)
        self.radio_assimetrico.setObjectName(u"radio_assimetrico")
        self.radio_assimetrico.setFont(font6)

        self.gridLayout_76.addWidget(self.radio_assimetrico, 0, 1, 1, 1)

        self.label_61 = QLabel(self.groupLesoes_27)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(30, 150, 141, 18))
        self.label_61.setFont(font6)
        self.label_61.setStyleSheet(u"")
        self.label_61.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_62 = QLabel(self.groupLesoes_27)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(30, 230, 151, 18))
        self.label_62.setFont(font6)
        self.label_62.setStyleSheet(u"")
        self.label_62.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.marcas_de_estiramento = QGroupBox(self.groupLesoes_27)
        self.marcas_de_estiramento.setObjectName(u"marcas_de_estiramento")
        self.marcas_de_estiramento.setGeometry(QRect(210, 205, 101, 51))
        self.marcas_de_estiramento.setStyleSheet(u"")
        self.gridLayout_78 = QGridLayout(self.marcas_de_estiramento)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.radio_sim = QRadioButton(self.marcas_de_estiramento)
        self.radio_sim.setObjectName(u"radio_sim")
        self.radio_sim.setFont(font6)
        self.radio_sim.setCheckable(False)

        self.gridLayout_78.addWidget(self.radio_sim, 0, 0, 1, 1)

        self.radio_nao = QRadioButton(self.marcas_de_estiramento)
        self.radio_nao.setObjectName(u"radio_nao")
        self.radio_nao.setFont(font6)

        self.gridLayout_78.addWidget(self.radio_nao, 0, 1, 1, 1)

        self.label_63 = QLabel(self.groupLesoes_27)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(30, 104, 161, 18))
        self.label_63.setFont(font6)
        self.label_63.setStyleSheet(u"")
        self.label_63.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_64 = QLabel(self.groupLesoes_27)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(30, 270, 119, 18))
        self.label_64.setFont(font6)
        self.label_64.setStyleSheet(u"")
        self.label_64.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_65 = QLabel(self.groupLesoes_27)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(30, 60, 100, 18))
        self.label_65.setFont(font6)
        self.label_65.setStyleSheet(u"")
        self.label_65.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formato_abdomen = QGroupBox(self.groupLesoes_27)
        self.formato_abdomen.setObjectName(u"formato_abdomen")
        self.formato_abdomen.setGeometry(QRect(210, 33, 271, 60))
        self.formato_abdomen.setStyleSheet(u"")
        self.gridLayout_79 = QGridLayout(self.formato_abdomen)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.radio_escavado = QRadioButton(self.formato_abdomen)
        self.radio_escavado.setObjectName(u"radio_escavado")
        self.radio_escavado.setFont(font6)

        self.gridLayout_79.addWidget(self.radio_escavado, 0, 5, 1, 1)

        self.radio_pendular = QRadioButton(self.formato_abdomen)
        self.radio_pendular.setObjectName(u"radio_pendular")
        self.radio_pendular.setFont(font6)

        self.gridLayout_79.addWidget(self.radio_pendular, 0, 4, 1, 1)

        self.radio_plano = QRadioButton(self.formato_abdomen)
        self.radio_plano.setObjectName(u"radio_plano")
        self.radio_plano.setFont(font6)

        self.gridLayout_79.addWidget(self.radio_plano, 0, 2, 1, 1)

        self.radio_globoso = QRadioButton(self.formato_abdomen)
        self.radio_globoso.setObjectName(u"radio_globoso")
        self.radio_globoso.setFont(font6)

        self.gridLayout_79.addWidget(self.radio_globoso, 0, 3, 1, 1)

        self.integridade_abdomen = QGroupBox(self.groupLesoes_27)
        self.integridade_abdomen.setObjectName(u"integridade_abdomen")
        self.integridade_abdomen.setGeometry(QRect(210, 245, 161, 51))
        self.integridade_abdomen.setStyleSheet(u"")
        self.gridLayout_80 = QGridLayout(self.integridade_abdomen)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.radioButton_118 = QRadioButton(self.integridade_abdomen)
        self.radioButton_118.setObjectName(u"radioButton_118")
        self.radioButton_118.setFont(font6)

        self.gridLayout_80.addWidget(self.radioButton_118, 0, 0, 1, 1)

        self.radio_alterada_2 = QRadioButton(self.integridade_abdomen)
        self.radio_alterada_2.setObjectName(u"radio_alterada_2")
        self.radio_alterada_2.setFont(font6)

        self.gridLayout_80.addWidget(self.radio_alterada_2, 0, 1, 1, 1)

        self.label_66 = QLabel(self.groupLesoes_27)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(30, 190, 91, 20))
        self.label_66.setFont(font6)
        self.label_66.setStyleSheet(u"")
        self.label_66.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_120.addWidget(self.groupLesoes_27, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_19, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.gridLayout_122 = QGridLayout(self.tab_21)
        self.gridLayout_122.setObjectName(u"gridLayout_122")
        self.groupLesoes_29 = QGroupBox(self.tab_21)
        self.groupLesoes_29.setObjectName(u"groupLesoes_29")
        self.groupLesoes_29.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"         border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"      border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.informacoes_adicionais_anal = QLineEdit(self.groupLesoes_29)
        self.informacoes_adicionais_anal.setObjectName(u"informacoes_adicionais_anal")
        self.informacoes_adicionais_anal.setGeometry(QRect(230, 120, 121, 31))
        self.informacoes_adicionais_anal.setFont(font6)
        self.informacoes_adicionais_anal.setStyleSheet(u"")
        self.informacoes_adicionais = QLabel(self.groupLesoes_29)
        self.informacoes_adicionais.setObjectName(u"informacoes_adicionais")
        self.informacoes_adicionais.setGeometry(QRect(70, 130, 151, 21))
        self.informacoes_adicionais.setFont(font6)
        self.integridade_anal = QGroupBox(self.groupLesoes_29)
        self.integridade_anal.setObjectName(u"integridade_anal")
        self.integridade_anal.setGeometry(QRect(230, 60, 191, 50))
        self.integridade_anal.setStyleSheet(u"")
        self.gridLayout_69 = QGridLayout(self.integridade_anal)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.opcao_preservada_e = QRadioButton(self.integridade_anal)
        self.opcao_preservada_e.setObjectName(u"opcao_preservada_e")
        self.opcao_preservada_e.setFont(font6)

        self.gridLayout_69.addWidget(self.opcao_preservada_e, 0, 0, 1, 1)

        self.opcao_alterada_e = QRadioButton(self.integridade_anal)
        self.opcao_alterada_e.setObjectName(u"opcao_alterada_e")
        self.opcao_alterada_e.setFont(font6)
        self.opcao_alterada_e.setStyleSheet(u"margin-left: 25px;")

        self.gridLayout_69.addWidget(self.opcao_alterada_e, 0, 1, 1, 1)

        self.especificacoes = QLabel(self.groupLesoes_29)
        self.especificacoes.setObjectName(u"especificacoes")
        self.especificacoes.setGeometry(QRect(70, 70, 91, 41))
        self.especificacoes.setFont(font6)
        self.tipo_alteracao_anal = QLineEdit(self.groupLesoes_29)
        self.tipo_alteracao_anal.setObjectName(u"tipo_alteracao_anal")
        self.tipo_alteracao_anal.setGeometry(QRect(440, 80, 121, 31))
        self.tipo_alteracao_anal.setFont(font6)
        self.tipo_alteracao_anal.setStyleSheet(u"")

        self.gridLayout_122.addWidget(self.groupLesoes_29, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_21, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_121 = QGridLayout(self.tab_20)
        self.gridLayout_121.setObjectName(u"gridLayout_121")
        self.groupLesoes_28 = QGroupBox(self.tab_20)
        self.groupLesoes_28.setObjectName(u"groupLesoes_28")
        self.groupLesoes_28.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"      border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.outras_geniturinario = QLineEdit(self.groupLesoes_28)
        self.outras_geniturinario.setObjectName(u"outras_geniturinario")
        self.outras_geniturinario.setGeometry(QRect(120, 309, 113, 21))
        self.label_81 = QLabel(self.groupLesoes_28)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(20, 270, 61, 18))
        self.label_81.setFont(font6)
        self.aspecto = QLineEdit(self.groupLesoes_28)
        self.aspecto.setObjectName(u"aspecto")
        self.aspecto.setGeometry(QRect(120, 270, 113, 20))
        self.label_82 = QLabel(self.groupLesoes_28)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(20, 230, 91, 18))
        self.label_82.setFont(font6)
        self.edemas = QGroupBox(self.groupLesoes_28)
        self.edemas.setObjectName(u"edemas")
        self.edemas.setGeometry(QRect(120, 120, 101, 51))
        self.gridLayout_96 = QGridLayout(self.edemas)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.radioButton_135 = QRadioButton(self.edemas)
        self.radioButton_135.setObjectName(u"radioButton_135")

        self.gridLayout_96.addWidget(self.radioButton_135, 0, 1, 1, 1)

        self.radioButton_136 = QRadioButton(self.edemas)
        self.radioButton_136.setObjectName(u"radioButton_136")

        self.gridLayout_96.addWidget(self.radioButton_136, 0, 0, 1, 1)

        self.label_83 = QLabel(self.groupLesoes_28)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(20, 50, 81, 18))
        self.label_83.setFont(font6)
        self.secrecoes_geniturinario = QLineEdit(self.groupLesoes_28)
        self.secrecoes_geniturinario.setObjectName(u"secrecoes_geniturinario")
        self.secrecoes_geniturinario.setGeometry(QRect(120, 230, 113, 20))
        self.label_84 = QLabel(self.groupLesoes_28)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(20, 100, 81, 18))
        self.label_84.setFont(font6)
        self.condicao = QGroupBox(self.groupLesoes_28)
        self.condicao.setObjectName(u"condicao")
        self.condicao.setGeometry(QRect(120, 24, 711, 51))
        self.gridLayout_97 = QGridLayout(self.condicao)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.radioButton_137 = QRadioButton(self.condicao)
        self.radioButton_137.setObjectName(u"radioButton_137")

        self.gridLayout_97.addWidget(self.radioButton_137, 0, 3, 1, 1)

        self.radioButton_138 = QRadioButton(self.condicao)
        self.radioButton_138.setObjectName(u"radioButton_138")

        self.gridLayout_97.addWidget(self.radioButton_138, 0, 0, 1, 1)

        self.radioButton_139 = QRadioButton(self.condicao)
        self.radioButton_139.setObjectName(u"radioButton_139")

        self.gridLayout_97.addWidget(self.radioButton_139, 0, 2, 1, 1)

        self.radioButton_140 = QRadioButton(self.condicao)
        self.radioButton_140.setObjectName(u"radioButton_140")

        self.gridLayout_97.addWidget(self.radioButton_140, 0, 1, 1, 1)

        self.radioButton_141 = QRadioButton(self.condicao)
        self.radioButton_141.setObjectName(u"radioButton_141")

        self.gridLayout_97.addWidget(self.radioButton_141, 0, 4, 1, 1)

        self.lesoes_geniturinario = QGroupBox(self.groupLesoes_28)
        self.lesoes_geniturinario.setObjectName(u"lesoes_geniturinario")
        self.lesoes_geniturinario.setGeometry(QRect(120, 170, 101, 51))
        self.gridLayout_98 = QGridLayout(self.lesoes_geniturinario)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.radioButton_142 = QRadioButton(self.lesoes_geniturinario)
        self.radioButton_142.setObjectName(u"radioButton_142")

        self.gridLayout_98.addWidget(self.radioButton_142, 0, 1, 1, 1)

        self.radioButton_143 = QRadioButton(self.lesoes_geniturinario)
        self.radioButton_143.setObjectName(u"radioButton_143")

        self.gridLayout_98.addWidget(self.radioButton_143, 0, 0, 1, 1)

        self.label_85 = QLabel(self.groupLesoes_28)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(20, 310, 51, 18))
        self.label_85.setFont(font6)
        self.label_86 = QLabel(self.groupLesoes_28)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(20, 190, 71, 18))
        self.label_86.setFont(font6)
        self.integridade_geniturinario = QGroupBox(self.groupLesoes_28)
        self.integridade_geniturinario.setObjectName(u"integridade_geniturinario")
        self.integridade_geniturinario.setGeometry(QRect(120, 70, 171, 51))
        self.gridLayout_99 = QGridLayout(self.integridade_geniturinario)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.radioButton_144 = QRadioButton(self.integridade_geniturinario)
        self.radioButton_144.setObjectName(u"radioButton_144")

        self.gridLayout_99.addWidget(self.radioButton_144, 0, 0, 1, 1)

        self.radioButton_145 = QRadioButton(self.integridade_geniturinario)
        self.radioButton_145.setObjectName(u"radioButton_145")

        self.gridLayout_99.addWidget(self.radioButton_145, 0, 1, 1, 1)

        self.label_87 = QLabel(self.groupLesoes_28)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(20, 150, 82, 18))
        self.label_87.setFont(font6)

        self.gridLayout_121.addWidget(self.groupLesoes_28, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_20, "")

        self.gridLayout_286.addWidget(self.tabWidget_2, 0, 1, 1, 6)

        self.btn_imprimir_pdf = QPushButton(self.frame_6)
        self.btn_imprimir_pdf.setObjectName(u"btn_imprimir_pdf")
        self.btn_imprimir_pdf.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"padding: 7px 15px;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius: 6px;\n"
"\n"
"")

        self.gridLayout_286.addWidget(self.btn_imprimir_pdf, 1, 2, 1, 1)


        self.verticalLayout_143.addWidget(self.frame_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout.addWidget(self.scrollArea_2, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.info_paciente)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"  QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid rgb(85, 140, 127);\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
""
                        "\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.gridLayout_179 = QGridLayout(self.groupBox_2)
        self.gridLayout_179.setObjectName(u"gridLayout_179")
        self.labelTitulo_4 = QLabel(self.groupBox_2)
        self.labelTitulo_4.setObjectName(u"labelTitulo_4")
        self.labelTitulo_4.setStyleSheet(u"\n"
"       QLabel {\n"
"        font-size: 22px;\n"
"        font-weight: bold;\n"
"        color: white;\n"
"        background-color: rgb(85, 170, 127);\n"
"        padding: 12px;\n"
"        border-radius: 6px;\n"
"       }\n"
"      ")
        self.labelTitulo_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_179.addWidget(self.labelTitulo_4, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.info_paciente)
        self.dados_paciente = QWidget()
        self.dados_paciente.setObjectName(u"dados_paciente")
        self.gridLayout_6 = QGridLayout(self.dados_paciente)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupTecidos_8 = QGroupBox(self.dados_paciente)
        self.groupTecidos_8.setObjectName(u"groupTecidos_8")
        self.groupTecidos_8.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid rgb(85, 140, 127);\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462"
                        ";\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.gridLayout_484 = QGridLayout(self.groupTecidos_8)
        self.gridLayout_484.setObjectName(u"gridLayout_484")
        self.labelTitulo_7 = QLabel(self.groupTecidos_8)
        self.labelTitulo_7.setObjectName(u"labelTitulo_7")
        self.labelTitulo_7.setStyleSheet(u"\n"
"       QLabel {\n"
"        font-size: 22px;\n"
"        font-weight: bold;\n"
"        color: white;\n"
"        background-color: rgb(85, 170, 127);\n"
"        padding: 12px;\n"
"        border-radius: 6px;\n"
"       }\n"
"      ")
        self.labelTitulo_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_484.addWidget(self.labelTitulo_7, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupTecidos_8, 0, 0, 1, 4)

        self.scrollArea_5 = QScrollArea(self.dados_paciente)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"border: none;")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 213, 52))
        self.gridLayout_181 = QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_181.setObjectName(u"gridLayout_181")
        self.groupTecidos_4 = QGroupBox(self.scrollAreaWidgetContents_8)
        self.groupTecidos_4.setObjectName(u"groupTecidos_4")
        self.groupTecidos_4.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"\n"
"QRad"
                        "ioButton{\n"
"font-size: 13px;\n"
"}")
        self.label_13 = QLabel(self.groupTecidos_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 34, 51, 21))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"font-size: 16px;")
        self.campo_nome = QLineEdit(self.groupTecidos_4)
        self.campo_nome.setObjectName(u"campo_nome")
        self.campo_nome.setGeometry(QRect(80, 30, 181, 30))
        self.campo_nome.setMinimumSize(QSize(0, 30))
        self.campo_nome.setFont(font6)
        self.campo_nome.setStyleSheet(u"")
        self.campo_nome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_302 = QLabel(self.groupTecidos_4)
        self.label_302.setObjectName(u"label_302")
        self.label_302.setGeometry(QRect(320, 32, 111, 21))
        self.label_302.setFont(font6)
        self.label_302.setStyleSheet(u"font-size: 16px;")
        self.campo_prontuario = QLineEdit(self.groupTecidos_4)
        self.campo_prontuario.setObjectName(u"campo_prontuario")
        self.campo_prontuario.setGeometry(QRect(440, 30, 41, 30))
        self.campo_prontuario.setMinimumSize(QSize(0, 30))
        self.campo_prontuario.setFont(font6)
        self.campo_prontuario.setStyleSheet(u"")
        self.campo_prontuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tabela_paciente = QTableWidget(self.groupTecidos_4)
        if (self.tabela_paciente.columnCount() < 10):
            self.tabela_paciente.setColumnCount(10)
        font10 = QFont()
        font10.setFamilies([u"MS Shell Dlg 2"])
        font10.setPointSize(13)
        font10.setBold(True)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font10);
        self.tabela_paciente.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        font11 = QFont()
        font11.setPointSize(13)
        font11.setBold(True)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font11);
        self.tabela_paciente.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font10);
        self.tabela_paciente.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font10);
        self.tabela_paciente.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font10);
        self.tabela_paciente.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        if (self.tabela_paciente.rowCount() < 20):
            self.tabela_paciente.setRowCount(20)
        self.tabela_paciente.setObjectName(u"tabela_paciente")
        self.tabela_paciente.setGeometry(QRect(20, 80, 1421, 701))
        self.tabela_paciente.setFont(font6)
        self.tabela_paciente.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    gridline-color: #e0e0e0;\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Cabe\u00e7alho */\n"
"QHeaderView::section {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Linhas */\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Altern\u00e2ncia de linhas */\n"
"QTableWidget::item:nth-child(even) {\n"
"    background-color: #f6f9f8;\n"
"}\n"
"\n"
"/* Hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(85, 170, 127, 40);\n"
"}\n"
"\n"
"/* Sele\u00e7\u00e3o */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Barra de rolagem */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"    bo"
                        "rder-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(85, 170, 127);\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(70, 150, 110);\n"
"}")
        self.tabela_paciente.setRowCount(20)
        self.tabela_paciente.horizontalHeader().setDefaultSectionSize(360)
        self.tabela_paciente.verticalHeader().setVisible(False)
        self.tabela_paciente.verticalHeader().setMinimumSectionSize(45)
        self.tabela_paciente.verticalHeader().setDefaultSectionSize(40)
        self.tabela_paciente.verticalHeader().setHighlightSections(True)

        self.gridLayout_181.addWidget(self.groupTecidos_4, 0, 0, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_6.addWidget(self.scrollArea_5, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.btn_pesquisar = QPushButton(self.dados_paciente)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"padding: 7px 15px;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius: 6px;\n"
"\n"
"")

        self.gridLayout_6.addWidget(self.btn_pesquisar, 2, 1, 1, 1)

        self.btn_limpar_campos = QPushButton(self.dados_paciente)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        self.btn_limpar_campos.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_6.addWidget(self.btn_limpar_campos, 2, 2, 1, 1)

        self.btn_excluir = QPushButton(self.dados_paciente)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_6.addWidget(self.btn_excluir, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.dados_paciente)
        self.adicionar_usuario = QWidget()
        self.adicionar_usuario.setObjectName(u"adicionar_usuario")
        self.gridLayout_182 = QGridLayout(self.adicionar_usuario)
        self.gridLayout_182.setObjectName(u"gridLayout_182")
        self.btn_excluir_tec = QPushButton(self.adicionar_usuario)
        self.btn_excluir_tec.setObjectName(u"btn_excluir_tec")
        self.btn_excluir_tec.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_182.addWidget(self.btn_excluir_tec, 2, 3, 1, 1)

        self.btn_limpar_campos_tec = QPushButton(self.adicionar_usuario)
        self.btn_limpar_campos_tec.setObjectName(u"btn_limpar_campos_tec")
        self.btn_limpar_campos_tec.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"padding: 7px 15px;\n"
"border-radius: 6px;\n"
"")

        self.gridLayout_182.addWidget(self.btn_limpar_campos_tec, 2, 2, 1, 1)

        self.btn_pesquisar_tec = QPushButton(self.adicionar_usuario)
        self.btn_pesquisar_tec.setObjectName(u"btn_pesquisar_tec")
        self.btn_pesquisar_tec.setStyleSheet(u"color: black;\n"
"font-size: 11px;\n"
"font-weight: bold;\n"
"border: 1px solid black;\n"
"padding: 7px 15px;\n"
"border: 2px solid #388e3c;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius: 6px;\n"
"\n"
"")

        self.gridLayout_182.addWidget(self.btn_pesquisar_tec, 2, 1, 1, 1)

        self.scrollArea_3 = QScrollArea(self.adicionar_usuario)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"border: none;")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 216, 52))
        self.gridLayout_180 = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_180.setObjectName(u"gridLayout_180")
        self.groupTecidos_5 = QGroupBox(self.scrollAreaWidgetContents_7)
        self.groupTecidos_5.setObjectName(u"groupTecidos_5")
        self.groupTecidos_5.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid #b0bec5;\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {	\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462;\n"
"}\n"
"\n"
"QRad"
                        "ioButton{\n"
"font-size: 13px;\n"
"}")
        self.label_318 = QLabel(self.groupTecidos_5)
        self.label_318.setObjectName(u"label_318")
        self.label_318.setGeometry(QRect(20, 34, 51, 21))
        self.label_318.setFont(font6)
        self.label_318.setStyleSheet(u"font-size: 16px;")
        self.campo_nome_tec = QLineEdit(self.groupTecidos_5)
        self.campo_nome_tec.setObjectName(u"campo_nome_tec")
        self.campo_nome_tec.setGeometry(QRect(80, 30, 181, 30))
        self.campo_nome_tec.setMinimumSize(QSize(0, 30))
        self.campo_nome_tec.setFont(font6)
        self.campo_nome_tec.setStyleSheet(u"")
        self.campo_nome_tec.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_326 = QLabel(self.groupTecidos_5)
        self.label_326.setObjectName(u"label_326")
        self.label_326.setGeometry(QRect(310, 34, 121, 21))
        self.label_326.setFont(font6)
        self.label_326.setStyleSheet(u"font-size: 16px;")
        self.campo_ra_tec = QLineEdit(self.groupTecidos_5)
        self.campo_ra_tec.setObjectName(u"campo_ra_tec")
        self.campo_ra_tec.setGeometry(QRect(440, 30, 121, 30))
        self.campo_ra_tec.setMinimumSize(QSize(0, 30))
        self.campo_ra_tec.setFont(font6)
        self.campo_ra_tec.setStyleSheet(u"")
        self.campo_ra_tec.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tabela_tecnicos = QTableWidget(self.groupTecidos_5)
        if (self.tabela_tecnicos.columnCount() < 4):
            self.tabela_tecnicos.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font10);
        self.tabela_tecnicos.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font11);
        self.tabela_tecnicos.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font11);
        self.tabela_tecnicos.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font11);
        self.tabela_tecnicos.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        if (self.tabela_tecnicos.rowCount() < 20):
            self.tabela_tecnicos.setRowCount(20)
        self.tabela_tecnicos.setObjectName(u"tabela_tecnicos")
        self.tabela_tecnicos.setGeometry(QRect(20, 80, 1421, 701))
        self.tabela_tecnicos.setFont(font6)
        self.tabela_tecnicos.setStyleSheet(u"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    gridline-color: #e0e0e0;\n"
"    font-size: 14px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* Cabe\u00e7alho */\n"
"QHeaderView::section {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border: none;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Linhas */\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Altern\u00e2ncia de linhas */\n"
"QTableWidget::item:nth-child(even) {\n"
"    background-color: #f6f9f8;\n"
"}\n"
"\n"
"/* Hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(85, 170, 127, 40);\n"
"}\n"
"\n"
"/* Sele\u00e7\u00e3o */\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(85, 170, 127);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Barra de rolagem */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f0f0f0;\n"
"    width: 8px;\n"
"    margin: 0px;\n"
"    bo"
                        "rder-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(85, 170, 127);\n"
"    min-height: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(70, 150, 110);\n"
"}")
        self.tabela_tecnicos.setRowCount(20)
        self.tabela_tecnicos.horizontalHeader().setDefaultSectionSize(360)
        self.tabela_tecnicos.verticalHeader().setVisible(False)
        self.tabela_tecnicos.verticalHeader().setMinimumSectionSize(45)
        self.tabela_tecnicos.verticalHeader().setDefaultSectionSize(40)
        self.tabela_tecnicos.verticalHeader().setHighlightSections(True)

        self.gridLayout_180.addWidget(self.groupTecidos_5, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_182.addWidget(self.scrollArea_3, 1, 0, 1, 4)

        self.groupTecidos_7 = QGroupBox(self.adicionar_usuario)
        self.groupTecidos_7.setObjectName(u"groupTecidos_7")
        self.groupTecidos_7.setStyleSheet(u"\n"
"       QGroupBox {\n"
"        font-size: 15px;\n"
"        font-weight: bold;\n"
"        border: 2px solid rgb(85, 140, 127);\n"
"        border-radius: 10px;\n"
"		margin-top: 12px;\n"
"       }\n"
"       QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        left: 12px;\n"
"        padding: 0 6px;\n"
"        color: rgb(85, 170, 127);\n"
"       }\n"
"       QLabel {\n"
"        font-size: 14px;\n"
"       }\n"
"       QLineEdit {\n"
"        font-size: 14px;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        border: 1px solid #B0BEC5;\n"
"       }\n"
"       QLineEdit:focus {\n"
"        border: 2px solid rgb(85, 170, 127);;\n"
"       }\n"
"      \n"
"          \n"
"	 \n"
"		QRadioButton::indicator {\n"
"    width: 5px;\n"
"    height:5px;\n"
"}\n"
" \n"
"QRadioButton::indicator::hover {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
" \n"
"QRadioButton::indicator:checked {\n"
" \n"
"	background-color: rgb(85, 170, 127);\n"
"    border: 2px solid #418462"
                        ";\n"
"}\n"
"\n"
"QRadioButton{\n"
"font-size: 13px;\n"
"}")
        self.gridLayout_482 = QGridLayout(self.groupTecidos_7)
        self.gridLayout_482.setObjectName(u"gridLayout_482")
        self.labelTitulo_5 = QLabel(self.groupTecidos_7)
        self.labelTitulo_5.setObjectName(u"labelTitulo_5")
        self.labelTitulo_5.setStyleSheet(u"\n"
"       QLabel {\n"
"        font-size: 22px;\n"
"        font-weight: bold;\n"
"        color: white;\n"
"        background-color: rgb(85, 170, 127);\n"
"        padding: 12px;\n"
"        border-radius: 6px;\n"
"       }\n"
"      ")
        self.labelTitulo_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_482.addWidget(self.labelTitulo_5, 0, 0, 1, 1)


        self.gridLayout_182.addWidget(self.groupTecidos_7, 0, 0, 1, 4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_182.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.adicionar_usuario)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.gridLayout_4 = QGridLayout(self.page_widgets)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_div_content_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_usuario_conta = QLabel(self.frame_4)
        self.label_usuario_conta.setObjectName(u"label_usuario_conta")
        self.label_usuario_conta.setGeometry(QRect(90, 30, 311, 51))
        self.label_usuario_conta.setFont(font11)
        self.label_usuario_conta.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_107 = QLabel(self.frame_4)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(570, 0, 121, 51))
        self.label_107.setFont(font11)
        self.label_107.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_123 = QLabel(self.frame_4)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(570, 40, 121, 51))
        self.label_123.setFont(font11)
        self.label_123.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_124 = QLabel(self.frame_4)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(650, 0, 121, 51))
        self.label_124.setFont(font11)
        self.label_124.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_ra_conta = QLabel(self.frame_4)
        self.label_ra_conta.setObjectName(u"label_ra_conta")
        self.label_ra_conta.setGeometry(QRect(610, 40, 121, 51))
        self.label_ra_conta.setFont(font11)
        self.label_ra_conta.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 40, 41, 31))
        icon7 = QIcon()
        icon7.addFile(u"icons/16x16/cil-user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1110, 0, 131, 71))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(90, 90))

        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setPointSize(10)
        font12.setBold(True)
        self.labelBoxBlenderInstalation.setFont(font12)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)
        self.label_10.setStyleSheet(u"font-size: 30px;\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_10)


        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.page_widgets)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"    background-color: rgb(39, 44, 54);\n"
"border: none;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_183 = QGridLayout(self.frame_5)
        self.gridLayout_183.setObjectName(u"gridLayout_183")
        self.tabela_tec_conta = QTableWidget(self.frame_5)
        if (self.tabela_tec_conta.columnCount() < 4):
            self.tabela_tec_conta.setColumnCount(4)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font11);
        self.tabela_tec_conta.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font11);
        self.tabela_tec_conta.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font11);
        self.tabela_tec_conta.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font11);
        self.tabela_tec_conta.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        if (self.tabela_tec_conta.rowCount() < 1):
            self.tabela_tec_conta.setRowCount(1)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabela_tec_conta.setVerticalHeaderItem(0, __qtablewidgetitem25)
        self.tabela_tec_conta.setObjectName(u"tabela_tec_conta")
        self.tabela_tec_conta.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(39, 44, 54);\n"
"    border-radius: 5px;\n"
"    gridline-color: rgba(255, 255, 255, 30);\n"
"    color: #ECEFF1;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(30, 34, 41);\n"
"    color: #90CAF9;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 6px;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 25);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(144, 202, 249, 80);\n"
"    color: black;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(144, 202, 249, 40);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: rgb(39, 44, 54);\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(90, 100, 120);\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::hand"
                        "le:vertical:hover {\n"
"    background: rgb(120, 130, 150);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.tabela_tec_conta.horizontalHeader().setDefaultSectionSize(450)

        self.gridLayout_183.addWidget(self.tabela_tec_conta, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font3)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.gridLayout_209.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.nome_completo, self.data_de_nascimento)
        QWidget.setTabOrder(self.data_de_nascimento, self.idade)
        QWidget.setTabOrder(self.idade, self.opcao_masculino_5)
        QWidget.setTabOrder(self.opcao_masculino_5, self.campo_feminino_5)
        QWidget.setTabOrder(self.campo_feminino_5, self.opcao_outro_5)
        QWidget.setTabOrder(self.opcao_outro_5, self.opcao_solteiro_5)
        QWidget.setTabOrder(self.opcao_solteiro_5, self.opcao_casado_5)
        QWidget.setTabOrder(self.opcao_casado_5, self.opcao_divorciado_5)
        QWidget.setTabOrder(self.opcao_divorciado_5, self.opcao_viuvo_5)
        QWidget.setTabOrder(self.opcao_viuvo_5, self.data_de_emissao_consulta)
        QWidget.setTabOrder(self.data_de_emissao_consulta, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.motivo_da_internacao)
        QWidget.setTabOrder(self.motivo_da_internacao, self.radio_subito_6)
        QWidget.setTabOrder(self.radio_subito_6, self.radio_progressivo_6)
        QWidget.setTabOrder(self.radio_progressivo_6, self.data)
        QWidget.setTabOrder(self.data, self.avaliacao_de_dor)
        QWidget.setTabOrder(self.avaliacao_de_dor, self.radio_aguda_6)
        QWidget.setTabOrder(self.radio_aguda_6, self.radio_cronica_6)
        QWidget.setTabOrder(self.radio_cronica_6, self.radio_queimacao_6)
        QWidget.setTabOrder(self.radio_queimacao_6, self.radio_pontada_6)
        QWidget.setTabOrder(self.radio_pontada_6, self.radio_pressao_6)
        QWidget.setTabOrder(self.radio_pressao_6, self.radio_colica_6)
        QWidget.setTabOrder(self.radio_colica_6, self.radio_continua_6)
        QWidget.setTabOrder(self.radio_continua_6, self.escala_da_dor)
        QWidget.setTabOrder(self.escala_da_dor, self.hipotenso_2)
        QWidget.setTabOrder(self.hipotenso_2, self.hipertenso_2)
        QWidget.setTabOrder(self.hipertenso_2, self.arritmico_2)
        QWidget.setTabOrder(self.arritmico_2, self.eucardiaco_2)
        QWidget.setTabOrder(self.eucardiaco_2, self.cheio_2)
        QWidget.setTabOrder(self.cheio_2, self.filiforme_2)
        QWidget.setTabOrder(self.filiforme_2, self.taquicardico_2)
        QWidget.setTabOrder(self.taquicardico_2, self.bradicardio_2)
        QWidget.setTabOrder(self.bradicardio_2, self.febril_2)
        QWidget.setTabOrder(self.febril_2, self.subfebril_2)
        QWidget.setTabOrder(self.subfebril_2, self.afebril_2)
        QWidget.setTabOrder(self.afebril_2, self.eupnetico_2)
        QWidget.setTabOrder(self.eupnetico_2, self.dispnetico_2)
        QWidget.setTabOrder(self.dispnetico_2, self.taquipneico_2)
        QWidget.setTabOrder(self.taquipneico_2, self.radio_isocoricas)
        QWidget.setTabOrder(self.radio_isocoricas, self.radio_anisoricas)
        QWidget.setTabOrder(self.radio_anisoricas, self.radio_sim_3)
        QWidget.setTabOrder(self.radio_sim_3, self.radio_nao_3)
        QWidget.setTabOrder(self.radio_nao_3, self.radio_preservada)
        QWidget.setTabOrder(self.radio_preservada, self.radio_reduzida)
        QWidget.setTabOrder(self.radio_reduzida, self.radio_preservados)
        QWidget.setTabOrder(self.radio_preservados, self.radio_alterados)
        QWidget.setTabOrder(self.radio_alterados, self.radio_normal)
        QWidget.setTabOrder(self.radio_normal, self.radio_reduzida_sensibilidade)
        QWidget.setTabOrder(self.radio_reduzida_sensibilidade, self.radio_sim_coma)
        QWidget.setTabOrder(self.radio_sim_coma, self.radio_nao_coma)
        QWidget.setTabOrder(self.radio_nao_coma, self.abertura_ocular)
        QWidget.setTabOrder(self.abertura_ocular, self.resposta_verbal)
        QWidget.setTabOrder(self.resposta_verbal, self.resposta_motora)
        QWidget.setTabOrder(self.resposta_motora, self.resposta_pupilar)
        QWidget.setTabOrder(self.resposta_pupilar, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.botao_limpar)
        QWidget.setTabOrder(self.botao_limpar, self.botao_proximo)
        QWidget.setTabOrder(self.botao_proximo, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.campo_nome)
        QWidget.setTabOrder(self.campo_nome, self.tabela_paciente)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.pushButton_2.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"  BEM CUIDAR", None))
        self.btn_tema.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, Usu\u00e1rio", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.botao_buscar_paciente.setText("")
        self.botao_limpar_dashboard.setText("")
        self.label_nome_paciente.setText(QCoreApplication.translate("MainWindow", u"Nome Do Paciente:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Paciente", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome: ---", None))
        self.lbl_leito.setText(QCoreApplication.translate("MainWindow", u"Idade: ---", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sinais Vitais", None))
        self.lbl_pa.setText(QCoreApplication.translate("MainWindow", u"PA: ---", None))
        self.lbl_fc.setText(QCoreApplication.translate("MainWindow", u"FC: ---", None))
        self.lbl_spo2.setText(QCoreApplication.translate("MainWindow", u"SpO\u2082: ---", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"Avalia\u00e7\u00e3o Geral", None))
        self.lbl_estado_geral.setText(QCoreApplication.translate("MainWindow", u"Estado Geral: ---", None))
        self.lbl_ndc.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel de Consci\u00eancia: ---", None))
        self.card_internacao.setStyleSheet(QCoreApplication.translate("MainWindow", u"QFrame { background:#111827; border-radius:10px; color:white; }", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"Interna\u00e7\u00e3o", None))
        self.lbl_dias.setText(QCoreApplication.translate("MainWindow", u"Dias: ---", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"Status: Ativo", None))
        ___qtablewidgetitem = self.table_registros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Prontu\u00e1rio", None));
        ___qtablewidgetitem1 = self.table_registros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Estado Civil", None));
        ___qtablewidgetitem2 = self.table_registros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem3 = self.table_registros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Profiss\u00e3o", None));
        ___qtablewidgetitem4 = self.table_registros.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem5 = self.table_registros.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem6 = self.table_registros.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data de Consulta", None));
        self.frame_grafico.setStyleSheet(QCoreApplication.translate("MainWindow", u"QFrame { background:#111827; border-radius:10px; }", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"Evolu\u00e7\u00e3o Cl\u00ednica", None))
        self.botao_proximo.setText(QCoreApplication.translate("MainWindow", u"PR\u00d3XIMO", None))
        self.botao_finalizar.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.botao_anterior.setText(QCoreApplication.translate("MainWindow", u"ANTERIOR", None))
        self.botao_limpar.setText(QCoreApplication.translate("MainWindow", u"LIMPAR", None))
        self.groupTecidos_3.setTitle(QCoreApplication.translate("MainWindow", u"INFORMA\u00c7\u00d5ES DO PACIENTE", None))
        self.estado_civil.setTitle("")
        self.opcao_solteiro_5.setText(QCoreApplication.translate("MainWindow", u"Solteiro(a)", None))
        self.opcao_casado_5.setText(QCoreApplication.translate("MainWindow", u"Casado(a)", None))
        self.opcao_divorciado_5.setText(QCoreApplication.translate("MainWindow", u"Divorciado(a)", None))
        self.opcao_viuvo_5.setText(QCoreApplication.translate("MainWindow", u"Vi\u00favo(a)", None))
        self.sexo.setTitle("")
        self.opcao_masculino_5.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.campo_feminino_5.setText(QCoreApplication.translate("MainWindow", u"Feminino", None))
        self.opcao_outro_5.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.nome_1.setText(QCoreApplication.translate("MainWindow", u"Nome Completo:", None))
        self.data_nascimento_1.setText(QCoreApplication.translate("MainWindow", u"Data de Nascimento:", None))
        self.idade_1.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.sexo_1.setText(QCoreApplication.translate("MainWindow", u"Sexo:", None))
        self.estado_civil_1.setText(QCoreApplication.translate("MainWindow", u"Estado civil:", None))
        self.profissao_5.setText(QCoreApplication.translate("MainWindow", u"Profiss\u00e3o:", None))
        self.endereco_5.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o:", None))
        self.telefone_5.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.responsavel_5.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel:", None))
        self.numero_p_5.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Prontu\u00e1rio:", None))
        self.data_co_5.setText(QCoreApplication.translate("MainWindow", u"Data de consulta:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Info.Paciente", None))
        self.groupLesoes_8.setTitle(QCoreApplication.translate("MainWindow", u"MOTIVO DA INTERNA\u00c7\u00c3O", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"Motivo:", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Locomo\u00e7\u00e3o at\u00e9 a unidade de saude:", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Inicio dos Sintomas:", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"Data:", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"Dura\u00e7\u00e3o dos Sintomas:", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Localiza\u00e7\u00e3o:", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"Irradia\u00e7\u00e3o:", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"Sintomas Associados:", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"Tratamentos Realizados:", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"Avalia\u00e7\u00e3o da dor: ", None))
        self.avaliacao_de_dor.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.avaliacao_de_dor.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.avaliacao_de_dor.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.avaliacao_de_dor.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.avaliacao_de_dor.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.avaliacao_de_dor.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.avaliacao_de_dor.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.avaliacao_de_dor.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.avaliacao_de_dor.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.avaliacao_de_dor.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Tipo de Dor:", None))
        self.tipo_de_dor.setTitle("")
        self.radio_aguda_6.setText(QCoreApplication.translate("MainWindow", u"Aguda", None))
        self.radio_cronica_6.setText(QCoreApplication.translate("MainWindow", u"Cr\u00f4nica", None))
        self.radio_queimacao_6.setText(QCoreApplication.translate("MainWindow", u"Queima\u00e7\u00e3o", None))
        self.radio_pontada_6.setText(QCoreApplication.translate("MainWindow", u"Pontada", None))
        self.radio_pressao_6.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o", None))
        self.radio_colica_6.setText(QCoreApplication.translate("MainWindow", u"C\u00f3lica", None))
        self.radio_continua_6.setText(QCoreApplication.translate("MainWindow", u"Cont\u00ednua", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Localiza\u00e7\u00e3o da Dor:", None))
        self.inicio_dos_sintomas.setTitle("")
        self.radio_subito_6.setText(QCoreApplication.translate("MainWindow", u"S\u00fabito", None))
        self.radio_progressivo_6.setText(QCoreApplication.translate("MainWindow", u"Progressivo", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"Motivo Interna\u00e7\u00e3o", None))
        self.groupLesoes_9.setTitle(QCoreApplication.translate("MainWindow", u"SINAIS VITAIS", None))
        self.mmhg_2.setText(QCoreApplication.translate("MainWindow", u"mmHg", None))
        self.bpm_2.setText(QCoreApplication.translate("MainWindow", u"bpm", None))
        self.ritmo.setTitle("")
        self.arritmico_2.setText(QCoreApplication.translate("MainWindow", u"Arr\u00edtmico", None))
        self.filiforme_2.setText(QCoreApplication.translate("MainWindow", u"Filiforme", None))
        self.eucardiaco_2.setText(QCoreApplication.translate("MainWindow", u"Euc\u00e1rdiaco", None))
        self.taquicardico_2.setText(QCoreApplication.translate("MainWindow", u"Taquic\u00e1rdico", None))
        self.cheio_2.setText(QCoreApplication.translate("MainWindow", u"Cheio", None))
        self.bradicardio_2.setText(QCoreApplication.translate("MainWindow", u"Bradic\u00e1rdio", None))
        self.irpm_2.setText(QCoreApplication.translate("MainWindow", u"irpm", None))
        self.tipo.setTitle("")
        self.dispnetico_2.setText(QCoreApplication.translate("MainWindow", u"Dispnetico", None))
        self.eupnetico_2.setText(QCoreApplication.translate("MainWindow", u"Eupnetico", None))
        self.taquipneico_2.setText(QCoreApplication.translate("MainWindow", u"Taquipn\u00e9ico", None))
        self.classificacao_pressao.setTitle("")
        self.hipotenso_2.setText(QCoreApplication.translate("MainWindow", u"Hipotenso", None))
        self.hipertenso_2.setText(QCoreApplication.translate("MainWindow", u"Hipertenso", None))
        self.celsius_2.setText(QCoreApplication.translate("MainWindow", u"C\u00b0", None))
        self.classificacao_temperatura.setTitle("")
        self.subfebril_2.setText(QCoreApplication.translate("MainWindow", u"Subfebril", None))
        self.febril_2.setText(QCoreApplication.translate("MainWindow", u"Febril", None))
        self.afebril_2.setText(QCoreApplication.translate("MainWindow", u"Afebril", None))
        self.porcentagem_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.escala_da_dor.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.escala_da_dor.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.escala_da_dor.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.escala_da_dor.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.escala_da_dor.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.escala_da_dor.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.escala_da_dor.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.escala_da_dor.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.escala_da_dor.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.escala_da_dor.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.escala_da_dor.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))

        self.pressao_art_2.setText(QCoreApplication.translate("MainWindow", u"Press\u00e3o Arterial:", None))
        self.frequencia_cardiaca_2.setText(QCoreApplication.translate("MainWindow", u"Frequencia Caridiaca:", None))
        self.frequencia_respiratoria_2.setText(QCoreApplication.translate("MainWindow", u"Frequencia Respiratoria:", None))
        self.temperatura_2.setText(QCoreApplication.translate("MainWindow", u"Temperatura:", None))
        self.saturacao_o2_2.setText(QCoreApplication.translate("MainWindow", u"Satura\u00e7\u00e3o de O2:", None))
        self.escala_dor_2.setText(QCoreApplication.translate("MainWindow", u"Escala de Dor:", None))
        self.classificacao_pressao_2.setText(QCoreApplication.translate("MainWindow", u"Classifica\u00e7\u00e3o de Press\u00e3o:", None))
        self.ritmico_2.setText(QCoreApplication.translate("MainWindow", u"R\u00edtmico", None))
        self.clas_temperatura_2.setText(QCoreApplication.translate("MainWindow", u"Classifica\u00e7\u00e3o de Temperatura:", None))
        self.tipo_frequencia_r_2.setText(QCoreApplication.translate("MainWindow", u"Tipo de Frequ\u00eancia Respirat\u00f3rio:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"Sinais Vitais", None))
        self.groupLesoes_10.setTitle(QCoreApplication.translate("MainWindow", u"AVALIA\u00c7\u00c3O GERAL", None))
        self.nivel_de_consciencia.setTitle("")
        self.radio_alerta_2.setText(QCoreApplication.translate("MainWindow", u"Alerta", None))
        self.radio_semi_consciente_2.setText(QCoreApplication.translate("MainWindow", u"Semi Consciente", None))
        self.radio_confuso_2.setText(QCoreApplication.translate("MainWindow", u"Confuso", None))
        self.radio_sonolento_2.setText(QCoreApplication.translate("MainWindow", u"Sonolento", None))
        self.radio_inconsciente_2.setText(QCoreApplication.translate("MainWindow", u"Inconsciente", None))
        self.estado_geral.setTitle("")
        self.radio_bom_2.setText(QCoreApplication.translate("MainWindow", u"Bom", None))
        self.radio_regular_2.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.radio_ruim_2.setText(QCoreApplication.translate("MainWindow", u"Ruim", None))
        self.hidratacao.setTitle("")
        self.radio_hidratado_2.setText(QCoreApplication.translate("MainWindow", u"Hidratado", None))
        self.radio_desidratado_2.setText(QCoreApplication.translate("MainWindow", u"Desidratado", None))
        self.nutricao.setTitle("")
        self.radio_eutrofico_2.setText(QCoreApplication.translate("MainWindow", u"Eutr\u00f3fico", None))
        self.radio_caquetico_2.setText(QCoreApplication.translate("MainWindow", u"Caqu\u00e9tico", None))
        self.radio_obeso_2.setText(QCoreApplication.translate("MainWindow", u"Obeso", None))
        self.locomocao.setTitle("")
        self.radio_independente_2.setText(QCoreApplication.translate("MainWindow", u"Independente", None))
        self.radio_com_ajuda_2.setText(QCoreApplication.translate("MainWindow", u"Com Ajuda", None))
        self.radio_restrito_2.setText(QCoreApplication.translate("MainWindow", u"Restrito ao Leito", None))
        self.orientacao.setTitle("")
        self.radio_desorientado_2.setText(QCoreApplication.translate("MainWindow", u"Desorientado", None))
        self.radio_orientado_2.setText(QCoreApplication.translate("MainWindow", u"Orientado", None))
        self.quanto_ao.setTitle("")
        self.radio_tempo_2.setText(QCoreApplication.translate("MainWindow", u"Tempo", None))
        self.radio_pessoa_2.setText(QCoreApplication.translate("MainWindow", u"Pessoa", None))
        self.radio_espaco_2.setText(QCoreApplication.translate("MainWindow", u"Espa\u00e7o", None))
        self.comunicacao.setTitle("")
        self.radio_verbal_presente_2.setText(QCoreApplication.translate("MainWindow", u"Comunica\u00e7\u00e3o Verbal Presente", None))
        self.radio_comunicativo_2.setText(QCoreApplication.translate("MainWindow", u"Comunicativo", None))
        self.radio_verbal_prejudicada_2.setText(QCoreApplication.translate("MainWindow", u"Comunica\u00e7\u00e3o Verbal Prejudicada", None))
        self.radio_nao_comunicativo_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Comunicativo", None))
        self.postura.setTitle("")
        self.radio_sofrivel_2.setText(QCoreApplication.translate("MainWindow", u"Sofr\u00edvel", None))
        self.radio_boa_2.setText(QCoreApplication.translate("MainWindow", u"Boa", None))
        self.atencao.setTitle("")
        self.radio_vigilancia_2.setText(QCoreApplication.translate("MainWindow", u"Vigil\u00e2ncia", None))
        self.radio_tenacidade_2.setText(QCoreApplication.translate("MainWindow", u"Tenacidade", None))
        self.memoria.setTitle("")
        self.radio_integra_2.setText(QCoreApplication.translate("MainWindow", u"Integra", None))
        self.radio_deficiente_2.setText(QCoreApplication.translate("MainWindow", u"Deficiente", None))
        self.radio_recente_2.setText(QCoreApplication.translate("MainWindow", u"Recente", None))
        self.radio_passada_2.setText(QCoreApplication.translate("MainWindow", u"Passada", None))
        self.atitude.setTitle("")
        self.radio_ativa_2.setText(QCoreApplication.translate("MainWindow", u"Ativa", None))
        self.radio_passiva_2.setText(QCoreApplication.translate("MainWindow", u"Passiva", None))
        self.radio_forcada_2.setText(QCoreApplication.translate("MainWindow", u"For\u00e7ada", None))
        self.movimentacao.setTitle("")
        self.radio_semi_acamado_2.setText(QCoreApplication.translate("MainWindow", u"Semi-Acamado", None))
        self.radio_deambula_2.setText(QCoreApplication.translate("MainWindow", u"Deambula", None))
        self.radio_acamado_2.setText(QCoreApplication.translate("MainWindow", u"Acamado", None))
        self.radio_restrito_leito_2.setText(QCoreApplication.translate("MainWindow", u"Restrito ao Leito", None))
        self.radio_sem_movimentacao_2.setText(QCoreApplication.translate("MainWindow", u"Sem Movimenta\u00e7\u00e3o", None))
        self.radio_deambula_ajuda_2.setText(QCoreApplication.translate("MainWindow", u"Deambula com Ajuda", None))
        self.movimenta_se_com_ajuda.setTitle("")
        self.radio_sim_2.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.expressao_facial.setTitle("")
        self.radio_inexpressivo_2.setText(QCoreApplication.translate("MainWindow", u"Inexpressivo", None))
        self.radio_apatico_2.setText(QCoreApplication.translate("MainWindow", u"Ap\u00e1tico", None))
        self.radio_desapontado_2.setText(QCoreApplication.translate("MainWindow", u"Desapontado", None))
        self.radio_desconfiado_2.setText(QCoreApplication.translate("MainWindow", u"Desconfiado", None))
        self.radio_colerico_2.setText(QCoreApplication.translate("MainWindow", u"Col\u00e9rico", None))
        self.radio_tenso_2.setText(QCoreApplication.translate("MainWindow", u"Tenso", None))
        self.radio_triste_2.setText(QCoreApplication.translate("MainWindow", u"Triste", None))
        self.radio_alegre_2.setText(QCoreApplication.translate("MainWindow", u"Alegre", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"N\u00edvel de Consci\u00eancia:", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Estado Geral:", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Hidrata\u00e7\u00e3o:", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Nutri\u00e7\u00e3o:", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Locomo\u00e7\u00e3o:", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Orienta\u00e7\u00e3o:", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Quanto ao:", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Comunica\u00e7\u00e3o:", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Causa:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Postura:", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Aten\u00e7\u00e3o:", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Express\u00e3o Facial:", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Movimenta\u00e7\u00e3o:", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Mem\u00f3ria:", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Atitude:", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Movimenta-se com Ajuda:", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"De:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Avalia\u00e7\u00e3o Geral", None))
        self.groupLesoes_11.setTitle(QCoreApplication.translate("MainWindow", u"NEUROLOGICO", None))
        self.pupilas.setTitle("")
        self.radio_isocoricas.setText(QCoreApplication.translate("MainWindow", u"Isoc\u00f3ricas", None))
        self.radio_anisoricas.setText(QCoreApplication.translate("MainWindow", u"Anisoc\u00f3ricas", None))
        self.reagentes_a_luz.setTitle("")
        self.radio_sim_3.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_3.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.forca_muscular.setTitle("")
        self.radio_preservada.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_reduzida.setText(QCoreApplication.translate("MainWindow", u"Reduzida", None))
        self.reflexos.setTitle("")
        self.radio_preservados.setText(QCoreApplication.translate("MainWindow", u"Preservados", None))
        self.radio_alterados.setText(QCoreApplication.translate("MainWindow", u"Alterados", None))
        self.sensibilidade.setTitle("")
        self.radio_normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.radio_reduzida_sensibilidade.setText(QCoreApplication.translate("MainWindow", u"Reduzida", None))
        self.escala_de_coma_de_Glasgow.setTitle("")
        self.radio_sim_coma.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_coma.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.abertura_ocular.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.abertura_ocular.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.abertura_ocular.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.abertura_ocular.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))

        self.resposta_verbal.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.resposta_verbal.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.resposta_verbal.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.resposta_verbal.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.resposta_verbal.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))

        self.resposta_motora.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.resposta_motora.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.resposta_motora.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.resposta_motora.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.resposta_motora.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.resposta_motora.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))

        self.resposta_pupilar.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.resposta_pupilar.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.resposta_pupilar.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Pupilas:", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Reagentes a Luz:", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"For\u00e7a Muscular:", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Reflexos:", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade:", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Escala de coma de Glasgow:", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Abertura Ocular:", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Resposta Verbal:", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Resposta Motora:", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Resposta Pupilar:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Neurologico", None))
        self.groupLesoes_12.setTitle(QCoreApplication.translate("MainWindow", u"TECIDOS CUT\u00c2NEOS E MUCOSAS", None))
        self.mobilidade.setTitle("")
        self.radio_mobilidade_presente.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.radio_mobilidade_ausente.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.elasticidade.setTitle("")
        self.radio_elasticidade_preservada.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_elasticidade_diminuida.setText(QCoreApplication.translate("MainWindow", u"Diminu\u00edda", None))
        self.espessura.setTitle("")
        self.radio_eufrofica_espessura.setText(QCoreApplication.translate("MainWindow", u"Eutr\u00f3fica", None))
        self.radio_atrofica.setText(QCoreApplication.translate("MainWindow", u"Atr\u00f3fica", None))
        self.radio_hipertrofica.setText(QCoreApplication.translate("MainWindow", u"Hipertr\u00f3fica", None))
        self.radio_espessa.setText(QCoreApplication.translate("MainWindow", u"Espessa", None))
        self.textura.setTitle("")
        self.radio_eufrofica.setText(QCoreApplication.translate("MainWindow", u"Eutr\u00f3fica", None))
        self.radio_seca.setText(QCoreApplication.translate("MainWindow", u"Seca", None))
        self.radio_lisa.setText(QCoreApplication.translate("MainWindow", u"Lisa", None))
        self.radio_aspera.setText(QCoreApplication.translate("MainWindow", u"\u00c1spera", None))
        self.radio_enrugada.setText(QCoreApplication.translate("MainWindow", u"Enrugada", None))
        self.presenca_de_sudorese.setTitle("")
        self.radio_presenca_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_presenca_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radio_diaforese.setText(QCoreApplication.translate("MainWindow", u"Diaforese", None))
        self.radio_hiperidrose.setText(QCoreApplication.translate("MainWindow", u"Hiperidrose", None))
        self.radio_xerodermia.setText(QCoreApplication.translate("MainWindow", u"Xerodermia", None))
        self.coloracao_da_pele.setTitle("")
        self.radio_hipocorada.setText(QCoreApplication.translate("MainWindow", u"Hipocorada", None))
        self.radio_palidez.setText(QCoreApplication.translate("MainWindow", u"Palidez", None))
        self.radio_normocorada.setText(QCoreApplication.translate("MainWindow", u"Normocorada", None))
        self.radio_hiperemiade.setText(QCoreApplication.translate("MainWindow", u"Hiperemiada", None))
        self.cianose.setTitle("")
        self.radio_acianotico.setText(QCoreApplication.translate("MainWindow", u"Acian\u00f3tico", None))
        self.radio_cianotico.setText(QCoreApplication.translate("MainWindow", u"Cian\u00f3tico", None))
        self.icterica.setTitle("")
        self.radio_anicterico.setText(QCoreApplication.translate("MainWindow", u"Anict\u00e9rico", None))
        self.radio_icterico.setText(QCoreApplication.translate("MainWindow", u"Ict\u00e9rico", None))
        self.turgor_cutaneo.setTitle("")
        self.radio_preservado.setText(QCoreApplication.translate("MainWindow", u"Preservado", None))
        self.radio_Diminuido.setText(QCoreApplication.translate("MainWindow", u"Diminu\u00eddo", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Turgor Cut\u00e2neo:", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Icter\u00edcia:", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Cianose:", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o da Pele:", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Outra:", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"Elasticidade:", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de sudorese:", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Textura:", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Espessura:", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Mobilidade:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tecidos Cut\u00e2neos", None))
        self.groupLesoes_13.setTitle(QCoreApplication.translate("MainWindow", u"LES\u00d5ES I", None))
        self.m_distribuicao.setTitle("")
        self.btn_linear.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.btn_circular.setText(QCoreApplication.translate("MainWindow", u"Circular", None))
        self.btn_arco.setText(QCoreApplication.translate("MainWindow", u"Em arco", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.lesoes_hemorragicas.setTitle("")
        self.btn_sim_3.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_3.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.lh_tipo.setTitle("")
        self.btn_esquimose.setText(QCoreApplication.translate("MainWindow", u"Esquimose", None))
        self.btn_petequias.setText(QCoreApplication.translate("MainWindow", u"Pet\u00e9quias", None))
        self.btn_hematoma.setText(QCoreApplication.translate("MainWindow", u"Hematoma", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Distibui\u00e7\u00e3o:", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.lv_distribuicao.setTitle("")
        self.btn_circular_2.setText(QCoreApplication.translate("MainWindow", u"Circular", None))
        self.btn_arco_2.setText(QCoreApplication.translate("MainWindow", u"Em arco", None))
        self.btn_linear_2.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es hemorr\u00e1gicas:", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Distribui\u00e7\u00e3o:", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es Planas:", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Solu\u00e7\u00f5es de continuidade:", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.lv_tamanho.setTitle("")
        self.btn_p_3.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m_3.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g_3.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lh_tamanho.setTitle("")
        self.btn_p_2.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m_2.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g_2.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.sc_tipo.setTitle("")
        self.btn_escoriacoes.setText(QCoreApplication.translate("MainWindow", u"Escoria\u00e7\u00f5es", None))
        self.btn_fissura.setText(QCoreApplication.translate("MainWindow", u"Fissura", None))
        self.btn_fistula.setText(QCoreApplication.translate("MainWindow", u"F\u00edstula", None))
        self.btn_ulceras.setText(QCoreApplication.translate("MainWindow", u"\u00dalceras", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.m_formato.setTitle("")
        self.btn_regular.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.btn_irregular.setText(QCoreApplication.translate("MainWindow", u"Irregular", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Manchas:", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es vasculares:", None))
        self.lesoes_vasculares.setTitle("")
        self.btn_sim_4.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_4.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.m_tamanho.setTitle("")
        self.btn_p.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.tipo_das_manchas.setTitle("")
        self.btn_hipo.setText(QCoreApplication.translate("MainWindow", u"Hipocr\u00f4nicas", None))
        self.btn_hiper.setText(QCoreApplication.translate("MainWindow", u"Hiperc\u00f4nicas", None))
        self.manchas.setTitle("")
        self.btn_sim_2.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.solucoes_de_continuidade.setTitle("")
        self.btn_presentes.setText(QCoreApplication.translate("MainWindow", u"Presentes", None))
        self.btn_ausentes.setText(QCoreApplication.translate("MainWindow", u"Ausentes", None))
        self.lesoes_planas.setTitle("")
        self.btn_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.lv_formato.setTitle("")
        self.btn_regular_3.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.btn_irregular_2.setText(QCoreApplication.translate("MainWindow", u"Irregular", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.lv_tipo.setTitle("")
        self.btn_telangectasia.setText(QCoreApplication.translate("MainWindow", u"Telangectasia", None))
        self.btn_eritmatosa.setText(QCoreApplication.translate("MainWindow", u"Eritmatosa", None))
        self.label_270.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.sc_tamanho.setTitle("")
        self.btn_p_4.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m_4.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g_4.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_273.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_277.setText(QCoreApplication.translate("MainWindow", u"Secre\u00e7\u00e3o:", None))
        self.sc_odor.setTitle("")
        self.btn_nao_5.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.btn_sim_5.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_279.setText(QCoreApplication.translate("MainWindow", u"Odor:", None))
        self.label_281.setText(QCoreApplication.translate("MainWindow", u"Contorno (\u00falcera):", None))
        self.sc_secrecao.setTitle("")
        self.btn_sim_25.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_25.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Les\u00f5es I", None))
        self.groupLesoes_30.setTitle(QCoreApplication.translate("MainWindow", u"LES\u00d5ES II", None))
        self.le_tipo.setTitle("")
        self.btn_escama.setText(QCoreApplication.translate("MainWindow", u"Escama", None))
        self.btn_crosta.setText(QCoreApplication.translate("MainWindow", u"Crosta", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Especificar:", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Cicatriz:", None))
        self.le_prurido.setTitle("")
        self.btn_sim_13.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_13.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.lesoes_escamativas.setTitle("")
        self.btn_presentes_2.setText(QCoreApplication.translate("MainWindow", u"Presentes", None))
        self.btn_ausentes_2.setText(QCoreApplication.translate("MainWindow", u"Ausentes", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Prurido:", None))
        self.le_cicatriz.setTitle("")
        self.btn_sim_14.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_14.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.btn_remanescente.setText(QCoreApplication.translate("MainWindow", u"Remanecentes", None))
        self.btn_recentes.setText(QCoreApplication.translate("MainWindow", u"Recente", None))
        self.le_atrofia.setTitle("")
        self.btn_sim_15.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_15.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Atrofia:", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es escamativas:", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.ls_contorno.setTitle("")
        self.btn_plano.setText(QCoreApplication.translate("MainWindow", u"Plano", None))
        self.btn_elevado.setText(QCoreApplication.translate("MainWindow", u"Elevado", None))
        self.btn_deprimido.setText(QCoreApplication.translate("MainWindow", u"Deprimido", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"Odor:", None))
        self.ls_tipos.setTitle("")
        self.btn_papula.setText(QCoreApplication.translate("MainWindow", u"P\u00e1pula", None))
        self.btn_nodulo.setText(QCoreApplication.translate("MainWindow", u"N\u00f3dulo", None))
        self.btn_urticaria.setText(QCoreApplication.translate("MainWindow", u"Urtic\u00e1ria", None))
        self.btn_espessamento.setText(QCoreApplication.translate("MainWindow", u"Espessamento", None))
        self.btn_tuberculo.setText(QCoreApplication.translate("MainWindow", u"Tub\u00e9rculo", None))
        self.ls_distribuicao.setTitle("")
        self.btn_linear_3.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.btn_circular_3.setText(QCoreApplication.translate("MainWindow", u"Circular", None))
        self.btn_arco_3.setText(QCoreApplication.translate("MainWindow", u"Em arco", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Distribui\u00e7\u00e3o:", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Distribui\u00e7\u00e3o:", None))
        self.lcl_secrecao.setTitle("")
        self.btn_sim_16.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_16.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"Contorno:", None))
        self.lcl_formato.setTitle("")
        self.btn_regular_4.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.btn_irregular_4.setText(QCoreApplication.translate("MainWindow", u"Irregular", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"Secre\u00e7\u00e3o:", None))
        self.lesoes_com_conteudo_liquido.setTitle("")
        self.btn_sim_17.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_17.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es S\u00f3lidas:", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.lcl_tamanho.setTitle("")
        self.btn_p_6.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m_6.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g_6.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es com Liqu\u00eddo: ", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.lesoes_solidas.setTitle("")
        self.btn_sim_18.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_18.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.lcl_distribuicao.setTitle("")
        self.btn_linear_4.setText(QCoreApplication.translate("MainWindow", u"Linear", None))
        self.btn_circular_4.setText(QCoreApplication.translate("MainWindow", u"Circular", None))
        self.btn_arco_4.setText(QCoreApplication.translate("MainWindow", u"Em arco", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.ls_tamanho.setTitle("")
        self.btn_p_5.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.btn_m_5.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.btn_g_5.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"Odor:", None))
        self.lcl_odor.setTitle("")
        self.btn_sim_19.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_19.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.ls_odor.setTitle("")
        self.btn_sim_20.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_20.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.ls_formato.setTitle("")
        self.btn_regular_5.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.btn_irregular_3.setText(QCoreApplication.translate("MainWindow", u"Irregular", None))
        self.lcl_tipo.setTitle("")
        self.btn_vesicula.setText(QCoreApplication.translate("MainWindow", u"Ves\u00edcula", None))
        self.btn_bolha.setText(QCoreApplication.translate("MainWindow", u"Bolha", None))
        self.btn_pustula.setText(QCoreApplication.translate("MainWindow", u"P\u00fastula", None))
        self.btn_abcesso.setText(QCoreApplication.translate("MainWindow", u"Abcesso", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Les\u00f5es II", None))
        self.groupLesoes_31.setTitle(QCoreApplication.translate("MainWindow", u"Integridade Membros Superiores e Inferiores", None))
        self.limitacoes_im.setTitle("")
        self.radioButton_182.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_183.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.mobilidade_im.setTitle("")
        self.radioButton_184.setText(QCoreApplication.translate("MainWindow", u"Ativa", None))
        self.radioButton_185.setText(QCoreApplication.translate("MainWindow", u"Passiva", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es Locomotora-Marcha:", None))
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"Altera\u00e7\u00f5es Vasculares:", None))
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"Qual:", None))
        self.musculatura_im.setTitle("")
        self.radioButton_186.setText(QCoreApplication.translate("MainWindow", u"Eutr\u00f3fica", None))
        self.radioButton_187.setText(QCoreApplication.translate("MainWindow", u"Atr\u00f3fica", None))
        self.radioButton_188.setText(QCoreApplication.translate("MainWindow", u"Hipotr\u00f3fica", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"Rigidez  Articular:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade:", None))
        self.groupBox.setTitle("")
        self.deformidades_im.setTitle("")
        self.radioButton_189.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_190.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"Perfus\u00e3o Tissular: ", None))
        self.coordenacao_im.setTitle("")
        self.radioButton_191.setText(QCoreApplication.translate("MainWindow", u"Preserva\u00e7\u00e3o", None))
        self.radioButton_192.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.perfusao_im.setTitle("")
        self.radioButton_193.setText(QCoreApplication.translate("MainWindow", u"Maior que 2 Seg.", None))
        self.radioButton_194.setText(QCoreApplication.translate("MainWindow", u"Menor que 2 Seg.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"Coordena\u00e7\u00e3o Motora:", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"For\u00e7a:", None))
        self.rigidez_im.setTitle("")
        self.radioButton_195.setText(QCoreApplication.translate("MainWindow", u"Crepta\u00e7\u00f5es Ausente", None))
        self.radioButton_196.setText(QCoreApplication.translate("MainWindow", u"Crepta\u00e7\u00f5es Presente", None))
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"Simetria", None))
        self.sensibilidade_im.setTitle("")
        self.radioButton_197.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.radioButton_198.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.simetria_im.setTitle("")
        self.radio_sim_seni_3.setText(QCoreApplication.translate("MainWindow", u"Simetricos", None))
        self.radioButton_199.setText(QCoreApplication.translate("MainWindow", u"Assimetricos", None))
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"Deformidades:", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"Mobilidade:", None))
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"Musculatura:", None))
        self.alteracoes_im.setTitle("")
        self.radioButton_200.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_201.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"Limita\u00e7\u00f5es de Movimento:", None))
        self.forca_im.setTitle("")
        self.radioButton_202.setText(QCoreApplication.translate("MainWindow", u"Hipertonia", None))
        self.radioButton_203.setText(QCoreApplication.translate("MainWindow", u"Hipotonia", None))
        self.radioButton_204.setText(QCoreApplication.translate("MainWindow", u"Atonia", None))
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"Formas de Locomo\u00e7\u00e3o:", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"Integridade M.S I", None))
        self.groupLesoes_14.setTitle(QCoreApplication.translate("MainWindow", u"MEMBROS SUPERIORES", None))
        self.sensibilidade_ms.setTitle("")
        self.radio_sim_seni.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.forca_motora_ms.setTitle("")
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Diminuida", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.edema_ms.setTitle("")
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.pulsos_perifericos_ms.setTitle("")
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.paresia_ms.setTitle("")
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.plegia_ms.setTitle("")
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade:", None))
        self.label_169.setText(QCoreApplication.translate("MainWindow", u"For\u00e7a Motora:", None))
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Edemas:", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Pulsos Perif\u00e9ricos:", None))
        self.label_160.setText(QCoreApplication.translate("MainWindow", u"Paresia:", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Plegia:", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"Amputa\u00e7\u00f5es:", None))
        self.amputacoes_ms.setTitle("")
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"SIm", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Gesso:", None))
        self.gesso_ms.setTitle("")
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tala_gessado_ms.setTitle("")
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_163.setText(QCoreApplication.translate("MainWindow", u"Tala Gessado:", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"Dispositivo Venoso:", None))
        self.dispositivo_venoso_ms.setTitle("")
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.lesos_ms.setTitle("")
        self.radioButton_22.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_23.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es:", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_166.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"M.Superiores", None))
        self.groupLesoes_15.setTitle(QCoreApplication.translate("MainWindow", u"MEMBROS INFERIORES", None))
        self.sensibilidade_mi.setTitle("")
        self.radio_preservada_2.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_alterada.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade:", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"For\u00e7a Motora:", None))
        self.forca_motora_mi.setTitle("")
        self.radio_preservada_forca.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_diminuida_forca.setText(QCoreApplication.translate("MainWindow", u"Diminuida", None))
        self.radio_ausente_forca.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.edema_mi.setTitle("")
        self.radio_sim_edemas.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_edemas.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.pulsos_perifericos_mi.setTitle("")
        self.radio_palpaveis.setText(QCoreApplication.translate("MainWindow", u"Palp\u00e1veis", None))
        self.radio_nao_palpaveis.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o Palp\u00e1veis", None))
        self.paresia_mi.setTitle("")
        self.radio_sim_paresia.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_paresia.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.plegia_mi.setTitle("")
        self.radio_sim_plegia.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_plegia.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.amputacoes_mi.setTitle("")
        self.radio_sim_amputacoes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_amputacoes.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.gesso_mi.setTitle("")
        self.radio_sim_gesso.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_gesso.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tala_gessado_mi.setTitle("")
        self.radio_sim_tala.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_tala.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.dispositivo_venoso_mi.setTitle("")
        self.radio_sim_venoso.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao_venoso.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.lesos_mi.setTitle("")
        self.radio_nao_lesoes.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radio_sim_lesoes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"Edemas:", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Pulsos Perif\u00e9ricos:", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Paresia:", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Plegia:", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"Amputa\u00e7\u00f5es:", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Gesso:", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"Tala Gessado:", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Dispositivo Venoso:", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es:", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"M.Inferiores", None))
        self.groupLesoes_16.setTitle(QCoreApplication.translate("MainWindow", u"UNHAS", None))
        self.unha.setTitle("")
        self.radio_regular_3.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.radio_irregular.setText(QCoreApplication.translate("MainWindow", u"Irregular", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Unhas:", None))
        self.implantacao.setTitle("")
        self.radio_angulo_reto.setText(QCoreApplication.translate("MainWindow", u"\u00c2ngulo reto", None))
        self.radio_menor.setText(QCoreApplication.translate("MainWindow", u"Menor de 160\u00b0", None))
        self.radio_maior.setText(QCoreApplication.translate("MainWindow", u"Maior que 160\u00b0", None))
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Implanta\u00e7\u00e3o:", None))
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Outra:", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Superf\u00edcie:", None))
        self.superficie.setTitle("")
        self.radio_lisa_2.setText(QCoreApplication.translate("MainWindow", u"Lisa", None))
        self.radio_distrofica.setText(QCoreApplication.translate("MainWindow", u"Distr\u00f3fica (irregular, espessada e rugosa)", None))
        self.espessura_olhos.setTitle("")
        self.radio_preservada_3.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_fina.setText(QCoreApplication.translate("MainWindow", u"Fina", None))
        self.radio_grossa.setText(QCoreApplication.translate("MainWindow", u"Grossa", None))
        self.coloracao.setTitle("")
        self.radio_rosada.setText(QCoreApplication.translate("MainWindow", u"Rosada", None))
        self.radio_cianotica.setText(QCoreApplication.translate("MainWindow", u"Cian\u00f3tica", None))
        self.radio_palida.setText(QCoreApplication.translate("MainWindow", u"P\u00e1lida", None))
        self.radio_descorada.setText(QCoreApplication.translate("MainWindow", u"Descorada", None))
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o:", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Outra:", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Espessura:", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Outra:", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Brilho:", None))
        self.brilho.setTitle("")
        self.radio_presente.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.radio_opaco.setText(QCoreApplication.translate("MainWindow", u"Opaco", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"Consist\u00eancia:", None))
        self.consistencia.setTitle("")
        self.radio_fragil.setText(QCoreApplication.translate("MainWindow", u"Fr\u00e1gil", None))
        self.radio_forte.setText(QCoreApplication.translate("MainWindow", u"Forte", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Leucon\u00edquia:", None))
        self.leuconiquia.setTitle("")
        self.radio_leuconiquia_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_leuconiquia_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Qual:", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Onicofagia:", None))
        self.onicofagia.setTitle("")
        self.radio_onicofagia_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_onicofagia_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es de higiene:", None))
        self.condicoes_de_higiene.setTitle("")
        self.radio_precaria.setText(QCoreApplication.translate("MainWindow", u"Prec\u00e1ria", None))
        self.radio_satisfatoria.setText(QCoreApplication.translate("MainWindow", u"Satisfat\u00f3ria", None))
        self.radio_regular_4.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Unhas", None))
        self.groupLesoes_17.setTitle(QCoreApplication.translate("MainWindow", u"CR\u00c2NIO", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Outro:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Escamas:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.massas.setTitle("")
        self.btn_sim_7.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_7.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es:", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Cabelos Colora\u00e7\u00e3o:", None))
        self.simetria_cranio.setTitle("")
        self.btn_simetrico.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9trico", None))
        self.btn_assimetrico.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9trico", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.forma_cranio.setTitle("")
        self.btn_arredondado.setText(QCoreApplication.translate("MainWindow", u"Arredonado", None))
        self.btn_oval.setText(QCoreApplication.translate("MainWindow", u"Oval", None))
        self.escamas.setTitle("")
        self.btn_sim_8.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_8.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Massas:", None))
        self.abaulamento.setTitle("")
        self.btn_sim_9.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_9.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9tria:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Contorno:", None))
        self.cabelos_cor.setTitle("")
        self.btn_artificial.setText(QCoreApplication.translate("MainWindow", u"Artificial", None))
        self.btn_natural.setText(QCoreApplication.translate("MainWindow", u"Natural", None))
        self.btn_distribuicao.setText(QCoreApplication.translate("MainWindow", u"Distribui\u00e7\u00e3o", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Abaulamento:", None))
        self.lesoes.setTitle("")
        self.btn_sim_10.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_10.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.quantidade.setTitle("")
        self.btn_preservada.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.btn_com_alteracao.setText(QCoreApplication.translate("MainWindow", u"Com altera\u00e7\u00e3o", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Localiza\u00e7\u00e3o das Anormalidades:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Parasitas:", None))
        self.prurido.setTitle("")
        self.btn_sim_11.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_11.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.localizacao_das_anormalidades.setTitle("")
        self.btn_anterior.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.btn_central.setText(QCoreApplication.translate("MainWindow", u"Central", None))
        self.btn_posterior.setText(QCoreApplication.translate("MainWindow", u"Posterior", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.tipo_alteracao_cabelo.setTitle("")
        self.btn_queda.setText(QCoreApplication.translate("MainWindow", u"Queda", None))
        self.btn_alopecia.setText(QCoreApplication.translate("MainWindow", u"Alopecia", None))
        self.bt_hirutismo.setText(QCoreApplication.translate("MainWindow", u"Hirsutismo", None))
        self.btn_calvicie.setText(QCoreApplication.translate("MainWindow", u"Calv\u00edcie", None))
        self.btn_hipertricose.setText(QCoreApplication.translate("MainWindow", u"Hipertricose", None))
        self.btn_madarose.setText(QCoreApplication.translate("MainWindow", u"Madarose", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es de Higiene Satisfast\u00f3ria:", None))
        self.condicoes_de_higiene_cranio.setTitle("")
        self.btn_regular_2.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.btn_precaria.setText(QCoreApplication.translate("MainWindow", u"Prec\u00e1ria", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Prurido:", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Outra:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.parasitas.setTitle("")
        self.btn_sim_12.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_12.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Cr\u00e2nio", None))
        self.groupLesoes_18.setTitle(QCoreApplication.translate("MainWindow", u"FACE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.simetria_face.setTitle("")
        self.btn_simetrica.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9trica", None))
        self.btn_assimetrica.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9trica", None))
        self.dor_seios_frontais.setTitle("")
        self.btn_sim_21.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_21.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Dor \u00e0 palpa\u00e7\u00e3o nos seios maxilares:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Simetria:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.dor_seios_paranasais.setTitle("")
        self.btn_sim_22.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_22.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.formato.setTitle("")
        self.btn_arredondar.setText(QCoreApplication.translate("MainWindow", u"Arredondada", None))
        self.btn_triangular.setText(QCoreApplication.translate("MainWindow", u"Triangular", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Outro:", None))
        self.dor_seios_maxilares.setTitle("")
        self.btn_nao_23.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.btn_sim_23.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Dor \u00e0 palpa\u00e7\u00e3o nos seios paranasais:", None))
        self.edema_palpebral.setTitle("")
        self.btn_sim_24.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.btn_nao_24.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Edema Palpebral:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Dor \u00e0 palpa\u00e7\u00e3o nos seios frontais:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Face", None))
        self.groupLesoes_19.setTitle(QCoreApplication.translate("MainWindow", u"OLHOS", None))
        self.acuidade_visual.setTitle("")
        self.radioButton_49.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.radioButton_50.setText(QCoreApplication.translate("MainWindow", u"D\u00edminuida", None))
        self.fotorreativas.setTitle("")
        self.radioButton_51.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_52.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Acuidade Visual:", None))
        self.halo_senil.setTitle("")
        self.radioButton_53.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.radioButton_54.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.distancia.setTitle("")
        self.radioButton_55.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_56.setText(QCoreApplication.translate("MainWindow", u"Aumentada", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Simetricos:", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"Integridade", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Conjutiva:", None))
        self.esclerotica.setText(QCoreApplication.translate("MainWindow", u"Esclerotica", None))
        self.presenca_de_secrecoes.setTitle("")
        self.radioButton_57.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_58.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tamanho.setTitle("")
        self.radioButton_60.setText(QCoreApplication.translate("MainWindow", u"Preservado", None))
        self.radioButton_61.setText(QCoreApplication.translate("MainWindow", u"Miose", None))
        self.radioButton_59.setText(QCoreApplication.translate("MainWindow", u"Midriase", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Fotorreativas:", None))
        self.label_271.setText(QCoreApplication.translate("MainWindow", u"Dist\u00e2ncia:", None))
        self.label_272.setText(QCoreApplication.translate("MainWindow", u"Preservada:", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o:", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"Halo Senil:", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Secre\u00e7\u00f5es:", None))
        self.conjuntiva.setTitle("")
        self.radioButton_62.setText(QCoreApplication.translate("MainWindow", u"Brilhante", None))
        self.radioButton_63.setText(QCoreApplication.translate("MainWindow", u"Seca", None))
        self.radioButton_64.setText(QCoreApplication.translate("MainWindow", u"Hiperemiada", None))
        self.radioButton_65.setText(QCoreApplication.translate("MainWindow", u"\u00damida", None))
        self.radioButton_66.setText(QCoreApplication.translate("MainWindow", u"Levemente rosada", None))
        self.radioButton_67.setText(QCoreApplication.translate("MainWindow", u"Ict\u00e9rica", None))
        self.simetricos.setTitle("")
        self.radioButton_68.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_69.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.integridade_2.setText(QCoreApplication.translate("MainWindow", u"Pupilas", None))
        self.preservada.setTitle("")
        self.radioButton_70.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_71.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.integro.setText(QCoreApplication.translate("MainWindow", u"Integridade:", None))
        self.label_274.setText(QCoreApplication.translate("MainWindow", u"Movimentos Oculares:", None))
        self.label_275.setText(QCoreApplication.translate("MainWindow", u"Forumen Lacrimal", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.forumen_lacrimal.setTitle("")
        self.radioButton_72.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_73.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.movimentos_oculares.setTitle("")
        self.radioButton_74.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_75.setText(QCoreApplication.translate("MainWindow", u"Aumentada", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Olhos", None))
        self.groupLesoes_20.setTitle(QCoreApplication.translate("MainWindow", u"NARINAS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Integridade Preservada:", None))
        self.simetria_narinas.setTitle("")
        self.radio_simetricas_3.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9tricas", None))
        self.radio_simetricas_4.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9tricas", None))
        self.coloracao_interna.setTitle("")
        self.radioButton_90.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_91.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.secrecoes.setTitle("")
        self.radioButton_92.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_93.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.lesoes_narinas.setTitle("")
        self.radioButton_94.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_95.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Edemas:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Simetria:", None))
        self.integridade_preservada_narinas.setTitle("")
        self.radio_sim_4.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_96.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Integridade Preservada:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cavidade Nasal:", None))
        self.edemas_simetria.setTitle("")
        self.radioButton_97.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_98.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Secre\u00e7\u00f5es:", None))
        self.cavidade_nasal.setTitle("")
        self.radioButton_99.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_100.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.tipo_secrecao_nasal.setTitle("")
        self.radioButton_102.setText(QCoreApplication.translate("MainWindow", u"Aquosa", None))
        self.radioButton_103.setText(QCoreApplication.translate("MainWindow", u"Mucoide", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.tamanho_narinas.setTitle("")
        self.radioButton_148.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.radioButton_152.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.radioButton_153.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"Desvio de Septo:", None))
        self.desvio_de_septo.setTitle("")
        self.radioButton_154.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_155.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.olfato.setTitle("")
        self.radioButton_156.setText(QCoreApplication.translate("MainWindow", u"Preservado", None))
        self.radioButton_157.setText(QCoreApplication.translate("MainWindow", u"Diminuido", None))
        self.radioButton_158.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"Olfato:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Narinas", None))
        self.groupLesoes_22.setTitle(QCoreApplication.translate("MainWindow", u"PAVILH\u00c3O AUDITIVO", None))
        self.groupBox_150.setTitle("")
        self.groupBox_151.setTitle("")
        self.groupBox_152.setTitle("")
        self.groupBox_154.setTitle("")
        self.groupBox_155.setTitle("")
        self.integridade_preservada_pa.setTitle("")
        self.opcao_sim_ip.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_ip.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_276.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Cerumen:", None))
        self.label_280.setText(QCoreApplication.translate("MainWindow", u"Queixa de Odor:", None))
        self.acuidade_auditiva_pa.setTitle("")
        self.opcao_diminuida_aa.setText(QCoreApplication.translate("MainWindow", u"Diminu\u00edda", None))
        self.opcao_preservada_aa.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"Queixa de Zumbido:", None))
        self.condicoes_de_higiene_pa.setTitle("")
        self.opcao_satisfatoria_ch.setText(QCoreApplication.translate("MainWindow", u"Satisfatoria", None))
        self.opcao_precaria_ch.setText(QCoreApplication.translate("MainWindow", u"Prec\u00e1ria", None))
        self.ssxzxzx.setText(QCoreApplication.translate("MainWindow", u"Integridade Preservada:", None))
        self.queixa_de_zumbido.setTitle("")
        self.opcao_sim_qz.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_qz.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_278.setText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00f5es de Higiene:", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"Acuidade Auditiva:", None))
        self.queixa_de_odor.setTitle("")
        self.opcao_sim_qo.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_qo.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.presenca_de_cerumen.setTitle("")
        self.opcao_sim_pc.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_pc.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_282.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Secre\u00e7\u00f5es:", None))
        self.presenca_de_secrecoes_pa.setTitle("")
        self.opcao_sim_ps.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_ps.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.uso_de_aparelho_auditivo.setTitle("")
        self.opcao_sim_upa.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_upa.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"Implementa\u00e7\u00e3o:", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Uso de aparelho auditivo:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Pavilh\u00e3o Auditivo ", None))
        self.groupLesoes_23.setTitle(QCoreApplication.translate("MainWindow", u"REGI\u00c3O CERVICAL", None))
        self.groupBox_156.setTitle("")
        self.groupBox_157.setTitle("")
        self.groupBox_160.setTitle("")
        self.groupBox_161.setTitle("")
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"Fremil Tatil:", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.central_rc.setTitle("")
        self.opcao_sim_central.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_central.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Movimenta\u00e7\u00e3o:", None))
        self.pulso_carotideo_rc.setTitle("")
        self.opcao_ausente_pc.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.opcao_presente_pc.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.presenca_de_massas_rc.setTitle("")
        self.opcao_sim_pm.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_pm.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.movimentacao_rc.setTitle("")
        self.opcao_preservada_m.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.opcao_alterada_m.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"Pulso Carotideo:", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"Cicatrizes:", None))
        self.rigidez_de_nuca.setTitle("")
        self.opcao_sim_rn.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_rn.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"Central:", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de massas:", None))
        self.ingurgimento_jugular_rc.setTitle("")
        self.opcao_ausente_ij.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.opcao_presente_ij.setText(QCoreApplication.translate("MainWindow", u"Presente", None))
        self.simetrica_rc.setTitle("")
        self.opcao_sim_simetrica.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_simetrica.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.cicratizes.setTitle("")
        self.opcao_sim_cicatrizes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_cicatrizes.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"Ingurgimento Jugular:", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"Simetrica:", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"Rigidez da Nuca:", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.linfonodos.setTitle("")
        self.opcao_dolores_lin.setText(QCoreApplication.translate("MainWindow", u"Dolores", None))
        self.opcao_palpaveis_lin.setText(QCoreApplication.translate("MainWindow", u"Palpaveis", None))
        self.opcao_indolores_lin.setText(QCoreApplication.translate("MainWindow", u"Indolores", None))
        self.opcao_nao_p_lin.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o palpaveis", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"Tireoide:", None))
        self.tireoide_rc.setTitle("")
        self.opcao_preservada_tir.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.opcao_aumentada_tir.setText(QCoreApplication.translate("MainWindow", u"Aumentada", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"Linfomodos:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Regi\u00e3o Cervical", None))
        self.groupLesoes_24.setTitle(QCoreApplication.translate("MainWindow", u"TORAX", None))
        self.groupBox_162.setTitle("")
        self.groupBox_163.setTitle("")
        self.groupBox_164.setTitle("")
        self.groupBox_165.setTitle("")
        self.groupBox_166.setTitle("")
        self.groupBox_167.setTitle("")
        self.oxigenacao.setTitle("")
        self.radioButton_48.setText(QCoreApplication.translate("MainWindow", u"Oxigenoterapia", None))
        self.radioButton_76.setText(QCoreApplication.translate("MainWindow", u"Ar Ambiente", None))
        self.radioButton_77.setText(QCoreApplication.translate("MainWindow", u"Entubado", None))
        self.radioButton_78.setText(QCoreApplication.translate("MainWindow", u"Traqueostomizado", None))
        self.radioButton_79.setText(QCoreApplication.translate("MainWindow", u"Sem Ventila\u00e7\u00e3o Mec\u00e2nica", None))
        self.radioButton_80.setText(QCoreApplication.translate("MainWindow", u"Com Ventila\u00e7\u00e3o Mec\u00e2nica", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Expansibilidade:", None))
        self.bulhas_dois_tempos.setTitle("")
        self.radioButton_82.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_81.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.bulhas_cardiacas.setTitle("")
        self.radioButton_83.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_84.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.integridade_cutanea.setTitle("")
        self.radioButton_85.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_86.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Deformidades:", None))
        self.forma_torax.setTitle("")
        self.radioButton_87.setText(QCoreApplication.translate("MainWindow", u"Peito de Pombo", None))
        self.radioButton_88.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9trica", None))
        self.radioButton_89.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9trica", None))
        self.radioButton_101.setText(QCoreApplication.translate("MainWindow", u"Em Tonel", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fonese:", None))
        self.tipo_deformidades.setTitle("")
        self.radioButton_119.setText(QCoreApplication.translate("MainWindow", u"Escoliose", None))
        self.radioButton_120.setText(QCoreApplication.translate("MainWindow", u"Cifose", None))
        self.radioButton_121.setText(QCoreApplication.translate("MainWindow", u"Lordose", None))
        self.fonese.setTitle("")
        self.radioButton_122.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.radioButton_123.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Local:", None))
        self.tipo_de_alteracao.setTitle("")
        self.radioButton_124.setText(QCoreApplication.translate("MainWindow", u"Abaulamento", None))
        self.radioButton_125.setText(QCoreApplication.translate("MainWindow", u"Depress\u00f5es", None))
        self.radioButton_126.setText(QCoreApplication.translate("MainWindow", u"Regi\u00e3o Dolorosa", None))
        self.expansibilidade.setTitle("")
        self.radioButton_127.setText(QCoreApplication.translate("MainWindow", u"Toraxica", None))
        self.radioButton_128.setText(QCoreApplication.translate("MainWindow", u"Abdominal", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Altera\u00e7\u00f5es:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Integridade Cut\u00e2nea:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Respira\u00e7\u00e3o:", None))
        self.deformidades.setTitle("")
        self.radioButton_129.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_130.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Especificar Fonese:", None))
        self.alteracoes.setTitle("")
        self.radioButton_131.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_132.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Tipo:", None))
        self.respiracao_torax.setTitle("")
        self.radioButton_133.setText(QCoreApplication.translate("MainWindow", u"Toraxica", None))
        self.radioButton_134.setText(QCoreApplication.translate("MainWindow", u"Abdominal", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Bulhas Cardiacas:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Oxigena\u00e7\u00e3o:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Bulhas Em Dois Tempos:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Torax", None))
        self.groupLesoes_21.setTitle(QCoreApplication.translate("MainWindow", u"BOCA E FARINGE", None))
        self.groupBox_146.setTitle("")
        self.groupBox_37.setTitle("")
        self.groupBox_147.setTitle("")
        self.groupBox_149.setTitle("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Sangramento:", None))
        self.ml_rima_labial.setTitle("")
        self.radioButton_24.setText(QCoreApplication.translate("MainWindow", u"Simetrica", None))
        self.radioButton_25.setText(QCoreApplication.translate("MainWindow", u"Assimetrica", None))
        self.ml_edema_bf.setTitle("")
        self.radioButton_26.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_27.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Integridade Preservada:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Rima labial:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Edema:", None))
        self.ml_integridade_preservada_bf.setTitle("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_28.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Especificar Les\u00f5es:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Gengiva", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Especificar a rima:", None))
        self.g_sangramento_bf.setTitle("")
        self.radioButton_29.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_30.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Mucosa Labial", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es no Edema:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Integridade Preservada:", None))
        self.g_integridade_reservada_bf.setTitle("")
        self.radioButton_31.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_32.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.g_edema_bf.setTitle("")
        self.radioButton_33.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_34.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Edema:", None))
        self.g_lesoes_bf.setTitle("")
        self.radioButton_35.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_36.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Denti\u00e7\u00e3o Natural:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Uso de Pr\u00f3tese:", None))
        self.uso_de_protese.setTitle("")
        self.radioButton_37.setText(QCoreApplication.translate("MainWindow", u"Superior", None))
        self.radioButton_38.setText(QCoreApplication.translate("MainWindow", u"Inferior", None))
        self.radioButton_39.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_40.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Conserva\u00e7\u00e3o:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Dentes", None))
        self.denticao_natural.setTitle("")
        self.radioButton_41.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_42.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.d_conservacao_bf.setTitle("")
        self.radioButton_43.setText(QCoreApplication.translate("MainWindow", u"Regular", None))
        self.radioButton_44.setText(QCoreApplication.translate("MainWindow", u"Satisfatoria", None))
        self.radioButton_45.setText(QCoreApplication.translate("MainWindow", u"Precaria", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es no Palato:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o do Palato:", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Palato", None))
        self.p_lesoes_palato.setTitle("")
        self.radioButton_46.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_47.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Ulcera\u00e7\u00f5es:", None))
        self.l_lesoes_lingua.setTitle("")
        self.radioButton_104.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_105.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es na l\u00edngua:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o da L\u00edngua:", None))
        self.l_ulceracoes_bf.setTitle("")
        self.radioButton_106.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_107.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"L\u00edngua", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Faringe:", None))
        self.n_faringe_bf.setTitle("")
        self.radioButton_108.setText(QCoreApplication.translate("MainWindow", u"Hipercorada", None))
        self.radioButton_109.setText(QCoreApplication.translate("MainWindow", u"Nomocorada", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Amigdalas", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Colora\u00e7\u00e3o da Faringe:", None))
        self.n_edema_faringe.setTitle("")
        self.radioButton_110.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_111.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Aspectos:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Integra:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Edema:", None))
        self.n_coloracao_faringe.setTitle("")
        self.radioButton_112.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radioButton_113.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Nodulos", None))
        self.n_acpectos_bf.setTitle("")
        self.radioButton_114.setText(QCoreApplication.translate("MainWindow", u"Lateralizada", None))
        self.radioButton_115.setText(QCoreApplication.translate("MainWindow", u"Centralizada", None))
        self.radioButton_116.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9trica", None))
        self.radioButton_117.setText(QCoreApplication.translate("MainWindow", u"Simetrica", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Altera\u00e7\u00f5es:", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"\u00davula:", None))
        self.a_integra_bf.setTitle("")
        self.radioButton_146.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_147.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.a_uvula_bf.setTitle("")
        self.radioButton_151.setText(QCoreApplication.translate("MainWindow", u"Centralizada", None))
        self.radioButton_150.setText(QCoreApplication.translate("MainWindow", u"Desvio \u00e0 Direita", None))
        self.radioButton_149.setText(QCoreApplication.translate("MainWindow", u"Desvio \u00e0 Esquerda", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Boca e Faringe", None))
        self.groupLesoes_25.setTitle(QCoreApplication.translate("MainWindow", u"MAMAS", None))
        self.mastectomia.setText(QCoreApplication.translate("MainWindow", u"Mastectomia:", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade:", None))
        self.expressao_mamilar_2.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de secre\u00e7\u00f5es:", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Consist\u00eancia:", None))
        self.forma_mamas.setTitle("")
        self.opcao_globosa_f.setText(QCoreApplication.translate("MainWindow", u"Globosa", None))
        self.opcao_pendular_f.setText(QCoreApplication.translate("MainWindow", u"Pendular", None))
        self.opcao_ingurtidas_f.setText(QCoreApplication.translate("MainWindow", u"Ingurtidas", None))
        self.planicie_dos_mamilos.setTitle("")
        self.opcao_plano_pm.setText(QCoreApplication.translate("MainWindow", u"Planos", None))
        self.opcao_semiplanos_pm.setText(QCoreApplication.translate("MainWindow", u"Semiplanos", None))
        self.opcao_invertidos_pm.setText(QCoreApplication.translate("MainWindow", u"Invertidos", None))
        self.opcao_protusos_pm.setText(QCoreApplication.translate("MainWindow", u"Protusos", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"Express\u00e3o Mamilar", None))
        self.tamanho_2.setText(QCoreApplication.translate("MainWindow", u"Tamanho:", None))
        self.planice_mamilos.setText(QCoreApplication.translate("MainWindow", u"Planice dos Mamilos:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Localiza\u00e7\u00e3o:", None))
        self.palpacao_de_massas.setTitle("")
        self.opcao_sim_pm_2.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_pm_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.palpacao_massas.setText(QCoreApplication.translate("MainWindow", u"Palpa\u00e7\u00e3o de Massas:", None))
        self.forma.setText(QCoreApplication.translate("MainWindow", u"Forma:", None))
        self.expressao_mamilar_mamas.setTitle("")
        self.opcao_sim_ps_2.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_ps_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"Mobilidade:", None))
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"Simetria:", None))
        self.mastectomia_mamas.setTitle("")
        self.opcao_direita_m.setText(QCoreApplication.translate("MainWindow", u"Direta", None))
        self.opcao_esquerda_m.setText(QCoreApplication.translate("MainWindow", u"Esquerda", None))
        self.opcao_nr_m.setText(QCoreApplication.translate("MainWindow", u"Nunca realizou", None))
        self.simetria_mamas.setTitle("")
        self.opcao_sim_simetria.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.opcao_nao_simetria.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"Mamas", None))
        self.groupLesoes_26.setTitle(QCoreApplication.translate("MainWindow", u"PULM\u00d5ES", None))
        self.groupBox_175.setTitle("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Expectora\u00e7\u00e3o:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Murm\u00farios Vesiculares:", None))
        self.expectoracao.setTitle("")
        self.radio_expectoracao_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_expectoracao_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tipo de Ru\u00eddos Advent\u00edcios (se presentes):", None))
        self.tosse.setTitle("")
        self.radio_presente_2.setText(QCoreApplication.translate("MainWindow", u"Presente\u2003", None))
        self.radio_ausente.setText(QCoreApplication.translate("MainWindow", u"Ausente", None))
        self.murmurios_vesiculares.setTitle("")
        self.radio_Fisiologicos.setText(QCoreApplication.translate("MainWindow", u"Fisiol\u00f3gicos", None))
        self.radio_sem_ruidos.setText(QCoreApplication.translate("MainWindow", u"Sem ru\u00eddos advent\u00edcios", None))
        self.radio_com_ruidos.setText(QCoreApplication.translate("MainWindow", u"Com ru\u00eddos advent\u00edcios", None))
        self.tipos_de_ruidos.setTitle("")
        self.radio_estertores_subcrepitantes.setText(QCoreApplication.translate("MainWindow", u"Estertores subcrepitantes", None))
        self.radio_sibilos.setText(QCoreApplication.translate("MainWindow", u"Sibilos", None))
        self.radio_roncos.setText(QCoreApplication.translate("MainWindow", u"Roncos", None))
        self.radio_atrito_pleural.setText(QCoreApplication.translate("MainWindow", u"Atrito pleural", None))
        self.radio_estertores_crepitantes.setText(QCoreApplication.translate("MainWindow", u"Estertores crepitantes", None))
        self.radio_nao_presente.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o presente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tosse:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Pulm\u00f5es", None))
        self.groupLesoes_27.setTitle(QCoreApplication.translate("MainWindow", u"ABD\u00d4MEN", None))
        self.sensibilidade_palpacao.setTitle("")
        self.radio_flacido.setText(QCoreApplication.translate("MainWindow", u"Fl\u00e1cido \u00e0 Palpa\u00e7\u00e3o", None))
        self.radio_indolor.setText(QCoreApplication.translate("MainWindow", u"Indolor", None))
        self.radio_dor.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Dor", None))
        self.radio_resistente.setText(QCoreApplication.translate("MainWindow", u"Resistente \u00e0 Palpa\u00e7\u00e3o", None))
        self.ausculta_abdominal.setTitle("")
        self.radio_presenca.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Ruidos Hidroa\u00e9reos", None))
        self.radio_ausencia.setText(QCoreApplication.translate("MainWindow", u"Aus\u00eancia de Ruidos Hidroa\u00e9reos", None))
        self.simetria.setTitle("")
        self.radio_simetrico.setText(QCoreApplication.translate("MainWindow", u"Sim\u00e9trico", None))
        self.radio_assimetrico.setText(QCoreApplication.translate("MainWindow", u"Assim\u00e9trico", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Ascultura Abdominal:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Marcas de Estiramento:", None))
        self.marcas_de_estiramento.setTitle("")
        self.radio_sim.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.radio_nao.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Sensibilidade a Palpa\u00e7\u00e3o:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Integridade:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Formato:", None))
        self.formato_abdomen.setTitle("")
        self.radio_escavado.setText(QCoreApplication.translate("MainWindow", u"Escavado", None))
        self.radio_pendular.setText(QCoreApplication.translate("MainWindow", u"Pendular", None))
        self.radio_plano.setText(QCoreApplication.translate("MainWindow", u"Plano", None))
        self.radio_globoso.setText(QCoreApplication.translate("MainWindow", u"Globoso", None))
        self.integridade_abdomen.setTitle("")
        self.radioButton_118.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radio_alterada_2.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Simetria:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Abd\u00f4men", None))
        self.groupLesoes_29.setTitle(QCoreApplication.translate("MainWindow", u"INSPE\u00c7\u00c3O ANAL", None))
        self.informacoes_adicionais.setText(QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es Adicionais:", None))
        self.integridade_anal.setTitle("")
        self.opcao_preservada_e.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.opcao_alterada_e.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.especificacoes.setText(QCoreApplication.translate("MainWindow", u"Especifica\u00e7\u00e3o:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"Inspe\u00e7\u00e3o Anal", None))
        self.groupLesoes_28.setTitle(QCoreApplication.translate("MainWindow", u"GENITU\u00c1RIOS", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Aspecto:", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Secre\u00e7\u00f5es:", None))
        self.edemas.setTitle("")
        self.radioButton_135.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_136.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Condi\u00e7\u00e3o:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Integridade:", None))
        self.condicao.setTitle("")
        self.radioButton_137.setText(QCoreApplication.translate("MainWindow", u"Irriga\u00e7\u00e3o Vesical", None))
        self.radioButton_138.setText(QCoreApplication.translate("MainWindow", u"Mic\u00e7\u00e3o Espont\u00e2nea", None))
        self.radioButton_139.setText(QCoreApplication.translate("MainWindow", u"Sonda Vesical de Demora", None))
        self.radioButton_140.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a de Anomalias", None))
        self.radioButton_141.setText(QCoreApplication.translate("MainWindow", u"Incontin\u00eancia Urin\u00e1ria", None))
        self.lesoes_geniturinario.setTitle("")
        self.radioButton_142.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.radioButton_143.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Outras:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Les\u00f5es:", None))
        self.integridade_geniturinario.setTitle("")
        self.radioButton_144.setText(QCoreApplication.translate("MainWindow", u"Preservada", None))
        self.radioButton_145.setText(QCoreApplication.translate("MainWindow", u"Alterada", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Edemas:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Genitu\u00e1rios", None))
        self.btn_imprimir_pdf.setText(QCoreApplication.translate("MainWindow", u"IMPRIMIR PDF", None))
        self.groupBox_2.setTitle("")
        self.labelTitulo_4.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE PRONTU\u00c1RIO ELETR\u00d4NICO", None))
        self.groupTecidos_8.setTitle("")
        self.labelTitulo_7.setText(QCoreApplication.translate("MainWindow", u"CONSULTA DE PACIENTES", None))
        self.groupTecidos_4.setTitle(QCoreApplication.translate("MainWindow", u"CONSULTA DE PACIENTE", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.campo_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO PACIENTE", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Prontu\u00e1rio:", None))
        self.campo_prontuario.setText("")
        self.campo_prontuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00b0", None))
        ___qtablewidgetitem7 = self.tabela_paciente.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 PRONTUARIO", None));
        ___qtablewidgetitem8 = self.tabela_paciente.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem9 = self.tabela_paciente.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DATA DE NASCIMENTO", None));
        ___qtablewidgetitem10 = self.tabela_paciente.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"IDADE", None));
        ___qtablewidgetitem11 = self.tabela_paciente.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"SEXO", None));
        ___qtablewidgetitem12 = self.tabela_paciente.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ESTADO CIVIL", None));
        ___qtablewidgetitem13 = self.tabela_paciente.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PROFISS\u00c3O", None));
        ___qtablewidgetitem14 = self.tabela_paciente.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem15 = self.tabela_paciente.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem16 = self.tabela_paciente.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"DATA DA CONSULTA", None));
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.btn_limpar_campos.setText(QCoreApplication.translate("MainWindow", u"LIMPAR", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_excluir_tec.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR", None))
        self.btn_limpar_campos_tec.setText(QCoreApplication.translate("MainWindow", u"LIMPAR", None))
        self.btn_pesquisar_tec.setText(QCoreApplication.translate("MainWindow", u"PESQUISAR", None))
        self.groupTecidos_5.setTitle(QCoreApplication.translate("MainWindow", u"CONSULTA DE T\u00c9CNICOS", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.campo_nome_tec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO T\u00c9CNICO", None))
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"RA DO T\u00c9CNICO", None))
        self.campo_ra_tec.setText("")
        self.campo_ra_tec.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RA", None))
        ___qtablewidgetitem17 = self.tabela_tecnicos.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem18 = self.tabela_tecnicos.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem19 = self.tabela_tecnicos.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"RA", None));
        ___qtablewidgetitem20 = self.tabela_tecnicos.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        self.groupTecidos_7.setTitle("")
        self.labelTitulo_5.setText(QCoreApplication.translate("MainWindow", u"CONSULTA DE T\u00c9CNICOS", None))
        self.label_usuario_conta.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"STATUS:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"RA:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"ATIVO", None))
        self.label_ra_conta.setText(QCoreApplication.translate("MainWindow", u"registro", None))
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.labelBoxBlenderInstalation.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"T\u00c9CNICOS CADASTRADOS", None))
        ___qtablewidgetitem21 = self.tabela_tec_conta.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.tabela_tec_conta.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"USU\u00c1RIO", None));
        ___qtablewidgetitem23 = self.tabela_tec_conta.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"RA", None));
        ___qtablewidgetitem24 = self.tabela_tec_conta.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem25 = self.tabela_tec_conta.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

