# Exercise: Experiment With Activation, Loss, Optimizers, and Regularization

In this exercise, your will be experimenting with activation and loss functions, optimizers, network architecture, and regularization in order to achieve a desired result on the MNIST dataset. The goal of this exercise is to gain familiarity with these deep learning concepts, not to achieve a state of the art result on MNIST. However, one of the goals is to achieve a fairly good result on the MNIST dataset, and in so doing learn a bit about how choices related to activation functions, loss functions, optimizers, regularization, and  can impact the outcome.

## Exercise Goals

This exercise is meant to help you:

* Use several different activation functions.
* Use several different loss functions.
* Use several different optimizers.
* Use dropout layers.
* Use early stopping.
* Evaluate the impact of the above on network performance.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise may take longer than 1 hour to complete, but if after 2 hours of experimentation you have not achieved a 97% validation accuracy, you may wish to move on anyway. Again, the purpose of this exercise is to become more familiar with deep learning concepts and applying them with Tensorflow. The 97% accuracy score is an arbitrary bar provided to make the exercise more challenging and engaging.

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Tensorflow docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

This exercise is deceptively simple in its description: build at least two neural networks that achieve 97% or better validation accuracy on the MNIST dataset without using convolutional layers. Once you have (at least) two such networks, evaluate their performance on the test data and compare the results.

In your endeavor to achieve this result, apply the scientific method and iteratively improve your models. Start by forming a hypothesis about network architecture, specifically:

* How many layers, and how many nodes per layer should I start with?
  * Where should I apply dropout layers, and what percent dropout should I use in those layers?
  * Which activation function should I use on these layers?
* Which loss function should I use?
* Which optimizer should I use?
* Should I enable early stopping?
  * What parameters should I use related to early stopping?

Once you've made these decisions, write the code to build and train the model. Once you've trained the model and seen its validation scores, make a change to some aspect of your network (seriously consider making just one change at a time), and re-evaluate. With each change, make a note of the change and document how that change impacted performance—being explicit and documenting these impacts is not just a good scientific practice, it will help you learn and build an intuition for how changes might impact results.

Be careful not to over-generalize your findings, though. There are complex interactions between datasets, network architectures, different optimizers, and so on. What is true in one situation might be a generalizable truth, but it might be specific to the current situation as well.
