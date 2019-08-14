# Exercise: Build a CNN

In this exercise, your will be experimenting with convolutional layers in Keras.

## Exercise Goals

This exercise is meant to help you:

* Build a simple CNN from scratch using the Keras framework.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with. Our goal is to provide an exercise that helps you learn solidify Deep Learning concepts and the details of the Keras framework—not to enforce a specific workflow, tool, or strategy for executing Python code.

This exercise may take longer than 1 hour to complete, but if after 2 hours of experimentation you have not achieved a 92% validation accuracy, you may wish to move on anyway. Again, the purpose of this exercise is to become more familiar with deep learning concepts and applying them with Keras. The 92% accuracy score is an arbitrary bar provided to make the exercise more challenging and engaging, but *is* a high bar.

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Keras docs, the provided external reading material, and other sources. You are encouraged to search for information on your own.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise

This exercise is simple: build and train a CNN using Keras that achieves at least 92% validation accuracy on the Fashion MNIST. While simple in description, this is challenging in practice. In your endeavor to achieve this result, apply the scientific method and iteratively improve your models. Start by forming a hypothesis about network architecture, specifically:

* How many convolutional layers should I use?
  * Should I use striding?
  * Should I use pooling?
  * How many filters should I use at each layer?
  * Which activation function should I use on these layers?
* How many Dense layers should I use in the classification section?
  * How many nodes per layer should I start with?
  * Where should I apply dropout layers, and what percent dropout should I use in those layers?
  * Which activation function should I use on these layers?
* Which loss function should I use?
* Which optimizer should I use?
* Should I enable early stopping?
  * What parameters should I use related to early stopping?

Once you've made these decisions, write the code to build and train the model. Once you've trained the model and seen its validation scores, make a change to some aspect of your network (seriously consider making just one change at a time), and re-evaluate. With each change, make a note of the change and document how that change impacted performance—being explicit and documenting these impacts is not just a good scientific practice, it will help you learn and build an intuition for how changes might impact results.

Be careful not to over-generalize your findings, though. There are complex interactions between datasets, network architectures, different optimizers, and so on. What is true in one situation might be a generalizable truth, but it might be specific to the current situation as well.
