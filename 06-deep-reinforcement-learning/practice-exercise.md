# Exercise: Implement Q-Learning

In this exercise you'll be asked to recreate some of the features from the previous Jupyter notebook in order to create a deep reinforcement learning agent that plays games from pixels. Using OpenAI's Gym and Universe packages, you can readily choose from several Atari games, some of which are easier than others to solve in this way.

## Exercise Goals

This exercise is meant to help you:

* Understand deep reinforcement learning, specifically Deep Q-Networks.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with.

Depending on the game you choose to explore, this exercise can range from relatively easy to *exceedingly difficult*. Q-Learning may not be an appropriate choice for every game in the Gym/Universe packages. Not only that, but given that you are probably learning these concepts for the first time, your implementation of Q-Learning will probably not be highly optimized. **There is no good reason to think every game can be readily solved with Q-Learning, or by reinforcement learning in general.**

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Keras docs, the provided external reading material, and other sources. You are encouraged to search for information on your own. There are many open-source implementations of reinforcement learning, as well as specific reinforcement learning agents to play specific games. You may want to utilize those packages or at least study them to improve your own code.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise:

Build a Deep Q-Network that can consistently win games from OpenAi's Gym. Sounds easy... but it is not.

You may select any of the [Atari games](http://gym.openai.com/envs/#robotics) for this exercise, since they provide state as the current pixels on the screen. You may wish to use a package like [keras-rl](https://github.com/keras-rl/keras-rl) in order to benefit from relatively recent achievements
(e.g. experience replay, dueling network architecture) and well optimized code, or if you're seeking a very serious challenge you may wish to build these features "from scratch" using Keras.

When selecting a game, consider that you'll get better results with games that have short feedback loops. Breakout, Freeway, Bowling, and Ms. Pac Man for example. Long running games with keys, dungeons, and that require complex navigation are *much harder to solve* with reinforcement learning.

Good luck!
