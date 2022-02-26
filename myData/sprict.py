import os
import cv2

path = "/home/the_heart_fickle/darknet/myData/JPEGImages"


def xml_message(img_name, height, width):
    filename = img_name
    pathname = path + '/' + img_name
    # if img_name.find("cat") != -1:
    #     object_name = "cat"
    # elif img_name.find("dog") != -1:
    #     object_name = "dog"
    # else:
    #     object_name = "girl"
    object_name = "ganyu"
    xmin = 1
    xmax = width-1
    ymin = 1
    ymax = height-1
    message_contant = """<annotation>
        <folder>JPEGImages</folder>
        <filename>{filename}</filename>
        <path>{pathname}</path>
        <source>
                <database>Unknown</database>
        </source>
        <size>
                <width>{width}</width>
                <height>{height}</height>
                <depth>3</depth>
        </size>
        <segmented>0</segmented>
        <object>
                <name>{object_name}</name>
                <pose>Unspecified</pose>
                <truncated>1</truncated>
                <difficult>0</difficult>
                <bndbox>
                        <xmin>{xmin}</xmin>
                        <ymin>{ymin}</ymin>
                        <xmax>{xmax}</xmax>
                        <ymax>{ymax}</ymax>
                </bndbox>
        </object>
</annotation>""".format(filename=filename, pathname=pathname, width=width, height=height,
               object_name=object_name, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)
    # print(message_contant)
    return message_contant


def xml_create(name, msg):
    desktop_path = "/home/the_heart_fickle/darknet/myData/Annotations/"  # 新创建的xml文件的存放路径
    full_path = desktop_path + name + '.xml'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()


def read_path(pathname):  # 读取文件夹下的图片
    # global img_name
    path_list = os.listdir(pathname)
    i = 0
    for filename in path_list:
        img_name =filename[0:-4]  # 变量名
        i += 1
        print('变量名:', img_name, '文件名:', filename, '|rank=', i)
        img_name = cv2.imread(pathname+'/'+filename, 0)  # 写入图像
        # print('img.shape =', img_name.shape)
        height, width = img_name.shape
        # cv2.imshow(filename, img_name)
        # cv2.waitKey(1)
        # cv2.destroyWindow(filename)
        xml_create(filename[0:-4], xml_message(filename, height, width))


if __name__ == '__main__':
    read_path(path)
