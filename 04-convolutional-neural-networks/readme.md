# Section 4: Convolutional Neural Networks

Convolutional neural networks are a specialization of neural networks that are designed specifically to work with data that has spatial relationships. The most common use of CNN's is in the field of computer vision and image processing. This is because images have clear spatial relationships. Neighboring pixels have a stronger relationship than pixels in opposite corners of an image.

By adding ideas from image processing to neural networks, especially the idea of a 'kernel', convolutional neural networks have achieved fantastic performance on a number of computer vision tasks.

**By the end of this section students should be able to:**

* Define convolutional neural networks and their critical components.
* Describe why CNN's are such a good fit for computer vision tasks.
* Build convolutional neural networks using Tensorflow.
* Describe the concept of Transfer Learning and apply it to CNNs using Tensorflow.
* Contrast classification and segmentation.
* Apply CNNs to perform classification, localization, and segmentation.

## Part 1: What Are CNNs and What Are They Good At?

See the above!

### Pre-Reading

* [Image Processing With Kernals](http://setosa.io/ev/image-kernels/)
* [The Math of Convolutional Networks](https://towardsdatascience.com/gentle-dive-into-math-behind-convolutional-neural-networks-79a07dd44cf9)
* [Global Average Pooling](https://alexisbcook.github.io/2017/global-average-pooling-layers-for-object-localization/)

### Resources for Further Exploration

* [Neural Networks and Deep Learning, Chapter 6](http://neuralnetworksanddeeplearning.com/chap6.html#introducing_convolutional_networks)
* [Deep Learning Book, Chapter 9](http://www.deeplearningbook.org/contents/convnets.html)
* [Types of Convolutions](https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d)

## Part 2: Building CNNs For Classification

Just like with artificial neural networks, the theory is great but it's more fun to put the concepts into practice. In this section we'll build a few CNNs from scratch. We'll also import well known, pre-trained neural networks and apply them. Oftentimes, due to the enormous training costs of modern CNNs, it can be more effective to just use an existing model.

### Pre-Reading

* [Build a CNN in Keras](https://towardsdatascience.com/building-a-convolutional-neural-network-cnn-in-keras-329fbbadc5f5)

### Helpful Documentation

* [TF/Keras Datasets](https://www.tensorflow.org/api_docs/python/tf/keras/datasets)
* [TF/Keras Conv2D layer](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D)
* [TF Spatial Dropout](https://www.tensorflow.org/api_docs/python/tf/keras/layers/SpatialDropout2D)
* [NumPy Reshape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)
* [An example of a CNN architecture with 95%+ accuracy on Fashion MNIST](https://github.com/cmasch/zalando-fashion-mnist)
* [SciKit Learn's Confusuion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
* [Seaborn's Heatmap Plot](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

### Resources for Further Exploration

* [cs231: Convolutional Networks](https://cs231n.github.io/convolutional-networks/)
* [cs231: Understanding Convolutional Networks](https://cs231n.github.io/understanding-cnn/)
* [Detailed Intro to Keras CNNs](https://www.pyimagesearch.com/2018/12/31/keras-conv2d-and-convolutional-layers/)
* [More detailed implementation of Keras CNN & Fashion MNIST](https://www.pyimagesearch.com/2019/02/11/fashion-mnist-with-keras-and-deep-learning/)
* [Gradient Activated Heat Maps paper](https://arxiv.org/abs/1610.02391)
  * [Somewhat More Approachable GRAD-CAM Writeup](https://jacobgil.github.io/deeplearning/class-activation-maps)
* [Visualizing Internal Convolutional Layers](https://machinelearningmastery.com/how-to-visualize-filters-and-feature-maps-in-convolutional-neural-networks/)
* [**Designing Network Design Spaces (very useful on how to approach network design)**](https://openaccess.thecvf.com/content_CVPR_2020/papers/Radosavovic_Designing_Network_Design_Spaces_CVPR_2020_paper.pdf)

## Part 3: Transfer Learning

Transfer learning is a tactic that allows us to take a pre-trained neural network, and apply it to a new task. Transfer learning is especially popular with CNNs because a lot of images share the same useful features, which means the "lessons" learned by a CNN for one task can be immediately applied to another task. In this section we'll look at two different styles of transfer learning, feature extraction and fine-tuning, and apply them using Tensorflow.

### Pre-Reading

* [A Gentle Introduction to Transfer Learning](https://machinelearningmastery.com/transfer-learning-for-deep-learning/)

### Helpful Documentation

* [TF/Keras Models](https://www.tensorflow.org/api_docs/python/tf/keras/Model)
* [scipy zoom](http://scipy.github.io/devdocs/generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom)
* [TF/Keras Pre-built Models](https://www.tensorflow.org/api_docs/python/tf/keras/applications)
  * There are tons and these are updated regularly, check it out!
* [ImageNet Documentation](http://image-net.org/about-overview)
* [ImageNet classifications dictionary](https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a)
* [Image transform using PIL](https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/)
* [Pillow documentation](https://pillow.readthedocs.io/en/stable/)

### Resources for Further Exploration

* [Paper: How Transferable are Features in Deep Neural Networks?](https://arxiv.org/pdf/1411.1792.pdf)
* [Fine Tuning and Fixed Transfer](http://cs231n.github.io/transfer-learning/)
* [A Comprehensive Guide to Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
* [Transfer Learning Tutorial With Keras](https://www.hackerearth.com/practice/machine-learning/transfer-learning/transfer-learning-intro/tutorial/)
* [Transfer Learning in Keras](https://towardsdatascience.com/keras-transfer-learning-for-beginners-6c9b8b7143e)
* [Introduction to Separable Convolutions](https://towardsdatascience.com/a-basic-introduction-to-separable-convolutions-b99ec3102728)
* [Discussion of MobileNetV2's Architecture](https://towardsdatascience.com/mobilenetv2-inverted-residuals-and-linear-bottlenecks-8a4362f4ffd5)
* [Differences between fit and fit_generator](https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/)
* [Nice stack Exchange answer on fine tuning](https://datascience.stackexchange.com/questions/28383/using-a-pre-trained-cnn-classifier-and-apply-it-on-a-different-image-dataset/28387#28387)
* [A Dog Breed Dataset on Kaggle, a good candidate for your own transfer learning application since ImageNet includes some dog breeds already](https://www.kaggle.com/c/dog-breed-identification/data)

## Part 4: Localization and Segmentation

Object localization and segmentation are both forms of detecting where in an image some object is. We call this task object localization when the result is a bounding box (a rectangle that contains the object in question) and segmentation when we identify the specific pixels within the image that contain the object in question. Typically, networks that localize objects also classify the objects. Although that is not strictly a requirement, it's obviously more useful if the network can say "There is a cat right there," and less useful to say, "An object is right there."

Many of the same CNN architectures that are effective for classification are effective for localization and segmentation. Changes must be made to the output layers, since the meaning of a prediction has changed from, "This is an image of [CLASS]." to "This is an image of [CLASS] which exists within (x, y, w, h)" where those four integers represent the bounding box, e.i. (x, y) is the top left corner of the box and (w, h) is width and height of the box.

Segmentation requires even more output data. In fact, for segmentation the output must be an activation map with the same dimensions as the input image where (for single item segmentation) each pixel is labeled as 0 (not a pixel belonging to the object) or 1 (a pixel belonging to the object). One way to handle more classes is to add more activation maps the output layer, generally one per class. Although there are others, see YOLO in additional resources.

### Pre-Reading

* [Evolution of Objet Detection](https://towardsdatascience.com/evolution-of-object-detection-and-localization-algorithms-e241021d8bad)
* [An overview of semantic image segmentation](https://www.jeremyjordan.me/semantic-segmentation/)

### Helpful Documentation

* [TF/Keras Losses](https://www.tensorflow.org/api_docs/python/tf/keras/losses)
* [TF/Keras Backend](https://www.tensorflow.org/api_docs/python/tf/keras/backend)
* [TF/Keras Functional API](https://www.tensorflow.org/guide/keras/functional)
* [TF/Keras Conv2DTranspose](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2DTranspose)

### Resources for Further Exploration

* [Multi-output models in Keras](https://www.pyimagesearch.com/2018/06/04/keras-multiple-outputs-and-multiple-losses/)
* [Intersection Over Union](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)
* [Loss functions for Segmentation](https://lars76.github.io/neural-networks/object-detection/losses-for-segmentation/)
* [Transposed Convolutions](https://medium.com/apache-mxnet/transposed-convolutions-explained-with-ms-excel-52d13030c7e8)
* [Gentle Introduction to YOLO Object Detection Part 1](https://hackernoon.com/gentle-guide-on-how-yolo-object-localization-works-with-keras-part-1-aec99277f56f)
* [Gentle Introduction to YOLO Part 2](https://heartbeat.fritz.ai/gentle-guide-on-how-yolo-object-localization-works-with-keras-part-2-65fe59ac12d)
* [Detailed guide to YOLO Net](https://hackernoon.com/understanding-yolo-f5a74bbc7967)
* [Segmentation implementations in Keras]( https://github.com/divamgupta/image-segmentation-keras)
* [Kaggle Ultrasound Nerve Segmentation Dataset & Challenge](https://www.kaggle.com/c/ultrasound-nerve-segmentation/discussion/21358)
* [A Non-Experts Guide to Segmentation With Keras](https://medium.com/@hanrelan/a-non-experts-guide-to-image-segmentation-using-deep-neural-nets-dda5022f6282)
* [Microsoft Developer Blog about U-Net For Segmentation](https://www.microsoft.com/developerblog/2018/07/18/semantic-segmentation-small-data-using-keras-azure-deep-learning-virtual-machine/)
* [Paper: U-Net](https://arxiv.org/abs/1505.04597)
* [Open Source Implementation of U-Net](https://github.com/zhixuhao/unet)
* [Some Object Localization Experiments on Github w/ Pet Dataset](https://github.com/lars76/object-localization)
