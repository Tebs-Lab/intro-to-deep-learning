# Exercise: Apply Transfer Learning With CNNs

In this exercise, your will be implementing transfer learning to retrain models that have been trained on the ImageNet dataset in order to perform classification on the CIFAR dataset.

## Exercise Goals

This exercise is meant to help you:

* Import a pre-trained network using Keras.
* Implement transfer learning using Keras.
* Evaluate the success of that transfer learning.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise should take about 1 hour of actual work, but the training time for these models can be significant. You may wish to run training sessions overnight, during your lunch break, or just plan on leaving your computer while training your networks.

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Keras docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

Your goal is to compare the performance of two styles of transfer learning on two different base models. This means you'll implement 4 examples of transfer learning in total. First, import the built in CIFAR100 dataset, then select one of the built in models from Keras (MobileNetV2 for example) to serve as your base model and follow these steps:

### Part 1: Fixed Feature Extraction

* Import this model using the `imagenet` weights, and `include_top=False`.
* Run the CIFAR 100 test and training data through this model and save the resulting features.
  * An example of this can be found in 03-transfer-learning.ipynb directly under the "Transfer Learning Tips and Pitfalls" header.
* Create a classification network for the CIFAR 100 dataset which will:
  * Accept as input the result of our pretrained model (i.e. the features you just saved)
  * Produce as output a classification for the CIFAR100 dataset.
* Train your classification network on the saved features.
* Plot your results.

### Part 2: Partially Frozen Transfer Learning

* Import this model using the `imagenet` weights, and `include_top=False`.
* Freeze at least the first half of all convolutional layers in that model.
* Add a classification section to the model corresponding to the CIFAR100 dataset.
* Train this model on the CIFAR100 dataset.
* Plot your results

### Part 3: Repeat

Repeat the previous two sections with a different base model (Xception for example instead of MobileNetV2), and compare your results. Make a note especially of the difference in training time—some of these models are significantly more complex.
