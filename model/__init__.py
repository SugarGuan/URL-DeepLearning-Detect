from keras.models import Sequential
from keras.layers import Dense, Activation
import time
import numpy as np


def train(data, label):
    model = Sequential()
    # layer1 =
    # layer2 =
    # model.add()
    # model.compile()

    # return model
    layer1 = Dense(32, activation='relu', input_dim=2)
    layer2 = Dense(1, activation='sigmoid')
    model.add(layer1)
    model.add(layer2)
    model.compile(optimizer='rmsprop',
                   loss='binary_crossentropy',
                   metrics=['accuracy'])
    model.fit(data, label, epochs=1000, batch_size=32)
    return model


def save(model):
    now = time.strftime("%Y%m%d-%H%M%S", time.localtime())
    path = './model.' + str(now) + '.h5'
    model.save(path)
    return path


def load(path):
    from keras.models import load_model
    return load_model(path)

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
savepath = 'D:\\Project\\2020\\URL-DeepLearning-Detect\\model\\model.20200306-161812.h5'
# savepath = save(train(data=data2, label=labels2))
print(savepath)
model = load(savepath)

prediction_data1 = [100, 99]
prediction_data2 = [100, 98]
prediction_data3 = [1, 2]
prediction_data = np.array([prediction_data1, prediction_data2, prediction_data3])
result_tmp = model.predict(prediction_data)
result = []
for number in result_tmp:
    result.append(int(number))

print(result)
print(result_tmp)