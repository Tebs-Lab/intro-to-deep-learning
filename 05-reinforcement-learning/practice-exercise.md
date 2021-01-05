# Exercise: Implement Q-Learning

In this exercise you'll be asked to recreate some of the features from the previous Jupyter notebook in order to create a reinforcement learning agent that plays games. Using OpenAI's Gym and Universe packages, you can readily choose from a variety of games. Below, we have made some suggestions for which games to start with, and which ones to work your way up to.

## Exercise Goals

This exercise is meant to help you:

* Understand reinforcement learning, specifically Q-Learning.
* Explore the benefits and pitfalls of state-extraction and reward augmentation.

## Exercise Notes

You may wish to use Jupyter notebooks to complete this exercise or you might prefer to write Python code and run it via the terminal, use an IDE like PyCharm, or some other technology stack. Feel free to use any technology stack and workflow you are comfortable with.

Depending on the game you choose to explore, this exercise can range from relatively easy to *exceedingly difficult*. Q-Learning may not be an appropriate choice for every game in the Gym/Universe packages. Not only that, but given that you are probably learning these concepts for the first time, your implementation of Q-Learning will probably not be highly optimized. **There is no good reason to think every game can be readily solved with Q-Learning, or by reinforcement learning in general.**

The provided Jupyter notebooks contain much of the information you need to complete this exercise. However, you should also expect to look up information from the Tensorflow docs, the provided external reading material, and other sources. You are encouraged to search for information on your own. There are many open-source implementations of reinforcement learning, as well as specific reinforcement learning agents to play specific games. You may want to utilize those packages or at least study them to improve your own code.

Finally, this is not an exam. Correct answers are not provided. In fact, the exercise has enough ambiguity that many different answers will qualify as correct. You should be able to prove the correctness of your own answers using readily available tools—and in so doing you'll have learned quite a lot.

## The Exercise:

Build a q-learning agent that can consistently win games from OpenAi's Gym. Sounds easy... but it is not.

#### Suggested Games

Some games are easily solved with Q-Learning, while others are not. We suggest achieving success on at least one "easy" game before trying some of the harder games. Some games, like Montezuma's Revenge, are still the subject of ongoing research.

**Easy: Start Here**  

* Any of the [text based games](http://gym.openai.com/envs/#toy_text)
  * (We already solved FrozenLake in the provided notebooks)
* Any of the [Classic Control](http://gym.openai.com/envs/#classic_control) problems, especially CartPole.

**Medium: Challenge Yourself**  

* Any of the [Box2D games](http://gym.openai.com/envs/#box2d)

These games provide better documented, and easier understood, state values. These can still be quite challenging!

* An alternative to OpenAI's Gym are the [Berkeley AI Pacman RL Project](http://ai.berkeley.edu/reinforcement.html)
* This will require some additional setup, but also provides more guidance and structured feedback than solving a Gym game on your own.

**Hard: REALLY challenge yourself**  

* [Atari games](http://gym.openai.com/envs/#robotics). These are hard because the 'state' provided is just the state of RAM. Interpreting RAM and extracting useful state information for your Q-Agent is the main challenge for some of these games. For other games, such as Montezuma's Revenge, the game's long time horizon between rewards makes the game a subject of ongoing RL research.
  * If you go this route try starting with Breakout: there isn't THAT MUCH important information (paddle position, ball position, ball velocity) and there are known AI systems that can play breakout basically perfectly.
* [Robotics](http://gym.openai.com/envs/#robotics): A very real world example of where RL research is having significant impact is the field of Robotics. These robotics control problems are a good challenge, and not a toy in the sense that most games are toys.
