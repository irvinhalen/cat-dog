import pickle

from img2vec_pytorch import Img2Vec
from PIL import Image

with open('./model.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

image_path_dog = './data/pet_dataset/val/dog/dog15.jpg'
image_path_cat = './data/pet_dataset/val/cat/cat15.jpg'

img_dog = Image.open(image_path_dog)
img_cat = Image.open(image_path_cat)

features = img2vec.get_vec(img_cat)

pred = model.predict([features])

print(pred, type(pred))
