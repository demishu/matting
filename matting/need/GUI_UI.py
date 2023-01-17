#compiled by 界面.ui

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QTextBrowser, QTreeWidget,
                               QTreeWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 547)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")

        self.verticalLayout_5.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.refresh_id_pushButton = QPushButton(self.centralwidget)
        self.refresh_id_pushButton.setObjectName("refresh_id_pushButton")
        self.refresh_id_pushButton.setAcceptDrops(True)

        self.horizontalLayout_3.addWidget(self.refresh_id_pushButton)

        self.delete_path_pushButton = QPushButton(self.centralwidget)
        self.delete_path_pushButton.setObjectName("delete_path_pushButton")

        self.horizontalLayout_3.addWidget(self.delete_path_pushButton)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tree = QTreeWidget(self.centralwidget)
        self.tree.setObjectName("tree")

        self.verticalLayout_3.addWidget(self.tree)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input_path_label = QLabel(self.centralwidget)
        self.input_path_label.setObjectName("input_path_label")

        self.horizontalLayout.addWidget(self.input_path_label)

        self.input_path_lineEdit = QLineEdit(self.centralwidget)
        self.input_path_lineEdit.setObjectName("input_path_lineEdit")
        self.input_path_lineEdit.setAcceptDrops(False)
        self.input_path_lineEdit.setDragEnabled(True)

        self.horizontalLayout.addWidget(self.input_path_lineEdit)

        self.open_file_pushButton = QPushButton(self.centralwidget)
        self.open_file_pushButton.setObjectName("open_file_pushButton")

        self.horizontalLayout.addWidget(self.open_file_pushButton)

        self.open_input_pushButton = QPushButton(self.centralwidget)
        self.open_input_pushButton.setObjectName("open_input_pushButton")

        self.horizontalLayout.addWidget(self.open_input_pushButton)

        self.add_input_pushButton = QPushButton(self.centralwidget)
        self.add_input_pushButton.setObjectName("add_input_pushButton")

        self.horizontalLayout.addWidget(self.add_input_pushButton)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.output_path_label = QLabel(self.centralwidget)
        self.output_path_label.setObjectName("output_path_label")
        self.output_path_label.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.output_path_label)

        self.output_path_lineEdit = QLineEdit(self.centralwidget)
        self.output_path_lineEdit.setObjectName("output_path_lineEdit")
        self.output_path_lineEdit.setEnabled(False)
        self.output_path_lineEdit.setAcceptDrops(False)
        self.output_path_lineEdit.setDragEnabled(True)

        self.horizontalLayout_2.addWidget(self.output_path_lineEdit)

        self.open_output_pushButton = QPushButton(self.centralwidget)
        self.open_output_pushButton.setObjectName("open_output_pushButton")
        self.open_output_pushButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.open_output_pushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName("output_label")

        self.verticalLayout.addWidget(self.output_label)

        self.myConsole = QTextBrowser(self.centralwidget)
        self.myConsole.setObjectName("myConsole")

        self.verticalLayout.addWidget(self.myConsole)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.run_pushButton = QPushButton(self.centralwidget)
        self.run_pushButton.setObjectName("run_pushButton")

        self.verticalLayout_4.addWidget(self.run_pushButton)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.checkBox.clicked["bool"].connect(self.output_path_label.setEnabled)
        self.checkBox.clicked["bool"].connect(self.output_path_lineEdit.setEnabled)
        self.checkBox.clicked["bool"].connect(self.open_output_pushButton.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)

    setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", "open...", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      "\u9996\u6b21\u4f7f\u7528\u65f6\u4f1a\u4e0b\u8f7d200-300MB\u7684\u6743\u91cd\u6587\u4ef6\u5230\u6211\u7684\u6587\u6863\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85\u3002\n"
                                                      "\u8bb0\u5f97\u6e05\u7a7a\u8f93\u51fa\u76ee\u5f55\uff0c\u4e0d\u7136\u5bb9\u6613\u56e0\u4e3a\u4e0d\u77e5\u540d\u539f\u56e0\u95ea\u9000\uff08\u5b8c\u5168\u65e0\u6cd5debug\uff09",
                                                      None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "\u9700\u8981\u62a0\u7684\u56fe\u7247\u8def\u5f84\u5217\u8868",
                                       None))
        self.refresh_id_pushButton.setText(QCoreApplication.translate("MainWindow", "\u5237\u65b0\u5e8f\u53f7", None))
        self.delete_path_pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u5220\u9664\u9009\u4e2d\u8def\u5f84", None))
        ___qtreewidgetitem = self.tree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", "\u8def\u5f84", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", "\u5e8f\u53f7", None));
        self.input_path_label.setText(QCoreApplication.translate("MainWindow", "\u8f93\u5165\u76ee\u5f55\uff1a", None))
        self.open_file_pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u5f00\u56fe\u7247(Alt+I)", None))
        # if QT_CONFIG(shortcut)
        self.open_file_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+I", None))
        # endif // QT_CONFIG(shortcut)
        self.open_input_pushButton.setText(QCoreApplication.translate("MainWindow", "\u6253\u5f00...(Alt+O)", None))
        # if QT_CONFIG(shortcut)
        self.open_input_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+O", None))
        # endif // QT_CONFIG(shortcut)
        self.add_input_pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u6dfb\u52a0\u8fdb\u5217\u8868\uff08Alt+A)", None))
        # if QT_CONFIG(shortcut)
        self.add_input_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+A", None))
        # endif // QT_CONFIG(shortcut)
        self.checkBox.setText(QCoreApplication.translate("MainWindow",
                                                         "\u81ea\u5b9a\u4e49\u8f93\u51fa\u76ee\u5f55\uff08\u4e0d\u81ea\u5b9a\u4e49\u7684\u8bdd\uff0c\u9ed8\u8ba4\u5728\u8fd9\u4e2a\u7a0b\u5e8f\u7684\u6839\u76ee\u5f55\u4e0b\u751f\u6210\"/matted\"\u6587\u4ef6\u5939)",
                                                         None))
        self.output_path_label.setText(
            QCoreApplication.translate("MainWindow", "\u8f93\u51fa\u76ee\u5f55\uff1a", None))
        self.open_output_pushButton.setText(QCoreApplication.translate("MainWindow", "\u6253\u5f00...(Alt+S)", None))
        # if QT_CONFIG(shortcut)
        self.open_output_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+S", None))
        # endif // QT_CONFIG(shortcut)
        self.output_label.setText(QCoreApplication.translate("MainWindow", "\u8f93\u51fa\u6846", None))
        self.run_pushButton.setText(QCoreApplication.translate("MainWindow", "\u8fd0\u884c(Alt+R)", None))
        # if QT_CONFIG(shortcut)
        self.run_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+R", None))
# endif // QT_CONFIG(shortcut)
# retranslateUi
