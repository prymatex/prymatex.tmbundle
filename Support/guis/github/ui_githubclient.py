# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'githubclient.ui'
#
# Created: Tue Dec 11 14:59:00 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from prymatex.qt import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GitHubClientDialog(object):
    def setupUi(self, GitHubClientDialog):
        GitHubClientDialog.setObjectName(_fromUtf8("GitHubClientDialog"))
        GitHubClientDialog.resize(500, 462)
        GitHubClientDialog.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalLayout = QtGui.QVBoxLayout(GitHubClientDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(GitHubClientDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelSearch = QtGui.QLabel(GitHubClientDialog)
        self.labelSearch.setObjectName(_fromUtf8("labelSearch"))
        self.horizontalLayout_2.addWidget(self.labelSearch)
        self.lineEditQuery = QtGui.QLineEdit(GitHubClientDialog)
        self.lineEditQuery.setObjectName(_fromUtf8("lineEditQuery"))
        self.horizontalLayout_2.addWidget(self.lineEditQuery)
        self.buttonSearch = QtGui.QPushButton(GitHubClientDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonSearch.setFont(font)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-find"))
        self.buttonSearch.setIcon(icon)
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.horizontalLayout_2.addWidget(self.buttonSearch)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableViewResults = QtGui.QTableView(GitHubClientDialog)
        self.tableViewResults.setAlternatingRowColors(True)
        self.tableViewResults.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableViewResults.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableViewResults.setSortingEnabled(True)
        self.tableViewResults.setObjectName(_fromUtf8("tableViewResults"))
        self.verticalLayout.addWidget(self.tableViewResults)
        self.line_2 = QtGui.QFrame(GitHubClientDialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.widgetInfo = QtGui.QWidget(GitHubClientDialog)
        self.widgetInfo.setObjectName(_fromUtf8("widgetInfo"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widgetInfo)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.widgetInfo)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.comboBoxNamespace = QtGui.QComboBox(self.widgetInfo)
        self.comboBoxNamespace.setObjectName(_fromUtf8("comboBoxNamespace"))
        self.gridLayout_2.addWidget(self.comboBoxNamespace, 8, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.widgetInfo)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widgetInfo)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widgetInfo)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.widgetInfo)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.labelForks = QtGui.QLabel(self.widgetInfo)
        self.labelForks.setText(_fromUtf8(""))
        self.labelForks.setObjectName(_fromUtf8("labelForks"))
        self.gridLayout_2.addWidget(self.labelForks, 5, 5, 1, 1)
        self.label_10 = QtGui.QLabel(self.widgetInfo)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_2.addWidget(self.label_10, 8, 3, 1, 1)
        self.labelFollowers = QtGui.QLabel(self.widgetInfo)
        self.labelFollowers.setText(_fromUtf8(""))
        self.labelFollowers.setObjectName(_fromUtf8("labelFollowers"))
        self.gridLayout_2.addWidget(self.labelFollowers, 5, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.widgetInfo)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 2, 1, 1)
        self.labelCreated = QtGui.QLabel(self.widgetInfo)
        self.labelCreated.setText(_fromUtf8(""))
        self.labelCreated.setObjectName(_fromUtf8("labelCreated"))
        self.gridLayout_2.addWidget(self.labelCreated, 4, 1, 1, 2)
        self.labelUrl = QtGui.QLabel(self.widgetInfo)
        self.labelUrl.setText(_fromUtf8(""))
        self.labelUrl.setObjectName(_fromUtf8("labelUrl"))
        self.gridLayout_2.addWidget(self.labelUrl, 6, 1, 1, 5)
        self.labelHomepage = QtGui.QLabel(self.widgetInfo)
        self.labelHomepage.setText(_fromUtf8(""))
        self.labelHomepage.setObjectName(_fromUtf8("labelHomepage"))
        self.gridLayout_2.addWidget(self.labelHomepage, 3, 1, 1, 5)
        self.line = QtGui.QFrame(self.widgetInfo)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 7, 0, 1, 6)
        self.label_9 = QtGui.QLabel(self.widgetInfo)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.labelDescription = QtGui.QLabel(self.widgetInfo)
        self.labelDescription.setText(_fromUtf8(""))
        self.labelDescription.setObjectName(_fromUtf8("labelDescription"))
        self.gridLayout_2.addWidget(self.labelDescription, 1, 0, 1, 6)
        self.labelWatchers = QtGui.QLabel(self.widgetInfo)
        self.labelWatchers.setText(_fromUtf8(""))
        self.labelWatchers.setObjectName(_fromUtf8("labelWatchers"))
        self.gridLayout_2.addWidget(self.labelWatchers, 5, 1, 1, 1)
        self.labelPushed = QtGui.QLabel(self.widgetInfo)
        self.labelPushed.setText(_fromUtf8(""))
        self.labelPushed.setObjectName(_fromUtf8("labelPushed"))
        self.gridLayout_2.addWidget(self.labelPushed, 4, 4, 1, 2)
        self.label_8 = QtGui.QLabel(self.widgetInfo)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 5, 4, 1, 1)
        self.lineEditFolder = QtGui.QLineEdit(self.widgetInfo)
        self.lineEditFolder.setObjectName(_fromUtf8("lineEditFolder"))
        self.gridLayout_2.addWidget(self.lineEditFolder, 8, 4, 1, 2)
        self.label_11 = QtGui.QLabel(self.widgetInfo)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_2.addWidget(self.label_11, 9, 0, 1, 1)
        self.labelDestiny = QtGui.QLabel(self.widgetInfo)
        self.labelDestiny.setText(_fromUtf8(""))
        self.labelDestiny.setObjectName(_fromUtf8("labelDestiny"))
        self.gridLayout_2.addWidget(self.labelDestiny, 9, 1, 1, 5)
        self.line_3 = QtGui.QFrame(self.widgetInfo)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 2, 0, 1, 6)
        self.verticalLayout.addWidget(self.widgetInfo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonOk = QtGui.QPushButton(GitHubClientDialog)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-ok"))
        self.buttonOk.setIcon(icon)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.horizontalLayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(GitHubClientDialog)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("dialog-cancel"))
        self.buttonCancel.setIcon(icon)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GitHubClientDialog)
        QtCore.QMetaObject.connectSlotsByName(GitHubClientDialog)

    def retranslateUi(self, GitHubClientDialog):
        GitHubClientDialog.setWindowTitle(QtGui.QApplication.translate("GitHubClientDialog", "GitHub Client", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GitHubClientDialog", "<html><head/><body><p>This tool allows you to get TextMate bundles from <br/>GitHub and install them in your current profile.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSearch.setText(QtGui.QApplication.translate("GitHubClientDialog", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearch.setText(QtGui.QApplication.translate("GitHubClientDialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("GitHubClientDialog", "Homepage:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GitHubClientDialog", "Url:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("GitHubClientDialog", "Watchers:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("GitHubClientDialog", "Pushed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("GitHubClientDialog", "Created:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("GitHubClientDialog", "Folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("GitHubClientDialog", "Followers:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("GitHubClientDialog", "Namespace:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("GitHubClientDialog", "Forks:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("GitHubClientDialog", "Destiny:", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("GitHubClientDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("GitHubClientDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

