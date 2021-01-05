## Most helpful resources so far...

* [Stanford Lecture RNNs in Computer Vision](https://www.youtube.com/watch?v=6niqTuYFZLQ)
    * [Companion written piece from the same lab](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Simple illustrated intro to RNNs](https://towardsdatascience.com/illustrated-guide-to-recurrent-neural-networks-79e5eb8049c9)
* [SO question clearly explaining Embedding layers vs Dense layers](https://stackoverflow.com/questions/47868265/what-is-the-difference-between-an-embedding-layer-and-a-dense-layer)

## Promising but have not read

* [Understanding LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Word Embeddings TF Docs](https://www.tensorflow.org/tutorials/text/word_embeddings)
* [Build RNN TF Docs](https://www.tensorflow.org/guide/keras/rnn#rnn_state_reuse)
* [Sentiment analysis w/ TF2](https://curiousily.com/posts/sentiment-analysis-with-tensorflow-2-and-keras-using-python/)
* [Understanding LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [What are embeddings](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture)

## Further resources

* [Very Explicit Guide to RNN/GRU/LSTM, code from scratch](https://datascience-enthusiast.com/DL/Building_a_Recurrent_Neural_Network-Step_by_Step_v1.html)
* [Transformers are replacing RNN in some cases](https://www.youtube.com/watch?v=S27pHKBEp30)
* [More kinds of Embeddings in TF](https://www.tensorflow.org/tutorials/text/word_embeddings)
    * Sometimes we train on our data, and sometimes we use a pre-trained embedder (e.g. Word2Vec)
* [understanding the hidden memories of RNNs](https://blog.acolyer.org/2019/02/25/understanding-hidden-memories-of-recurrent-neural-networks/)

## Proposed Topic Order:

* Problems with sequence data and using plain ANN or CNN...
    * Fixed input size can work, but there are issues. 
        * e.g. each moment in time is a single node in the input vector.
            * Again works well with some kinds of specific & simple data
            * But cannot work with variable length input data
        * for text processing the text with e.g. "Bag of Words" and TFIDF also turns a sequence into a single fixed length vector.
            * This works well for very simple data (e.g. tweets) with simple output (sentiment 1-5)
            * But doesn't work at all for machine translation, image captioning, and other more complex tasks or tasks with variable length outputs.
        
    * 1D CNN can actually do decently and are much faster than RNNs.
        * But... the fixed window based on the kernel size is ultimately limiting.
        * We want a way to deal with long sequences where the meaningful relationships might be very far apart. 

* Where are RNN's most appropriate?
    * Problems with variable length inputs and/or outputs: 
        * Machine translation (both), 
        * image captioning (fixed input, variable output), 
        * audio-to-text (both).
        * Text classification (variable input fixed output)
        * Text generation (both)

* Structure of RNN's
    * Hidden state changes each timestep,
    * BUT the weights are shared parameters at every timestep,
    * Training as a for loop / network unrolling
    * Gradient backprop with the time component.
        * Exploding and vanishing gradients
            * RNN's are frequently shorter than their ANN and CNN cousins
            * "Gradient clipping" can help which is a bit of a hack but works.
            * ReLU / leaklyReLU also help the same way it has in ANNs
            * LSTM and GRU are the most robust mitigations (gated cells).

* Key Preprocessing Idea: Word and Character Embeddings.

* Build an RNN for sentiment analysis.
    * Compare equivalent networks with LSTM and GRU instead of "vanilla" RNNs.
        * Somewhat Comparable to resnets / skip connections in CNN