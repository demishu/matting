# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:17:38 2023

@author: demishu
"""
from typing import NewType
import pathlib
import os
from PIL import Image
from rembg import remove, new_session

path = NewType("path", str)
path_list = list[path]


def _img_transpose(img):
    exif_data = img.getexif()  # 获取 EXIF 信息
    if exif_data and exif_data.get(274):
        orientation = exif_data.get(274)
        if orientation == 3:
            print('图像旋转 180 度')
            img = img.rotate(180, expand=True)
        elif orientation == 6:
            print('图像旋转 270 度')
            img = img.rotate(270, expand=True)
        elif orientation == 8:
            print('图像旋转 90 度')
            img = img.rotate(90, expand=True)
        else:
            print('正常图片')
    return img


def matting(input_path: path, output_path: path, session=None) -> None:
    """
    对rembg的remove函数重新打包。 首次运行时会自动下载权重文件到我的文档里。

    matting(输入文件_路径，输出文件_路径）->None
    matting函数接收两个参数：
        1，需要抠图的文件在哪里？
        2，扣好的图保存在哪里？
    """

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_bytes = i.read()
            if session:
                output = remove(input_bytes, session=session)
            else:
                output = remove(input_bytes)
            o.write(output)


class FileManager:
    def __init__(self, output_path: path = None):
        """
        FileManager用于管理需要抠的图片和已经抠好的图片。

        用法1：
        FileManager(输出到哪个目录？）

        用法2:
        FileManager()
        p.s.:用法2会在os.getcwd()下创建一个matted文件夹，并把图片都输出到matted文件夹下

        通过put_img（需要抠图的图片在哪里）方法来添加单张图片。
        通过put_imgs(需要抠图的图片们放在哪个目录？)方法来添加目录下的所有图片。
        通过get_img方法来获取一张还没扣过的图片。
        通过has_img方法来确定还有没有没扣过的图片。
        """
        self._not_matted_imgs = set()  # 放未抠图的图片的集合
        self._matted_imgs = set()  # 放扣好图的图片的集合

        '如果没传参output_path的话，就创建/matted文件夹'
        if output_path is None:
            self._output_path = f'{os.getcwd()}/扣好的图/'.replace('\\', '/')
        else:
            self._output_path = output_path

        if not os.path.exists(self._output_path):
            os.makedirs(self._output_path)

    def __repr__(self):
        """用于print FileManger"""
        return f"""\nFileManger 发现了{len(self._not_matted_imgs) + len(self._matted_imgs)}张图片:
还没抠的:{self._not_matted_imgs}\n扣好了的:{self._matted_imgs}\n"""

    @property
    def output_path(self):
        return self._output_path

    @property
    def matted_imgs(self) -> set:
        return self._matted_imgs.copy()

    @property
    def not_matted_imgs(self) -> set:
        return self._not_matted_imgs.copy()

    def get_img(self) -> path:
        """从self._not_matted_imgs中取出一个img文件的path，把它塞入self._matted_imgs后，再返回img"""
        if self._not_matted_imgs:
            img_path = self._not_matted_imgs.pop()
            self._matted_imgs.add(img_path)
            return img_path

    @staticmethod
    def _rename(path: pathlib.Path) -> str:
        """改名,把“/款号/颜色.png”改名成“/款号/款号 颜色.png”, 再返回改好名的新path"""
        root = path.parent.as_posix()
        style_name = path.parent.stem.replace("款号", "").replace(" ", '').replace('加单', "")
        if style_name in path.stem:
            new_path = f'{root}/{path.name}'
        else:
            new_path = f'{root}/{style_name} {path.name}'
        return new_path

    def put_imgs(self, input_path: path):
        """自动遍历input_path下的所有目录，找出所有的.jpg,.jpeg,.png 图片，并把符合要求的图片加入未抠图的集合里"""
        input_path = pathlib.Path(input_path)
        pics = list(input_path.glob('**/*.jpg')) + \
               list(input_path.glob('**/*.jpeg')) + \
               list(input_path.glob('**/*.png'))
        for pic in pics:
            pic = self._rename(pic)
            self.put_img(pic)
        # walk_obj = os.walk(input_path)
        # for root, dirs, files in walk_obj:
        #     for file in files:
        #         if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        #             '我不喜欢“/款号/颜色.png”这种格式，只能多添加几行代码改名成“/款号/款号 颜色.png”了'
        #             img_path = self._rename(root, file)
        #             '改好名了，把img的path加入img_list'
        #             img_path = path(img_path)
        #             self.put_img(img_path)

    def put_img(self, img_path: path):
        """加入单张图片进未抠图的集合里"""
        self._not_matted_imgs.add(img_path)

    def has_img(self) -> bool:
        """是不是还有未抠图的图片存在？"""
        if len(self._not_matted_imgs):
            return True
        return False


if __name__ == '__main__':
    pics_path = path("D:/wdir/原图")
    manager = FileManager(output_path='D:/wdir/扣好的图/')
    manager.put_imgs(pics_path)

    # manager = FileManager(output_path='D:/wdir/扣好的图/')
    output_path = manager.output_path
    # manager.put_img(pic_path)
    session = new_session()
    is_png = False
    while manager.has_img():
        img_path = manager.get_img()
        if img_path.endswith('.png'):
            old_img_path = img_path
            img = Image.open(img_path)
            img_path = img_path.replace('png', 'jpg')
            is_png = True
        else:
            img = Image.open(img_path)
        output_file = output_path + os.path.basename(img_path)
        print(f'正在抠：{img_path}, \n扣好的图在这里：{output_file}')
        img = _img_transpose(img)
        img = img.convert("RGB")
        img.save(img_path)
        matting(img_path, output_file, session=session)
        if is_png:
            os.remove(old_img_path)
            old_img_path = ""
            is_png = False
    # print(manager)
