# Section 8: Natural Language Processing with Recurrent Neural Networks

Working with textual data and neural networks requires us to process text into a numerical format that ideally encodes the semantic meaning of words, characters, or other tokens. Not only do we need specialized preprocessing steps, but due to the sequential nature of textual data an alternative form of network that works with variable input and output sizes.

**By the end of this section students should be able to:**

* Describe the following (older) methods for text encoding at a high level:
    * Rules Based Systems
    * Bag of Words
    * Term-Frequency Inverse-Document-Frequency
* Define and apply embeddings to preprocess text with Tensorflow.
* Describe the key ideas behind RNNs, especially the use of hidden states.
* Build simple RNNs for classification in Tensorflow
* Build RNNs with Long Short Term Memory for text generation in Tensorflow

## Part 1: Text Encodings

Text encoding has been around for a long time. We'll briefly describe some of the older methods for preprocessing textual data, then we'll discuss the most popular current strategy — Embeddings — in more detail.

## Part 1: Text Encodings

We'll describe four strategies for encoding text for historical purposes, but the only one we'll use is called "Embedding."

### Pre-reading Material

* [What are embeddings](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture)

### Resources for Further Exploration

* [More kinds of Embeddings in TF](https://www.tensorflow.org/tutorials/text/word_embeddings)
    * Sometimes we train on our data, and sometimes we use a pre-trained embedder (e.g. Word2Vec)

### Helpful Documentation

* [Word Embeddings TF Docs](https://www.tensorflow.org/tutorials/text/word_embeddings)
* [SO question clearly explaining Embedding layers vs Dense layers](https://stackoverflow.com/questions/47868265/what-is-the-difference-between-an-embedding-layer-and-a-dense-layer)

## Part 2: Intro to RNNs

RNN's are a specialized form of neural network designed specifically with two goals in mind:

1. Work with sequential data such as language and time-series by maintaining "context" over "time" with respect to the sequence.
2. Allow variable length inputs and outputs.

### Pre-reading Material

* [Simple illustrated intro to RNNs](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9)

### Resources for Further Exploration

* [Stanford Lecture RNNs in Computer Vision](https://www.youtube.com/watch?v=6niqTuYFZLQ)
    * [Companion written piece from the same lab](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Sentiment analysis w/ TF2](https://curiousily.com/posts/sentiment-analysis-with-tensorflow-2-and-keras-using-python/)

### Helpful Documentation

* [Build RNN TF Docs](https://www.tensorflow.org/guide/keras/rnn)

## Part 3: LSTM and Sequence to Sequence

Long Short Term Memory layers are an alternative to simpleRNN layers that allow the network to "remember" things easier, and provide a kind of highway for back-propagation (similar to skip layers in CNNs). We'll explore this layer's unique setup and strengths. 

Then, we'll use a network with an LSTM layer to perform text generation

### Pre-reading Material

* [Understanding LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Sequence to Sequence tutorial](https://blog.keras.io/a-ten-minute-introduction-to-sequence-to-sequence-learning-in-keras.html)

### Resources for Further Exploration

* [Very Explicit Guide to RNN/GRU/LSTM, code from scratch](https://datascience-enthusiast.com/DL/Building_a_Recurrent_Neural_Network-Step_by_Step_v1.html)
* [understanding the hidden memories of RNNs](https://blog.acolyer.org/2019/02/25/understanding-hidden-memories-of-recurrent-neural-networks/)
* [Learn why Transformers are replacing RNN in many cases](https://www.youtube.com/watch?v=S27pHKBEp30)

### Helpful Documentation

* [Text Generation w/ RNNs](https://www.tensorflow.org/tutorials/text/text_generation)
* [TF LSTM Docs](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)