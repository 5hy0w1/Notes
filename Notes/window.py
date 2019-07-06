# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Notes - Заметки")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        #self.textEdit.setLineWrapMode(QtGui.WidgetWrap)
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setAcceptRichText(True)
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sidebar = QtWidgets.QDockWidget(MainWindow)
        self.sidebar.setFloating(False)
        self.sidebar.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable)
        self.sidebar.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.sidebar.setObjectName("sidebar")
        self.sidebar_content = QtWidgets.QWidget()
        self.sidebar_content.setObjectName("sidebar_content")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar_content)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.notes_list = QtWidgets.QListWidget(self.sidebar_content)
        self.notes_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notes_list.setObjectName("notes_list")
        self.verticalLayout_2.addWidget(self.notes_list)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setContentsMargins(10, -1, -1, -1)
        self.buttons_layout.setSpacing(12)
        self.buttons_layout.setObjectName("buttons_layout")
        self.new_button = QtWidgets.QToolButton(self.sidebar_content)
        self.new_button.setMaximumSize(QtCore.QSize(25, 25))
        self.new_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_button.setText("")
        # #icon = QtGui.QIcon()
        # #icon.addPixmap(QtGui.QPixmap("/home/5hy0w1/notes/plus.png").scaled(20,20), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # #self.new_button.setIcon(icon)
        self.new_button.setIconSize(QtCore.QSize(20, 20))
        self.new_button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.new_button.setAutoRaise(True)
        self.new_button.setObjectName("new_button")
        self.buttons_layout.addWidget(self.new_button)
        self.del_button = QtWidgets.QToolButton(self.sidebar_content)
        self.del_button.setMaximumSize(QtCore.QSize(25, 25))
        self.del_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_button.setText("")
        # #icon1 = QtGui.QIcon()
        # #icon1.addPixmap(QtGui.QPixmap("/home/5hy0w1/notes/minus.png").scaled(20,20), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # #self.del_button.setIcon(icon1)
        self.del_button.setIconSize(QtCore.QSize(20, 20))
        self.del_button.setAutoRaise(True)
        self.del_button.setObjectName("del_button")
        self.buttons_layout.addWidget(self.del_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.buttons_layout)
        self.sidebar.setWidget(self.sidebar_content)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.sidebar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        # # Paragraph settings
        self.alignLeftButton = QtWidgets.QToolButton()
        # #self.alignLeftButton.setIcon(QtGui.QIcon("./left-alignment.png"))
        self.alignRightButton = QtWidgets.QToolButton()
        # #self.alignRightButton.setIcon(QtGui.QIcon("./right-alignment.png"))
        self.alignCenterButton = QtWidgets.QToolButton()
        # #self.alignCenterButton.setIcon(QtGui.QIcon("./center-alignment.png"))
        self.alignLeftButton.setCheckable(True)
        self.alignRightButton.setCheckable(True)
        self.alignCenterButton.setCheckable(True)
        # # Font settings
        self.fontSelector = QtWidgets.QFontComboBox()
        self.boldButton = QtWidgets.QToolButton()
        self.boldButton.setCheckable(True)
        self.boldButton.setText("B")
        self.boldButton.setStyleSheet("font-weight: 700;font-size: 20px;")
        self.boldButton.setMinimumSize(QtCore.QSize(35, 35))
        self.italicButton = QtWidgets.QToolButton()
        self.italicButton.setText("I")
        self.italicButton.setCheckable(True)
        self.italicButton.setMinimumSize(QtCore.QSize(35, 35))
        self.italicButton.setStyleSheet("font-size: 20px; font-style: italic;")
        self.underButton = QtWidgets.QToolButton()
        self.underButton.setText("U")
        self.underButton.setCheckable(True)
        self.underButton.setStyleSheet("font-size: 20px; text-decoration: underline;")
        self.fontsizeSpinBox = QtWidgets.QSpinBox()
        self.fontsizeSpinBox.setValue(12)
        # # List settings
        self.numList = QtWidgets.QToolButton()
        self.numList.setText("1.\n2.")
        self.numList.setMinimumSize(QtCore.QSize(35, 35))
        self.numList.setStyleSheet("font-size:7px;line-height:1;")
        self.markedList = QtWidgets.QToolButton()
        self.markedList.setText("•\n•")
        self.markedList.setStyleSheet("font-size:10px;line-height:0.8;")
        self.markedList.setMinimumSize(QtCore.QSize(35, 35))

        self.toolBar.addWidget(self.alignLeftButton)
        self.toolBar.addWidget(self.alignCenterButton)
        self.toolBar.addWidget(self.alignRightButton)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.boldButton)
        self.toolBar.addWidget(self.italicButton)
        self.toolBar.addWidget(self.underButton)
        self.toolBar.addWidget(self.fontSelector)
        self.toolBar.addWidget(self.fontsizeSpinBox)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.numList)
        self.toolBar.addWidget(self.markedList)

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Notes - Заметки"))
        __sortingEnabled = self.notes_list.isSortingEnabled()
        self.notes_list.setSortingEnabled(False)
        #item = self.notes_list.item(0)
        #item.setText(_translate("MainWindow", "Новый элемент"))
        self.notes_list.setSortingEnabled(__sortingEnabled)
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

# #import res_rc