from matplotlib import pyplot
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
import os

def age_model():
    prediction_age = ['0 - 5', '6 - 10', '11 - 15', '16 - 20', '21 - 30', '31 - 40', 
                      '41 - 50', '51 - 60', '61 - 70', '71 - 80', '81 - 90', '90 above']
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(64, 3, activation = 'relu', input_shape = (200, 200, 3)))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Conv2D(128, 3, activation = 'relu'))
    model.add(tf.keras.layers.MaxPool2D())
    #model.add(tf.keras.layers.Conv2D(256, 3, activation = 'relu'))
    #model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(512, activation = 'relu'))
    model.add(tf.keras.layers.Dense(256, activation = 'relu'))
    model.add(tf.keras.layers.Dense(12, activation = 'softmax'))
    #model.compile(optimizer = 'adam', loss = tf.losses.SparseCategoricalCrossentropy(from_logits = False), metrics = ['accuracy'])
    if os.path.basename(os.getcwd()) == 'Pybuilder':
        model.load_weights('../models/checkpoint')
    else:
        model.load_weights('./models/checkpoint')
    #print('Age:', model.trainable_weights)
    return model, prediction_age

def gender_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(64, 3, activation='relu', input_shape=(200, 200, 3)))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Conv2D(128, 3, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Conv2D(256, 3, activation='relu'))
    model.add(tf.keras.layers.MaxPool2D())
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(1024, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(512, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.1))
    model.add(tf.keras.layers.Dense(2, activation='softmax'))
    #model.compile(optimizer='sgd', loss=tf.losses.SparseCategoricalCrossentropy(from_logits=False), metrics=['accuracy'])
    if os.path.basename(os.getcwd()) == 'Pybuilder':
        model.load_weights('../models_gender/checkpoint')
    else:
        model.load_weights('./models_gender/checkpoint')
    #print('Gender:', model.trainable_weights)
    return model

def contrast(img):
    # img = cv2.imread(filename)
    Y = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(np.array(img))

    min = int(np.min(Y))
    max = int(np.max(Y))
    contrast = (max-min)/(max+min)
    return contrast


def face_detect(filename, faces, b):
    data = pyplot.imread(filename)
    # pyplot.imshow(data)
    ax = pyplot.gca()

    for face in faces:
        x, y, width, height = face["box"]
        box = (x, y, width, height)
        b.append(box)
        # print(b)
        rect = Rectangle((x, y), width, height, fill=False, color="red")
        ax.add_patch(rect)
        # for key,value in face['keypoints'].items():
        #   dot=Circle(value,radius=1.5,color="yellow")
        #  ax.add_patch(dot)

    # pyplot.show()


def crop(b, filename):
    img = Image.open(filename)
    for bb in b:
        box = bb
        box = ((box[0] + box[2] // 2) - box[3] // 2, box[1], (box[0] + box[2] // 2) + box[3] // 2, box[3]+box[1])
        c = img.crop(box)  # (left,upper,right,lower)
        #print(c.size)
        # pyplot.imshow(c)
        c.save(f"IM/cropped_image.jpg")
        downscale(c)


def downscale(img):
    # basewidth = 100
    # wpercent = (basewidth/float(img.size[0]))
    # print(wpercent)
    # hsize = int((float(img.size[1])*float(wpercent)))
    img5 = img.resize((200, 200), Image.ANTIALIAS)
    img5.save("IM/resized_image.jpg")
    # print(img5.size)