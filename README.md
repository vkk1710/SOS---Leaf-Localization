# [SOS---Leaf-Localization](https://github.com/vkk1710/System-on-silicon)
My work during the Deep Learning Intern at System on Silicon Ltd

The original repo is private according to the company norms.
GitHub Link : https://github.com/vkk1710/System-on-silicon

Objective
----------

The main objective was to spot the diseased areas of the leafs.

Data
-----

### Classifier Data :

1. Cropped the images of the PlantVilage Dataset into the size of 50 x 50.
2. Segregated the crops into *diseased* (crops containing mostly the diseased area of the leaf) and *healthy* (crops including background or healthy parts of the leaf) labels.

### Localization model Data :

1. Currated images of leaves taken in real life setting from many sources like the PlantDoc Dataset.
2. Cropped those images to get an images consisting of a single leaf.
3. Collected random background images from the web to use them as negative label images.
3. Annotated the dataset using *LabelImg* annotation tool. 
4. Labels : 1. Leaf , 2. Background.

Models
------

### Localization Model :

The main objective of this model is to localize the leaf from a noisy background in a real life image.

### Classifier :

The main objective of this binary classifier is to predict whether the input image contains any diseased part of the leaf or not.

After the leaf is localized in the raw image, we use the sliding window technique and run this binary classifier on each window region to predict whether the region contains diseased part of a leaf or not. We use anchor boxes of different sizes to predict the diseased area as accurately as possible.
