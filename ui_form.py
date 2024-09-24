# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 491)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 761, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.timeStampButton = QPushButton(self.verticalLayoutWidget)
        self.timeStampButton.setObjectName(u"timeStampButton")
        self.timeStampButton.setEnabled(False)

        self.verticalLayout_2.addWidget(self.timeStampButton)

        self.commentButton = QPushButton(self.verticalLayoutWidget)
        self.commentButton.setObjectName(u"commentButton")
        self.commentButton.setEnabled(False)

        self.verticalLayout_2.addWidget(self.commentButton)

        self.endExportButton = QPushButton(self.verticalLayoutWidget)
        self.endExportButton.setObjectName(u"endExportButton")
        self.endExportButton.setEnabled(False)

        self.verticalLayout_2.addWidget(self.endExportButton)

        self.startNewButton = QPushButton(self.verticalLayoutWidget)
        self.startNewButton.setObjectName(u"startNewButton")

        self.verticalLayout_2.addWidget(self.startNewButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.nameText = QTextEdit(self.verticalLayoutWidget)
        self.nameText.setObjectName(u"nameText")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameText.sizePolicy().hasHeightForWidth())
        self.nameText.setSizePolicy(sizePolicy)
        self.nameText.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.nameText)

        self.idText = QTextEdit(self.verticalLayoutWidget)
        self.idText.setObjectName(u"idText")
        sizePolicy.setHeightForWidth(self.idText.sizePolicy().hasHeightForWidth())
        self.idText.setSizePolicy(sizePolicy)
        self.idText.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_4.addWidget(self.idText)

        self.DOBEdit = QDateEdit(self.verticalLayoutWidget)
        self.DOBEdit.setObjectName(u"DOBEdit")

        self.verticalLayout_4.addWidget(self.DOBEdit)

        self.sexBox = QComboBox(self.verticalLayoutWidget)
        self.sexBox.addItem("")
        self.sexBox.addItem("")
        self.sexBox.setObjectName(u"sexBox")

        self.verticalLayout_4.addWidget(self.sexBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.commentText = QTextEdit(self.verticalLayoutWidget)
        self.commentText.setObjectName(u"commentText")

        self.verticalLayout.addWidget(self.commentText)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.timeStampButton.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None))
        self.commentButton.setText(QCoreApplication.translate("MainWindow", u"Add Comment", None))
        self.endExportButton.setText(QCoreApplication.translate("MainWindow", u"End And Export CSV", None))
        self.startNewButton.setText(QCoreApplication.translate("MainWindow", u"Start New Experiment", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"NAME:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DOB:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SEX:", None))
        self.nameText.setPlaceholderText("")
        self.sexBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.sexBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

    # retranslateUi

