# Exercise: Perform Segmentation With a CNN

In this exercise you'll be asked to recreate some of the features from the previous Jupyter notebook in order to create a neural network that performs segmentation. 

## Exercise Goals

This exercise is meant to help you:

* Read and prepare the Oxford pets dataset for processing with a Neural Network
* Implement a convolutional neural network that performs segmentation

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise should take about 1 hour of actual work, but the training time for these models can be significant. You may wish to run training sessions overnight, during your lunch break, or just plan on leaving your computer while training your networks.

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Keras docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

In this exercise you'll make a subtle, but important change to the structure of the segmentation model provided in the segmentation Jupyter Notebook. In that notebook we created a model that was trained against two output feature maps, one for cat pixels and one for dog pixels. The result is a network that, in a sense, makes two separate predictions: one prediction for where cat pixels are and a separate prediction for where dog pixels are.

An undesirable outcome of this design is that for any given pixel, our model is allowed to predict that it belongs to both a cat AND a dog. Another problem is that our model does not make any explicit predictions about which pixels belong to the background. Background perditions are only implicit: a pixel that was not activated in either the cat or dog feature-map can be considered a background pixel.

In this exercise you'll fix this problem! Your model in this exercise will assign each pixel to one of threw possible classes. In this case that means each pixel will belong to one of three classes: cat, dog, or background. This change is a significant improvement on the old design because it more easily allows segmentation of photos that might contain several different classes.

### Step 1: Download and prepare the data

The Oxford Pets dataset can be found here: [http://www.robots.ox.ac.uk/~vgg/data/pets/](http://www.robots.ox.ac.uk/~vgg/data/pets/)

Download the dataset and the groundtruth data. Then, read and process the images and their matching trimap masks. You can leverage the code from the Jupyter notebook extensively to do this.

During this process you will have to change the way training data is prepared from the trimaps from what is in the notebook. Specifically, you should create three output feature maps (one for each: dog, cat and background) instead of two (one for dog, one for cat). The feature maps for the "dog" and "cat" layer will be identical to the ones in the notebook, and all three will still only contain values of 0 or 1, where zero indicates "this pixel is not a member of this feature-map's class" and one indicates "this pixel is a member of this feature-map's class". The new feature-map will contain 1's for pixels that are a part of the background, and 0's for pixels that are NOT a part of the background.

### Step 2: Build the model

You can again leverage much of the code in the notebook, but critically to support the changes we made to our training data you will have to update the number of kernels (from 2 to 3) and activation function (from sigmoid to softmax) in the final layer. You'll also need to change the loss function (from binary cross entropy to categorial cross entropy).

### Step 3: Train and evaluate the model

Did your changes result in any significant improvements on the models performance on this dataset?
