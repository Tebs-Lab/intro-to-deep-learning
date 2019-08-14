# Exercise: Neural Network Basics in Keras

If you've worked through the three notebooks you should be somewhat familiar with the basics of neural networks, and how they are built using Keras. Now, you should solidify your understanding of these concepts by building and training some networks of your own.

## Exercise Goals

This exercise is meant to help you:

* Gain familiarity with the syntax and function of the Keras library.
* Gain familiarity with the Keras documentation.
* Practice using neural network terminology.
* Practice building, training, evaluating models with Keras.
* Create mental connections between deep learning theory and Keras code.
* Compare the performance of different neural networks.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise should take between 30 minutes and 1 hour to complete. The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Keras docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

You will build a few neural networks during this exercise, for all the networks you build you should:

* Build a network for classification using the built in MNIST dataset.
* Use the sigmoid activation function.
* Use the categorical cross entropy loss function.
* Use stochastic gradient descent as the optimizer.
* Train for at least 10 epochs.
* Plot a chart with your network's performance on training and validation data during training.

### Part One:

Use Keras to build a network with a single hidden layer and at least 300,000 trainable parameters. Answer the following questions about this model:

* How many total trainable parameters does this model have?
  * How many weights?
  * How many biases?
* How accurate was this model on the validation data after 10 epochs?
  * How different was the model's performance on the training data?
  * How different was the model's performance on the test data?
* About how long did each epoch take?

Use Keras to build a network with a single hidden layer at fewer than 50,000 trainable parameters, then answer the same questions.

### Part Two:

Use Keras to build 3 networks, each with at least 10 hidden layers such that:

* The first model has fewer than 10 nodes per layer.
* The second model has between 10-50 nodes per layer.
* The third model has between 50-100 nodes per layer.

Then, answer these questions:  

* Did any of these models achieve better than 20% accuracy on validation or test data?
  * State a hypothesis about why these networks performed the way they did.
  * *An answer to this question is given in a notebook from the next section [01-activations](/02-training-and-regularization-tactics/01-activations.ipynb)*
* How many total trainable parameters do each of these models have?
* Is there a clear correlation between number of trainable parameters and accuracy?
  * Consider your results from part one in answering this question.

### Part Three:

Build a network with at least 3 hidden layers that achieves better than 92% accuracy on validation and test data. You may need to train for more than 10 epochs to achieve this result.

* Compare your best results to the result you got in part one:
  * Which network achieved the best accuracy on test data after training?
  * Did the networks train for a similar number of epochs?
