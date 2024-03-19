---
license: bsd-3-clause
  
language:
- en
  
tags:
- sentiment
- bert
- sentiment-analysis
- transformers

pipeline_tag: text-classification
---
> Authors : GRP209

# User Comment Sentiment Analysis

This model aims to analyze user comments on products and extracting the expressed sentiments. 

User ratings on the internet do not always provide detailed qualitative information about their experience. 

Therefore, it is important to go beyond these ratings and extract more insightful information that can help a brand improve their product or service.

# Objective

The model utilizes the BERT architecture and is trained on a dataset of user comments with sentiment labels.

The model is capable of analyzing comments and extracting sentiments such as **positive**, **negative**, or **neutral**.

# Features

**Sentiment Classification**: The model can classify user comments into positive, negative, or neutral sentiments, providing an overall indication of the expressed opinion.

**Improvement Suggestions**: In cases where a comment expresses a negative or neutral sentiment, the model suggests an improved version of the text with a more positive sentiment. 
This can help businesses understand consumer reactions and identify areas for product or service improvement.

# Usage

To use this sentiment analysis system, follow these steps:

- Install the required dependencies by running the command pip install -r requirements.txt.
- Once the training is complete, the best-trained model will be saved in the best_model_state.bin file.
- To make predictions on new comments, use the analyze_sentiment(comment_text) function, replacing comment_text with the actual comment text to analyze. 
- The model will return the sentiment expressed in the comment.
- To suggest an improved version of a comment, use the suggest_improved_text(comment_text) function. 
- If the comment expresses a negative or neutral sentiment, the function will generate an improved version of the text with a more positive sentiment. Otherwise, the original text will be returned without modification.
