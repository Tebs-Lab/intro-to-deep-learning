# Generative Adversarial Networks

Generative Adversarial Networks (GANs) are an adaptation of deep neural networks that allow users to create fake data that mimics or mirrors a training set. GANs have been used to generate works of art, realistic fake images, realistic fake video, and text.

A number of websites that generate examples of these so called "deep fakes" have been [collected on this website](https://thisxdoesnotexist.com/). Some websites, like [This Marketing Blog Does Not Exist](http://thismarketingblogdoesnotexist.com/) train multiple GANs, some for the images, others for the text.

These websites typically use a well known open-source architecture such as StyleGAN, BigGAN, and Pix2Pix for images. For text generation something like BERT or GPT-2. Using an established architecture — and often an open source implementation & training regimen as well — the creators of these websites then train them on a dataset of their own choice.

GANs are actually a combination of two separate neural networks (the Generator and the Discriminator) who compete against each other during the training process (hence "adversarial"). The generator's job is to create convincing fake images, where "convincing" means good enough to trick the discriminator. Therefore, the discriminator's job is to detect images that are produced by the generator, and distinguish them from images that are in the actual training set.

One result of this setup is a complex training process. Because the two networks are competing, they must be trained "separately." But, because the generator's performance only makes sense in terms of the discriminator (i.e. the generator is "good" when it "fools" the discriminator, and bad otherwise) they must be trained together! Furthermore, there aren't any real "objective" metrics that tell us if the GAN is doing a good job — we have to actually look at the results of the generator to tell if it's generating fakes that can fool a human.

As a result, GANs are notoriously hard to train. In addition to improving architectural patterns and expanding those patterns into new domains (image, text, video, audio...), many of the advancements in GAN research are related to creating more successful training regimes.

**By the end of this section students should be able to:**

* Describe the components of a GAN, specifically the generator and discriminator networks.
* Describe the "adversarial" relationship between the two networks.
* Implement and train GANs that create passable images for both the CIFAR-10 and MNIST datasets.
* Apply best practices to their GAN's training regimen.
* Study state of the art GANs on their own.

## Part 1: GANs on MNIST

For our introduction to GANs, we're headed back to the trusty MNIST dataset. We're using MNIST for a variety of reasons. One major one is that GANs are complex and expensive to train so a simple dataset has advantages for all of us using commodity hardware. The small images, a single color channel, and a comparatively simple task allow us explore basic GAN architectures without getting lost in the complexities of state-of-the-art models.

### Pre-Reading

* [GAN for MNIST in TF/Keras](https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-an-mnist-handwritten-digits-from-scratch-in-keras/)
* [Alternate GAN for MNIST in TF/Keras](https://www.wouterbulten.nl/blog/tech/getting-started-with-generative-adversarial-networks/)

### Resources for Further Exploration

* [A Beginners Guide to Generative Adversarial Networks](https://pathmind.com/wiki/generative-adversarial-network-gan)
* [Review of GAN Architectures](https://sigmoidal.io/beginners-review-of-gan-architectures/)
* [Alternative Neural Networks Exist: Variational Autoencoders vs GANs](https://syncedreview.com/2019/06/06/going-beyond-gan-new-deepmind-vae-model-generates-high-fidelity-human-faces/)

## Part 2: Adding Color, Improving Training Stability, and Other Best Practices

GANs have earned a reputation for being hard to train. In the early days of GAN research (2014) very little was known about how and why exactly GANs worked, and therefore how to train them. Like many areas in Deep Learning,  GAN research was advanced more from empirical research than through theoretical breakthroughs. In many ways, the theory still lags behind the empirical research. Nevertheless, over the last few years some best practices have been established to greatly improve training stability and overall GAN performance.

### Pre-Reading

* [How to Develop a GAN for CIFAR10](https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-a-cifar-10-small-object-photographs-from-scratch/)
* [How to Develop a Conditional GAN](https://machinelearningmastery.com/how-to-develop-a-conditional-generative-adversarial-network-from-scratch/)

### Helpful Documentation

* [TF/Keras Embedding Layer](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding)

### Resources for Further Exploration

* [Adding Noise to Stabilize Training](https://www.inference.vc/instance-noise-a-trick-for-stabilising-gan-training/)
* [Improved Techniques for Training GANS (paper)](https://arxiv.org/abs/1606.03498)
* [Embedding Layers Explained](https://towardsdatascience.com/neural-network-embeddings-explained-4d028e6f0526)
* [Best Practices for GAN Architecture](https://machinelearningmastery.com/how-to-code-generative-adversarial-network-hacks/)
* [Tips for Training Stable GANs](https://machinelearningmastery.com/how-to-train-stable-generative-adversarial-networks/)
* [Deconvolution and Checkerboard Artifacts](https://distill.pub/2016/deconv-checkerboard/)


## Advanced GAN Resources: Style Transfer, Resolution Recovery, Photo In-Painting, Video, and More

Since their invention, GANs were quickly adapted for use in tons interesting ways. "DeepFake" videos are one of the most well known applications of GANs, but the strategy is also proving to be useful in image editing, photo resolution recovery, photo reconstruction/inpainting, the creation of art, black-and-white photo colorization, and more.

Implementing examples of everything GANs can do is beyond the scope of this class (and my personal ability!) but there are numerous wonderful resources available elsewhere. Here is a collection of fascinating and detailed articles, papers, code repos, and tools that the curious student can use to continue their exploration of GANs.

### Collections of GAN Applications

* [18 Impressive Applications of GANs](https://machinelearningmastery.com/impressive-applications-of-generative-adversarial-networks/)
* [Collection of Powerful GAN Image Architectures](https://towardsdatascience.com/must-read-papers-on-gans-b665bbae3317)
* [GAN papers and implementations on Github](https://github.com/nashory/gans-awesome-applications)

### Controlling The Generated Images / AI Assisted Photo Realistic Painting

* [Guide to StyleGAN](https://machinelearningmastery.com/introduction-to-style-generative-adversarial-network-stylegan/)
* [Another Guide to StyleGAN](https://towardsdatascience.com/explained-a-style-based-generator-architecture-for-gans-generating-and-tuning-realistic-6cb2be0f431)
* [StyleGAN2 Official Implementation](https://github.com/NVlabs/stylegan2)
* [NVIDIA's GauGAN Explained](https://adamdking.com/blog/gaugan/)
* [A Gentle Introduction to BigGAN](https://machinelearningmastery.com/a-gentle-introduction-to-the-biggan/)
* [Papers With Code: Class Conditional GANs](https://paperswithcode.com/task/conditional-image-generation)

### Style Transfer

* [Style Transfer Guide](https://www.fritz.ai/style-transfer/)
* [Exploring Neural Style Transfer (paper)](http://cs231n.stanford.edu/reports/2017/pdfs/428.pdf)
* [pix2pix (paper, code, demos)](https://phillipi.github.io/pix2pix/)
* [CycleGAN (articles, papers, exercises and code)](https://junyanz.github.io/CycleGAN/)
* [Fast Style Transfer (open source tool)](https://github.com/lengstrom/fast-style-transfer)

### Resolution Recovery / Super Resolution

* [An Introduction to Super Resolution](https://medium.com/beyondminds/an-introduction-to-super-resolution-using-deep-learning-f60aff9a499d)
* [Image Super Resolution With Tensorflow](https://krasserm.github.io/2019/09/04/super-resolution/)
* [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (paper)](https://arxiv.org/abs/1609.04802)
* [Deep Learning for Image Super Resolution, a Review (paper)](https://arxiv.org/pdf/1808.03344.pdf)

### Photo Inpainting

* [A Guide to Photo Inpainting With Deep Learning](https://heartbeat.fritz.ai/guide-to-image-inpainting-using-machine-learning-to-edit-and-correct-defects-in-photos-3c1b0e13bbd0)
* [Comparing Inpainting Algorithms to Each Other and To Humans](https://towardsdatascience.com/image-inpainting-humans-vs-ai-48fc4bca7ecc)
* [Papers With Code Collection: Inpainting](https://paperswithcode.com/task/image-inpainting)
* [Context Encoders: Feature Learning by Inpainting (paper)](https://arxiv.org/abs/1604.07379)

### Face Swapping / Deep Video Portraits / Deep Fakes

* [Series on Deep Fakes Including AutoEncoders and GANs](https://www.alanzucconi.com/2018/03/14/introduction-to-deepfakes/)
* [Accessible Face Swap GAN With Code & Google Colab Examples](https://github.com/shaoanlu/fewshot-face-translation-GAN)
* [Deep Video Portraits (paper)](https://arxiv.org/pdf/1805.11714.pdf)
