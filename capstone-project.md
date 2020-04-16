# Capstone Project

This document describes the motivation for a larger self-guided deep learning project, outlines some general requirements for such a project, and provides a few tips for students about where to start. Whether you're a self guided learner or an instructor/student using these materials as part of a structured course, we highly recommend attempting a capstone project in addition to the simpler (though challenging) exercises provided throughout. 

This project description is appropriate for solo or group work, both provide their own benefits and drawbacks for learners. In industry this kind of work is rarely done by an individual in isolation. Academic research such as a Ph.D program is often spearheaded by a single person. There is no "one true path" so decide for yourself (or your students) whether or not to work on this project in groups.

## Why Do We Suggest a Project Like This?

Great question, there are three reasons.

### 1: Better Approximate The Real World

Applying deep learning from end to end is quite a bit different from working on targeted exercises. The latter are useful steps in the learning process, but ultimately for deep learning models to be useful they have to start from a problem description and finish as a useful implementation — frequently deployed and accessible as an API or service.

A small sampling of the difference between a simple exercise and a real ML project includes:

* Datasets are gathered and built rather than imported.
* It's not clear from the start if your task is possible.
* Infrastructural, logistical, legal, and many other types of problems arise in addition to the mathematical and statistical problems associated with training and testing a model.
    * How do we collect the data we need?
    * How do we prepare that data for processing?
    * How do we store that data and create and effective data pipeline?
    * How do we deploy the model once it has been deployed?
    * How will we monitor the models performance?
    * What will we do when it starts to fail?
    * ... and so on ...

A larger, more self guided project provides many learning opportunities related to this full-ecosystem compared to the practice exercises.

### 2: Project Based Learning Teaches Meta Skills

Deciding what to pursue, managing one's time wisely, performing self-guided research, creating one's own goals, and evaluating one's own success or failure are all examples of skills that are hard to teach with targeted exercises. Project based learning gives learners a chance to develop these valuable skills. 

### 3: A Chance to Explore, a Chance to Reinforce

Deep learning is a massive field with myriad approaches and applications. Students should be empowered to explore topics that are inevitably left out of any structured course. Additionally, each student will proceed through the curriculum at a different pace. By the end of the class some students will be hungry for more information, and others will be overwhelmed by the veritable flood of information they just received.

A self-guided project is an invitation for students who are ready to push further afield. It's also a chance for students who want more time to work on the material they've already encountered to circle back and try to better understand those concepts.

## Project Description and Requirements

> Note: this description is intentionally broad and slightly vague, the reasons for that are outlined above. 

To complete this project students must:

1. Select a problem.
1. Apply deep learning to that problem.
1. Evaluate the results.
1. Prepare a short (5-10 minute) presentation about those results.

That's it, good luck!

## Project Ideas:

If you have no idea where to start, consider these:

### Go End to End on a Simple Task

Get some data, build a model from scratch, train the model, and evaluate your results. You'll be surprised what a wonderful challenge this is, especially if you have never done and end-to-end ML project before.

### Try a Kaggle Challenge

Kaggle has a number of well formed problem descriptions and quality datasets. They also have helpful benchmarks and publicly available results from other competitors. Kaggle is a great way to practice, especially if you want to focus on the model rather than data collection. 

### Recreate an Established Result

A great project can almost always be made by attempting to recreate a highly cited paper or rebuilding a well-known architecture. This kind of project will help students become more comfortable with complex architectures, and the paper itself can provide a useful guide for the kind of performance that architecture should be able to achieve.

Search on arxiv, Google Scholar, or elsewhere for an interesting paper, and see if you can recreate their results! Beware, deep learning (like other disciplines) has a but of a reproducibility problem. If you're using the paper's results as a guide for how well you're doing, make sure you choose a paper that has been highly cited and whose results have already been reproduced by others.

### Use an Open Source Architecture Or Implementation To Solve a Problem

You don't have to reinvent the wheel, sometimes it's better to just use an existing wheel. Plenty of industrial applications of deep learning simply apply an open source implementation of a pre-trained network to a problem. As developers the model might not be the most interesting part of the problem, perhaps you'd rather focus on attaching a model to some other task or process.

Maybe you want to connect an object localization model to your webcam and start recording whenever your cat comes into frame. 

Maybe you want to experiment with an implementation of StyleGAN2 to generate realistic deep fakes of flowers, renaissance paintings, or pies. 

Maybe you want to use a pre-trained image segmentation model to auto-crop images, anonymize webcam footage by blurring faces, or something else. 

All of these are perfectly appropriate projects.

## A Final Word of Advice: Focus on Learning Over Outcomes

Achieving a "good" result in terms of accuracy or some other metric is neither required nor expected. In fact, often times we learn more from "failures" than "successes." In the real world, you'll tend to fail many times before you succeed. Engineering is an iterative process, embrace this!

If your model doesn't perform as well as you'd have liked then candidly describe its shortcomings and form a hypothesis for:

* What went wrong, 
* Whether the shortcoming can be improved/overcome, and
* What to try next in order to improve the model's performance.