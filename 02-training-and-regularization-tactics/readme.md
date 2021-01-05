# Section 2: Training and Regularization Tactics

Despite what you’ve heard, neural networks are not a panacea to every AI problem. They certainly provide advantages over other AI and ML tactics, such as reducing the need for feature engineering and capturing complex relationships in high dimensional data. They also have weaknesses such as huge data and computational resource requirements, lack of interpretability, and risk of overfitting.

In this class we're going to dive deeper into the most important component parts of neural networks, and explore the impact of choices we can make regarding each component.

**By the end of this section students should be able to:**

* Describe a few different activation functions and what factors contribute to their effectiveness.
* Build neural networks with different activation functions.
* Describe a few different loss functions and why you might use one over another.
* Train neural networks with different loss functions.
* Describe the role of optimizers in machine learning and name a few popular optimizers.
* Train neural networks with different optimizers.
* Describe regularization and its importance in machine learning.
* Apply regularization tactics to neural networks specifically dropout and early stopping.

## Part 1: Activation Functions

Every node in a neural network has an activation function. The primary purpose of these functions is to transform the input of that node. Selection of an activation function depends on the mathematical behavior of that function as well as the its computational efficiency. In this section we'll discuss a few common activation functions and their strengths/weaknesses.

### Pre-Reading Material:

* [Understanding Activation Functions in Neural Networks](https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0)
* [The Vanishing Gradient Problem](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484)

### Helpful documentation

* [TF/Keras Activations](https://www.tensorflow.org/api_docs/python/tf/keras/activations)
* [ML Cheatsheet: Activation Functions](https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html)

### Resources For Further Exploration

* [Deep Learning and Neural Networks Chapter 5: Why Are Deep Neural Networks Hard to Train](http://neuralnetworksanddeeplearning.com/chap5.html)
* [Pros and cons of Activation functions](https://yashuseth.blog/2018/02/11/which-activation-function-to-use-in-neural-networks/)
* [The Exploding Gradient Problem](https://machinelearningmastery.com/exploding-gradients-in-neural-networks/)
* [Many ReLUs](https://medium.com/tinymind/a-practical-guide-to-relu-b83ca804f1f7)
* [Combining different activations, paper](https://arxiv.org/abs/1801.09403v1)
* [Benefits of ELUs, paper](https://arxiv.org/abs/1511.07289v1)

## Part 2: Loss Functions

Loss functions are the way we quantify our network's error, and therefore how we optimize the network itself. Every time our network performs a batch of training, it is updated based on the loss function. In extreme cases the loss function might be hand constructed based on the problem domain, but most of the time practitioners pick from a handful of well known loss functions. Crucially, some of these functions are more appropriate for different tasks. Regression, binary classification, and multi-class classification generally do not use the same loss function. In this section we'll look at some of the most common loss functions.

### Pre-Reading Material

* [Common Loss Functions](https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23)

### Helpful Documentation

* [TF/Keras Built In Loss Functions](https://www.tensorflow.org/api_docs/python/tf/keras/losses)
* [ML Cheatsheet: Loss functions](https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html)

### Resources for Further Exploration

* [5 Regression Loss Functions All Machine Learners Should Know](https://heartbeat.fritz.ai/5-regression-loss-functions-all-machine-learners-should-know-4fb140e9d4b0)
* [How to Choose a Loss Function](https://machinelearningmastery.com/how-to-choose-loss-functions-when-training-deep-learning-neural-networks/)
* [Picking Loss Functions](https://rohanvarma.me/Loss-Functions/)
* [Building a Complex Custom Loss Function in TF/Keras](https://www.tensorflow.org/guide/keras/train_and_evaluate#custom_losses)


## Part 3: Optimizers

Optimizers are the algorithms we use to train our neural networks. All of them are based on calculus, and specifically the multi-variable derivative, which is called the gradient. Since the invention of the original optimizer, called Gradient Descent, a lot of research has been done to make the process of gradient descent more efficient and more robust. In this section we'll explore the impact of using different optimizers with our neural networks.

### Pre-Reading Material:

* [Gradient Descent](https://medium.com/tebs-lab/gradient-descent-604f6d6c116d)
* [Introduction to Optimizers](https://blog.algorithmia.com/introduction-to-optimizers/)

### Helpful Documentation:

* [Keras Optimizers](https://keras.io/optimizers/)
* [ML Cheat Sheet, Optimizers](https://ml-cheatsheet.readthedocs.io/en/latest/optimizers.html)

### Resources For Further Exploration

* [Optimizing Gradient Descent](http://ruder.io/optimizing-gradient-descent/)
* [Different Optimizers in Depth](https://towardsdatascience.com/types-of-optimization-algorithms-used-in-neural-networks-and-ways-to-optimize-gradient-95ae5d39529f)

## Part 4: Regularization

Regularization is a key aspect of any kind of statistical modeling. In general it refers to any tactic that improves performance on test and validation data at the expense of performance on training data. The goal of regularization is to guard against overfitting, and it is crucial in most machine learning situations, but especially in neural networks which are easy to overfit. In this section we'll apply two kinds of regularization, dropout and early stopping.

### Pre-Reading Material

* [A Gentle Introduction to Dropout for Regularizing Deep Neural Networks](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/)
* [Early Stopping in Keras](https://chrisalbon.com/deep_learning/keras/neural_network_early_stopping/)

### Helpful Documentation

* [TF/Keras Docs, Dropout](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout)
* [TF/Keras Docs, Early Stopping](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping)

### Resources For Further Exploration

* [Deep Learning Book, Chapter 7: Regularization for Deep Learning](https://www.deeplearningbook.org/contents/regularization.html)
* [Early Stopping and Its Faults](http://alexadam.ca/ml/2018/08/03/early-stopping.html)
