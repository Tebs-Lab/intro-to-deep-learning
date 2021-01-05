# Exercise: Perform Object Localization With a CNN

In this exercise you'll be asked to recreate some of the features from the previous Jupyter notebook in order to create a neural network that performs Object Localization. You'll also be asked to use a custom loss function in order to improve the performance above and beyond the levels that the previous notebook achieves.

## Exercise Goals

This exercise is meant to help you:

* Read and prepare the Oxford pets dataset for processing with a Neural Network
* Implement a convolutional neural network that performs object localization.
* Implement a CNN that provides two predictions (classification and localization) by using the [Tensorflow functional API](https://www.tensorflow.org/guide/keras/functional).

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise should take about 1 hour of actual work, but the training time for these models can be significant. You may wish to run training sessions overnight, during your lunch break, or just plan on leaving your computer while training your networks.

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Tensorflow docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

Your goal is to build and train a neural network that performs single object localization using the Tensorflow framework and the Oxford Pets dataset. You can leverage much of the code from the Object Localization Jupyter notebook, and you'll have to add and modify some code as well.

### Part 1: Download the data

You can download the images and annotations for the Oxford Pets dataset from this website [https://www.robots.ox.ac.uk/~vgg/data/pets/](https://www.robots.ox.ac.uk/~vgg/data/pets/). The downloads section is near the top of the page. You will need to download both the "images" and "ground truth" datasets for this exercise.

### Part 2: Parse and prepare the data

The dataset is described extensively on the website, as well as the Object Localization notebook in this same folder. Additionally, the notebook contains Python code that parses the raw data into a format that is ready for Tensorflow to process. For each image you should:

1. Extract the image data and turn it into a Numpy array.
1. Ensure the image is square by padding it appropriately with black pixels.
1. Scale the image to an appropriate size as determined by the neural network you import (e.g. Xception, MobileNetV2, etc.)
1. Extract the bounding box from the XML file associated with each image.
1. Appropriately adjust the bounding box for any padding and resizing that the image received.
1. Extract the classification labels for each image.
1. Ignore images that do not have a bounding box in the provided annotations.

The provided notebook has code that performs all of these steps, you may wish to use it here.

### Part 3: Import and prepare a CNN

Like in previous labs and exercises, we're applying transfer learning. Import a pre-trained network from Tensorflow with `include_top=False`. Then, using the Tensorflow functional API, give that network two prediction heads: one for classification and one for object localization.

You'll have to decide which loss functions to use, and how to weight the predictions from each head during training at this point as well. In the notebook we used `binary_crossentropy` for the classifier, and `mse` for the localizer with weights of `1` and `800` respectively (those weights were chosen arbitrarily, but worked decently). You may wish to experiment with other options.

**Challenge Opportunity** in the provided notebook, we only classify images as being of a "dog" or "cat" but the provided dataset has more detailed labels for the breed of each dog or cat. You can choose to implement a simpler "dog or cat" classifier, as done in the provided notebook, or make your network predict the breed. If you go for breed then your classification head will need a node for each possible breed, which means you will also not want to use `binary_crossentropy` as your loss function, since it is designed for binary classifiers.

**Challenge Opportunity** in the provided notebook we have our network predict the pixel position of the bounding box. Better performance can often be achieved by normalizing these values between 0-1. In other words, for each of the four points in our bounding box, have your model predict those positions as a scalar relative to the image size, rather than absolute pixel position. Normalizing these outputs will require you to change the way we process the image and XML input data.

**Challenge Opportunity** Accuracy is one popular metric for judging the performance of a classifier. [Intersection over Union](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/) is a popular metric for judging the accuracy of an object localization model. Consider implementing a custom metric to compute the intersection over union as a validation metric for your model, and plot its change over time during training alongside accuracy and the `mse` loss.

### Part 4: Train and evaluate the model

Training the model may take a long time, particularly if you'd like to do several epochs. Once you've trained the network evaluate its performance by looking at the loss and accuracy metrics, as well as looking at several of your networks predictions. Code for visualizing the networks predicted bounding boxes and the ground truth from in the dataset is provided in the Object Localization Jupyter notebook.
