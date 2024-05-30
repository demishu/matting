# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:17:38 2023

@author: demishu
"""
from PySide6.QtWidgets import QApplication, QFrame, QFileDialog, QTreeWidgetItem, QMainWindow
from PySide6.QtGui import QPixmap, QColor, QIcon, QImage, QTextCursor
from PySide6.QtCore import QByteArray, Qt, QThread
from need.GUI_UI import Ui_MainWindow
from need.matting import matting, FileManager, new_session
from need.icon import b64_icon
import os
import sys


def get_icon(img_data=None, color=None, fmt='png'):
    """
    通过base64编码的图片字符串获取QIcon对象
    :param img_data: Base64编码的图片字符串
    :param color: 图片需要填充的颜色
    :param fmt: 图片的格式
    :return:
    """
    if not img_data:
        pix = QPixmap(32, 32)
    else:
        data = QByteArray().fromBase64(img_data.encode())
        image = QImage()
        image.loadFromData(data, fmt)
        pix = QPixmap.fromImage(image)
    if color:
        pix.fill(QColor(color))

    return QIcon(pix)


class MyThread(QThread):
    def __init__(self, manager: FileManager):
        super().__init__()
        self._manager = manager

    def run(self):
        print(self._manager)
        print('开始抠图')
        output_path = self._manager.output_path
        print('获取输出路径')
        session = new_session()
        n_imgs = len(self._manager.not_matted_imgs)             # 进度条
        i = 1                                                   # 进度条
        while self._manager.has_img():                          # 还有没扣的图吗？ 有的话就执行一下代码
            '打印进度条'
            print('进度条')
            print(f'{i}/{n_imgs}')
            pic = self._manager.get_img()                       # 获取img的路径
            output_file = output_path + os.path.basename(pic)   # 获取输出路径
            print(f'正在抠：{pic}, \n扣好的图在这里：{output_file}')
            matting(pic, output_file, session=session)                           # 开始抠图
            i += 1
        print('完成抠图！')


class MyWindow(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        'setup ui'
        self.root = QMainWindow()
        self.form = Ui_MainWindow()
        self.form.setupUi(self.root)

        'setup icon'
        icon = get_icon(b64_icon)
        self.root.setWindowIcon(icon)

        'setup title'
        self.root.setWindowTitle('批量抠图小程序')

        'redirect stdout to self.form.myConsole'
        sys.stdout = self
        sys.stderr = self

        'set connections'
        self.__connect_functions()

        'show GUI'
        self.root.show()

    def __connect_functions(self):
        self.form.run_pushButton.clicked.connect(self.__run)
        self.form.open_file_pushButton.clicked.connect(self.__open_input_file)
        self.form.open_input_pushButton.clicked.connect(self.__open_input_folder)
        self.form.add_input_pushButton.clicked.connect(self.__add_path_to_tree)
        self.form.delete_path_pushButton.clicked.connect(self.__delete_paths)
        self.form.refresh_id_pushButton.clicked.connect(self.__refresh_id)
        self.form.open_output_pushButton.clicked.connect(self.__open_output_folder)

    def __delete_paths(self):
        selected_items = self.form.tree.selectedItems()
        for item in selected_items:
            item.removeChild(item)
            print('删除成功')

    def __refresh_id(self):
        '刷新序号'
        n_row = self.form.tree.topLevelItemCount()
        for row in range(n_row):
            item = self.form.tree.topLevelItem(row)
            print(item.text(0))
            item.setText(0, str(row+1))
            print(item)

    def __open_input_file(self):
        print('打开单个文件')
        path, file_type = QFileDialog.getOpenFileName(self,
                                                      '选取文件',
                                                      os.getcwd(),
                                                      "Jpg 文件 (*.jpg);;Jpeg 文件(*.jpeg);;Png 文件(*.png)")
        if path != '':
            print(f'你选了这个文件：{path}')
            self.form.input_path_lineEdit.setText(path)
        else:
            print("你没选取任何文件。")

    def __open_input_folder(self):
        path = QFileDialog.getExistingDirectory(self,
                                                "选取文件夹",
                                                os.getcwd())
        if path != '':
            print(f'你选了这个文件夹：{path}')
            self.form.input_path_lineEdit.setText(path)
        else:
            print("你没选取任何文件夹。")

    def __add_path_to_tree(self):
        path = self.form.input_path_lineEdit.text()
        if (os.path.isfile(path) or os.path.isdir(path)) and os.path.exists(path):
            print('文件格式正确')
            item = self.form.tree.findItems(path, Qt.MatchFlag.MatchExactly, 1)
            if not item:
                child_item = QTreeWidgetItem(self.form.tree,
                                                [
                                                 str(self.form.tree.topLevelItemCount()+1),
                                                 path
                                                ]
                                             )
            else:
                print(f'该路径已经存在{item.count}')

        else:
            print('文件格式错误，返回')
            return

    def __open_output_folder(self):
        path = QFileDialog.getExistingDirectory(self,
                                                "选取文件夹",
                                                os.getcwd())
        if path != '':
            if not path.endswith('/'):
                path += '/'
            print(f'你选了这个文件夹：{path}')
            self.form.output_path_lineEdit.setText(path)
        else:
            print("你没选取任何文件夹。")

    def write(self, text):
        cursor = self.form.myConsole.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(text)
        self.form.myConsole.setTextCursor(cursor)
        self.form.myConsole.ensureCursorVisible()

    def __del__(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def __run(self):
        """抠图函数"""
        '获取输出路径，用于给FileManager传参'
        output_path = None
        if self.form.output_path_lineEdit.isEnabled():
            text = self.form.output_path_lineEdit.text()
            if os.path.isdir(text):
                print('有输出路径')
                output_path = text
                print(output_path)

        manager = FileManager(output_path)                  # 初始化一个FileManager对象
        n_row = self.form.tree.topLevelItemCount()
        for row in range(n_row):
            item = self.form.tree.topLevelItem(row)
            path = item.text(1)                             # 获取tree下的所有路径
            if os.path.isdir(path):
                manager.put_imgs(path)
            if os.path.isfile(path):
                manager.put_img(path)

        self.thread = MyThread(manager)
        self.thread.start()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        gui = MyWindow()
        sys.exit(app.exec())
    except Exception as e:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        print(e)
