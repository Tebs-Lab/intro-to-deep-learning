# Exercise: Data Preprocessing

In this exercise you'll practice applying your knowledge of data collection and preprocessing. This is, in some ways, a qualitative exercise and in others a quantitative exercise. Additionally, instead of focusing on building a neural network to obtain a result, in this exercise you'll be focused on the question: is this data a good fit for modeling with a neural network.

## Exercise Goals

This exercise is meant to help you:

* Identify possible sources of bias and error in a dataset.
* Use pandas, sklearn, and matplotlib to explore data.
* Apply statistical reasoning to make an argument.

## Exercise Notes

This exercise lends itself particularly well to Jupyter notebook, as opposed to other Python runtime environments, because fundamentally it is about exploring data. Charts and figures will help immensely in this process. You may still choose to use another option if you wish.

This exercise could take a couple hours, or many days, depending on how well you want to support your conclusions. The provided Jupyter notebooks contain examples of tactics that you might wish to apply, but they are far from a complete reference of possible tactics. As such, you should expect to search for information, tactics, and ideas on your own.

Due to the highly ambiguous nature of this exercise, there is no such thing as a "correct answer". The important thing is to try to convince yourself (and perhaps a skeptical friend) of your hypothesis. As with any good science, you should constantly be asking yourself what you may have missed, how your reasoning could be flawed, or what assumptions you've made that might not hold up.

The purpose of this exercise is not to find some objective truth. Such a truth probably does not exist. Instead the purpose of this exercise is to wrestle with the ambiguity that permeates all statistical analysis, and try to make the most honest argument that you can.

## The Exercise

Your goal is to create a document that wrestles with the following question:

**Is this dataset a good candidate for training a neural network based regression model to predict housing prices?**

The dataset is the same dataset linked and discussed in 02-preprocessing-structured-data.ipynb, and can be downloaded here: [https://www.kaggle.com/new-york-city/nyc-property-sales](https://www.kaggle.com/new-york-city/nyc-property-sales)

Your report should have 3 sections.

In the first section, you should write 2-3 paragraphs about the potential sources of bias and errors that could impact this dataset. You should consider issues such as where the data came from, who compiled it, what societal or institutional biases could be at play, how the data might be misinterpreted by a machine learning model. These paragraphs you should be as descriptive as possible about the risks (or lack thereof) of using this data. In other words, if we train a regression model using this data, will it tell us what we think it should tell us (e.g. accurately predict the price of similar houses into the future) or are the sources of bias and error likely to result in our models failure to achieve its goals.

In the second section, you should perform data cleanup and numerical analysis. Here, you should assume the data is relatively bias-free, and determine if it is still a good fit for a neural network using statistical arguments. Questions to ask here: does the data have strong signal, do the fields in our data correlate with the labels (price)? Is there a lot of missing, or misleading data in the data set? Are there too many outliers? Furthermore, you should argue in favor of keeping or removing certain pieces of data. Are all the columns actually useful, or should some be removed? Is it appropriate to remove some outliers? If we do, will we still have enough data to train our model?

Finally, in the third section, write 1 or 2 paragraphs describing your conclusion: is this dataset good enough to train a neural network based regression model to predict housing prices in NYC.

Regardless of what you conclude in your report—you may enjoy testing your hypothesis by attempting to build a neural network based regression model using this as training data. Good luck!
