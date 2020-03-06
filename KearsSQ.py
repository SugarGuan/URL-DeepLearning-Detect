from keras.models import Sequential
from keras.layers import Dense, Activation
#
# model = Sequential()
# model.add(Dense(32, activation='relu', input_dim=100))
# model.add(Dense(1, activation='sigmoid'))
# model.compile(optimizer='rmsprop',
#               loss='binary_crossentropy',
#               metrics=['accuracy'])
#
# # 生成虚拟数据
import numpy as np
# data = np.random.random((1000, 100))
# labels = np.random.randint(2, size=(1000, 1))
#
# print(data)
# print(labels)
# #
# # # 训练模型，以 32 个样本为一个 batch 进行迭代
# model.fit(data, labels, epochs=10, batch_size=32)
# j = model.to_json()
# print(j)
# # model.save(filepath="D:\\Project\\2020\\URL-DeepLearning-Detect\\123\\")


model2 = Sequential()
layer1 = Dense(32, activation='relu', input_dim=2)
layer2 = Dense(1, activation='sigmoid')
model2.add(layer1)
model2.add(layer2)
model2.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

data2 = np.array([[0, 0],
                 [0, 1],
                 [1, 1],
                 [1, 0],
                 [100, 100],
                 [99, 99],
                 [99, 100],
                 [100, 98]
                 ])
#
labels2 = np.array([[0], [0], [0], [0], [1], [1], [1], [1]])
model2.fit(data2, labels2, epochs=1000, batch_size=32)
prediction_data1 = [100, 99]
prediction_data2 = [100, 98]
prediction_data3 = [1, 2]
prediction_data = np.array([prediction_data1, prediction_data2, prediction_data3])
result_tmp = model2.predict(prediction_data)
result = []
for number in result_tmp:
    result.append(int(number))

print(result)
print(result_tmp)

# string = "www.qq.com"
#
# from domain import count
# print(count.dots(string))
# print(count.numbers(string))
# print(count.symbol(string))
# print(count.vowels(string))

# import requests
# import urllib3
# urllib3.disable_warnings()
# url = 'https://api.devopsclub.cn/api/whoisquery?type=json&domain='
# response = requests.get(url + string, verify=False)
# print(response.text)
