
# 图像就是结构化存储的数据信息
# 图像属性：通道数目、高与宽、像素数据、位图深度（每个像素点由多少位表示）、图像类型

import cv2 as cv


# 定义一个函数，读取图像的各属性的信息
def get_image_info(image):
    # 首先打印一下图像的类型
    print(type(image))
    # 打印出图像的高宽以及通道数
    print(image.shape)
    # 打印出图像的大小
    print(image.size)
    # 打印出图像的字节位数占多少
    print(image.dtype)


print("------------- Hello Guyan ------------")

# 读出图像，赋值给变量
src = cv.imread('images/handsomeboy01.jpg')
# 创建窗口
cv.namedWindow("Guyan01 image",cv.WINDOW_AUTOSIZE)
# 将读出的图像进行显示到当前窗口
cv.imshow("Guyan01 image",src)

# 调用定义的函数
get_image_info(src)
cv.waitKey(0)

cv.destroyAllWindows()
