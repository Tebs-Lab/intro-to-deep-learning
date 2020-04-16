# Exercise: Data Preprocessing

In this exercise you'll practice applying your knowledge of data collection and preprocessing as it relates to images.

## Exercise Goals

This exercise is meant to help you:

* Apply image preprocessing techniques using the Keras 

## Exercise Notes

This exercise should take about two an hour, possibly less. It is more straightforward than many other exercises in this series. Fundamentally, it is focused on applying the data generator to a series of images.

I suggest using a Jupyter notebook for this exercise, as it is easy to visualize the results of the data generator and inspect the results to ensure they are what you exepct.

## The Exercise

This simple exercise has two simple parts:

1. Download at least 10 images, from anywhere.
2. Apply the `ImageDataGenerator` to those images, and show them on the screen.

Step one, I hope, is self explainatory. 

In step two make sure that you:

* Make at least 4 different `ImageDataGenerators` using different values for the parameters.
* Generate at least 3 batches per `ImageDataGenerator`.

Then, consider these questions:

* Can you think of a situation or dataset where image rotation might be innappropriate, or damage the models performance?
    * What about flipping?
    * Skewing?
* What advantages and disadvantages might the different values for `fill_mode` provide?
* Can you think of a situation where *any* data augmentation might be innappropriate?
* What could the advantages and disadvantages of data normalization and scaling on image data? e.g. normalizing from (0,255) into (0, 1) or (-1, 1)
