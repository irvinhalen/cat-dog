import pickle

from img2vec_pytorch import Img2Vec
from PIL import Image

with open('./model.p', 'rb') as f:
    model = pickle.load(f)

img2vec = Img2Vec()

filename = input('Info:\n• Filename is case sensitive\n• Include the extension\n\te.g., "Photo.JPEG", "Photo.jpg", "Photo.png"\n\nEnter filename: ')
img_path = f'./classify/{filename}'

try:
    img = Image.open(img_path)
    features = img2vec.get_vec(img)
    pred = model.predict([features])

    pred_str = str(pred).strip('[]')
    print(f"Prediction: {pred_str}")
except:
    print(f'File "{filename}" could not be found')
