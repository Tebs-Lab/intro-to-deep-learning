# Deep Reinforcement Learning

## Important Dependencies Note:

> Current release does not have RL labs up to date with TensorFlow 2, and I have been made aware there are additional difficulties installing box2d on OSX after Catalina... We're working on it.

To run the code in this section, additional dependencies are required. See the [main readme](/readme.md) for installation instructions under the heading "Note: Dev Dependencies for Reinforcement Learning Sections"

## Deep Reinforcement Learning:

Deep reinforcement learning marries the concepts from deep neural networks and reinforcement learning. In this section we look at one class of deep reinforcement learning algorithm: Deep Q-Networks (DQNs). Instead of keeping track of a table of possible state-action pairs and their transitions, we use a deep neural network.

## Part 1: Intro to Deep Reinforcement Learning / Naive DQNs

The simplest forms of DQNs simply replace the Q table with a deep neural network. When the state information is structured data, this replacement is simple and involves little more than building a neural network with an input vector that represents the state and an output vector that represents the possible actions that can be taken from that state. Each time we take an action and get a reward, we train the network on that single example using the Bellman equation to continuously update the "labels," which are our Q-value estimates in this context.

### Pre-Reading

* [An Introduction to Deep Q Learning](https://www.freecodecamp.org/news/an-introduction-to-deep-q-learning-lets-play-doom-54d02d8017d8/)

## Part 2: Improved DQNs

In recent years several improvements to the naive DQN approach have emerged.  Separating the "target network" and "Q network," allows the agent to learn against a fixed set of Q-values for a period of time before adjusting the targets, instead of constantly aiming for a moving target. The concept of "experience replay" allows our network to both escape the chronological aspect of training "online," it also provides a mechanic that allows us to run gradient descent on batches of data instead of individual samples.

### Pre-Reading

* [Improvements to Deep Q Learning](https://www.freecodecamp.org/news/improvements-in-deep-q-learning-dueling-double-dqn-prioritized-experience-replay-and-fixed-58b130cc5682/)

### Helpful Documentation

* [Keras RL Github](https://github.com/keras-rl/keras-rl)
* [Kerasl RL Docs (Deep Q Network)](https://keras-rl.readthedocs.io/en/latest/agents/dqn/)
* [Keras RL Cartpole Example](https://github.com/keras-rl/keras-rl/blob/master/examples/dqn_cartpole.py)

### Resources for Further Exploration

* [Advanced DQNs: Play Pac Man With Reinforcement Learning](https://towardsdatascience.com/advanced-dqns-playing-pac-man-with-deep-reinforcement-learning-3ffbd99e0814)
* [Implementing Deep Reinforcement Learning With Tensor Flow](https://lilianweng.github.io/lil-log/2018/05/05/implementing-deep-reinforcement-learning-models.html)

## Part 3: Playing From Pixels With CNNs

By using CNNs we can use the pixels on the screen as the "state" of any given environment (provided it involves visual feedback). This approach is computationally expensive, but promising because it enables a very generalized approach to reinforcement learning in any kind of visual environment.

### Pre-Reading

* [Deep Q-Networks and Beyond](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df)

### Helpful Documentation

* [OpenAI Gym: Breakout Docs](https://gym.openai.com/envs/Breakout-v0/)
* [Keras RL: Atari Example](https://github.com/keras-rl/keras-rl/blob/master/examples/dqn_atari.py)

### Resources for Further Exploration

* [Reinforcement Learning and DQN, learning to play from pixels](https://rubenfiszel.github.io/posts/rl4j/2016-08-24-Reinforcement-Learning-and-DQN.html)
