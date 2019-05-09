# Section 5: Reinforcement Learning

**This section is incomplete, it will be updated very soon**

In contrast to supervised learning—of which CNNs and DNNs are an example—reinforcement learning is focused on creating agents that can make decisions in an evolving environment. Neural networks are primarily focused on classifying individual pieces of data. Is that a cat? Is this a bird? Reinforcement learning systems are about acting and adapting. They are better suited to tasks like playing a video game, driving a car, controlling robotics systems, and trading stocks.

Reinforcement learning is not inherently linked to deep learning, but some of the most interesting recent developments in the world of AI involve combining reinforcement learning and deep learning. Deep learning techniques help the computer understand the environment and reinforcement learning helps the system decide what to do with that information.

**By the end of this section students should be able to:**

* Define reinforcement learning and differentiate it from supervised learning.
* Identify situations where reinforcement learning can be applied.
* Build a policy based reinforcement learning agent and train it on an OpenAI Gym environment.

## Part 1: Reinforcement Learning Concepts

...todo...

## Part 2: Building A Q-Agent

The first kind of reinforcement learning we're going to build is called Q-Learning. Q-Learning is an iterative process that learns an optimal policy based on reward for reaching any particular state. These rewards can be positive or negative. Q-learning propagates the value of states (based on the rewards) to the previous states iteratively. The value of the states that can be reached from the current state inform the algorithm's idea of the current state's value. By repeatedly getting rewards (or punishments) for being in particular states and taking particular actions, the algorithm learns to associate state-action pairs with value, and learns to take actions that lead to high value states.

### Pre-Reading

* [Introduction to Reinforcement Learning](https://medium.freecodecamp.org/an-introduction-to-reinforcement-learning-4339519de419)
* [Diving Deeper into Reinforcement Learning](https://medium.freecodecamp.org/diving-deeper-into-reinforcement-learning-with-q-learning-c18d0db58efe)

### Helpful Documentation

* [OpenAI Gym Docs](http://gym.openai.com/docs/)
* [OpenAI Lunar Lander Environment](http://gym.openai.com/envs/LunarLander-v2/)
* [Lunar Lander Source Code](https://github.com/openai/gym/blob/master/gym/envs/box2d/lunar_lander.py)

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

### Helpful Documentation

### Resources for Further Exploration

* [Exploration vs Exploitation](https://towardsdatascience.com/reinforcement-learning-demystified-exploration-vs-exploitation-in-multi-armed-bandit-setting-be950d2ee9f6)

### External Dependencies

I had to install box2d and ffmpeg using brew to get the lunar lander environment to work:

```
brew install box2d
brew install ffmpeg
```
