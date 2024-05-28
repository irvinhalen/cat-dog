# CatDog

## Image Classifier

### About

CatDog is an image classification application built with Python. It is made with the scikit-learn library. By presenting a picture of a dog or a cat, the application will predict whether it is a dog or a cat.

### Setup

#### Environment

1. Create a virtual environment with Python version 3.11.8
2. Run command
```sh
pip install -r requirements.txt
```

#### Model

1. Create a **data** folder and place it inside the root folder
2. Create a **pet_dataset** folder and place it inside the data folder
3. Create two folders, **train** and **val**, and place them inside the pet_dataset folder
4. Create two folders, **cat** and **dog**, and place them inside the train folder
    - Put pictures of cats inside the cat folder
    - Put pictures of dogs inside the dog folder
5. Create two folders, **cat** and **dog**, and place them inside the val folder
    - Put pictures of cats inside the cat folder (Make sure they are different from the pictures placed in the train folder)
    - Put pictures of gods inside the dog folder (Make sure they are different from the pictures placed in the val folder)
6. Run the command
```sh
python scikit_psyche.py
```
7. After the application executes, make sure there is a file named **model.p** inside the root folder

### Quick Start

*This application will not run without completing the setup*
1. Place photos of dogs and or cats inside the **classify** folder
2. Run the command
```sh
python scikit_psychic.py
```
3. Enter a filename of one of the images in the classify folder
    - Filename is case sensitive
    - Include the extension
        - e.g., "Photo.JPEG", "Photo.jpg", "Photo.png"
