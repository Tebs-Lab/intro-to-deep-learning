# Generative Adversarial Networks

Generative Adversarial Networks (GANs) are an adaptation of deep neural networks that allow users to create fake data that mimics or mirrors a training set. GANs have been used to generate works of art, realistic fake images, realistic fake video, and text.

A number of websites that generate examples of these so called "deep fakes" have been [collected on this website](https://thisxdoesnotexist.com/). Some websites, like [This Marketing Blog Does Not Exist](http://thismarketingblogdoesnotexist.com/) train multiple GANs, some for the images, others for the text.

These websites typically use a well known open-source architecture such as StyleGAN, BigGAN, and Pix2Pix for images. For text generation something like BERT or GPT-2. Using an established architecture — and often an open source implementation & training regimen as well — the creators of these websites then train them on a dataset of their own choice.

GANs are actually a combination of two separate neural networks (the Generator and the Discriminator) who compete against each other during the training process (hence "adversarial"). The generator's job is to create convincing fake images, where "convincing" means good enough to trick the discriminator. Therefore, the discriminator's job is to detect images that are produced by the generator, and distinguish them from images that are in the actual training set.

One result of this setup is a complex training process. Because the two networks are competing, they must be trained "separately." But, because the generator's performance only makes sense in terms of the discriminator (i.e. the generator is "good" when it "fools" the discriminator, and bad otherwise) they must be trained together! Furthermore, there aren't any real "objective" metrics that tell us if the GAN is doing a good job — we have to actually look at the results of the generator to tell if it's generating fakes that can fool a human.

As a result, GANs are notoriously hard to train. In addition to improving architectural patterns and expanding those patterns into new domains (image, text, video, audio...), many of the advancements in GAN research are related to creating more successful training regimes.

## Part 1: GANs on MNIST

For our introduction to GANs, we're headed back to the trusty MNIST dataset. We're using MNIST for a variety of reasons. One major one is that GANs are complex and expensive to train so a simple dataset has advantages for all of us using commodity hardware. The small images, a single color channel, and a comparatively simple task allow us explore basic GAN architectures without getting lost in the complexities of state-of-the-art models.

### Pre-Reading

* [GAN for MNIST in Keras](https://machinelearningmastery.com/how-to-develop-a-generative-adversarial-network-for-an-mnist-handwritten-digits-from-scratch-in-keras/)
* [Alternate GAN for MNIST in Keras](https://www.wouterbulten.nl/blog/tech/getting-started-with-generative-adversarial-networks/)

### Helpful Documentation

* [Keras Convolutional Layers](https://keras.io/layers/convolutional/)
* [Keras Optimizers](https://keras.io/optimizers/)
* [Keras Sequential Model Guide](https://keras.io/getting-started/sequential-model-guide/)
* [Github Discussion of Keras' Freeze and Compile Behavior](https://github.com/keras-team/keras/issues/8585)


### Resources for Further Exploration

* [Best Practices for GAN Architecture](https://machinelearningmastery.com/how-to-code-generative-adversarial-network-hacks/)
* [Adding Noise to Stabilize Training](https://www.inference.vc/instance-noise-a-trick-for-stabilising-gan-training/)
* [Collection of Powerful GAN Image Architectures](https://towardsdatascience.com/must-read-papers-on-gans-b665bbae3317)
* [GPT-2 Writeup and Code](https://openai.com/blog/better-language-models/)
* [StyleGAN2 Official implementation](https://github.com/NVlabs/stylegan2)
