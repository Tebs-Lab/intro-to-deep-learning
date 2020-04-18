# Section 5: Reinforcement Learning

## Important Dependencies Note:

> Current release does not have RL labs up to date with TensorFlow 2, and I have been made aware there are additional difficulties installing box2d on OSX after Catalina... We're working on it.

To run the code in this section, additional dependencies are required. See the [main readme](/readme.md) for installation instructions under the heading "Note: Dev Dependencies for Reinforcement Learning Sections"

## Reinforcement Learning:

In contrast to supervised learning—of which CNNs and DNNs are an example—reinforcement learning is focused on creating agents that can make decisions in an evolving environment. Neural networks are primarily focused on classifying individual pieces of data. Is that a cat? Is this a bird? Reinforcement learning systems are about acting and adapting. They are better suited to tasks like playing a video game, driving a car, controlling robotics systems, and trading stocks.

Reinforcement learning is not inherently linked to deep learning, but some of the most interesting recent developments in the world of AI involve combining reinforcement learning and deep learning. Deep learning techniques help the computer understand the environment and reinforcement learning helps the system decide what to do with that information.

**By the end of this section students should be able to:**

* Define reinforcement learning and differentiate it from supervised learning.
* Identify situations where reinforcement learning can be applied.
* Build a policy based reinforcement learning agent (specifically Q-Learning) and train it on an OpenAI Gym environment.
* Describe some weaknesses/challenges associated with Q-Learning, specifically:
  * Continuous state-spaces
  * Sparse rewards
* Discretize continuous state spaces in order to apply Q-Learning.
* Apply reward augmentation to address sparse rewards.

## Part 1: Reinforcement Learning Concepts

Reinforcement learning requires us to model our problem using the following two constructs:

* An agent, the thing that makes decisions.
* An environment, the world which encodes what decisions can be made, and the impact of those decisions.  

The environment contains all the possible states, knows all the actions that can be taken from each state, and knows when rewards should be given and what the magnitude of those rewards should be. An agent gets this information from the environment by exploring and learns from experience which states provide the best rewards. Rewards slowly percolate outward to neighboring states iteratively, which helps the agent make decisions over longer time horizons.

### Pre-Reading

* [Reinforcement Learning Demystified: A Gentle Introduction](https://towardsdatascience.com/reinforcement-learning-demystified-36c39c11ec14)
* [Applications of Reinforcement Learning in Real World](https://towardsdatascience.com/applications-of-reinforcement-learning-in-real-world-1a94955bcd12)

### Resources for Further Exploration

* [Richard Sutton's Book, Reinforcement Learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)
* [Reinforcement Learning Demystified: Markov Decision Processes (Part 2)](https://towardsdatascience.com/reinforcement-learning-demystified-markov-decision-processes-part-2-b209e8617c5a)


## Part 2: Building A Q-Agent

The first kind of reinforcement learning we're going to build is called Q-Learning. Q-Learning is an iterative process that learns an optimal policy based on reward for reaching any particular state. These rewards can be positive or negative. Q-learning propagates the value of states (based on the rewards) to the previous states iteratively. The value of the states that can be reached from the current state inform the algorithm's idea of the current state's value. By repeatedly getting rewards (or punishments) for being in particular states and taking particular actions, the algorithm learns to associate state-action pairs with value, and learns to take actions that lead to high value states.

### Pre-Reading

* [Introduction to Reinforcement Learning](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419)
* [Diving Deeper into Reinforcement Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)

### Helpful Documentation

* [OpenAI Gym Docs](http://gym.openai.com/docs/)
* [Frozen Lake Docs](https://gym.openai.com/envs/FrozenLake-v0/)
* [Frozen Lake Implementation](https://github.com/openai/gym/blob/master/gym/envs/toy_text/frozen_lake.py)

### Resources for Further Exploration

* [UC Berkeley's Pacman Reinforcement Learning Exercise](http://ai.berkeley.edu/reinforcement.html)
* [UC Berkeley's AI Lectures, Markov Decision Processes and Reinforcement Learning are especially relevant](http://ai.berkeley.edu/lecture_videos.html)
* [Reinforcement Learning Demystified](https://towardsdatascience.com/reinforcement-learning-demystified-36c39c11ec14)
* [Reinforcement Learning Article Series](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)

## Part 3: Q-Learning Drawbacks and Advanced Tactics

Like anything, Q-Learning has strengths and weaknesses. For example, Q-Learning is great in discrete spaces, where the valid state-action pairs can be reasonably enumerated. But when the state-space grows large, or the state-space is continuous, Q-Learning can become untenable.

Q-learning also struggles with a problem called "sparse rewards," when there aren't very many rewards relative to the size of the space as a whole. The value of a reward has to percolate backwards from the reward granting state. If that state is hundreds of actions away from the starting state, Q-Learning agents will struggle to learn the string of actions that get them to that state.

Reward augmentation and function approximation are tactics to mitigate these problems.

### Pre-reading

* [Learning to Generalize from Sparse and Underspecified Rewards](https://ai.googleblog.com/2019/02/learning-to-generalize-from-sparse-and.html)

### Helpful Documentation

* [OpenAI Lunar Lander Environment](http://gym.openai.com/envs/LunarLander-v2/)
* [Lunar Lander Source Code](https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py)

### Resources for Further Exploration

* [UC Berkeley's Pacman Reinforcement Learning Exercise (again)](http://ai.berkeley.edu/reinforcement.html)
* [UC Berkeley's AI Lectures, Markov Decision Processes and Reinforcement Learning are especially relevant (also again)](http://ai.berkeley.edu/lecture_videos.html)
