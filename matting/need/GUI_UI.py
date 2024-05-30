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
                                                      "首次使用时会下载176MB的权重文件到我的文档，请耐心等待。n"
                                                      "记得清空输出目录，不然容易因为不知名原因闪退（完全无法debug）",
                                                      None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "需要抠的图片路径列表",
                                       None))
        self.refresh_id_pushButton.setText(QCoreApplication.translate("MainWindow", "刷新序号", None))
        self.delete_path_pushButton.setText(
            QCoreApplication.translate("MainWindow", "删除选中路径", None))
        ___qtreewidgetitem = self.tree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", "路径", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", "序号", None));
        self.input_path_label.setText(QCoreApplication.translate("MainWindow", "输入目录：", None))
        self.open_file_pushButton.setText(
            QCoreApplication.translate("MainWindow", "打开图片(Alt+I)", None))
        # if QT_CONFIG(shortcut)
        self.open_file_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+I", None))
        # endif // QT_CONFIG(shortcut)
        self.open_input_pushButton.setText(QCoreApplication.translate("MainWindow", "打开...(Alt+O)", None))
        # if QT_CONFIG(shortcut)
        self.open_input_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+O", None))
        # endif // QT_CONFIG(shortcut)
        self.add_input_pushButton.setText(
            QCoreApplication.translate("MainWindow", "添加进列表（Alt+A)", None))
        # if QT_CONFIG(shortcut)
        self.add_input_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+A", None))
        # endif // QT_CONFIG(shortcut)
        self.checkBox.setText(QCoreApplication.translate("MainWindow",
                                                         '自定义输出目录（不自定义的话，默认在这个程序的根目录下生成"/扣好的图"文件夹)',
                                                         None))
        self.output_path_label.setText(
            QCoreApplication.translate("MainWindow", "输出目录：", None))
        self.open_output_pushButton.setText(QCoreApplication.translate("MainWindow", "打开...(Alt+S)", None))
        # if QT_CONFIG(shortcut)
        self.open_output_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+S", None))
        # endif // QT_CONFIG(shortcut)
        self.output_label.setText(QCoreApplication.translate("MainWindow", "输出框", None))
        self.run_pushButton.setText(QCoreApplication.translate("MainWindow", "运行(Alt+R)", None))
        # if QT_CONFIG(shortcut)
        self.run_pushButton.setShortcut(QCoreApplication.translate("MainWindow", "Alt+R", None))
# endif // QT_CONFIG(shortcut)
# retranslateUi
