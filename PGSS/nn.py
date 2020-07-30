import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
import seaborn as sns

df = pd.read_csv('full_rules1.csv')
train_labels = pickle.load(open('train_labels1.pkl','rb'))

train_data = df.to_numpy()
train_data = train_data[:,1:]

data_train, data_test, label_train, label_test = train_test_split(train_data, train_labels, test_size=0.3, random_state=0)

print(train_labels)
model = keras.Sequential([
    keras.layers.Dense(1092),
    keras.layers.Dense(2000, activation='relu'), # 728
    keras.layers.Dense(6)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(data_train, label_train, epochs=10)

test_loss, test_acc = model.evaluate(data_test, label_test, verbose=2)

print('\nTest accuracy:', test_acc)


predictions = model.predict(data_test)
predictions = predictions.argmax(axis=1)

print(predictions.shape,label_test.shape)
# df_results = pd.DataFrame({'predictions': predictions, 'targets': label_test})
df = pd.crosstab(predictions,label_test) # .apply(lambda r: round(r/r.sum()*100,2), axis=1)
print(df)
df.columns = ['Even','Odd','Red','Black','Prime','Red & Even']
df.index = ['   Even','   Odd','   Red','   Black','   Prime','   Red & Even']
sns.heatmap(df, cmap='coolwarm', linewidths=0.5, annot=True)
# sns.palplot(sns.light_palette("navy", reverse=True))
# sns.palplot(sns.color_palette("husl", 8))
# pd.crosstab(df.A, df.B).apply(lambda r: r/r.sum(), axis=1)
plt.rcParams.update({'font.size': 100})
plt.ylabel('True Rule Labels')
plt.xlabel('Neural Network Predictions')
plt.show()