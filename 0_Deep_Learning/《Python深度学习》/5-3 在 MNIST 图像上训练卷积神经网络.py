本章主要讲解这三种策略——从头开始训练一个小型卷积神经网络模型、使用预训练的网络做特征提取、对预训练的网络
进行微调——构成了你的工具箱，未来可用于解决小型数据集的图像分类问题。

下面我们在MNIST 数字图像上训练这个卷积神经网络。我们将复用第2 章MNIST 示例中的很多代码。 

代码清单5-3　在MNIST 图像上训练卷积神经网络 

from keras.datasets import mnist  
from keras.utils import to_categorical  
from keras import layers   
from keras import models  

#1. 输入样本集、标签集、测试集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()  

train_images = train_images.reshape((60000, 28, 28, 1))  
train_images = train_images.astype('float32') / 255  

test_images = test_images.reshape((10000, 28, 28, 1))  
test_images = test_images.astype('float32') / 255  

train_labels = to_categorical(train_labels)  
test_labels = to_categorical(test_labels)  

#2. 创建模型
model = models.Sequential()  
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))   
model.add(layers.MaxPooling2D((2, 2)))  
model.add(layers.Conv2D(64, (3, 3), activation='relu'))   
model.add(layers.MaxPooling2D((2, 2)))  
model.add(layers.Conv2D(64, (3, 3), activation='relu'))      //(None, 3, 3, 64)
# 需要将 3D 输出展平为 1D，将(3, 3, 64)输出展平为(576, )
#Flatten层用来将输入“压平”，即把多维的输入一维化，常用在从卷积层到全连接层的过渡。Flatten不影响batch的大小。
model.add(layers.Flatten())      //(None, 576)
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
# 查看模型各层状态
model.summary()

#3. 编译模型
model.compile(optimizer='rmsprop',  
            loss='categorical_crossentropy',  
            metrics=['accuracy'])  

#4. 拟合模型
model.fit(train_images, train_labels, epochs=5, batch_size=64) 



我们在测试数据上对模型进行评估。 

 >>> test_loss, test_acc = model.evaluate(test_images, test_labels)  
 >>> test_acc  
 0.99080000000000001 



第2 章密集连接网络的测试精度为97.8% ，但这个简单卷积神经网络的测试精度达到了 99.3% ，我们将错误率降低了68%  （相对比例）。相当不错！ 
与密集连接模型相比，为什么这个简单卷积神经网络的效果这么好？要回答这个问题，我们来深入了解Conv2D 层和MaxPooling2D 层的作用。
5.1.1　卷积运算
密集连接层和卷积层的根本区别在于， Dense 层从输入特征空间中学到的是全局模式（比如对于 MNIST数字，全局模式就是涉及所有像素的模式），
而卷积层学到的是局部模式（见图 5-1），对于图像来说，学到的就是在输入图像的二维小窗口中发现的模式。在上面的例子中，这些窗口的大小都是 3×3。
这个重要特性使卷积神经网络具有以下两个有趣的性质。
（1）卷积神经网络学到的模式具有平移不变性（translation invariant）。卷积神经网络在图像右下角学到某个模式之后，它可以在任何地方识别这个模式，比如左上角。
对于密集连接网络来说，如果模式出现在新的位置，它只能重新学习这个模式。这使得卷积神经网络在处理图像时可以高效利用数据（因为视觉世界从根本上具有平移不变性），它只需要更少的训练样本就可以学到具有泛化能力的数据表示。
（2）卷积神经网络可以学到模式的空间层次结构（spatial hierarchies of patterns），见图 5-2。第一个卷积层将学习较小的局部模式（比如边缘），第二个卷积层将学习由第一层特征组成的更大的模式，以此类推。这使得卷积神经网络可以有效地学习越来越复杂、越来
越抽象的视觉概念（因为视觉世界从根本上具有空间层次结构）。

对于 Keras 的 Conv2D 层，这些参数都是向层传入的前几个参数： Conv2D(output_depth,(window_height, window_width))。

5.2　在小型数据集上从头开始训练一个卷积神经网络
使用很少的数据来训练一个图像分类模型，这是很常见的情况，如果你要从事计算机视觉
方面的职业，很可能会在实践中遇到这种情况。“很少的”样本可能是几百张图像，也可能是几
万张图像。来看一个实例，我们将重点讨论猫狗图像分类，数据集中包含 4000 张猫和狗的图像
（2000 张猫的图像， 2000 张狗的图像）。我们将 2000 张图像用于训练， 1000 张用于验证， 1000
张用于测试。
本节将介绍解决这一问题的基本策略，即使用已有的少量数据从头开始训练一个新模型。
首先，在 2000 个训练样本上训练一个简单的小型卷积神经网络，不做任何正则化，为模型目标
设定一个基准。这会得到 71% 的分类精度。此时主要的问题在于过拟合。然后，我们会介绍数
据增强（data augmentation），它在计算机视觉领域是一种非常强大的降低过拟合的技术。使用
数据增强之后，网络精度将提高到 82%。
5.3 节会介绍将深度学习应用于小型数据集的另外两个重要技巧： 用预训练的网络做特征提
取（得到的精度范围在 90%~96%）， 对预训练的网络进行微调（最终精度为 97%）。总而言之，
这三种策略——从头开始训练一个小型模型、使用预训练的网络做特征提取、对预训练的网络
进行微调——构成了你的工具箱，未来可用于解决小型数据集的图像分类问题。
 