# Section 1: What is deep learning and why has it taken off?

Deep learning is a subset of machine learning which is itself a subset of AI. Specifically, deep learning involves the application of a particular kind of statistical model called neural networks. Neural networks are a model suitable for supervised learning, and they excel at modeling complex relationships in multi-dimensional data. While the algorithmic foundation for modern neural networks was laid in the 1970’s it has only recently become mainstream for two reasons. Lack of computational power and lack of large datasets.

**By the end of this section students should be able to:**

* Define key machine learning and deep learning terminology.
* Describe neural networks as computational graphs and as complex mathematical formulas.
* Describe how neural networks are trained at a high level.
* Use Tensorflow to build, train, and evaluate simple neural networks.

## Part 1: What Are Neural Networks, and Why Now?

Neural networks have taken off in no small part due to improvements in computing hardware. The first papers describing neural networks were written in the 1970's, but it was 40 years of Moore's Law that made the technique viable. In addition to the increase in computational power and massive improvements in parallel computing, neural networks have benefited from the collection of massive amounts of data.

In this section we'll discuss what neural networks are, the process through which they are trained, what they are good at, and some critical terminology. We'll also try to get past the hype and recognize some of the weaknesses of ML techniques and deep learning in general.

### Pre-reading Material

* [Introduction to Deep Learning](https://medium.com/tebs-lab/introduction-to-deep-learning-a46e92cb0022)
* [Neural Networks as Computational Graphs](https://medium.com/tebs-lab/deep-neural-networks-as-computational-graphs-867fcaa56c9)

### Resources for Further Exploration

* [Deep Learning Book, Chapter 4: Universal Approximation Theorem](http://neuralnetworksanddeeplearning.com/chap4.html)
* [The Bias/Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html)
* [Why Deep Learning Over Traditional Machine Learning](https://towardsdatascience.com/why-deep-learning-is-needed-over-traditional-machine-learning-1b6a99177063)
* [Historical Trends in AI/ML/Deep Learning](https://www.technologyreview.com/s/612768/we-analyzed-16625-papers-to-figure-out-where-ai-is-headed-next/)
* [High Performance Computing is More Parallel Than Ever](https://medium.com/tebs-lab/the-age-of-parallel-computing-b3f4319c97b0)
* [OpenAI: AI and Compute](https://openai.com/blog/ai-and-compute/)
* [Neural Networks Are Hackable](https://towardsdatascience.com/hacking-neural-networks-2b9f461ffe0b)

## Part 2: Building Neural Networks With Keras

Theory is great, but putting the theory into practice is more practical. In this section we'll build a handful of simple neural networks using the Keras library.

### Pre-Reading Material

* [Classifying MNIST Digits With Keras](https://medium.com/tebs-lab/how-to-classify-mnist-digits-with-different-neural-network-architectures-39c75a0f03e3)

### Helpful Documentation

* [Tensorflow Main Python Docs](https://www.tensorflow.org/api_docs/python/tf/)
* [TF Keras Frontend Docs](https://www.tensorflow.org/api_docs/python/tf/keras)
* [Matplotlib docs](https://matplotlib.org/)

## Part 3: Exploring Neural Network Architectures

Neural networks are very flexible models. The architecture of individual networks has a dramatic impact on their performance. Different architectures might be better suited to different tasks. Much of the ongoing research into neural networks is related to creating new architectures that out-perform the existing state of the art.

In this section we'll explore some of the impacts of different network architectures by constructing a few networks with different architectures.

### Pre-Reading Material

* [Picking The Number of Hidden Layers](https://www.heatonresearch.com/2017/06/01/hidden-layers.html)

### Resources For Further Exploration

* [How To Configure The Number of Nodes and Layers in a Neural Network](https://machinelearningmastery.com/how-to-configure-the-number-of-layers-and-nodes-in-a-neural-network/)
* [Stack Exchange Discussion on Choosing Number of Nodes and Layers](https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw)
* [List of Neural Network Topologies](https://towardsdatascience.com/the-mostly-complete-chart-of-neural-networks-explained-3fb6f2367464)
* [Asimov Institute's "Neural Network Zoo", another great collection of different types of network architectures](https://www.asimovinstitute.org/neural-network-zoo/)
