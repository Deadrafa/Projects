import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from tensorflow import keras
from keras.layers import Dense, Flatten



# Загрузка обучающеё и тестовой выборки
(x_train, y_train), (x_test, y_test)  = mnist.load_data() 


#Стандартизация данных
x_train = x_train / 255
x_test = x_test / 255


# Преобразование выходных значений в векторы по категориям
y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

#Отображение первых 25 изображений из обучающей выборки
plt.figure(figsize=(10, 5))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(x_train[i], cmap=plt.cm.binary)

plt.show()


#Формирование модели НС и вывод её структуры в консоль

model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)), 
    Dense(128, activation='relu'), 
    Dense(10, activation='softmax')
])

print(model.summary())



# Компилация Нс с оптимизацией по Adam и критерием - категориальная кросс-энтропия 
model.compile(optimizer='adam',
loss='categorical_crossentropy',
metrics=['accuracy'])


# Запуск процесса обучения: 80% - обучающая выборка, 20% - проверочная выборка
model.fit(x_train, y_train_cat, batch_size=32, epochs=10, validation_split=0.2)

model.evaluate(x_test, y_test_cat)


# Проверка распознания цифр

n = 0
x = np.expand_dims(x_test[n], axis=0)
res = model.predict(x)
print( res )
print( f'Распознанная цифра {np.argmax(res)}' )

plt.imshow(x_test[n], cmap=plt.cm.binary)
plt.show()


# Распознание всей тестовой выборки 
pred = model.predict(x_test)
pred = np.argmax(pred, axis=1)
 
print(pred.shape)
 
print(pred[:20])
print(y_test[:20])


# Выделение не верных результатов

mask = pred == y_test
print(mask[:10])
 
x_false = x_test[~mask]
y_false = pred[~mask]
 
print(x_false.shape)


# Вывод не верных результатов
for i in range(5):
  print("Значение сети: "+str(y_test[i]))
  plt.imshow(x_false[i], cmap=plt.cm.binary)
  plt.show()