# Deep Learning in Production

There is a significant difference between solving simple problems with deep learning in a Jupyter notebook and deploying a highly available server that provides access to a trained model. Similarly, there is another chasm between learning from carefully curated datasets like those built into the Keras framework and creating a data pipeline to power your own models. Whether you want to integrating a fraud detection model into your payment infrastructure or use a GAN to generate deepfake cat videos, moving deep learning from an academic exercise to a production system presents unique challenges that go beyond applied mathematics.

To apply deep learning in production you have to tackle unique problems like:

* Where and how are we going to get all the data we need?
* Once we have it, where are we going to store it?
* Once it's stored, how are we going to deliver it to the engineers who'll train the model, and the infrastructure on which that model will be trained?
* By the way, what infrastructure will that be?
* How will we define success for our model and for our product over all?
  * (A successful model does not ensure a successful product...)
* Once we have a model, how does it fit into the rest of our systems, and into the lives of our customers?

In addition to new questions and problems posed by the unique aspects of ML there are age old software problems that still apply to ML:

* How should we manage scope creep?
* Should we build or buy?
* Should we train/host the models in our own datacenter, a cloud service, or a hybrid model?
* How will we monitor the system, and ensure its continued success?
  * What will we do when the monitoring suggests we're starting to fail?
* How will we approach version control for our models?
  * Plot twist: the code AND the training data comprise the trained model, so now we have to version our datasets.
* How will we integrate or separate the deployment of a new model from the deployment of the application?
* Can we do this within our budget?!

As you can see, there is quite a lot that goes into successfully taking a successful neural network and turning it into a successful business or product.

**By the end of this section students should be able to:**

* Identify and describe key components of the machine learning lifecycle.
* Anticipate problems that could arise during that lifecycle.
* Participate meaningfully in meetings about adopting ML/Deep Learning within their own company or organization.
* Save and load models without retraining them.
* Integrate saved models into other programs.

## Part 1: The Machine Learning Lifecycle

### Suggested Pre-Reading

* [The Machine Learning Lifecyce (video)](https://www.youtube.com/watch?v=ZmBUnJ7lGvQ)
* [DataRobot, The Machine Learning Lifecycle](https://www.datarobot.com/wiki/machine-learning-life-cycle/)

### Resources for Further Exploration

* [Google ML Crash Course: Production Systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems)
* [Another collection of resources for lots of specific languages/frameworks/infrastructure](https://github.com/ahkarami/Deep-Learning-in-Production)
* [An Overview of ML Deployment Approaches](https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html)

## Part 2: Creating and Training Models With Production in Mind



### Suggested Pre-Reading

* [The Machine Learning Lifecyce (video)](https://www.youtube.com/watch?v=ZmBUnJ7lGvQ)
* [DataRobot, The Machine Learning Lifecycle](https://www.datarobot.com/wiki/machine-learning-life-cycle/)

### Helpful Documentation

### Resources for Further Exploration

* [Google ML Crash Course: Production Systems](https://developers.google.com/machine-learning/crash-course/production-ml-systems)
* [Another collection of resources for lots of specific languages/frameworks/infrastructure](https://github.com/ahkarami/Deep-Learning-in-Production)
* [An Overview of ML Deployment Approaches](https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html)
