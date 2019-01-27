TensorFlow 中的 layers 模块提供用于深度学习的更高层次封装的 API，利用它我们可以轻松地构建模型，这一节我们就来看下这个模块的 API 的具体用法。

概览
layers 模块的路径写法为 tf.layers，这个模块定义在 tensorflow/python/layers/layers.py，其官方文档地址为： https://www.tensorflow.org/api_docs/python/tf/layers ，TensorFlow 版本为 1.5。

这里面提供了多个类和方法以供使用，下面我们分别予以介绍。

方法
tf.layers 模块提供的方法有：

Input(…): 用于实例化一个输入 Tensor，作为神经网络的输入。
average_pooling1d(…): 一维平均池化层
average_pooling2d(…): 二维平均池化层
average_pooling3d(…): 三维平均池化层
batch_normalization(…): 批量标准化层
conv1d(…): 一维卷积层
conv2d(…): 二维卷积层
conv2d_transpose(…): 二维反卷积层
conv3d(…): 三维卷积层
conv3d_transpose(…): 三维反卷积层
dense(…): 全连接层
dropout(…): Dropout层
flatten(…): Flatten层，即把一个 Tensor 展平
max_pooling1d(…): 一维最大池化层
max_pooling2d(…): 二维最大池化层
max_pooling3d(…): 三维最大池化层
separable_conv2d(…): 二维深度可分离卷积层