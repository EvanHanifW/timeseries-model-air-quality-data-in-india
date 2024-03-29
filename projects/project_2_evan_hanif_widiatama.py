# -*- coding: utf-8 -*-
"""Project 2 - Evan Hanif Widiatama.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X748dctC2mBqd_JRqZXGtCAL1vzU_Co1
"""

import numpy  as np
import pandas as pd
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import tensorflow as tf

df = pd.read_csv('air-quality-india.csv')
df.head()

df.isnull().sum()

dates = df['Timestamp'].values
pm = df['PM2.5'].values

plt.figure(figsize=(15,5))
plt.plot(dates, pm)

from sklearn.model_selection import train_test_split

x_train, x_valid, y_train, y_valid = train_test_split(pm, dates, test_size=0.2, shuffle=False)

print(len(x_train))
print(len(x_valid))

def windowed_dataset(series, window_size, batch_size, shuffle_buffer) :
  series = tf.expand_dims(series, axis=-1)
  ds = tf.data.Dataset.from_tensor_slices(series)
  ds = ds.window(window_size + 1, shift=1, drop_remainder=True)
  ds = ds.flat_map(lambda w: w.batch(window_size + 1))
  ds = ds.shuffle(shuffle_buffer)
  ds = ds.map(lambda w: (w[:-1], w[-1:]))
  return ds.batch(batch_size).prefetch(1)

train_set = windowed_dataset(x_train, window_size=60, batch_size=100, shuffle_buffer=1000)
valid_set = windowed_dataset(x_valid, 60, 100, 1000)

model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(60, return_sequences=True),
    tf.keras.layers.LSTM(60),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
])

Mae = (df['PM2.5'].max() - df['PM2.5'].min()) * 10/100
Mae

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('mae') < Mae and logs.get('val_mae') < Mae):
      self.model.stop_training = True
callbacks = myCallback()

optimizer = tf.keras.optimizers.SGD(lr=1.0000e-04, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(),
              optimizer=optimizer,
              metrics=["mae"])

history = model.fit(train_set, epochs=100, validation_data=valid_set, callbacks=[callbacks])

plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.title('Akurasi Model')
plt.ylabel('Mae')
plt.xlabel('epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss Model')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['Train', 'Val'], loc='upper right')
plt.show()