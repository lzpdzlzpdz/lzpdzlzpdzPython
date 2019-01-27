#代码清单5-17　使用预训练的卷积基提取特征 
#代码清单5-18　定义并训练密集连接分类器 
#训练速度非常快，因为你只需处理两个Dense 层。即使在CPU 上运行，每轮的时间也不到一秒钟。 

import os  
import numpy as np  
from keras.preprocessing.image import ImageDataGenerator  

from keras import models  
from keras import layers  
from keras import optimizers  

#1. 输入样本集、标签集、测试集
train_features, train_labels = extract_features(train_dir, 2000)   
validation_features, validation_labels = extract_features(validation_dir, 1000)   
test_features, test_labels = extract_features(test_dir, 1000) 


#2. 创建模型
model = models.Sequential()  
model.add(layers.Dense(256, activation='relu', input_dim=4 * 4 * 512))  
model.add(layers.Dropout(0.5))  
model.add(layers.Dense(1, activation='sigmoid'))  


#3. 编译模型
model.compile(optimizer=optimizers.RMSprop(lr=2e-5),  
		  loss='binary_crossentropy',  
		  metrics=['acc'])  


#4. 拟合模型
history = model.fit(train_features, train_labels,  
				epochs=30,  
				batch_size=20,  
				validation_data=(validation_features, validation_labels)) 



    