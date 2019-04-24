# Convolutional Neural Networks

Convolutional neural networks are a specialization of neural networks that are designed specifically to work with data that has spatial relationships. The most common use of CNN's is in the field of computer vision and image processing. This is because images have clear spatial relationships. Neighboring pixels have a stronger relationship than pixels in opposite corners of an image.

By adding ideas from image processing to neural networks, especially the idea of a 'kernel', convolutional neural networks have achieved fantastic performance on a number of computer vision tasks.

**By the end of this class students should be able to:**

* Define convolutional neural networks and their critical components.
* Describe why CNN's are such a good fit for computer vision tasks.
* Build convolutional neural networks using Keras.
* Describe the concept of Transfer Learning and apply it to CNNs using Keras.
* Contrast classification and segmentation.
* Apply CNNs to perform both classification and segmentation.

## Part 1: What Are CNNs and What Are They Good At?

See the above!

### Pre-Reading

* [Image Processing With Kernals](http://setosa.io/ev/image-kernels/)
* [The Math of Convolutional Networks](https://towardsdatascience.com/gentle-dive-into-math-behind-convolutional-neural-networks-79a07dd44cf9)

### Resources for Further Exploration

* [Neural Networks and Deep Learning, Chapter 6](http://neuralnetworksanddeeplearning.com/chap6.html#introducing_convolutional_networks)
* [Deep Learning Book, Chapter 9](http://www.deeplearningbook.org/contents/convnets.html)
* [Types of Convolutions](https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d)

## Part 2: Building CNNs For Classification

Just like with artificial neural networks, the theory is great but it's more fun to put the concepts into practice. In this section we'll build a few CNNs from scratch. We'll also import well known, pre-trained neural networks and apply them. Oftentimes, due to the enormous training costs of modern CNNs, it can be more effective to just use an existing model.

### Pre-Reading

* [Build a CNN in Keras](https://towardsdatascience.com/building-a-convolutional-neural-network-cnn-in-keras-329fbbadc5f5)

### Helpful Documentation

* [Keras Datasets](https://keras.io/datasets/)
* [Keras Convolutional layers](https://keras.io/layers/convolutional/)
* [NumPy Reshape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)
* [An example of a CNN architecture with 95%+ accuracy on Fashion MNIST](https://github.com/cmasch/zalando-fashion-mnist)
* [SciKit Learn's Confusuion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
* [Seaborn's Heatmap Plot](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

### Resources for Further Exploration

* [Detailed Intro to Keras CNNs](https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/)
* [More detailed implementation of Keras CNN & Fashion MNIST](https://www.pyimagesearch.com/2019/02/11/fashion-mnist-with-keras-and-deep-learning/)
* [Gradient Activated Heat Maps paper](https://arxiv.org/abs/1610.02391)

## Part 3: Transfer Learning

Transfer learning is a tactic that allows us to take a pre-trained neural network, and apply it to a new task. Transfer learning is especially popular with CNNs because a lot of images share the same useful features, which means the "lessons" learned by a CNN for one task can be immediately applied to another task. In this section we'll look at two different styles of transfer learning, feature extraction and fine-tuning, and apply them using Keras. 

### Pre-Reading

* [A Gentle Introduction to Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/)

### Helpful Documentation

* [Keras Models](https://keras.io/models/model/)
* [scipy zoom](http://scipy.github.io/devdocs/generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom)
* [Keras Pre-built Models](https://keras.io/applications/)
* [ImageNet Documentation](http://image-net.org/about-overview)
* [ImageNet classifications dictionary](https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a)
* [Image transform using PIL](https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/)]
* [Pillow documentation](https://pillow.readthedocs.io/en/stable/)

### Resources for Further Exploration

* [Fine Tuning and Fixed Transfer](http://cs231n.github.io/transfer-learning/)
* [A Comprehensive Guide to Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
* [Transfer Learning Tutorial With Keras](https://www.hackerearth.com/practice/machine-learning/transfer-learning/transfer-learning-intro/tutorial/)
* [Transfer Learning in Keras](https://towardsdatascience.com/keras-transfer-learning-for-beginners-6c9b8b7143e)
* [Introduction to Separable Convolutions](https://towardsdatascience.com/a-basic-introduction-to-separable-convolutions-b99ec3102728)
* [Discussion of MobileNetV2's Architecture](https://towardsdatascience.com/mobilenetv2-inverted-residuals-and-linear-bottlenecks-8a4362f4ffd5)
* [Differences between fit and fit_generator](https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/)
* [Nice stack Exchange answer on fine tuning](https://datascience.stackexchange.com/questions/28383/using-a-pre-trained-cnn-classifier-and-apply-it-on-a-different-image-dataset/28387#28387)
* [A Dog Breed Dataset on Kaggle, a good candidate for your own transfer learning application since ImageNet includes some dog breeds already](https://www.kaggle.com/c/dog-breed-identification/data)

## Part 4: CNNs For Segmentation

### Pre-Reading


SAVED FOR LATER READING, EVALUATE THESE:

[U-NET](https://arxiv.org/abs/1505.04597)
[U-Net Implementation Keras](https://github.com/zhixuhao/unet)

https://towardsdatascience.com/using-image-segmentation-to-identify-rooftops-in-low-resolution-satellite-images-c791975d91cc



* https://www.microsoft.com/developerblog/2018/07/18/semantic-segmentation-small-data-using-keras-azure-deep-learning-virtual-machine/

* https://medium.com/@hanrelan/a-non-experts-guide-to-image-segmentation-using-deep-neural-nets-dda5022f6282

* https://www.kaggle.com/c/ultrasound-nerve-segmentation/discussion/21358

* https://github.com/divamgupta/image-segmentation-keras


### Helpful Documentation

*

### Resources for Further Exploration

*
