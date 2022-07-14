The Chinese MNIST image classifcation is a machine learning model that I've created that is able to classify fifteen chinese characters. The data was collected from https://www.kaggle.com/datasets/gpreda/chinese-mnist. The model was created on Tensorflow using transfer learning (the convolutional base uses a pretrained VGG16 where all except the last conv2d block is frozen. Finally, the model was deployed on a website using Flask.

A source of inspiration for this project: https://devpost.com/software/text-to-text
