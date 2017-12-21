# Insights-From-Personal-Photos
Categorizing photos into lifestyle categories. 

## Summary ##
The purpose of this project is to categorize an individual into a specific lifestyle category based on their photos.
The training set of images is organized by lifestyle. Using the Clarifai API, image tags are generated for each photo.
We then aggregate the tags and classifications in order to build a word2vec model. This repository has sample lifestyle categories 
such as 'foodie', 'outdoorsy', 'family', and 'sporty'. Given the current dataset and categories, the testing accuracy falls
slighlty below 80%. With more niche or discminate categories, it is likely to achieve a higher accurracy.

There are two main scripts in this repo: *tag_generator.py* and *Insights_From_Photos_word2vec.ipynb*.

## tag_generator.py ##
This file is used to automatically generate tags for photos. In its current form it outputs tags for every photo in a folder into a JSON formatted text file

## Insights_From_Photos_word2vec.ipynb ##
This python notebook reads the tags from the text files and transfers the data and classification into a Pandas dataframe which is then used to build the word2vec model for the specific lifestyle categories.
