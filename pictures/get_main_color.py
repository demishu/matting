import cv2
import numpy as np
from sklearn.cluster import KMeans


def reduce_noise(image):
    # 使用高斯滤波器将噪点减少
    return cv2.GaussianBlur(image, (5, 5), 0)


def get_dominant_color(image):
    # 将图像数据转换为一维
    data = np.reshape(image, (-1, 3))
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(data)

    # 返回主要颜色
    return kmeans.cluster_centers_[0].astype(int)


def create_color_image(color, size=(100, 100)):
    # 创建一个指定大小和颜色的图像
    image = np.zeros((size[0], size[1], 3), dtype=np.uint8)
    image[:] = color
    return image


def main():
    from pathlib import Path
    pics = Path('raw').glob('*.png')
    for pic in pics:
        pic = pic.absolute()
        output_path = f'{pic.parent.parent.absolute()}\\done\\{pic.name}'
        print(output_path)
        image = cv2.imread(pic)

        # 降噪
        image = reduce_noise(image)

        # 获取主要颜色
        dominant_color = get_dominant_color(image)
        # 创建一个新的100x100像素的图像，并将主要颜色填充到这个图像中
        color_image = create_color_image(dominant_color)

        # 保存为PNG格式的文件
        cv2.imwrite(output_path, color_image)

        print(f"The dominant color is: {dominant_color}, and the image has been saved as {output_path}")
        print(f"The dominant color is: {dominant_color}")


if __name__ == "__main__":
    main()
