https://github.com/TheHeartFickle/The-graduation-of-Mitchell-in-lab.git

1:使用git clone从github上克隆项目后正在ubuntu下配置Makefile文档后即可make编译

2:YOLOv3需要原始图像，根据特定软件（labelimg）对目标进行标签化

3:将VOC数据集转换为YOLO训练集：使用python生成YOLO支持的格式

4：修改配置文件：在voc.data和my_yolov3.cfg中进行修改

​	voc.data中把路径修改为自己的训练集所处路径

​	my_yolov3.cfg中，

​	class=数据集中的种类个数

​	filters=3*（5+len（classes））

5：数据集所在文件夹下新建names文件并将自己的数据集中所有的种类名填入用于标志

6：wget https://pjreddie.com/media/files/darknet53.conv.74来下载预训练权重

7./darknet detector train cfg/my_data.data cfg/my_yolov3.cfg darknet53.conv.74（cpu）或

./darknet detector train cfg/my_data.data cfg/my_yolov3.cfg darknet53.conv.74 - gups 0,1,2,3（gpu）来训练，具体依照训练环境来配置makefile来编译

8：训练时1000次以内每100次保存一次模型，1000次后每10000次保存一次，修改保存函数在include/darknet.h中修改

9：如果每次的中最后一层的iou出现-nan说明数据集或标签做的不够好，不过也没什么太大影响

测试：./darknet detector test cfg/my_data.data cfg/my_yolov3.cfg weights/my_yolov3.weights 1.jpg

[cfg/my_data.data cfg/my_yolov3.cfg]:自己的配置文件路径
[weights/my_yolov3.weights]:训练完成的模型路径
[1.jpg]:测试图片的路径

以上所有流程在ubuntu系统下完成，如果没有gpu的化请租赁云服务器，gpu的效率大概是cpu的500倍左右（2000秒迭代一次的cpu和4秒迭代一次的gpu高下立判）

